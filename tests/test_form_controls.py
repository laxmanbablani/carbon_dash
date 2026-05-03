"""Input component tests — Dropdown, NumberInput, Link, Tag."""
from dash import Dash, html
import carbon_dash as cd


def test_dropdown_renders(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Dropdown(id="dd", label="Pick", items=["A", "B"])])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#dd", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_dropdown_disabled(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Dropdown(id="dd-d", label="Pick", items=["A"], disabled=True)])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#dd-d", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_numberinput_default(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.NumberInput(id="ni", label="Count")])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#ni", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_numberinput_minmax(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.NumberInput(id="ni-mm", label="Range", min=0, max=10, value=5)])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#ni-mm", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_link_renders(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Link(id="lnk", children="Click here")])
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#lnk", "Click here", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_tag_default(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.Tag(id="tg", children="New", type="blue")])
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#tg", "New", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_tag_sizes(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.Tag(id="t-sm", children="S", size="sm"),
        cd.Tag(id="t-md", children="M", size="md"),
    ])
    dash_duo.start_server(app)
    for tid in ["t-sm", "t-md"]:
        dash_duo.wait_for_element(f"#{tid}", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"
