"""DatePicker and TimePicker tests."""
from dash import Dash, html
import carbon_dash as cd

def test_datepicker_renders(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.DatePicker(id="dp", datePickerType="single", children=[
        cd.DatePickerInput(id="dpi", labelText="Date", placeholder="mm/dd/yyyy"),
    ])])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#dp", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_datepicker_range(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.DatePicker(id="dp-r", datePickerType="range", children=[
        cd.DatePickerInput(id="dpi1", labelText="Start", placeholder="mm/dd/yyyy"),
        cd.DatePickerInput(id="dpi2", labelText="End", placeholder="mm/dd/yyyy"),
    ])])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#dp-r", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"

def test_timepicker_renders(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([cd.TimePicker(id="tp", labelText="Time")])
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#tp", timeout=10)
    assert dash_duo.get_logs() == [], f"JS errors: {dash_duo.get_logs()}"
