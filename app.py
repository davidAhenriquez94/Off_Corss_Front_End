""" First Front End Team 69 """

# Dash Libraries
import dash
import dash_table
from dash import no_update
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# Flask libraries
from flask import Flask, send_from_directory

# Python Libraries
import io
import re
import cv2
import json
import base64
import numpy as np
import pandas as pd
from PIL import Image
from skimage import io
import matplotlib.cm as cm
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from datetime import date, datetime
from scipy.ndimage.filters import gaussian_filter
# SQL Alchemy
import sqlalchemy
from sqlalchemy import create_engine, text

# ///////////////////////////////////////////////////////////////////////////////////////////////////
# DataBase Credentials
host = 'team-cv.cfsx82z4jthl.us-east-2.rds.amazonaws.com'
port = 5432
user = 'ds4a_69'
password = 'DS4A!2020'
database = 'postgres'
# ///////////////////////////////////////////////////////////////////////////////////////////////////
# Image Sources
image_sidebar = 'Images/side_bar_logo3.png'  # replace with your own image
encoded_image = base64.b64encode(open(image_sidebar, 'rb').read())
# Cover Page images
cover_child = 'Images/portada_nignos.jpg'
cover_img = base64.b64encode(open(cover_child, 'rb').read())
# ---
metrics_images = "Images/Metrics_icon.png"
metrics_img = base64.b64encode(open(metrics_images, 'rb').read())
# ---
cloud_images = "Images/upload_vector.jpg"
cloud_img = base64.b64encode(open(cloud_images, 'rb').read())
# Crew
crew_1 = 'Images/Crew1.jpg'
crew_2 = 'Images/Crew2.jpg'
crew_3 = 'Images/Crew3.jpg'
crew_4 = 'Images/Crew4.jpg'
crew_5 = 'Images/Crew5.jpg'
crew_6 = 'Images/Crew6.jpg'
crew_7 = 'Images/Crew7.jpg'

encoded_crew1 = base64.b64encode(open(crew_1, 'rb').read())
encoded_crew2 = base64.b64encode(open(crew_2, 'rb').read())
encoded_crew3 = base64.b64encode(open(crew_3, 'rb').read())
encoded_crew4 = base64.b64encode(open(crew_4, 'rb').read())
encoded_crew5 = base64.b64encode(open(crew_5, 'rb').read())
encoded_crew6 = base64.b64encode(open(crew_6, 'rb').read())
encoded_crew7 = base64.b64encode(open(crew_7, 'rb').read())
# Team logo
team_l = "Images/Team.png"
encoded_logo = base64.b64encode(open(team_l, 'rb').read())

# Store Maps
san_diego_store = 'Images/Planos_San_Diego_1.jpg'
san_diego_blue = base64.b64encode(open(san_diego_store, 'rb').read())
# ///////////////////////////////////////////////////////////////////////////////////////////////////
# Upload directory definition
UPLOAD_DIRECTORY = "Uploaded_Videos"
# ///////////////////////////////////////////////////////////////////////////////////////////////////
# Button definition
button_groups = html.Div(
    [
        dbc.ButtonGroup(
            [dbc.Button("Upload"), dbc.Button(
                "Process"), dbc.Button("Cancel")],
            size="lg",
            className="mr-1")
    ]
)

button = dbc.Button("Upload", color="primary", block=True)
# ///////////////////////////////////////////////////////////////////////////////////////////////////
# JumboTron for the Home Page
card_content_cover = [
    dbc.CardImg(
        src='data:image/jpg;base64,{}'.format(cover_img.decode()), top=True),
]

card_cover = dbc.Jumbotron(
    className="jumboclass"
)

card_int_1 = [
    dbc.CardHeader("Explore the traffic metrics in the Stores"),
    dbc.CardBody(
        [
            dbc.CardImg(src='data:image/png;base64,{}'.format(metrics_img.decode()),
                        top=True, className="card-img-top"),
            html.Hr(className="my-2"),
            dbc.Button("Take me there!", href="/page-4",
                       color="primary", className="metrics_button"),
        ], className="home_card"
    ),
]

card_int_2 = [
    dbc.CardHeader("Upload and process your own videos!"),
    dbc.CardBody(
        [
            dbc.CardImg(
                src='data:image/jpg;base64,{}'.format(cloud_img.decode()), top=True),
            html.Hr(className="my-2"),
            dbc.Button("Take me there!", href="/page-2",
                       color="primary", className="metrics_button"),
        ], className="home_card"
    ),
]

