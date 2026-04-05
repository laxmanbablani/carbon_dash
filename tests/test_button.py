import carbon_dash
from dash import Dash, html, Input, Output
import time

def test_button_interaction(dash_duo):
    app = Dash(__name__)

    app.layout = html.Div([
        carbon_dash.Button(
            id='test-button',
            children='Click me!',
            
            
            
            
            
            
            
            
            
            
        ),
        html.Div(id='output', children='initial')
    ])

    @app.callback(
        Output('output', 'children'),
        Input('test-button', 'n_clicks'),
        prevent_initial_call=True
    )
    def update_output(val):
        return str(val)

    dash_duo.start_server(app)

    
    el = dash_duo.wait_for_element("#test-button")
    dash_duo.driver.execute_script("arguments[0].click();", el)
    
    
    dash_duo.wait_for_text_to_equal('#output', str('1'))
