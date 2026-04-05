import carbon_dash
from dash import Dash, html, Input, Output
import time

def test_radiobuttongroup_interaction(dash_duo):
    app = Dash(__name__)

    app.layout = html.Div([
        carbon_dash.RadioButtonGroup(
            id='test-radiobuttongroup',
            
            
            
            children=[carbon_dash.RadioButton(id='opt1', label='Opt 1', value='opt1'), carbon_dash.RadioButton(id='opt2', label='Opt 2', value='opt2')],
            
            
            
            
            
            
            
        ),
        html.Div(id='output', children='initial')
    ])

    @app.callback(
        Output('output', 'children'),
        Input('test-radiobuttongroup', 'valueSelected'),
        prevent_initial_call=True
    )
    def update_output(val):
        return str(val)

    dash_duo.start_server(app)

    
    el = dash_duo.wait_for_element("label[for='opt1']")
    dash_duo.driver.execute_script("arguments[0].click();", el)
    
    
    dash_duo.wait_for_text_to_equal('#output', str('opt1'))
