from dash import html

class ArchivePage:
    def __init__(self):
        self.name = 'Archive'
        self.path = '/archive'
        self.set_layout()

    def set_layout(self):
        self.layout = html.Div([
            html.H1('Archive Page'),
            html.Div('This is the content of the Archive Page.'),
        ])