card_int_3 = [
    dbc.CardHeader("Meet our Company"
                   " and Learn more about OffCorss"),
    dbc.CardBody(
        [
            dbc.CardImg(
                src='data:image/png;base64,{}'.format(encoded_image.decode()), top=True),
            html.Hr(className="my-2"),
            dbc.Button("Take me there!", href="https://www.offcorss.com/",
                       color="primary", className="metrics_button"),
        ], className="home_card"
    ),
]

cards_home = dbc.CardColumns(
    [
        dbc.Card(card_int_1, body=True),
        dbc.Card(card_int_2, body=True),
        dbc.Card(card_int_3, body=True),
    ]
)

jumbotron_links = html.Div(
    [
        dbc.Button("", href="https://www.mintic.gov.co/portal/inicio/",
                   color="primary", className="mintic_button"),
        dbc.Button("", href="https://www.correlation-one.com/ds4a-latam",
                   color="primary", className="correl_button"),
        dbc.Button("", href="https://dash.plotly.com/",
                   color="primary", className="ploty_button"),
    ],
    className="pretty_container"
)


jumbotron_int = dbc.Jumbotron(
    [
        html.P(
            "Welcome to the CV APP "
            ", we hope you to enjoy the Deep Learning Ride",
            className="lead",
        ),
        html.P(
            cards_home
        ),
        html.P(
            dbc.CardImg(src='data:image/png;base64,{}'.format(encoded_logo.decode()),
                        top=True, className="radius_img"),
        ),
        jumbotron_links
    ],
    className="welcome_jumbo"
)

# ///////////////////////////////////////////////////////////////////////////////////////////////////
# About Us cards
card_content_1 = [
    dbc.CardHeader("Crew Mate 1", className="center-text"),
    dbc.CardBody(
        [
            dbc.CardImg(src='data:image/jpg;base64,{}'.format(encoded_crew1.decode()),
                        top=True, className="radius_img"),
            html.H5("Alekcei Hernández", className="center-text"),
            html.Div(
                [
                    dbc.Button("", href="https://www.mintic.gov.co/portal/inicio/",
                               color="primary", className="linked_button"),
                    dbc.Button("", href="https://www.correlation-one.com/ds4a-latam",
                               color="primary", className="email_button"),
                ],
            )
        ], className="radius_card"
    ),
]

card_content_2 = [
    dbc.CardHeader("Crew Mate 2", className="center-text"),
    dbc.CardBody(
        [
            dbc.CardImg(src='data:image/jpg;base64,{}'.format(encoded_crew2.decode()),
                        top=True, className="radius_img"),
            html.H5("Alexander Sandoval", className="center-text"),
            html.Div(
                [
                    dbc.Button("", href="https://www.mintic.gov.co/portal/inicio/",
                               color="primary", className="linked_button"),
                    dbc.Button("", href="https://www.correlation-one.com/ds4a-latam",
                               color="primary", className="email_button"),
                ],
            )
        ], className="radius_card"
    ),
]

card_content_3 = [
    dbc.CardHeader("Crew Mate 3", className="center-text"),
    dbc.CardBody(
        [
            dbc.CardImg(src='data:image/jpg;base64,{}'.format(encoded_crew3.decode()),
                        top=True, className="radius_img"),
            html.H5("David Henriquez", className="center-text"),
            html.Div(
                [
                    dbc.Button("", href="https://www.mintic.gov.co/portal/inicio/",
                               color="primary", className="linked_button"),
                    dbc.Button("", href="https://www.correlation-one.com/ds4a-latam",
                               color="primary", className="email_button"),
                ],
            )
        ], className="radius_card"
    ),
]

card_content_4 = [
    dbc.CardHeader("Crew Mate 4", className="center-text"),
    dbc.CardBody(
        [
            dbc.CardImg(src='data:image/jpg;base64,{}'.format(encoded_crew4.decode()),
                        top=True, className="radius_img"),
            html.H5("Guillermo Valencia", className="center-text"),
            html.Div(
                [
                    dbc.Button("", href="https://www.mintic.gov.co/portal/inicio/",
                               color="primary", className="linked_button"),
                    dbc.Button("", href="https://www.correlation-one.com/ds4a-latam",
                               color="primary", className="email_button"),
                ],
            )
        ], className="radius_card"
    ),
]

