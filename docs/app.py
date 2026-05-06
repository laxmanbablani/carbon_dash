"""Carbon Dash Demo — Dashboard with all 25 charts, routing, and components."""
import dash
from dash import html, dcc, Output, Input, callback, State
import carbon_dash_components as cd

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    cd.Header(children=[
        cd.HeaderName(children="Carbon Dash"),
        cd.HeaderGlobalBar(children=[cd.HeaderGlobalAction(children="⚙️", id="settings-btn")]),
    ]),
    html.Div([
        cd.SideNav(children=[
            cd.SideNavItems(children=[
                cd.SideNavLink(children="Dashboard", href="/"),
                cd.SideNavLink(children="Charts", href="/charts"),
                cd.SideNavLink(children="Settings", href="/settings"),
            ]),
        ], isFixedNav=True, expanded=True, style={"width":"240px"}),
        cd.Content(children=[html.Div(id="page-content")], style={"padding":"2rem"}),
    ], style={"display":"flex","marginTop":"48px"}),
    cd.Modal(id="settings-modal", open=False, modalHeading="Settings", children="Settings panel"),
])

# ── Routing ───────────────────────────────────────────────────────────
@callback(Output("page-content","children"), Input("url","pathname"))
def render_page(path):
    if path == "/charts":
        return CHARTS
    elif path == "/settings":
        return SETTINGS
    return DASHBOARD  # home

# ── Dashboard ──────────────────────────────────────────────────────────
DASHBOARD = [
    cd.Heading(children="Dashboard", level=1),
    cd.Grid(children=[
        cd.Row(children=[
            cd.Column(sm=12, md=6, lg=3, children=[cd.Tile(children=[cd.Heading(children="$610K",level=3),cd.Text(children="Total Revenue")])]),
            cd.Column(sm=12, md=6, lg=3, children=[cd.Tile(children=[cd.Heading(children="1,245",level=3),cd.Text(children="Active Users")])]),
            cd.Column(sm=12, md=6, lg=3, children=[cd.Tile(children=[cd.Heading(children="98.5%",level=3),cd.Text(children="Uptime")])]),
            cd.Column(sm=12, md=6, lg=3, children=[cd.Tile(children=[cd.Heading(children="12",level=3),cd.Text(children="Deployments")])]),
        ]),
    ]),
    cd.Heading(children="Accounts", level=2),
    cd.DataTable(id="tbl", title="Client Accounts", rows=[
        {"id":"a","name":"Alpha Corp","status":"Active","rev":"$45K"},
        {"id":"b","name":"Beta Inc","status":"Active","rev":"$52K"},
        {"id":"c","name":"Gamma LLC","status":"Inactive","rev":"$18K"},
        {"id":"d","name":"Delta Co","status":"Active","rev":"$73K"},
    ], headers=[{"key":"name","header":"Name"},{"key":"status","header":"Status"},{"key":"rev","header":"Revenue"}],
        withToolbar=True, isSortable=True, useZebraStyles=True),
    cd.Pagination(id="pgn", totalItems=50, pageSize=10),
    cd.Heading(children="Add Account", level=2),
    cd.TextInput(id="name", labelText="Account Name"),
    cd.Button(id="add-btn", children="Add Account", kind="primary"),
]

# ── Charts Gallery ─────────────────────────────────────────────────────
def chart_column(chart_id, ChartClass, data, options, height="250px"):
    return html.Div(children=[
        ChartClass(id=chart_id, data=data, options={**options, "height": height}),
    ], style={"flex": "1 1 300px", "maxWidth": "500px", "margin": "0.5rem"})

