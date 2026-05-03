"""Tile component tests."""
from dash import Dash, html
import carbon_dash as cd

def test_tile_basic(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Tile(id="tl", children="Content")])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#tl", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_clickable_tile(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.ClickableTile(id="ctl", children="Click me")])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#ctl", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_selectable_tile(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.SelectableTile(id="stl", children="Select", value="opt1")])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#stl", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_expandable_tile(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.ExpandableTile(id="etl", children=[
        cd.TileAboveTheFoldContent(children=html.Div("Above", id="above")),
        cd.TileBelowTheFoldContent(children=html.Div("Below", id="below")),
    ])])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#etl", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_layer_renders(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Layer(id="lyr", children="Content")])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#lyr", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"