card_content_5 = [
    dbc.CardHeader("Crew Mate 5", className="center-text"),
    dbc.CardBody(
        [
            dbc.CardImg(src='data:image/jpg;base64,{}'.format(encoded_crew5.decode()),
                        top=True, className="radius_img"),
            html.H5("Harold García", className="center-text"),
            html.Div(
                [
                    dbc.Button("", href="https://www.linkedin.com/in/haroldgiovannygarciar",
                               color="primary", className="linked_button"),
                    dbc.Button("", href="https://www.correlation-one.com/ds4a-latam",
                               color="primary", className="email_button"),
                ],
            )
        ], className="radius_card"
    ),
]

card_content_6 = [
    dbc.CardHeader("Crew Mate 6", className="center-text"),
    dbc.CardBody(
        [
            dbc.CardImg(src='data:image/jpg;base64,{}'.format(encoded_crew6.decode()),
                        top=True, className="radius_img"),
            html.H5("Sebastian Garzón", className="center-text"),
            html.Div(
                [
                    dbc.Button("", href="https://www.linkedin.com/in/sebastiangarzonc/",
                               color="primary", className="linked_button"),
                    dbc.Button("", href="https://www.correlation-one.com/ds4a-latam",
                               color="primary", className="email_button"),
                ],
            )
        ], className="radius_card"
    ),
]

card_content_7 = [
    dbc.CardHeader("Crew Mate 7", className="center-text"),
    dbc.CardBody(
        [
            dbc.CardImg(src='data:image/jpg;base64,{}'.format(encoded_crew7.decode()),
                        top=True, className="radius_img"),
            html.H5("Nicolás González", className="center-text"),
            html.Div(
                [
                    dbc.Button("", href="https://www.linkedin.com/in/jose-nicol%C3%A1s-gonz%C3%A1lez-guatibonza-41205076/",
                               color="primary", className="linked_button"),
                    dbc.Button("", href="https://www.correlation-one.com/ds4a-latam",
                               color="primary", className="email_button"),
                ],
            )
        ], className="radius_card"
    ),
]

cards = dbc.CardColumns(
    [
        dbc.Card(card_content_1, color="warning", inverse=True),
        dbc.Card(card_content_2, color="warning", inverse=True),
        dbc.Card(card_content_3, color="warning", inverse=True),
    ]
)

cards_2 = dbc.CardColumns(
    [
        dbc.Card(card_content_4, color="warning", inverse=True),
        dbc.Card(card_content_5, color="warning", inverse=True),
        dbc.Card(card_content_6, color="warning", inverse=True),
    ]
)

cards_3 = dbc.CardColumns(
    [
        dbc.Card("", inverse=True, className="card_black"),
        dbc.Card(card_content_7, color="warning", inverse=True),
        dbc.Card("", inverse=True, className="card_black"),
    ]
)
# ///////////////////////////////////////////////////////////////////////////////////////////////////
# Form for the date, hour and cam picking
# 1. Form for stores
dropdown_stores = dbc.FormGroup(
    [
        dbc.Label("Stores", html_for="dropdown"),
        dcc.Dropdown(
            id="dropdown_store",
            options=[
                {"label": "San Diego Store", "value": 'san diego'},
                {"label": "Santa Fe Store", "value": 'santa fe'},
            ],
            value='san diego'
        ),
        html.Div(id='output-dropdown-stores')
    ],  className="form_style"
)

# 2. Form for the Hours
hour_picker_start = dbc.Card([
    dbc.Label("Start_Hour"),
    dcc.Input(
        id="Start Hour", type="number",
        debounce=True, placeholder="Hour", min=0, max=23
    ),
    dcc.Input(
        id="Start Minute", type="number",
        debounce=True, placeholder="Minute", min=0, max=59
    ),
    html.Div(id="number-out"),
], className="form_style")

hour_picker_end = dbc.Card([
    dbc.Label("End_Hour"),
    dcc.Input(
        id="End Hour", type="number",
        debounce=True, placeholder="Hour", min=0, max=23
    ),
    dcc.Input(
        id="End Minute", type="number",
        debounce=True, placeholder="Minute", min=0, max=59
    ),
    html.Div(id="number-out-end"),
], className="form_style")

