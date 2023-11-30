import dash
from dash import Dash, html, dcc
from pages.HomePage import HomePage
from pages.ArchivePage import ArchivePage

class App:
    def __init__(self):
        self.app = Dash(__name__, use_pages=True)
        self.register_pages()

    def register_pages(self):
        self.home_page = HomePage()
        self.archive_page = ArchivePage()

        dash.register_page(self.home_page.name, path=self.home_page.path, layout=self.home_page.layout)
        dash.register_page(self.archive_page.name, path=self.archive_page.path, layout=self.archive_page.layout)

        self.app.layout = html.Div([
            html.H1('Multi-page app with Dash Pages'),
            html.Div(dcc.Link('Home', href=dash.page_registry['Home']['path'])),
            html.Div(dcc.Link('Archive', href=dash.page_registry['Archive']['path'])),
            dash.page_container
        ])

    def run_app(self):
        self.app.run_server(debug=True)

app = App()
app.run_app()