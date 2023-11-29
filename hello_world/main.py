from dash import Dash, html

app = Dash("Simple App")

app.layout = html.Div([
    html.Div(children='Hello World')
])

app.run(debug=True)