# 3. Date Picking Form
date_picker = dbc.Card([
    dbc.Label("Date"),
    dcc.DatePickerSingle(
        id='my-date-picker-single',
        min_date_allowed=date(2020, 10, 1),
        max_date_allowed=date(2020, 10, 19),
        initial_visible_month=date(2020, 10, 1),
        date=date(2020, 10, 1),
        className="date_pick_style"
    ),
    html.Div(id='output-container-date-picker-single')
], className="form_style")

# 4. Cam Picking Form
Cam_picker = dbc.FormGroup(
    [
        dbc.Label("Cameras", html_for="dropdown"),
        dcc.Dropdown(
            id="dropdown_cams",
            options=[
                {"label": "Cam 1", "value": 'Cam 1'},
                {"label": "Cam 2", "value": 'Cam 2'},
                {"label": "Cam 3", "value": 'Cam 3'},
                {"label": "Cam 4", "value": 'Cam 4'},
                {"label": "Cam 5", "value": 'Cam 5'},
                {"label": "All", "value": 'All'},
            ],
            value='All'
        ),
        html.Div(id='output-dropdown-cameras')
    ], className="form_style"
)

xxx = dbc.Card([html.Div(id='output-dropdown-cameras')])

# 5. Final form
form_store_pick = html.Div(
    [
        dbc.Row(
            [dbc.Col(
                dbc.FormGroup([dropdown_stores, date_picker])

            ),
                dbc.Col(
                dbc.FormGroup([hour_picker_start, hour_picker_end])
            ),
                dbc.Col(
                dbc.FormGroup([Cam_picker,
                               html.Button('Launch!', id='submit-val', n_clicks=0, className="ico_submit")])
            )
            ])
    ])
# ///////////////////////////////////////////////////////////////////////////////////////////////////
card_date = dbc.Card(
    [
        dbc.CardHeader("Traffic Processing Module",
                       className="title_video_picker"),
        dbc.CardBody(
            [
                form_store_pick
            ]
        ),
        dbc.CardFooter("Please select a Date, Start and End Hour and the Cam to start the video analysis",
                       className="foot_video_picker"),
    ],
    className="big_form_style"
)

card_trends = dbc.Card(
    [
        dbc.CardHeader("Trends Module", className="title_video_picker"),
        dbc.CardBody(
            [
                form_store_pick
            ]
        ),
        dbc.CardFooter("Please select a Date, Start and End Hour and the Cam to start the video analysis",
                       className="foot_video_picker"),
    ],
    className="big_form_style_II"
)

# ///////////////////////////////////////////////////////////////////////////////////////////////////
# Database Functions


def get_db():
    """ Function to conect to data base in postgres """
    # Parameters
    host = "team-cv.cfsx82z4jthl.us-east-2.rds.amazonaws.com"
    user = "ds4a_69"
    port = "5432"
    password = "DS4A!2020"
    database = "postgres"

    # Create the engine with the db credentials
    engine = sqlalchemy.create_engine(
        f'postgresql://{user}:{password}@{host}:{port}/{database}', max_overflow=20)
    return engine


def filter_df(engine, store, date, start_hour, start_min, end_hour, end_min, cam):
    """ Function to generate fig, count people per second """
    # Filter dates
    start_date = datetime.strptime(
        date + ' ' + start_hour.zfill(2) + ':' + start_min.zfill(2) + ':00', '%d/%m/%Y %H:%M:%S')
    end_date = datetime.strptime(
        date + ' ' + end_hour.zfill(2) + ':' + end_min.zfill(2) + ':00', '%d/%m/%Y %H:%M:%S')

    connection = engine.connect()

    query = '''
            SELECT * from tracker 
            WHERE "Store_name"= :group 
            AND "current_datetime" BETWEEN :A AND :B 
            AND "Camera"= :C
            AND "Object"= :O
            '''

    tracker_conn = connection.execute(text(
        query), group='san diego', A=start_date, B=end_date, C=int(cam[-1]), O='person').fetchall()
    columns = ['Store_name', 'Start_date', 'End_date', 'current_datetime', 'Camera', 'Object', 'Id', 'X_center_original', 'Y_center_original',
               'X_center_perspective', 'Y_center_perspective', 'X_min', 'Y_min', 'X_max', 'Y_max', 'Frame']
    tracker = pd.DataFrame(tracker_conn, columns=columns)

    return tracker


