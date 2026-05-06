from dash import Dash, html
import carbon_dash_components as cd


def test_contentswitcher_basic(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.ContentSwitcher(
            id="cs1",
            children=[
                cd.Switch(id="sw1", text="Option 1", index=0),
                cd.Switch(id="sw2", text="Option 2", index=1),
            ],
        ),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#cs1")
    dash_duo.wait_for_text_to_equal("#sw1", "Option 1")
    dash_duo.wait_for_text_to_equal("#sw2", "Option 2")
    logs = dash_duo.get_logs()
    assert logs == [], "JS errors: %s" % logs


def test_contentswitcher_selected(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.ContentSwitcher(
            id="cs2",
            selected_index=1,
            children=[
                cd.Switch(id="sw3", text="First", index=0),
                cd.Switch(id="sw4", text="Second", index=1),
            ],
        ),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#cs2")
    logs = dash_duo.get_logs()
    assert logs == [], "JS errors: %s" % logs


def test_contentswitcher_size(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.ContentSwitcher(
            id="cs3",
            size="sm",
            children=[
                cd.Switch(id="sw5", text="Small", index=0),
            ],
        ),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#cs3")
    logs = dash_duo.get_logs()
    assert logs == [], "JS errors: %s" % logs
