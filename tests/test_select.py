import carbon_dash
from dash import Dash, html, Input, Output
import time

def test_select_interaction(dash_duo):
    app = Dash(__name__)

    app.layout = html.Div([
        carbon_dash.Select(
            id='test-select',
            
            
            children=[carbon_dash.SelectItem(text='Option 1', value='Option 1'), carbon_dash.SelectItem(text='Option 2', value='Option 2')],
            
            
            
            
            
            
            
            
        ),
        html.Div(id='output', children='initial')
    ])

    @app.callback(
        Output('output', 'children'),
        Input('test-select', 'value'),
        prevent_initial_call=True
    )
    def update_output(val):
        return str(val)

    dash_duo.start_server(app)

    
    el = dash_duo.wait_for_element("#test-select option[value='Option 1']")
    dash_duo.driver.execute_script("arguments[0].click();", el)
    
    
    dash_duo.wait_for_text_to_equal('#output', str('Option 1'))
