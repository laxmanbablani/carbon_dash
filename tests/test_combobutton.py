from dash import Dash, html, dependencies
import carbon_dash_components as cd


def test_combobutton_basic(dash_duo):
    """Test that ComboButton mounts without JS errors."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.ComboButton(
            id="combo-btn",
            label="Primary action",
            children=[
                cd.MenuItem(label="Second action"),
                cd.MenuItem(label="Third action"),
            ]
        )
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#combo-btn", "Primary action")
    assert dash_duo.get_logs() == []


def test_combobutton_click(dash_duo):
    """Test that ComboButton click callback fires."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.ComboButton(
            id="combo-btn",
            label="Click me",
        ),
        html.Div(id="output", children="Not clicked")
    ])

    @app.callback(
        dependencies.Output("output", "children"),
        [dependencies.Input("combo-btn", "n_clicks")],
    )
    def update_output(n_clicks):
        return f"Clicked {n_clicks} times"

    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#combo-btn", "Click me")
    dash_duo.click_at_coord_fractions("#combo-btn", 0.5, 0.5)
    dash_duo.wait_for_text_to_equal("#output", "Clicked 1 times")
    assert dash_duo.get_logs() == []


def test_combobutton_with_menuitem(dash_duo):
    """Test ComboButton with MenuItem children."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.ComboButton(
            id="combo-btn",
            label="Primary action",
            children=[
                cd.MenuItem(label="Second action"),
                cd.MenuItemDivider(),
                cd.MenuItem(label="Third action", kind="danger"),
            ]
        )
    ])
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#combo-btn", "Primary action")
    assert dash_duo.get_logs() == []


def test_combobutton_disabled(dash_duo):
    """Test that disabled ComboButton doesn't fire callbacks."""
    app = Dash(__name__)
    app.layout = html.Div([
        cd.ComboButton(
            id="combo-btn",
            label="Disabled",
            disabled=True,
        ),
        html.Div(id="output", children="Not clicked")
    ])

    @app.callback(
        dependencies.Output("output", "children"),
        [dependencies.Input("combo-btn", "n_clicks")],
    )
    def update_output(n_clicks):
        return f"Clicked {n_clicks} times"

    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#combo-btn", "Disabled")
    assert dash_duo.get_logs() == []