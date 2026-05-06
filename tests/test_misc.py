"""Modal, Search, and misc component tests."""
from dash import Dash, html
import carbon_dash_components as cd


def test_modal_open(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Modal(id="mod", open=True, modalHeading="Hello", children="Content")])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#mod", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_search_renders(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Search(id="srch", labelText="Find")])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#srch", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_search_disabled(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Search(id="srch-d", labelText="Find", disabled=True)])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#srch-d", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"
