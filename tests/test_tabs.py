import carbon_dash
from dash import Dash, html, Input, Output
import time

def test_tabs_interaction(dash_duo):
    app = Dash(__name__)

    app.layout = html.Div([
        carbon_dash.Tabs(
            id='test-tabs',
            
            
            
            
            
            
            children=[carbon_dash.TabList(children=[carbon_dash.Tab(label='Tab 1')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Panel 1')])],
            
            
            
            
        ),
        html.Div(id='output', children='initial')
    ])

    @app.callback(
        Output('output', 'children'),
        Input('test-tabs', 'id'),
        prevent_initial_call=True
    )
    def update_output(val):
        return str(val)

    dash_duo.start_server(app)

    
    dash_duo.wait_for_element(".cds--tabs")
    
    
    
