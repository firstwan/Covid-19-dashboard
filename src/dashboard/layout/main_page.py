from dash import html, dcc
from dashboard.callbacks.covid_callback import total_case_geo_graph

upper_graph = html.Div(id='upper-graph', children=[
    dcc.Graph(id='total-case-bar'),
    dcc.Graph(id='total-case-timeline')
    ],
    className='right-container'
)

lower_graph = html.Div(id='bottom-graph', children=[
    dcc.Graph(id='total-case-geo',figure=total_case_geo_graph()),
    ],
    className='right-container'
)

main_page = html.Div(id='main', 
    className='main-content',
    children=
        [
            upper_graph,
            lower_graph
        ]
)