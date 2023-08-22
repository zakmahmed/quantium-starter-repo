from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = Dash(__name__)


df = pd.read_csv('data/pink_morsel.csv').sort_values(by='date')

print(df)

fig = px.line(df, df.date, df.sales)

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales'),

    dcc.Graph(
        id='example-graph',
        figure=fig,

    )
])

if __name__ == '__main__':
    app.run(debug=True)
