import json
import os

from dash import Dash, dcc, html
import dash_auth
from graphs import get_random_scatter

import pandas as pd

try:
    with open('keys.json') as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    pass

try:
    USERNAME = data['USERNAME']
    PASSWORD = data['PASSWORD']
    DEBUG = True

except NameError:
    USERNAME = os.environ.get('USERNAME')
    PASSWORD = os.environ.get('PASSWORD')


VALID_USERNAME_PASSWORD_PAIRS = {
    USERNAME: PASSWORD
}

app = Dash(__name__)
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)
server = app.server

df = pd.read_csv('./data/test.csv')

app.layout = html.Div([
    html.H1("Hello Dash!"),
    dcc.Graph(figure=get_random_scatter()),
    html.P(df.iloc[0]['COL_1'])
])

if __name__ == '__main__':
    app.run_server(debug=True)