import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import pickle
import dash_bootstrap_components as dbc
import os
import dash
import pandas as pd


# Get the current working directory
cwd = os.getcwd()

# Specify the path to the dataset file
path = os.path.join(cwd, 'Model/data.pkl')

# Load the cleaned data
with open(path, 'rb') as f:
    drug_data_cleaned = pickle.load(f)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = dbc.Container([
     dbc.Row([
        dbc.Col(html.H1("Drug Reviews Analysis Dashboard", className="text-center mb-4"), width=12)
    ]),
    dcc.Dropdown(
        id='condition-dropdown',
        options=[{'label': condition, 'value': condition} for condition in drug_data_cleaned['condition'].unique()],
        value='Depression',
        clearable=False,
         style={'margin-bottom': '20px'}
    ),
    dcc.Graph(id='rating-distribution'),
    dcc.Graph(id='usefulness-score')
])

@app.callback(
    Output('rating-distribution', 'figure'),
    Input('condition-dropdown', 'value')
)
def update_rating_distribution(selected_condition):
    try:
        filtered_data = drug_data_cleaned[drug_data_cleaned['condition'] == selected_condition]
        if filtered_data.empty:
            return px.histogram(title=f'No data available for {selected_condition}')
        fig = px.histogram(filtered_data, x='rating', nbins=10, title=f'Rating Distribution for {selected_condition}', color_discrete_sequence=px.colors.qualitative.Pastel)
        return fig
    except Exception as e:
        print(f"Error in update_rating_distribution: {e}")
        return px.histogram(title='Error in loading data')

@app.callback(
    Output('usefulness-score', 'figure'),
    Input('condition-dropdown', 'value')
)
def update_usefulness_score(selected_condition):
    try:
        filtered_data = drug_data_cleaned[drug_data_cleaned['condition'] == selected_condition]
        if filtered_data.empty:
            return px.bar(title=f'No data available for {selected_condition}')
        fig = px.bar(filtered_data, x='drugName', y='usefulness_score', title=f'Usefulness Score for {selected_condition}', color='usefulness_score',
            color_continuous_scale='Bluered')
        fig.update_layout(transition_duration=500)
        return fig
    except Exception as e:
        print(f"Error in update_usefulness_score: {e}")
        return px.bar(title='Error in loading data')

if __name__ == '__main__':
    app.run_server(debug=True)