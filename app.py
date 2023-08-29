import pandas

from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from plotly.express import line

# the path to the formatted data file
DATA_PATH = "data/pink_morsel.csv"

# load in data
data = pandas.read_csv(DATA_PATH)
data = data.sort_values(by="date")

# initialize dash
dash_app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# create the visualization
line_chart = line(data, x="date", y="sales",
                  title="Pink Morsel Sales", )

visualization = dcc.Graph(
    id="visualization",
    figure=line_chart
)

# create the header
header = dbc.NavbarSimple(
    brand="Pink Morsel Visualiser", color="red", dark=True)


button = dbc.RadioItems(
    id='regions',
    options=[
        {'label': 'North', 'value': 'north', },
        {'label': 'South', 'value': 'south'},
        {'label': 'East', 'value': 'east'},
        {'label': 'West', 'value': 'west'},
        {'label': 'All', 'value': 'all'},
    ],
    value='north',
    inline=True,
    style={"width": "50%", 'display': 'inline-block'}
)


# define the app layout
dash_app.layout = html.Div([

    html.Div([
        header
    ]),

    html.Div([
        dbc.Label(['Regions:'], style={'font-weight': 'bold'}),
        html.Br(),
        button
    ]),

    html.Div([
        visualization
    ]),

])


@dash_app.callback(
    Output(component_id='visualization', component_property='figure'),
    Input(component_id='regions', component_property='value')
)
def update_graph(regions):
    if regions != 'all':
        dff = data[(data.region == regions)]
        graph = line(dff, x="date", y="sales", title="Pink Morsel Sales")
        return graph

    graph = line(data, x="date", y="sales", title="Pink Morsel Sales")
    return graph


# this is only true if the module is executed as the program entrypoint
if __name__ == '__main__':
    dash_app.run_server()
