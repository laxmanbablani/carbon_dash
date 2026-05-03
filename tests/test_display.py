"""Tabs, Accordion, Stack component tests."""
from dash import Dash, html
import carbon_dash as cd

def test_tabs_basic(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Tabs(id="tabs", children=[
        cd.TabList(children=[cd.Tab(id="t1", label="Tab 1")]),
        cd.TabPanels(children=[cd.TabPanel(children="Panel 1", id="p1")]),
    ])])
    dash_duo.start_server(app)
    dash_duo.wait_for_element(".cds--tabs", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_accordion_basic(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Accordion(id="acc", children=[
        cd.AccordionItem(id="ai", title="Section 1", children="Content"),
    ])])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#ai", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_stack_renders(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Stack(id="stk", children=[
        html.Div("A"), html.Div("B"),
    ])])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#stk", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_loading_active(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Loading(id="ld", active=True)])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#ld", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_codesnippet_single(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.CodeSnippet(id="cs", children="print('hello')", type="single")])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#cs", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_codesnippet_multi(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.CodeSnippet(id="cs2", children="line1\nline2\nline3", type="multi")])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#cs2", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"
