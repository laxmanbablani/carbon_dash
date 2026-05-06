# Carbon Dash — Agent Instructions

`carbon_dash_components` is a Dash wrapper for IBM Carbon Design System components. Each component is hand-authored as a single React/JSX file following the dash-mantine-components pattern.

## Project Structure

```
carbon_dash_components/
├── src/lib/
│   ├── components/          # Hand-authored React component wrappers (.jsx)
│   └── utils/
│       └── dash.js          # getLoadingState + shared props
├── carbon_dash_components/             # Generated Python backends (NEVER manually edit)
│   └── __init__.py          # Package init (manual)
├── docs/                    # Standalone Dash Pages docs app (future)
│   └── run.py               # Entry point
├── tests/                   # dash_duo render tests per component
...
## Build Pipeline (2 steps)

```bash
npm run build:js          # Webpack bundles JS
npm run build:backends    # dash-generate-components reads src/lib/components/ → carbon_dash_components/
```
...
6. **NEVER edit `carbon_dash_components/*.py`** — they regenerate from PropTypes via `npm run build:backends`.

### Loading State Pattern

When loading, swap the component for its Carbon Skeleton equivalent:

```jsx
import { Button as CarbonButton, ButtonSkeleton as CarbonButtonSkeleton } from '@carbon/react';

const Button = (props) => {
    const { id, setProps, children, className, style, loading_state, ...others } = props;

    // Show skeleton while loading
    if (loading_state && loading_state.is_loading) {
        return (
            <CarbonButtonSkeleton
                id={id}
                className={className}
                style={style}
                size={others.size}
            />
        );
    }

    return (
        <CarbonButton id={id} className={className} style={style} {...others}>
            {children}
        </CarbonButton>
    );
};
```

### AI Label Pattern

Components that support AI labeling expose an `aiLabel` boolean prop. When `true`, the Carbon `AILabel` decorator renders:

```jsx
import { Button as CarbonButton, ButtonSkeleton as CarbonButtonSkeleton } from '@carbon/react';
import { AILabel } from '@carbon/react';

const Button = (props) => {
    const { aiLabel, ...others } = props;
    const decorator = aiLabel ? <AILabel size="xs" /> : undefined;
    
    return <CarbonButton decorator={decorator} {...others}>{children}</CarbonButton>;
};
```

### Icon Pattern

Icons are accepted as Dash children. Carbon's `renderIcon` slot accepts any React node:
- `dash_iconify.DashIconify(icon="carbon:launch")` — serialized Dash component
- `html.Div(className="my-icon", ...)` — any Dash HTML component
- String names mapped to Carbon icons via `resolveIcon`

The `resolveIcon` utility does:
1. `React.isValidElement` → pass through
2. `typeof string` → look up Carbon icon by name
3. Serialized Dash component `{type, namespace, props}` → render via `window[namespace][type]`

### Children Pattern

Children are standard Dash children — any Dash component, string, or number. No special handling needed. Dash's renderer auto-deserializes children into React elements. Example:

```python
cd.Button(
    cd.DashIconify(icon="carbon:add"),
    " Add Item",
    kind="primary",
)
```

## Adding a Component

1. Create `src/lib/components/<Name>.react.js` — hand-author the wrapper
2. Add import + export to `src/lib/index.js`
3. Write `tests/test_<name>.py` — dash_duo render test
4. Run `npm run build:js && npm run build:backends`
5. Run `pytest tests/test_<name>.py` to verify

## Testing

```bash
# All tests in parallel
python -m pytest tests/ -q --tb=no -n auto

# Single component
pytest tests/test_button.py -v
```

### Test Coverage Rules

Each test must verify:
1. **Component mounts without JS errors** — `dash_duo.wait_for_element("#id")` + `assert dash_duo.get_logs() == []`
2. **Key prop variations** — test the variations that Carbon's own stories test
3. **Interactive behavior** — if the component has `onClick`/`onChange`, test the callback fires

### How to Design Tests

Reference the Carbon stories to understand what constitutes a "real" usage:
`_ref/carbon-design-system/packages/react/src/components/<Name>/stories/`

Carbon stories test:
- **Default/standard usage** — the basic story, test this first
- **Prop variations** — each dimension of props (size: sm/md/lg, kind: primary/secondary/danger, etc.)
- **Edge cases** — disabled state, loading state, empty state

For each component, write tests covering:
1. **Basic render** — mounts, renders children, no JS errors
2. **Every prop dimension** — test at least 2 variants of each meaningful prop category
3. **Loading/skeleton** — if component has skeleton counterpart, test `loading_state={"is_loading": True}`
4. **Callback** — for interactive components, verify callback fires

### Test Pattern

```python
from dash import Dash, html
import carbon_dash_components as cd

def test_button_basic(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Button(id="btn", children="Click me")])
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#btn", "Click me")
    assert dash_duo.get_logs() == []

def test_button_variants(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.Button(id="b1", children="Primary"),
        cd.Button(id="b2", children="Danger", kind="danger"),
        cd.Button(id="b3", children="Disabled", disabled=True),
    ])
    dash_duo.start_server(app)
    for bid in ["b1", "b2", "b3"]:
        dash_duo.wait_for_text_to_equal(f"#{bid}", bid.replace("b", ""), timeout=10)
    assert dash_duo.get_logs() == []
```

### Charts

Charts import from `@carbon/charts` (core package), NOT `@carbon/charts-react`. Constructor: `new ChartClass(element, {data, options})`. Each chart has `clickData` and `selectedPoint` props for interactivity.

Components reference: `_ref/carbon-design-system/packages/react/src/components/<Name>/`
Charts reference: `_ref/carbon-charts/packages/docs/src/lib/<name>/`
Test example: `_ref/dash-mantine-components/tests/`