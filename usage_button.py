import carbon_dash
from dash import Dash, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    carbon_dash.Button(
        id='my-button',
        kind='primary',
        children='Click me!',
    ),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    Input('my-button', 'n_clicks')
)
def update_output(n_clicks):
    if n_clicks is None:
        n_clicks = 0
    return f'Button has been clicked {n_clicks} times'

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
