#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.css.append_css(
    {'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

markdown_text = '''
### Dash and Markdown

Dash apps can be written in markdown.
Dash uses the [CommonMark](http://commonmark.org) specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help) if
this is your first introduction to Markdown!
'''

app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
])

if __name__ == '__main__':
    app.run_server()
