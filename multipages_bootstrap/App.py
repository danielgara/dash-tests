import dash
from dash import Dash, html, dcc
from views.layouts.AppLayout import AppLayout
from views.pages.HomePage import HomePage
from views.pages.ArchivePage import ArchivePage
from views.pages.AnalyticsPage import AnalyticsPage

class App:
    def __init__(self):
        self.app = Dash(__name__, use_pages=True, pages_folder="views/pages")
        self.register_pages()
        self.set_layout()

    def register_pages(self):
        self.home_page = HomePage()
        self.archive_page = ArchivePage()
        self.analytics_page = AnalyticsPage()

        dash.register_page(self.home_page.name, path=self.home_page.path, layout=self.home_page.layout)
        dash.register_page(self.archive_page.name, path=self.archive_page.path, layout=self.archive_page.layout)
        dash.register_page(self.analytics_page.name, path=self.analytics_page.path, layout=self.analytics_page.layout)

    def set_layout(self):
        self.app.layout = AppLayout.define_layout()

    def run_app(self):
        self.app.run_server(debug=True)

app = App()
app.run_app()