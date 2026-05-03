from dash import Dash, html
import carbon_dash as cd


def test_aspectratio_basic(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.AspectRatio(id="ar1", children=html.Div("Content")),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#ar1")
    logs = dash_duo.get_logs()
    assert logs == [], "JS errors: %s" % logs


def test_aspectratio_16x9(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.AspectRatio(id="ar2", ratio="16x9", children=html.Div("16:9 Content")),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#ar2")
    logs = dash_duo.get_logs()
    assert logs == [], "JS errors: %s" % logs


def test_aspectratio_4x3(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.AspectRatio(id="ar3", ratio="4x3", children=html.Div("4:3 Content")),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#ar3")
    logs = dash_duo.get_logs()
    assert logs == [], "JS errors: %s" % logs
