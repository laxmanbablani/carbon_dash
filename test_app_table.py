import dash
from dash import html
import carbon_dash

app = dash.Dash(__name__)

# Basic Data for DataTable
headers = [
    {"key": "name", "header": "Name"},
    {"key": "protocol", "header": "Protocol"},
    {"key": "port", "header": "Port"},
    {"key": "rule", "header": "Rule"},
]

rows = [
    {"id": "a", "name": "Load Balancer 1", "protocol": "HTTP", "port": 80, "rule": "Round Robin"},
    {"id": "b", "name": "Load Balancer 2", "protocol": "HTTP", "port": 8080, "rule": "DNS LRD"},
    {"id": "c", "name": "Load Balancer 3", "protocol": "HTTP", "port": 8000, "rule": "Least Connections"},
]

app.layout = html.Div([
    html.H1("Carbon DataTable Basic Example"),
    carbon_dash.DataTable(
        id="basic-table",
        headers=headers,
        rows=rows,
        title="Load Balancers",
        description="A list of active load balancers in the system.",
    )
])

if __name__ == "__main__":
    app.run_server(debug=False, port=8091)
