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

## Architectural Guidelines
*   **Idempotency:** The generation scripts must cleanly overwrite generated files without affecting manually maintained configuration files. Re-running the pipeline should safely synchronize the library with the latest `@carbon/react` version.
*   **Separation of Concerns:** Keep the generation scripts separate from the configuration logic. Edge cases and specific component behaviors must be handled via config files, not hardcoded into the generator.
*   **State Synchronization:** Ensure robust bridging between React's internal state management and Dash's `setProps` architecture, particularly for complex interactive components like DataTables and Tabs.