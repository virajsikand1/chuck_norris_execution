######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import os


####### Set up your app #####
app = dash.Dash(__name__)
server = app.server

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})


####### Layout of the app ########
app.layout = html.Div([
    html.H1('Your favorite color'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['yellow', 'red', 'green', 'blue']],
        value='yellow'
    ),
    dcc.Dropdown(
        id='dropdown2',
        options=[{'label': i, 'value': i} for i in ['yellow', 'red', 'green', 'blue']],
        value='yellow'
    ),
    html.Div(id='display-value'),
    html.Div(id='display-value2')
])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'Your favorite color is "{}"'.format(value)

@app.callback(dash.dependencies.Output('display-value2', 'children'),
              [dash.dependencies.Input('dropdown2', 'value')])
def display_value(value):
    return 'Your favorite color is "{}"'.format(value)

######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
