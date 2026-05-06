from dash import Dash, html
import carbon_dash_components as cd


def test_form_basic(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.Form(id="form1", children=[
            cd.TextInput(id="ti1", placeholder="Enter text"),
        ]),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#form1")
    dash_duo.wait_for_element("#ti1")
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"


def test_form_with_label(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.Form(id="form2", children=[
            cd.FormLabel(id="label1", children="Form Label"),
            cd.TextInput(id="ti2", placeholder="Input here"),
        ]),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#label1", "Form Label")
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"