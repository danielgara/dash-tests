from dash import html

class HomePage:
    def __init__(self):
        self.name = 'Home'
        self.path = '/'
        self.layout = html.Div([
            html.H1('Welcome to the Home Page!'),
            html.Div('This is the content of the Home Page.'),
        ])