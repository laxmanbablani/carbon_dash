import pytest
from dash.testing.composite import DashComposite
import os
import sys

# Ensure the project root is in PYTHONPATH
sys.path.append(os.getcwd())

def test_table_simple_rendering(dash_duo):
    from test_app_table import app
    
    dash_duo.start_server(app)
    
    # Wait for the data table to be rendered
    # In Carbon, DataTable usually has class .cds--data-table
    try:
        dash_duo.wait_for_element(".cds--data-table", timeout=10)
    except Exception:
        print("DOM structure when timeout occurred:")
        print(dash_duo.find_element("body").get_attribute("innerHTML"))
        raise
    
    # Check if the title is rendered
    assert dash_duo.find_element(".cds--data-table-header__title").text == "Load Balancers"
    
    # Check if we have 3 rows + 1 header row (sometimes header is distinct)
    rows = dash_duo.find_elements("table.cds--data-table tbody tr")
    assert len(rows) == 3
    
    # Check for JS errors
    logs = dash_duo.get_logs()
    js_errors = [log for log in logs if log['level'] == 'SEVERE']
    
    if js_errors:
        print("\nJavaScript Errors detected:")
        for error in js_errors:
            print(f"[{error['timestamp']}] {error['level']}: {error['message']}")
    
    assert not js_errors, f"Detected {len(js_errors)} JavaScript errors in console"

def test_table_expansion_rendering(dash_duo):
    import dash
    from dash import html
    import carbon_dash
    
    headers = [{"key": "name", "header": "Name"}, {"key": "status", "header": "Status"}]
    rows = [
        {"id": "a", "name": "App 1", "status": "Active", "description": "This is app 1"},
        {"id": "b", "name": "App 2", "status": "Inactive", "description": "This is app 2"},
    ]
    
    app = dash.Dash(__name__)
    app.layout = html.Div([
        carbon_dash.DataTable(
            id="expansion-table",
            headers=headers,
            rows=rows,
            withExpansion=True,
        )
    ])
    
    dash_duo.start_server(app)
    dash_duo.wait_for_element(".cds--data-table", timeout=10)
    
    # Check for expand buttons
    try:
        dash_duo.wait_for_element(".cds--table-expand__button", timeout=10)
        expand_buttons = dash_duo.find_elements(".cds--table-expand__button")
        assert len(expand_buttons) == 2
    except Exception:
        print("Expansion table HTML:")
        print(dash_duo.find_element("body").get_attribute("innerHTML"))
        print("\nAll Browser Logs:")
        for log in dash_duo.get_logs():
            print(f"[{log['timestamp']}] {log['level']}: {log['message']}")
        raise
    
    # Check for JS errors
    logs = dash_duo.get_logs()
    js_errors = [log for log in logs if log['level'] == 'SEVERE']
    assert not js_errors, f"Detected {len(js_errors)} JavaScript errors in expansion table"

def test_table_modular_rendering(dash_duo):
    import dash
    from dash import html
    import carbon_dash
    
    app = dash.Dash(__name__)
    app.layout = html.Div([
        carbon_dash.Table(id="modular-table", children=[
            carbon_dash.TableHead(children=[
                carbon_dash.TableRow(children=[
                    carbon_dash.TableHeader(children="Column 1"),
                    carbon_dash.TableHeader(children="Column 2"),
                ])
            ]),
            carbon_dash.TableBody(children=[
                carbon_dash.TableRow(children=[
                    carbon_dash.TableCell(children="Cell 1-1"),
                    carbon_dash.TableCell(children="Cell 1-2"),
                ])
            ])
        ])
    ])
    
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#modular-table", timeout=10)
    
    # Verify content
    assert dash_duo.find_element("th").text == "Column 1"
    assert dash_duo.find_element("td").text == "Cell 1-1"
    
    # Check for JS errors
    logs = dash_duo.get_logs()
    js_errors = [log for log in logs if log['level'] == 'SEVERE']
    assert not js_errors, f"Detected {len(js_errors)} JavaScript errors in modular table"
