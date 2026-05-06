from dash import Dash, html
import carbon_dash_components as cd


def test_formlabel_basic(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.FormLabel(id="fl1", children="Label Text"),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#fl1", "Label Text")
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_formlabel_with_input(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.FormLabel(id="fl2", children="Username"),
        cd.TextInput(id="ti5", placeholder="Enter username"),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#fl2", "Username")
    dash_duo.wait_for_element("#ti5")
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_formlabel_custom_class(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.FormLabel(id="fl3", children="Styled Label", className="custom-label"),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#fl3", "Styled Label")
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"