import dash
import dash_bootstrap_components as dbc
from layout.layout import serve_layout
from callbacks.sidebar_callback import register_sidebar_callback
from callbacks.navigation_callback import register_navigation_callback, redirigir_home



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = serve_layout()

redirigir_home(app)
register_sidebar_callback(app)
register_navigation_callback(app)


if __name__ == "__main__":
    app.run(debug=True)