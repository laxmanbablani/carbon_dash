# Carbon Dash Automation Architecture

This document outlines the architecture and strategy for automating the generation of the `carbon_dash` library from the IBM Carbon Design System React components. The primary goal is to maintain a fully automated, idempotent pipeline that creates Dash components, documentation, and tests with minimal manual intervention.

## Automation Pipeline Stages

### 1. Metadata Parsing and Configuration
*   **Input:** `@carbon/react` source code, specifically TypeScript definitions, `propTypes`, and component structures.
*   **Configuration Files:** Structured configurations (e.g., JSON/YAML) defining how specific Carbon components map to Dash. This includes defining event-to-property mappings (e.g., mapping `onChange` to `setProps({ value })`), specifying custom Dash properties (like `n_clicks`), and handling special types (like Icons or render props).
*   **Action:** Extract a unified metadata model for each component, merging raw Carbon prop types with our custom Dash configurations.

### 2. React Wrapper Generation
*   **Action:** Automatically generate the React boilerplate required by Dash for every component.
    *   `src/lib/components/ComponentName.react.js`: The public interface containing strictly formatted `propTypes` and JSDoc comments for Dash's backend generator.
    *   `src/lib/fragments/ComponentName.react.js`: The implementation layer. This wrapper will dynamically intercept React events, translate them into `setProps` calls, and handle complex child/prop mapping (e.g., resolving icon strings into React components).
    *   `src/lib/index.js` & `src/lib/LazyLoader.js`: Automatically updated to export all generated components.

### 3. Backend Generation & Build
*   **Action:** Utilize the standard Dash build pipeline (`npm run build`).
    *   `build:js`: Webpack bundles and transpiles the generated React wrappers, compiling any necessary SCSS/CSS.
    *   `build:backends`: The `dash-generate-components` tool parses the generated `.react.js` files to build the Python API (`carbon_dash/ComponentName.py`).

### 4. Automated Test Generation
*   **Action:** Generate end-to-end `dash_duo` integration tests for each component in the `tests/` directory.
    *   **Render Tests:** Automatically verify that every generated component successfully renders in the DOM without Python or React errors.
    *   **Interactivity Tests:** Use configuration definitions to automatically generate tests that simulate user actions (e.g., clicking a generated Button) and assert that Python callbacks receive the correct property updates.

### 5. Documentation & Storybook Sync
*   **Input:** Carbon's `.stories.tsx` and MDX documentation.
*   **Action:** Parse Carbon stories and translate them into a Dash interactive documentation app. Extract code examples and convert them from React JSX to Dash Python syntax, grouping related components (e.g., Grid, Row, Column) logically.

## Automation Pipeline Implementation Details

### 1. Metadata & Configuration (`scripts/config.json`)
We use a centralized `config.json` to define:
- `injectProps`: Standard Dash properties (like `id`, `n_clicks`, `value`, `label`) and their default values.
- `propMap`: Renaming standard props to Carbon-specific names (e.g., `label` -> `labelText`).
- `propTransforms`: Handling special types like `AILabel` (AI decorator).
- `eventMap`: Mapping React event arguments (e.g., `arguments[0].target.value`) to Dash property updates.
- `testStrategy`: Defining Selenium-based interaction steps and expected outcomes for automated testing.

### 2. Wrapper Generation (`scripts/generate.js`)
The generator dynamically creates:
- `src/lib/fragments/*.react.js`: Implementation wrappers that use `@carbon/react` and bridge `setProps`.
- `src/lib/components/*.react.js`: Lazy-loading entry points for the Dash component generator.
- `tests/test_*.py`: Automated `dash_duo` integration tests based on the `testStrategy`.

### 3. Build and Asset Management
- **Webfont Inlining:** All Carbon fonts are inlined in the main bundle via Webpack's `asset/inline` to prevent 404s in Dash's Flask server.
- **Dynamic Imports:** Components use `React.lazy` to keep the initial bundle size manageable, with Dash-renderer handling the async chunk loading.

