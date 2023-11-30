# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html
from components.Table import Table
import pandas as pd

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

app = Dash("Components")

app.layout = html.Div([
    html.H4(children='US Agriculture Exports (2011)'),
    Table.generate_table(df)
])

app.run(debug=True)