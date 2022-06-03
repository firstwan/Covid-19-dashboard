# Define Dash app layout
# Import callbacks module here
from dashboard.index import app
from dash import html

from dashboard.callbacks.covid_callback import location_total_case_timeline, total_case_horizontal_bar
from dashboard.layout.side_bar import side_bar_body
from dashboard.layout.main_page import main_page


app.layout = html.Div(id='parent', children=
[
    side_bar_body,
    main_page
])