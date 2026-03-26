from dash import html

def create_content():
    return html.Div(
        [
            html.H1("Dashboard"),
        ],
        id="content",
        className="content",
    )