def visual_count(tracker):
    """ Function to generate count og people per sec """
    # df_plot = tracker.groupby(['Store_name','Current_date','Frame']).count()['Second'].reset_index()
    df_plot = tracker.groupby(['current_datetime', 'Frame']).count()[
        'Store_name'].reset_index()
    # df_plot = df_plot.groupby(['Store_name','Current_date']).mean().reset_index()
    df_plot['hour'] = df_plot['current_datetime'].dt.hour
    df_plot['minute'] = df_plot['current_datetime'].dt.minute
    df_plot['second'] = df_plot['current_datetime'].dt.second
    df_plot = df_plot.groupby(['hour', 'minute']).mean().reset_index()
    df_plot['hour_minute'] = df_plot['hour'].astype(
        'str') + ':' + df_plot['minute'].astype('str')

    df_plot['People'] = np.round(df_plot['Store_name'])
    # fig = px.line(df_plot, x = "Current_date",  y = "People", color = 'Store_name', title = 'Number of persons per second of video')
    fig = px.line(df_plot, x='hour_minute',  y="People",
                  title='Number of persons per minute of video')
    fig.update_layout(yaxis=dict(range=[0, max(df_plot['People']) + 1]))
    fig.update_layout(width=900, height=600)
    return fig


def print_path(tracker, plane):
    """ Function to print path inside a plane """
    tracker = tracker[(tracker['X_center_perspective'] != 0)
                      & (tracker['Y_center_perspective'] != 0)]
    img = plane
    fig = px.imshow(img)
    fig.update_traces(hoverinfo='skip')
    fig.add_trace(go.Scatter(x=tracker['X_center_perspective'],
                             y=tracker['Y_center_perspective'],
                             marker_color=tracker['Id'],
                             name='Id',
                             mode='markers'))
    fig.update_layout(coloraxis_showscale=False)
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    fig.update_layout(autosize=False, width=900, height=600, margin=go.layout.Margin(
        l=0,  # left margin
        r=0,  # right margin
        b=0,  # bottom margin
        t=0  # top margin
    ))
    fig.update_yaxes(automargin=True)
    return fig


def print_hot_spots(df, plane, name_temp, sigma=4):
    # Get the data to plot
    df = df[(df['X_center_perspective'] != 0) &
            (df['Y_center_perspective'] != 0)]
    x = list(df['X_center_perspective'])
    y = list(df['Y_center_perspective'])

    # Create imagen and save temp
    base_image = plane
    fig, ax = plt.subplots(1, 1, figsize=(20, 16))
    heatmap, xedges, yedges = np.histogram2d(
        x, y, bins=200, range=[[0, 1280], [0, 720]])
    heatmap = gaussian_filter(heatmap, sigma=sigma)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    img = heatmap.T
    ax.imshow(img, extent=extent, cmap=cm.jet)
    ax.imshow(base_image, alpha=0.3)
    ax.set_xlim(0, 1280)
    ax.set_ylim(0, 720)
    ax.axes.get_yaxis().set_visible(False)
    ax.axes.get_xaxis().set_visible(False)
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    plt.savefig(name_temp, bbox_inches='tight')
    plt.close(fig)

    # Upload imagen in plotly
    img = io.imread(name_temp)
    fig = px.imshow(img)
    fig.update_traces(hoverinfo='skip')
    fig.update_layout(coloraxis_showscale=False)
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    fig.update_layout(autosize=False, width=900, height=600, margin=go.layout.Margin(
        l=0,  # left margin
        r=0,  # right margin
        b=0,  # bottom margin
        t=0  # top margin
    ))
    fig.update_yaxes(automargin=True)
    return fig


store = 'san diego'
date = '01/10/2020'
start_hour = '18'
start_min = '57'
end_hour = '23'
end_min = '59'
cam = 'Cam 1'
# ...
imgx = Image.open(
    '../../../../Downloads/Off_Corss_Front_End (1) 2/Off_Corss_Front_End/Images/Planos_San_Diego_1.jpg')
imgx = imgx.convert("RGBA")
# ----------------------------------------
engine = get_db()
df = filter_df(engine, store, date, start_hour,
               start_min, end_hour, end_min, cam)
