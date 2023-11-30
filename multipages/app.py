import dash
from dash import Dash, html, dcc

app = Dash("Multipages", use_pages=True)

app.layout = html.Div([
    html.H1('Multi-page app with Dash Pages'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    html.Div(dcc.Link('Dashboard', href=dash.page_registry['pages.analytics']['path'])),
    dash.page_container
])

app.run(debug=True)