### 4. Findings & Noteworthy Solutions
- **Comprehensive Component Coverage:** The automation pipeline now dynamically discovers all component exports from `@carbon/react`. This ensures that `carbon_dash` provides full access to the entire Carbon Design System, including all stable and newly added components.
- **Robust Import Validation:** During the generation process, the pipeline validates that every component requested (via `config.json` or discovery) is actually exported by the installed `@carbon/react` package. This prevents "Element type is invalid" errors caused by `undefined` imports.
- **Graceful Error Handling in Wrappers:** React wrappers for Dash components now include an existence check for the underlying Carbon component. If a component fails to load (e.g., due to dynamic import issues), it returns `null` rather than crashing the application.
- **Event Signature Normalization:** Carbon's event handlers vary significantly (some return events, some return value objects). The `eventMap` in `config.json` allows us to extract the correct value using `arguments` indexing.
- **Testing Portal-based Components:** Carbon components that use portals (like `Dropdown` or `Modal`) require specific Selenium interaction strategies. For example, using XPath to find options by text rather than CSS selectors can be more reliable when the menu is rendered outside the component's direct DOM hierarchy.
- **Nested Component Generation:** Automation now supports generating complex, multi-layered components (like `Tabs` or `Accordion`) by injecting relevant sub-components in automated tests.
- **Render-only Validation:** For purely structural or layout components (like `Grid` or `Row`), we've introduced a "render" test strategy that verifies the component appears in the DOM with its expected Carbon class names without requiring interactivity.
- **Event Handling Context:** We've successfully mapped complex event signatures, such as the `onChange` event for `RadioButtonGroup`, ensuring that Dash's `setProps` correctly captures the updated state.
- **CSS Variable Injection:** Carbon components rely on a specific CSS prefix (defaulting to `cds`). Our wrapper generation ensures that these prefixes are correctly applied and that all relevant styles are bundled into the final Dash component library.
- **Automated Test Stabilization:** Use `dash_duo.wait_for_element` instead of `find_element` to ensure the component is fully rendered and the React bundle is loaded before attempting interactions.
- **Boolean State in Tests:** Automated tests must explicitly cast boolean values to strings (`True`/`False`) to match the text output in the DOM for `wait_for_text_to_equal`.
- **Gatekeeper/Chromedriver:** macOS Gatekeeper can block `chromedriver`. Use `xattr -d com.apple.quarantine $(which chromedriver)` to resolve execution issues in the automation environment.
- **Story-driven Implementation:** Utilizing Carbon's raw `.stories.js` files (located in `_ref/carbon-design-system`) provides critical insights into complex component usage, such as `DataTable`'s render prop patterns, which informs the design of automated React wrappers.
- **DataTable Variant Support:** Enhanced `DataTable` wrappers now support `rows` and `headers` props directly, automatically rendering the necessary sub-components (`TableHead`, `TableBody`, etc.) while also supporting sorting, selection, and expansion variants.
- **Dynamic Prop Extraction:** The automation pipeline now automatically extracts `propTypes` from `@carbon/react` components, ensuring that all native Carbon props (like `kind`, `size`, `isPrimary`) are available in the Dash Python API without manual configuration.
- **Mandatory Dash Props:** All generated components now include standard Dash properties: `id`, `className`, `style`, `children`, and `setProps`. These are correctly passed through to the underlying Carbon components.
- **Invalid Identifier Sanitization:** Props containing hyphens (like `aria-label`) are automatically skipped during generation to prevent SyntaxErrors in the Dash Python backends, which do not support hyphens in keyword arguments.
- **Fragment Destructuring Safety:** The generator prevents duplicate variable declarations in React fragments by ensuring mandatory props are not redeclared if they also appear in custom `injectProps`.
- **Case-insensitive Component Discovery:** On macOS and other case-insensitive systems, the automation pipeline now handles casing conflicts (e.g., `AISkeletonText` vs `AiSkeletonText`) by prioritizing the first discovered variant, preventing file system collisions and build failures.
- **Dynamic Story-to-Python Parsing:** The gallery generator uses Babel AST traversal to extract JSX properties and children from Carbon story files, automatically translating them into Dash Python syntax with robust fallback and property filtering logic to ensure gallery stability.