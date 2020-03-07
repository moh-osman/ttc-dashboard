# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

ttc_east = pd.read_csv('data/ttc_east.csv')
station_order = ["KIP","ISL","RYK","OML","JNE","RUN","HPK","KEL",
                 "DNW","LAN","DUF","OSS","CHR","BAT","BSP","SGL",
                 "BAU","YNG","SHE","CFK","BRD","CHE","PAP","DON",
                 "GWD","COX","MST","VPK","WAR","KEN"]
index_rename = {"KIP":"Kipling","ISL":"Islington","RYK":"Royal York","OML":"Old Mill",
                              "JNE":"Jane","RUN":"Runnymede","HPK":"High Park","KEL":"Keele","DNW":"Dundas West",
                              "LAN":"Lansdowne","DUF":"Dufferin","OSS":"Ossington","CHR":"Christie","BAT":"Bathurst",
                              "BSP":"Spadina","SGL":"St. George","BAU":"Bay","YNG":"Yonge","SHE":"Sherbourne",
                              "CFK":"Castle Frank","BRD":"Broadview","CHE":"Chester","PAP":"Pape","DON":"Donlands",
                              "GWD":"Greenwood","COX":"Coxwell","MST":"Main Street","VPK":"Victoria Park",
                              "WAR":"Warden","KEN":"Kennedy"}

ttc_east['station_char'] = pd.Categorical(ttc_east['station_char'],station_order).remove_unused_categories()

te = ttc_east.copy()[['station_char','headway']].groupby('station_char').mean().rename(index=index_rename)
te['headway'] = np.round(te['headway'],2)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='TTC Subway Dashboard'),

    html.Div(children='''
        
    '''),

    dcc.Graph(
        id='example-graph2',
        figure={
            'data': [
                dict(
                    x=te.index,
                    y=te.headway,
                    type='bar'
                )
            ],
            'layout': {
                'title': 'EFbound'
            }
        }
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                dict(
                    x = te.index,
                    y = te.headway,
                    type = 'bar'
                )
            ],
            'layout': {
                'title': 'Eastbound'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)