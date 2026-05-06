"""Button component tests."""
from dash import Dash, html
import carbon_dash_components as cd

def test_button_renders(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.Button(id="btn", children="Click me"),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#btn", "Click me")
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_button_disabled(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.Button(id="btn-dis", children="Disabled", disabled=True),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#btn-dis", "Disabled")
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_button_skeleton(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.Button(id="btn-load", children="Loading", loading_state={"is_loading": True}),
    ])
    dash_duo.start_server(app)
    # Skeleton should render without JS errors
    dash_duo.wait_for_element("#btn-load", timeout=5)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"