lineplot = visual_count(df)
pathx = print_path(df, imgx)
# ---------------------------------------
heat_map = print_hot_spots(df, imgx, 'temp_hot_spot.jpeg')
# ---------------------------------------
Graphs_tracker = html.Div([
    html.P("People Tracker Map"),
    dcc.Graph(figure=pathx, id="map_traffic"),
    html.Hr(),
    html.P("Store Traffic Heat Map"),
    dcc.Graph(figure=heat_map, id="heat_traffic"),
    html.Hr(),
    html.P("Traffic Lineplot"),
    dcc.Graph(figure=lineplot, id="lin_traffic"),
], id='graph_tracker')
# ///////////////////////////////////////////////////////////////////////////////////////////////////
#engine = get_db()
#tracker_df = pd.read_sql('SELECT * FROM tracker', engine)
# -------------------
# dw_mapping={0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
#            4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
#tracker_df['day_of_week_name'] = tracker_df['current_datetime'].dt.weekday.map(dw_mapping)
#tracker_df['hour'] = tracker_df['current_datetime'].dt.hour
#tracker_df['minute'] = tracker_df['current_datetime'].dt.minute
# --------------------
#df_plot = tracker_df.groupby(['day_of_week_name', 'hour', 'minute', 'Frame']).count().reset_index()
#df_plot = df_plot.groupby(['day_of_week_name', 'hour', 'minute']).mean()['Store_name'].reset_index()
#df_plot = df_plot.rename(columns = {'Store_name':'Count'})
#df_plot['Count'] = np.round(df_plot['Count'])
#df_plot['diff_count'] = df_plot['Count'] - df_plot['Count'].shift(-1)
#df_plot['diff_count'] = [x if x >= 0 else 0 for x in df_plot['diff_count']]
# ---------------------
#df_plot = df_plot.groupby(['day_of_week_name', 'hour']).sum()['diff_count'].reset_index()
#df_plot = df_plot.rename(columns = {'diff_count':'Count'})
#fig_t = px.bar(df_plot, x='hour', y='Count', facet_col = 'day_of_week_name')
# ---------------------
#days_tracker = html.Div([dcc.Graph(figure=fig_t, id="day_traffic")])

# ///////////////////////////////////////////////////////////////////////////////////////////////////
video_upload = html.Div([
    dcc.Upload(
        id='upload-video',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-video-upload'),
])


# Building Blocks
# ------------------------------------------
# Meta Tags
# ------------------------------------------
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG],
    # These meta_tags ensure content is scaled correctly on different devices. Don't Delete!!
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
    suppress_callback_exceptions=True
)

server = app.server

app.title = 'CV Team-69 DS4A!'

# ------------------------------------------
# Sidebar Component
# ------------------------------------------
# we use the Row and Col components to construct the sidebar header
# it consists of a title, and a toggle, the latter is hidden on large screens
sidebar_header = dbc.Row(
    [
        dbc.Col(dbc.CardImg(
            src='data:image/png;base64,{}'.format(encoded_image.decode()), className="display-4")),
        dbc.Col(
            [
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="navbar-toggle",
                ),
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="sidebar-toggle",
                ),
            ],
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ]
)

sidebar = html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            [
                html.Hr(),
                html.P(
                    "Welcome to the OffCorss CV app!",
                    className="lead",
                ),
            ],
            id="blurb",
        ),
        # use the Collapse component to animate hiding / revealing links
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/page-1",
                                id="page-1-link", className="ico_home"),
                    dbc.NavLink("Upload my Video", href="/page-2",
                                id="page-2-link", className="ico_upload"),
                    # ----------------------------------------------------------------------------------------
                    dbc.Button(
                        "Store's Metrics",
                        className="ico_store",
                        block=True,
                        color="light",
                        id="collapse-button",
                    ),
                    # -------------------------------------------
                    dbc.Collapse(dbc.Nav(
                        [dbc.NavLink("Trends Analysis", href="/page-3", id="page-3-link", className="collap_menu"),
                         dbc.NavLink("Video Analysis results", href="/page-4", id="page-4-link", className="collap_menu"), ],
                        vertical=True,
                        pills=True,
                    ),
                        id="collapse_2",
                    ),
                    # ---------------------------------------r-------------------------------------------------
                    dbc.NavLink("About Us", href="/page-5",
                                id="page-5-link", className="ico_about_"),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
)

content = html.Div(id="page-content")
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on


