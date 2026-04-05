import carbon_dash
from dash import Dash, html, Input, Output
import time

def test_datatable_interaction(dash_duo):
    app = Dash(__name__)

    app.layout = html.Div([
        carbon_dash.DataTable(
            id='test-datatable',
            
            
            
            
            
            
            
            
            
            
            
        ),
        html.Div(id='output', children='initial')
    ])

    @app.callback(
        Output('output', 'children'),
        Input('test-datatable', 'id'),
        prevent_initial_call=True
    )
    def update_output(val):
        return str(val)

    dash_duo.start_server(app)

    
    dash_duo.wait_for_element(".cds--data-table")
    
    
    
