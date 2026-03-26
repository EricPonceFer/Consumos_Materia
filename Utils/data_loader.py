import pandas as pd
from pathlib import Path

# 🔥 ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

def load_csv(nombre_archivo):
    ruta = BASE_DIR / "Data" / nombre_archivo

    try:
        df = pd.read_csv(ruta, sep=";")
        df = limpieza_dataframe(df)
        return df

    except Exception as e:
        print(f"Error cargando {nombre_archivo}: {e}")
        return pd.DataFrame()

import pandas as pd

def limpieza_dataframe(df):

    if df is None or df.empty:
        raise ValueError("El DataFrame está vacío")

    # 🔹 limpiar nombres de columnas
    df.columns = df.columns.str.strip()

    # 🔹 convertir DIA, MES, AÑO
    for col in ["DIA", "MES", "AÑO"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # 🔹 eliminar filas sin fecha base
    df = df.dropna(subset=["DIA", "MES", "AÑO"])

    # 🔹 convertir todas las demás columnas numéricas
    cols_numericas = df.select_dtypes(include=["object", "float", "int"]).columns
    cols_numericas = [c for c in cols_numericas if c not in ["DIA", "MES", "AÑO"]]

    for col in cols_numericas:
        df[col] = pd.to_numeric(df[col], errors="coerce")

        # 🔹 reemplazar negativos por 0
        df[col] = df[col].clip(lower=0)

    # 🔹 crear FECHA si no existe
    if "FECHA" not in df.columns:
        df["FECHA"] = pd.to_datetime(
            dict(year=df["AÑO"], month=df["MES"], day=df["DIA"]),
            errors="coerce"
        )

    return df