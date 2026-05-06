from dash import Dash, html
import carbon_dash_components as cd


def test_formgroup_basic(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.FormGroup(id="fg1", legendText="Basic Group", children=[
            cd.Checkbox(id="cb1", labelText="Option 1"),
        ]),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#fg1")
    dash_duo.wait_for_element("#cb1")
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"




def test_formgroup_message(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([
        cd.FormGroup(
            id="fg3",
            legendText="Message Group",
            message=True,
            messageText="This is a helper message",
            children=[
                cd.TextInput(id="ti4", placeholder="Input here"),
            ],
        ),
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#fg3")
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"