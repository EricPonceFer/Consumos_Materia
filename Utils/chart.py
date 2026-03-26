import plotly.express as px

def create_area_chart(df, y, title="", anio=None, mes=None, nivel="mes"):

    if df is None or df.empty:
        raise ValueError("El DataFrame está vacío")

    # 🔹 filtros
    if anio is not None:
        df = df[df["AÑO"] == anio]

    if mes is not None:
        df = df[df["MES"] == mes]

    # 🔹 agrupación
    if nivel == "anio":
        df["PERIODO"] = df["FECHA"].dt.to_period("Y")
    elif nivel == "mes":
        df["PERIODO"] = df["FECHA"].dt.to_period("M")
    elif nivel == "dia":
        df["PERIODO"] = df["FECHA"]
    else:
        raise ValueError("nivel debe ser: 'anio', 'mes' o 'dia'")

    df_grouped = df.groupby("PERIODO", as_index=False)[y].sum()

    # 🔹 convertir periodo
    if nivel != "dia":
        df_grouped["PERIODO"] = df_grouped["PERIODO"].dt.to_timestamp()

    df_grouped = df_grouped.sort_values("PERIODO")

    # 🔹 formato largo
    df_grouped = df_grouped.melt(
        id_vars="PERIODO",
        value_vars=y,
        var_name="VARIABLE",
        value_name="VALOR"
    )

    # 🔹 gráfico
    fig = px.line(
        df_grouped,
        x="PERIODO",
        y="VALOR",
        color="VARIABLE",
        text="VALOR"
    )

    fig.update_traces(
        fill="tozeroy",
        mode="lines+markers+text",
        textposition="top center",
        texttemplate="%{y:,.0f}"
    )

    formato = {
        "anio": "%Y",
        "mes": "%b %Y",
        "dia": "%d %b %Y"
    }

    fig.update_layout(
        title=title,
        plot_bgcolor="white",
        paper_bgcolor="white",
        xaxis=dict(showgrid=False, tickformat=formato[nivel]),
        yaxis=dict(showgrid=True, gridcolor="#eee"),
        margin=dict(l=20, r=20, t=40, b=20),
        hovermode="x unified"
    )

    return fig

def create_stacked_bar_chart(df, y, title="", anio=None, mes=None, nivel="mes"):

    # 🔹 validar dataframe
    if df is None or df.empty:
        raise ValueError("El DataFrame está vacío")

    # 🔹 filtros
    if anio is not None:
        df = df[df["AÑO"] == anio]

    if mes is not None:
        df = df[df["MES"] == mes]

    # 🔹 agrupación
    if nivel == "anio":
        df["PERIODO"] = df["FECHA"].dt.to_period("Y")
    elif nivel == "mes":
        df["PERIODO"] = df["FECHA"].dt.to_period("M")
    elif nivel == "dia":
        df["PERIODO"] = df["FECHA"]
    else:
        raise ValueError("nivel debe ser: 'anio', 'mes' o 'dia'")

    df_grouped = df.groupby("PERIODO", as_index=False)[y].sum()

    # 🔹 convertir periodo
    if nivel != "dia":
        df_grouped["PERIODO"] = df_grouped["PERIODO"].dt.to_timestamp()

    df_grouped = df_grouped.sort_values("PERIODO")

    # 🔹 formato largo
    df_grouped = df_grouped.melt(
        id_vars="PERIODO",
        value_vars=y,
        var_name="VARIABLE",
        value_name="VALOR"
    )

    # 🔹 gráfico barras apiladas
    fig = px.bar(
        df_grouped,
        x="PERIODO",
        y="VALOR",
        color="VARIABLE",
        text="VALOR"
    )

    # 🔹 formato etiquetas
    fig.update_traces(
        texttemplate="%{y:,.0f}",
        textposition="inside"
    )

    # 🔹 formato eje X
    formato = {
        "anio": "%Y",
        "mes": "%b %Y",
        "dia": "%d %b %Y"
    }

    fig.update_layout(
        barmode="stack",  # 👈 clave
        title=title,
        plot_bgcolor="white",
        paper_bgcolor="white",
        xaxis=dict(showgrid=False, tickformat=formato[nivel]),
        yaxis=dict(showgrid=True, gridcolor="#eee"),
        margin=dict(l=20, r=20, t=40, b=20),
        hovermode="x unified"
    )

    return fig