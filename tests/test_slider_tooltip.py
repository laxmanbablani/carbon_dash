"""Slider and Tooltip tests."""
from dash import Dash, html
import carbon_dash_components as cd

def test_slider_renders(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Slider(id="sld", labelText="Volume", min=0, max=100, value=50)])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sld", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_slider_disabled(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Slider(id="sld-d", labelText="Disabled", disabled=True)])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sld-d", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_tooltip_renders(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Tooltip(id="tt", label="Help", children=html.Span("Hover", id="tt-inner"))])
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#tt-inner", "Hover", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"
