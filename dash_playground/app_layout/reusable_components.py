#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


def generate_table(df, max_rows=10):
    return html.Table(
        # header
        [html.Tr([html.Th(col) for col in df.columns])] +

        # body
        [html.Tr([
            html.Td(df.iloc[i][col]) for col in df.columns
        ]) for i in range(min(len(df), max_rows))]
    )


app = dash.Dash()

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/'
                 'c78bf172206ce24f77d6363a2d754b59/raw/'
                 'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
                 'usa-agricultural-exports-2011.csv')

app.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)
