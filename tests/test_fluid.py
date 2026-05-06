from dash import Dash, html
import carbon_dash_components as cd


def test_fluidtextinput_basic(dash_duo):
    """Test that FluidTextInput mounts without JS errors."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.FluidTextInput(
            id="fluid-input",
            labelText="Fluid Input",
            placeholder="Enter text"
        )
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#fluid-input")
    assert dash_duo.get_logs() == []


def test_fluidtextinput_value(dash_duo):
    """Test that FluidTextInput value can be set."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.FluidTextInput(
            id="fluid-input",
            labelText="Fluid Input",
            value="initial"
        )
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#fluid-input")
    assert dash_duo.get_logs() == []


def test_fluidpasswordinput_basic(dash_duo):
    """Test that FluidPasswordInput mounts without JS errors."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.FluidPasswordInput(
            id="fluid-password",
            labelText="Password"
        )
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#fluid-password")
    assert dash_duo.get_logs() == []


def test_fluidcombobox_basic(dash_duo):
    """Test that FluidComboBox mounts without JS errors."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.FluidComboBox(
            id="fluid-combo",
            labelText="Choose an option",
            items=[
                {"id": "1", "text": "Option 1"},
                {"id": "2", "text": "Option 2"},
            ]
        )
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#fluid-combo")
    assert dash_duo.get_logs() == []


def test_fluiddropdown_basic(dash_duo):
    """Test that FluidDropdown mounts without JS errors."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.FluidDropdown(
            id="fluid-dropdown",
            label="Choose an option",
            items=[
                {"id": "1", "text": "Option 1"},
                {"id": "2", "text": "Option 2"},
            ]
        )
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#fluid-dropdown")
    assert dash_duo.get_logs() == []


def test_fluidnumberinput_basic(dash_duo):
    """Test that FluidNumberInput mounts without JS errors."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.FluidNumberInput(
            id="fluid-number",
            labelText="Number"
        )
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#fluid-number")
    assert dash_duo.get_logs() == []


def test_fluidsearch_basic(dash_duo):
    """Test that FluidSearch mounts without JS errors."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.FluidSearch(
            id="fluid-search",
            labelText="Search"
        )
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#fluid-search")
    assert dash_duo.get_logs() == []


def test_fluidtextarea_basic(dash_duo):
    """Test that FluidTextArea mounts without JS errors."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.FluidTextArea(
            id="fluid-textarea",
            labelText="Text Area"
        )
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#fluid-textarea")
    assert dash_duo.get_logs() == []