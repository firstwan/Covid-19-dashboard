from dashboard.index import app
from dash.dependencies import Input, Output
from dashboard.data.covid import covid_df_excluded_owid
import pandas as pd
import plotly.express as px


def total_case_geo_graph():
    location_df = covid_df_excluded_owid[
        (covid_df_excluded_owid['date']  >= '2022-04-24') # the latest date in data set
    ][['iso_code','location','total_cases']]

    
    fig = px.choropleth(location_df, 
                        title="Latest Covid case",
                        locations="iso_code",
                        color="total_cases", # lifeExp is a column of gapminder
                        hover_name="location", # column to add to hover information
                        color_continuous_scale=px.colors.sequential.Plasma)
                        
    return fig

@app.callback(Output(component_id='total-case-timeline', component_property='figure'),
              [Input(component_id='location-ddl', component_property='value')])
def location_total_case_timeline(dropdown_value):
    location_covid = covid_df_excluded_owid[covid_df_excluded_owid['location'].isin(dropdown_value)]
    line_fig = px.line(location_covid, x='date', y='total_cases', title='time line', color='location')
    
    return line_fig


@app.callback(Output(component_id='total-case-bar', component_property='figure'),
              [Input(component_id='location-ddl', component_property='value')])
def total_case_horizontal_bar(dropdown_value):
    location_covid = covid_df_excluded_owid[(covid_df_excluded_owid['date']  >= '2022-04-24') &
        covid_df_excluded_owid['location'].isin(dropdown_value)]

    # Reshape to make data become vertical
    total_case_df = pd.melt(location_covid[['total_cases', 'total_deaths', 'location']], id_vars=['location'], var_name='Case')

    bar_fig = px.bar(total_case_df, x='value', y='location', color='Case',  orientation='h')
    bar_fig.update_layout(yaxis={'categoryorder':'total ascending'}) # Add this line for descending order

    return bar_fig