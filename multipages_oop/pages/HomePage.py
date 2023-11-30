from dash import html

class HomePage:
    def __init__(self):
        self.name = 'Home'
        self.path = '/'
        self.layout = self.set_layout()

    def set_layout(self):
        return html.Div([
            html.H1('This is our Home page'),
            html.Div('This is our Home page content.'),
        ])