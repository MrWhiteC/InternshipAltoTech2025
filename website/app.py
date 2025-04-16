from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('predicted_after_ai.csv')

app = Dash()

# All columns except date
columns = [col for col in df.columns if col != 'date']

app.layout = html.Div([
    html.H1(children='Energy Different between Pre-AI and Post-AI', style={'textAlign':'center'}),
    
    html.Div([
        dcc.Dropdown(
            id='y-axis-1',
            options=[{'label': col, 'value': col} for col in columns],
            value=columns[0],
            style={'width': '48%', 'display': 'inline-block'}
        ),
        dcc.Dropdown(
            id='y-axis-2',
            options=[{'label': col, 'value': col} for col in columns],
            value=columns[4] if len(columns) > 1 else columns[0],
            style={'width': '48%', 'display': 'inline-block', 'float': 'right'}
        )
    ]),
    
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('y-axis-1', 'value'),
    Input('y-axis-2', 'value')
)
def update_graph(col1, col2):
    hover_cols = [col for col in df.columns if col not in ['date', col1, col2]]
    
    fig = px.line(
        df,
        x='date',
        y=[col1, col2],
        hover_data=hover_cols,
        labels={'value': 'Value', 'variable': 'Type'}
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
