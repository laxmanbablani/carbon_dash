"""Checkbox and Toggle component tests — covers Carbon story variants."""
from dash import Dash, html
import carbon_dash_components as cd


def test_checkbox_default(dash_duo):
    """Default story: standard checkbox with label."""
    app = Dash(__name__)
    app.layout = html.Div([cd.Checkbox(id="cb", labelText="Check me")])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#cb", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_checkbox_checked(dash_duo):
    """Checked state."""
    app = Dash(__name__)
    app.layout = html.Div([cd.Checkbox(id="cb-c", labelText="Checked", checked=True)])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#cb-c", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_checkbox_disabled(dash_duo):
    """Disabled state."""
    app = Dash(__name__)
    app.layout = html.Div([cd.Checkbox(id="cb-d", labelText="Disabled", disabled=True)])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#cb-d", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_checkbox_indeterminate(dash_duo):
    """Indeterminate state."""
    app = Dash(__name__)
    app.layout = html.Div([cd.Checkbox(id="cb-i", labelText="Mixed", indeterminate=True)])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#cb-i", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_checkbox_skeleton(dash_duo):
    """Skeleton loading state."""
    app = Dash(__name__)
    app.layout = html.Div([cd.Checkbox(id="cb-sk", loading_state={"is_loading": True})])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#cb-sk", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_toggle_default(dash_duo):
    """Default toggle."""
    app = Dash(__name__)
    app.layout = html.Div([cd.Toggle(id="tg", labelText="Enable")])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#tg", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_toggle_toggled(dash_duo):
    """Toggled on state."""
    app = Dash(__name__)
    app.layout = html.Div([cd.Toggle(id="tg-on", labelText="On", toggled=True)])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#tg-on", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_toggle_disabled(dash_duo):
    """Disabled toggle."""
    app = Dash(__name__)
    app.layout = html.Div([cd.Toggle(id="tg-dis", labelText="Disabled", disabled=True)])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#tg-dis", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_toggle_small(dash_duo):
    """Small toggle variant from story."""
    app = Dash(__name__)
    app.layout = html.Div([cd.Toggle(id="tg-sm", labelText="Small", size="sm")])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#tg-sm", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_toggle_skeleton(dash_duo):
    """Skeleton loading state."""
    app = Dash(__name__)
    app.layout = html.Div([cd.Toggle(id="tg-sk", loading_state={"is_loading": True})])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#tg-sk", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"
