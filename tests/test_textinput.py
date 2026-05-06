"""TextInput component tests — covers Carbon story variants."""
from dash import Dash, html
import carbon_dash_components as cd


def test_textinput_default(dash_duo):
    """Default story: standard input with label and placeholder."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.TextInput(
            id="ti", labelText="Label text", placeholder="Placeholder text",
        ),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#ti", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_textinput_readonly(dash_duo):
    """ReadOnly story: readonly input with a default value."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.TextInput(
            id="ti-ro", labelText="Read only", readOnly=True,
            defaultValue="This is read only",
        ),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#ti-ro", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_textinput_invalid(dash_duo):
    """Invalid state: error message visible."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.TextInput(
            id="ti-inv", labelText="Email", invalid=True,
            invalidText="Error message",
        ),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#ti-inv", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_textinput_warn(dash_duo):
    """Warning state."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.TextInput(id="ti-w", labelText="Field", warn=True, warnText="Warning message"),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#ti-w", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_textinput_skeleton(dash_duo):
    """Skeleton story: loading state shows skeleton."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.TextInput(id="ti-sk", loading_state={"is_loading": True}),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#ti-sk", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_textinput_disabled(dash_duo):
    """Disabled state."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.TextInput(id="ti-dis", labelText="Disabled", disabled=True),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#ti-dis", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_textinput_ai_label(dash_duo):
    """AI Label story: decorator renders alongside the input."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.TextInput(id="ti-ai", labelText="AI Field", aiLabel=True),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#ti-ai", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_textinput_sizes(dash_duo):
    """All size variants."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.TextInput(id="s-sm", labelText="Small", size="sm"),
        cd.TextInput(id="s-md", labelText="Medium", size="md"),
        cd.TextInput(id="s-lg", labelText="Large", size="lg"),
    ])
    dash_duo.start_server(app)
    for sid in ["s-sm", "s-md", "s-lg"]:
        dash_duo.wait_for_element(f"#{sid}", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"
