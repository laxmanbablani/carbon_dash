"""Grid, Row, Column component tests."""
from dash import Dash, html
import carbon_dash_components as cd

def test_grid_renders(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Grid(id="g", children=[
        cd.Row(children=[cd.Column(children="Hello", sm=4)])
    ])])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#g", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_column_sizes(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Grid(children=[
        cd.Row(children=[
            cd.Column(children="A", sm=12, md=8, lg=6, id="c1"),
            cd.Column(children="B", sm=12, md=8, lg=6, id="c2"),
        ])
    ])])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#c1", timeout=10)
    dash_duo.wait_for_element("#c2", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_grid_condensed(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Grid(id="g2", condensed=True, children=[
        cd.Row(children=[cd.Column(children="Item")])
    ])])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#g2", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"
