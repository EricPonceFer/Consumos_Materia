from dash import Input, Output
from Pages import dashboard_agua, dashboard_combustible, dashboard_energia

def redirigir_home(app):

    @app.callback(
    Output("url", "pathname"),
    Input("url", "pathname"),
    prevent_initial_call=False
    )
    def redirect_home(pathname):
        if pathname in [None, "/"]:
            return "/agua"
        return pathname

def register_navigation_callback(app):

    @app.callback(
        Output("content", "children"),
        Input("url", "pathname")
    )
    def render_page(pathname):

        if pathname == "/agua":
            return dashboard_agua.layout()

        elif pathname == "/energia":
            return dashboard_energia.layout()

        elif pathname == "/combustible":
            return dashboard_combustible.layout()

        return dashboard_agua.layout()