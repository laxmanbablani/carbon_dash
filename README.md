# Carbon Dash

Carbon Dash is a Dash component library wrapping IBM's [Carbon Design System](https://carbondesignsystem.com/) React components for Python. Build Dash applications with Carbon's enterprise-grade UI components including buttons, forms, navigation, data tables, and charts.

## Installation

```bash
pip install carbon-dash-components
```

## Quick Start

```python
from dash import Dash, html, Input, Output
import carbon_dash_components as cd

app = Dash(__name__)

app.layout = html.Div([
    cd.Button(id="btn", children="Click me", kind="primary"),
    html.Div(id="output"),
])

@app.callback(
    Output("output", "children"),
    Input("btn", "n_clicks")
)
def update_output(n_clicks):
    return f"Button clicked {n_clicks} times"

if __name__ == "__main__":
    app.run_server(debug=True)
```

## Available Components

### Layout & Structure
- **Grid**, **Row**, **Column** - CSS Grid-based layout system
- **Stack** - Vertical/horizontal stacking utility
- **Layer** - Layering utility for z-index management

### Navigation
- **Breadcrumb**, **BreadcrumbItem** - Hierarchical navigation
- **Tabs**, **Tab**, **TabList**, **TabPanel**, **TabPanels** - Tabbed content
- **SideNav**, **SideNavLink**, **SideNavMenu**, **SideNavMenuItem** - Side navigation
- **Header**, **HeaderName**, **HeaderNavigation**, **HeaderMenu** - Application header
- **Pagination** - Data pagination controls
- **SkipToContent** - Accessibility skip link

### Forms & Inputs
- **Button**, **ButtonSet**, **IconButton**, **ComboButton** - Action buttons
- **TextInput**, **TextArea**, **NumberInput** - Text inputs
- **Select**, **SelectItem**, **MultiSelect** - Selection inputs
- **Dropdown**, **ComboBox** - Dropdown/select components
- **DatePicker**, **DatePickerInput**, **TimePicker** - Date/time pickers
- **Checkbox**, **CheckboxGroup**, **RadioButton**, **RadioButtonGroup** - Selection controls
- **Switch**, **Toggle** - Toggle switches
- **Search** - Search input
- **Slider** - Range slider

### Fluid Components
- **FluidTextInput**, **FluidTextArea**, **FluidNumberInput**
- **FluidSelect**, **FluidMultiSelect**, **FluidComboBox**
- **FluidDatePicker**, **FluidDatePickerInput**
- **FluidSearch**, **FluidDropdown**, **FluidPasswordInput**

### Data Display
- **DataTable** - Interactive data tables
- **CodeSnippet** - Code display with copy
- **Tag** - Label/tags display
- **Text** - Text component
- **Heading** - Heading text

### Feedback & Overlays
- **Modal** - Dialog overlays
- **Loading** - Loading indicators
- **ProgressIndicator**, **ProgressBar** - Progress displays
- **Toast**, **InlineNotification** - Notifications

### Tiles & Media
- **Tile**, **ClickableTile**, **SelectableTile**, **ExpandableTile** - Content tiles
- **TileAboveTheFoldContent**, **TileBelowTheFoldContent** - Tile content sections

### Charts
- **AreaChart**, **LineChart**, **BarChart**, **GroupedBarChart**, **StackedBarChart**
- **PieChart**, **DonutChart** - Pie/donut charts
- **GaugeChart**, **MeterChart** - Gauge/meter charts
- **HistogramChart**, **BoxplotChart**, **ScatterChart**
- **BubbleChart**, **LollipopChart**, **RadarChart**, **HeatmapChart**
- **ChoroplethChart**, **TreemapChart**, **CirclePackChart**, **TreeChart**
- **AlluvialChart**, **WordCloudChart**

### Utility Components
- **Form**, **FormGroup**, **FormItem**, **FormLabel** - Form structure
- **Content**, **ContentSwitcher** - Content containers
- **OverflowMenu**, **OverflowMenuItem** - Overflow menus
- **Tooltip**, **Link** - Helper components

## Development

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm

### Setup

```bash
# Clone the repository
git clone https://github.com/your-org/carbon_dash.git
cd carbon_dash

# Install npm dependencies
npm install

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
```

### Build

```bash
# Build JavaScript and generate Python backends
npm run build

# Or run separately:
npm run build:js        # Webpack bundle
npm run build:backends  # Generate Python components
```

### Testing

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_button.py -v

# Run tests in parallel
pytest tests/ -n auto
```

## Component Pattern

Each component follows the standard Dash pattern:

```python
import carbon_dash_components as cd

# Basic usage
cd.Button(id="primary-btn", children="Submit", kind="primary")

# With icon
cd.Button(
    id="icon-btn",
    children="Launch",
    renderIcon={"icon": "launch"},
    hasIconOnly=True
)

# Loading state
cd.Button(id="loading-btn", children="Saving...", loading_state={"is_loading": True})

# Click callback
@app.callback(
    Output("output", "children"),
    Input("primary-btn", "n_clicks")
)
def handle_click(n_clicks):
    return f"Clicked {n_clicks} times"
```

## AI Label Support

Components that support AI labeling expose an `aiLabel` prop:

```python
cd.Button(id="ai-btn", children="AI Action", aiLabel=True)
```

## Icon Support

Icons can be rendered using `dash_iconify` or Carbon icon names:

```python
import dash_iconify

cd.Button(
    id="icon-btn",
    children="Add item",
    renderIcon=dash_iconify.DashIconify(icon="carbon:add")
)
```

## Publishing

To publish a new version to PyPI:

1. Bump the version in `package.json` (and optionally `carbon_dash_components/__init__.py` if needed).
2. Commit and push to GitHub.
3. Create a GitHub Release with a tag `vX.Y.Z` matching the version. The release will automatically trigger the `Publish to PyPI` workflow.
4. The workflow builds the JavaScript bundles, generates Python backends, and publishes the package to PyPI using trusted publishing.

## License

MIT License

Copyright (c) 2024 Laxman Bablani

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Links

- [Carbon Design System](https://carbondesignsystem.com/)
- [Dash Documentation](https://dash.plotly.com/)
- [IBM Carbon React](https://github.com/carbon-design-system/carbon/tree/main/packages/react)