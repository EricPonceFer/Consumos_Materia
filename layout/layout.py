from dash import html, dcc
from layout.header import create_header
from layout.sidebar import create_sidebar
from layout.content import create_content

def serve_layout():
    return html.Div([
        dcc.Location(id="url"),
        create_header(),
        html.Div([
            dcc.Store(id="sidebar-state", data=True),
            create_sidebar(),
            create_content()
        ], className="main")
    ])