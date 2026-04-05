import carbon_dash
from dash import Dash, html, Input, Output
import time

def test_numberinput_interaction(dash_duo):
    app = Dash(__name__)

    app.layout = html.Div([
        carbon_dash.NumberInput(
            id='test-numberinput',
            
            
            
            
            
            
            
            
            
            
            
        ),
        html.Div(id='output', children='initial')
    ])

    @app.callback(
        Output('output', 'children'),
        Input('test-numberinput', 'value'),
        prevent_initial_call=True
    )
    def update_output(val):
        return str(val)

    dash_duo.start_server(app)

    
    el = dash_duo.wait_for_element("#test-numberinput")
    el.send_keys('42')
    
    
    dash_duo.wait_for_text_to_equal('#output', str('42'))
