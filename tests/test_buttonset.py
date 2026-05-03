from dash import Dash, html
import carbon_dash as cd


def test_buttonset_basic(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.ButtonSet(id="bs1", children=[
            cd.Button(id="btn1", children="Button 1"),
            cd.Button(id="btn2", children="Button 2"),
        ]),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#bs1")
    dash_duo.wait_for_text_to_equal("#btn1", "Button 1")
    dash_duo.wait_for_text_to_equal("#btn2", "Button 2")
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_buttonset_fluid(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.ButtonSet(id="bs2", fluid=True, children=[
            cd.Button(id="btn3", children="Fluid Button"),
        ]),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#bs2")
    dash_duo.wait_for_text_to_equal("#btn3", "Fluid Button")
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_buttonset_stacked(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.ButtonSet(id="bs3", stacked=True, children=[
            cd.Button(id="btn4", children="Stacked 1"),
            cd.Button(id="btn5", children="Stacked 2"),
        ]),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#bs3")
    dash_duo.wait_for_text_to_equal("#btn4", "Stacked 1")
    dash_duo.wait_for_text_to_equal("#btn5", "Stacked 2")
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"