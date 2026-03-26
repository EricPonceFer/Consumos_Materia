from dash import html

def create_header():
    return html.Div(
        [
            html.Div([
                html.Img(src="/assets/resources/levapan_logo.png", style={"width": "100px"})
            ]),

            html.Div([
                html.Button(
                    html.Img(src="/assets/resources/actualizar.png", className="img-icon"),
                    title="ACTUALIZAR DATOS",
                    className="btn-clean"
                ),
                html.Button(
                    html.Img(src="/assets/resources/informativo.png", className="img-icon"),
                    title="INFORMACIÓN",
                    className="btn-clean"
                ),
                html.Button(
                    html.Img(src="/assets/resources/notificaciones.png", className="img-icon"),
                    title="NOTIFICACIONES",
                    className="btn-clean"
                )
            ], style={"display": "flex", "gap": "2rem", "paddingRight": "2rem"})
        ],
        className="header"
    )