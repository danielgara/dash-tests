import dash
from dash import html, dcc

class AppLayout:
    @staticmethod
    def define_layout():
        return html.Div([
            html.H1('Multi-page app with Dash Pages'),
            html.Div(dcc.Link('Home', href=dash.page_registry['Home']['path'])),
            html.Div(dcc.Link('Archive', href=dash.page_registry['Archive']['path'])),
            html.Div(dcc.Link('Analytics', href=dash.page_registry['Analytics']['path'])),
            dash.page_container
        ])