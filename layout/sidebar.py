from dash import html
import dash_bootstrap_components as dbc

def create_sidebar():

    toggle_btn = html.Button(
        html.Img(src="/assets/resources/sidebar_flecha.png", className="toggle-icon"),
        id="toggle-sidebar",
        className="btn-toggle"
    )

    return html.Div(
        [
            html.Div(toggle_btn, className="sidebar-header"),

            html.P("PRINCIPAL", className="sidebar-section"),
            dbc.Nav(
                [
                    dbc.NavLink("Consumo Agua", href="/agua", active="exact"),
                    dbc.NavLink("Consumo Energía Eléctrica", href="/energia", active="exact"),
                    dbc.NavLink("Consumo Combustible", href="/combustible", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),

            html.P("COMPONENTES", className="sidebar-section"),
            dbc.Nav(
                [
                    dbc.NavLink("Gráficos", href="#"),
                    dbc.NavLink("Tablas", href="#"),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        id="sidebar",
        className="sidebar",
    )