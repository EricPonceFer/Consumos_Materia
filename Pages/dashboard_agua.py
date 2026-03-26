from dash import html, dcc
from Data.loader import df_agua
from Utils.chart import create_area_chart, create_stacked_bar_chart

def layout():

    fig = create_stacked_bar_chart(df_agua, y=["CONSUMO POZO  [m3]","TOTAL ingreso EMMAPQ","CONSUMO TOTAL [M3]"], nivel="mes")
    tarjetas = html.Div([
        html.Div([
            html.P("Consumo Pozo"),
            html.P("Pago Pozo"),
        ]),
        html.Div([
            html.P("EMMAPQ"),
            html.P("Pago EMMAPQ"),
        ]),
        html.Div([
            html.P("Consumo Total"),
            html.P("Pago Total"),
        ])
    ], className="tarjetas-container")

    return html.Div([
        tarjetas,
        dcc.Graph(figure=fig)
        
    ])