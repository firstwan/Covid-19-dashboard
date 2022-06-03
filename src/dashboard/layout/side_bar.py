from dash import html, dcc
from dashboard.index import app
from dashboard.helper.ddl_helper import create_dropdown_options
from dashboard.data.covid import covid_df_excluded_owid

header = html.H1(   
        id='H1', 
        children='Covid 19 Data Dashboard', 
        style = {'textAlign':'center','marginTop':40,'marginBottom':40}
    )

covid_img = html.Img(src=app.get_asset_url('site_bar_pic.png'))

localtion_label = html.Label("Location", className='dropdown-labels')

location_ddl_value = create_dropdown_options(covid_df_excluded_owid['location'])
location_ddl = dcc.Dropdown(
    options=location_ddl_value, 
    value=['Malaysia'], 
    multi=True,
    id='location-ddl', 
    className='dropdown')

side_bar_body = html.Div(id='side_bar', 
    className='sidebar',
    children=[
        header,
        covid_img,
        localtion_label,
        location_ddl
    ]
)
