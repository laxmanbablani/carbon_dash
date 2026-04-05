import carbon_dash
from dash import Dash, html, Input, Output
import time

def test_dropdown_interaction(dash_duo):
    app = Dash(__name__)

    app.layout = html.Div([
        carbon_dash.Dropdown(
            id='test-dropdown',
            
            items=['Option 1', 'Option 2'],
            
            
            
            
            
            
            
            
            
        ),
        html.Div(id='output', children='initial')
    ])

    @app.callback(
        Output('output', 'children'),
        Input('test-dropdown', 'selectedItem'),
        prevent_initial_call=True
    )
    def update_output(val):
        return str(val)

    dash_duo.start_server(app)

    
    # Open dropdown
    dash_duo.driver.find_element("css selector", "#test-dropdown button").click()
    # Wait for options and click first one
    time.sleep(1)
    dash_duo.driver.find_element("xpath", "//div[contains(@class, 'cds--list-box__menu-item__option') and text()='Option 1']").click()
    
    
    dash_duo.wait_for_text_to_equal('#output', str('Option 1'))