CHARTS = [
    cd.Heading(children="Charts Gallery", level=1),
    cd.Text(children="All 25 Carbon Chart types with sample data."),
    html.Div(children=[
        chart_column("bar", cd.SimpleBarChart, [{"group":"A","value":65},{"group":"B","value":29},{"group":"C","value":35}],
            {"title":"SimpleBarChart","axes":{"left":{"mapsTo":"value"},"bottom":{"mapsTo":"group"}}}),
        chart_column("gbar", cd.GroupedBarChart, [{"group":"Q1","key":"A","value":45},{"group":"Q1","key":"B","value":30},{"group":"Q2","key":"A","value":55},{"group":"Q2","key":"B","value":28}],
            {"title":"GroupedBarChart","axes":{"left":{"mapsTo":"value"},"bottom":{"mapsTo":"key"}}}),
        chart_column("sbar", cd.StackedBarChart, [{"group":"Q1","key":"A","value":30},{"group":"Q1","key":"B","value":20},{"group":"Q2","key":"A","value":40},{"group":"Q2","key":"B","value":25}],
            {"title":"StackedBarChart","axes":{"left":{"mapsTo":"value"},"bottom":{"mapsTo":"key"}}}),
        chart_column("line", cd.LineChart, [{"group":"S","date":"Jan","value":42},{"group":"S","date":"Feb","value":51},{"group":"S","date":"Mar","value":48}],
            {"title":"LineChart","axes":{"left":{"mapsTo":"value"},"bottom":{"mapsTo":"date"}}}),
        chart_column("area", cd.AreaChart, [{"group":"A","date":"Jan","value":30},{"group":"A","date":"Feb","value":40},{"group":"B","date":"Jan","value":20},{"group":"B","date":"Feb","value":25}],
            {"title":"AreaChart","axes":{"left":{"mapsTo":"value"},"bottom":{"mapsTo":"date"}}}),
        chart_column("sarea", cd.StackedAreaChart, [{"group":"A","date":"Jan","value":30},{"group":"A","date":"Feb","value":40},{"group":"B","date":"Jan","value":20},{"group":"B","date":"Feb","value":25}],
            {"title":"StackedAreaChart","axes":{"left":{"mapsTo":"value"},"bottom":{"mapsTo":"date"}}}),
        chart_column("pie", cd.PieChart, [{"group":"A","value":45},{"group":"B","value":30},{"group":"C","value":25}],
            {"title":"PieChart"}),
        chart_column("donut", cd.DonutChart, [{"group":"C","value":55},{"group":"O","value":25},{"group":"H","value":20}],
            {"title":"DonutChart"}),
        chart_column("scatter", cd.ScatterChart, [{"group":"A","x":10,"y":20},{"group":"A","x":20,"y":30},{"group":"B","x":15,"y":25}],
            {"title":"ScatterChart","axes":{"bottom":{"mapsTo":"x"},"left":{"mapsTo":"y"}}}),
        chart_column("bubble", cd.BubbleChart, [{"group":"A","x":10,"y":20,"value":100},{"group":"A","x":20,"y":30,"value":200},{"group":"B","x":15,"y":25,"value":150}],
            {"title":"BubbleChart","axes":{"bottom":{"mapsTo":"x"},"left":{"mapsTo":"y"}}}),
        chart_column("radar", cd.RadarChart, [{"group":"A","key":"Speed","value":80},{"group":"A","key":"Qlty","value":70},{"group":"A","key":"Price","value":60}],
            {"title":"RadarChart","axes":{"bottom":{"mapsTo":"key"},"left":{"mapsTo":"value"}}}),
        chart_column("lolli", cd.LollipopChart, [{"group":"A","key":"Qty","value":34},{"group":"B","key":"More","value":29},{"group":"C","key":"Sold","value":41}],
            {"title":"LollipopChart","axes":{"bottom":{"mapsTo":"key"},"left":{"mapsTo":"value"}}}),
        chart_column("meter", cd.MeterChart, [{"group":"Usage","value":65}],
            {"title":"MeterChart"}),
        chart_column("gauge", cd.GaugeChart, [{"group":"Progress","value":72}],
            {"title":"GaugeChart"}),
        chart_column("bullet", cd.BulletChart, [{"title":"R","group":"24","ranges":[350,650,980],"marker":1575,"value":400},{"title":"R","group":"23","ranges":[300,600,900],"marker":1400,"value":350}],
            {"title":"BulletChart","axes":{"bottom":{"mapsTo":"value"},"left":{"mapsTo":"title"}}}),
        chart_column("box", cd.BoxplotChart, [{"group":"A","values":{"q1":50,"q2":70,"q3":90,"min":30,"max":110}},{"group":"B","values":{"q1":40,"q2":60,"q3":80,"min":25,"max":95}}],
            {"title":"BoxplotChart","axes":{"bottom":{"mapsTo":"group"},"left":{"mapsTo":"values"}}}),
        chart_column("hist", cd.HistogramChart, [{"group":"Ages","key":"0-18","value":15},{"group":"Ages","key":"19-35","value":30},{"group":"Ages","key":"36-50","value":25},{"group":"Ages","key":"51+","value":20}],
            {"title":"HistogramChart","axes":{"bottom":{"mapsTo":"key"},"left":{"mapsTo":"value"}}}),
        chart_column("heat", cd.HeatmapChart, [{"x":"Mon","y":"AM","value":10},{"x":"Mon","y":"PM","value":20},{"x":"Tue","y":"AM","value":15},{"x":"Tue","y":"PM","value":25}],
            {"title":"HeatmapChart","axes":{"bottom":{"mapsTo":"x"},"left":{"mapsTo":"y"}}}),
        chart_column("alluv", cd.AlluvialChart, [{"source":"Home","target":"Search","value":5},{"source":"Search","target":"Product","value":4},{"source":"Product","target":"Cart","value":6},{"source":"Cart","target":"Buy","value":8}],
            {"title":"AlluvialChart","alluvial":{"nodes":[{"name":"Home","category":"T"},{"name":"Search","category":"T"},{"name":"Product","category":"P"},{"name":"Cart","category":"A"},{"name":"Buy","category":"O"}]}},"350px"),
        chart_column("cloud", cd.WordCloudChart, [{"word":"Cloud","value":100},{"word":"Carbon","value":85},{"word":"Dash","value":75},{"word":"Design","value":65},{"word":"React","value":55}],
            {"title":"WordCloudChart"},"350px"),
        chart_column("treemap", cd.TreemapChart, [{"name":"Root","children":[{"name":"A","value":45},{"name":"B","value":30},{"name":"C","value":25}]}],
            {"title":"TreemapChart"}),
        chart_column("circle", cd.CirclePackChart, [{"name":"Root","children":[{"name":"A","value":50},{"name":"B","value":30},{"name":"C","value":20}]}],
            {"title":"CirclePackChart"}),
        chart_column("tree", cd.TreeChart, [{"name":"Root","children":[{"name":"A","children":[{"name":"A1","value":20}]},{"name":"B","value":30}]}],
            {"title":"TreeChart"},"350px"),
        chart_column("combo", cd.ComboChart, [{"group":"A","key":"Q1","value":30},{"group":"A","key":"Q2","value":40},{"group":"B","key":"Q1","value":20},{"group":"B","key":"Q2","value":25}],
            {"title":"ComboChart","comboChartTypes":[{"type":"simple-bar","correspondingDatasets":["A"]},{"type":"line","correspondingDatasets":["B"]}],"axes":{"left":{"mapsTo":"value"},"bottom":{"mapsTo":"key"}}},"350px"),
    ], style={"display":"flex","flexWrap":"wrap","justifyContent":"center"}),
]

# ── Settings ────────────────────────────────────────────────────────────
SETTINGS = [
    cd.Heading(children="Settings", level=1),
    cd.Select(id="theme", labelText="Theme", children=[cd.SelectItem(value="light",text="Light"),cd.SelectItem(value="dark",text="Dark")]),
    cd.Slider(id="refresh", labelText="Refresh Rate (s)", min=5, max=60, value=30),
    cd.Toggle(id="notif", labelText="Email Notifications", toggled=True),
    cd.Toggle(id="sms", labelText="SMS Notifications"),
    cd.ProgressIndicator(currentIndex=2, children=[cd.ProgressStep(label="Setup",complete=True),cd.ProgressStep(label="Config",complete=True),cd.ProgressStep(label="Deploy",current=True)]),
]

# ── Modal ──────────────────────────────────────────────────────────────
@callback(Output("settings-modal","open"), Input("settings-btn","n_clicks"), State("settings-modal","open"), prevent_initial_call=True)
def toggle_modal(n, open):
    return not open

if __name__ == "__main__":
    app.run(debug=True)