@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 6)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 6)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return html.Div([card_cover,
                         jumbotron_int
                         ])
    elif pathname == "/page-2":
        return html.Div([
            html.P("Video Upload Module"),
            video_upload
        ])
    elif pathname == "/page-3":
        return html.Div([
                        card_trends
                        ])
    elif pathname == "/page-4":
        return html.Div([card_date,
                         html.Hr(),
                         Graphs_tracker])
    elif pathname == "/page-5":
        return html.Div([cards,
                         cards_2,
                         cards_3])
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


@app.callback(
    Output("sidebar", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar", "className")],
)
def toggle_classname(n, classname):
    if n and classname == "":
        return "collapsed"
    return ""


@app.callback(
    Output("collapse", "is_open"),
    [Input("navbar-toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("collapse_2", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse_2", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# Hour and minutes callback
# Start
@app.callback(
    Output("number-out", "children"),
    [Input("Start Hour", "value"), Input("Start Minute", "value")],
)
def number_render(dhour, dminute):
    return "Start Hour: {}, Start Minute: {}".format(dhour, dminute)

# End


@app.callback(
    Output("number-out-end", "children"),
    [Input("End Hour", "value"), Input("End Minute", "value")],
)
def number_render(dhour, dminute):
    return "End Hour: {}, End Minute: {}".format(dhour, dminute)

# Date Callback


@app.callback(
    Output('output-container-date-picker-single', 'children'),
    [Input('my-date-picker-single', 'date')])
def update_output(date_value):
    string_prefix = 'You have selected: '
    if date_value is not None:
        date_object = datetime.strptime(date_value.split(' ')[0], '%Y-%m-%d')
        date_string = date_object.strftime('%d, %B, %Y')
        return string_prefix + date_string

# Store Callback


@app.callback(
    Output('output-dropdown-stores', 'children'),
    [Input('dropdown_store', 'value')]
)
def update_output_store(value):
    string_prefix = 'You have selected: '
    if value is not None:
        return 'You have selected "{}"'.format(value)

# Camera Callback


@app.callback(
    Output('output-dropdown-cameras', 'children'),
    [Input('dropdown_cams', 'value')]
)
def update_output_camera(value):
    string_prefix = 'You have selected: '
    if value is not None:
        return 'You have selected "{}"'.format(value)

# Video upload Callback


def parse_contents(contents, filename, date):
    return html.Div([
        html.H5(filename),
        html.H6(datetime.fromtimestamp(date)),
        html.Video(src=contents, autoPlay=True, controls=True),
        html.Hr()
    ])


@app.callback(Output('output-video-upload', 'children'),
              [Input('upload-video', 'contents')],
              [State('upload-video', 'filename'),
               State('upload-video', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

#
# Start


@app.callback([Output('map_traffic', 'figure'),
               Output('lin_traffic', 'figure'),
               Output('heat_traffic', 'figure')],
              [Input("Start Hour", "value"),
               Input("Start Minute", "value"),
               Input("End Hour", "value"),
               Input("End Minute", "value"),
               Input('dropdown_cams', 'value'),
               Input('my-date-picker-single', 'date'),
               Input('submit-val', 'n_clicks')])
def process_form(start_hour, start_minute, end_hour, end_min, cam, date, submit):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'submit-val' in changed_id:
        store = 'san diego'
        start_hour = str(start_hour)
        start_minute = str(start_minute)
        end_hour = str(end_hour)
        end_min = str(end_min)
        cam = str(cam)
        date = datetime.strptime(date.split(' ')[0], '%Y-%m-%d')
        date = date.strftime('%d/%m/%Y')
        # ----------------------------------------
        imgx = Image.open(
            '../../../../Downloads/Off_Corss_Front_End (1) 2/Off_Corss_Front_End/Images/Planos_San_Diego_1.jpg')
        imgx = imgx.convert("RGBA")
        # ----------------------------------------
        engine = get_db()
        df = filter_df(engine, store, date, start_hour,
                       start_minute, end_hour, end_min, cam)
        # ------------------------------------
        lin_traffic = visual_count(df)
        map_traffic = print_path(df, imgx)
        heat_traffic = print_hot_spots(df, imgx, 'temp_hot_spot.jpeg')
        return map_traffic, lin_traffic, heat_traffic
    else:
        return (no_update, no_update, no_update)


if __name__ == "__main__":
    app.run_server(debug=True)