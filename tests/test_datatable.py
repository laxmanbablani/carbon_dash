"""DataTable tests — basic, sorting, selection, skeleton."""
from dash import Dash, html
import carbon_dash_components as cd

ROWS = [
    {"id": "a", "name": "Alpha", "score": 95},
    {"id": "b", "name": "Beta", "score": 85},
    {"id": "c", "name": "Gamma", "score": 72},
]
HEADERS = [
    {"key": "name", "header": "Name"},
    {"key": "score", "header": "Score"},
]

def test_datatable_basic(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.DataTable(id="dt", rows=ROWS, headers=HEADERS)])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#dt", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_datatable_sortable(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.DataTable(id="dt-s", rows=ROWS, headers=HEADERS, isSortable=True)])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#dt-s", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_datatable_selection(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.DataTable(id="dt-sel", rows=ROWS, headers=HEADERS, withSelection=True)])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#dt-sel", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_datatable_toolbar(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.DataTable(id="dt-tb", rows=ROWS, headers=HEADERS, withToolbar=True)])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#dt-tb", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_datatable_skeleton(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.DataTable(id="dt-sk", loading_state={"is_loading": True})])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#dt-sk", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_datatable_zebra(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.DataTable(id="dt-z", rows=ROWS, headers=HEADERS, useZebraStyles=True)])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#dt-z", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_datatable_title(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.DataTable(id="dt-t", rows=ROWS, headers=HEADERS, title="My Table", description="A sample table")])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#dt-t", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"
