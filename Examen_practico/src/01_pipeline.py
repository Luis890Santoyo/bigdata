import pandas as pd
import numpy as np
import requests


# ============================================================
# 1. OBTENCIÓN DE LOS DATOS
# ============================================================

# Ejemplo: carga desde archivo local
# df = pd.read_csv("data/raw/<carpeta_dataset>/<archivo>.csv")

# Ejemplo: carga desde URL (Our World in Data)
# url_datos = (
#     "https://ourworldindata.org/grapher/<dataset>.csv"
#     "?v=1&csvType=full&useColumnShortNames=true"
# )
# df = pd.read_csv(
#     url_datos,
#     storage_options={
#         "User-Agent": "Our World In Data data fetch/1.0"
#     }
# )


# ============================================================
# 2. FUNCIÓN DEL PIPELINE
# ============================================================

def ejecutar_pipeline(df):

    print("============================================")
    print("INICIO DEL PIPELINE")
    print("============================================")

    # --------------------------------------------------------
    # 2.1 Dimensiones iniciales
    # --------------------------------------------------------

    print("\nDimensiones iniciales:")
    print(df.shape)

    # --------------------------------------------------------
    # 2.2 Identificar las columnas disponibles
    # --------------------------------------------------------

    print("\nColumnas disponibles:")
    print(df.columns.tolist())

    # --------------------------------------------------------
    # 2.3 Tipos de datos
    # --------------------------------------------------------

    print("\nTipos de datos:")
    print(df.dtypes)

    # --------------------------------------------------------
    # 2.4 Valores nulos
    # --------------------------------------------------------

    print("\nValores nulos:")
    print(df.isnull().sum())

    # --------------------------------------------------------
    # 2.5 Eliminar filas con valores nulos
    # --------------------------------------------------------

    df = df.dropna()

    print("\nDimensiones después de eliminar nulos:")
    print(df.shape)

    # --------------------------------------------------------
    # 2.6 Eliminar posibles filas duplicadas
    # --------------------------------------------------------

    df = df.drop_duplicates()

    print("\nDimensiones después de eliminar duplicados:")
    print(df.shape)

    # --------------------------------------------------------
    # 2.7 Resultado
    # --------------------------------------------------------

    archivo_salida = "data/processed/resultado.csv"

    df.to_csv(
        archivo_salida,
        index=False
    )

    print("\n============================================")
    print("PIPELINE FINALIZADO")
    print("============================================")

    print(f"\nArchivo generado:")
    print(archivo_salida)

    return df


# ============================================================
# 3. EJECUCIÓN DEL PIPELINE
# ============================================================

if __name__ == "__main__":
    # df_procesado = ejecutar_pipeline(df)
    pass
