from dash import Input, Output, State

def register_sidebar_callback(app):

    @app.callback(
        Output("sidebar", "className"),
        Output("sidebar-state", "data"),
        Input("toggle-sidebar", "n_clicks"),
        State("sidebar-state", "data"),
        prevent_initial_call=True
    )
    def toggle_sidebar(n, is_open):

        is_open = not is_open

        if is_open:
            return "sidebar", is_open
        else:
            return "sidebar collapsed", is_open