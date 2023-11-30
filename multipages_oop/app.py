import dash
from dash import Dash, html, dcc
from pages.home import HomePage
from pages.archive import ArchivePage

class MultiPageApp:
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
            html.Div([
                html.Div(
                    dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
                ) for page in dash.page_registry.values()
            ]),
            html.Div(dcc.Link('Dashboard', href=dash.page_registry['Archive']['path'])),
            dash.page_container
        ])

    def run_app(self):
        self.app.run_server(debug=True)

app = MultiPageApp()
app.run_app()