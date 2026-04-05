import carbon_dash
from dash import Dash, html, Input, Output
import time

def test_fluidmultiselect_interaction(dash_duo):
    app = Dash(__name__)

    app.layout = html.Div([
        carbon_dash.FluidMultiSelect(
            id='test-fluidmultiselect',
            
            
            
            
            
            
            
            
            
            
            
        ),
        html.Div(id='output', children='initial')
    ])

    @app.callback(
        Output('output', 'children'),
        Input('test-fluidmultiselect', 'id'),
        prevent_initial_call=True
    )
    def update_output(val):
        return str(val)

    dash_duo.start_server(app)

    
    dash_duo.wait_for_element(".cds--${name.toLowerCase()}")
    
    
    
