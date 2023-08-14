### Import packeges ###
from dash import Dash, html, dcc, dash_table, callback, Output, Input, State, dash_table, exceptions
import pandas as pd 
import numpy as np
# import ipywidgets as widgets
# from IPython.display import display
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
import os



### Dash creation ###
app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server


### First page layout ###
homepage_layout = html.Div(
    className='total',
    children=[
        html.H1('Enzo vacilão'),
        dcc.Graph(id='graph')
    ]
)

@app.callback(
    Output('graph', 'figure'),
    [Input('graph', 'id')]
)
def update_graph(graph_id):
    df = pd.DataFrame(dict(
        x = [1, 3, 2, 4],
        y = [1, 2, 3, 4]
    ))
    fig = px.line(df, x="x", y="y", title="Unsorted Input") 
    return fig


### Def layout ###
app.layout = homepage_layout



# Execute o aplicativo Dash
if __name__ == '__main__':
    app.run_server(debug=True)  
    
