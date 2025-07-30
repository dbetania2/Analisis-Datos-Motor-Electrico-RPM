import pandas as pd 
import numpy as np 

def clean_and_prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    realizar limpieza de valores nulos y generar columna de tiempo.

    args:
        df (pd.DataFrame): dataframe original.

    returns:
        pd.DataFrame: dataframe limpio y con columna de tiempo.
    """
    if df is None:
        print("no poder limpiar un dataframe nulo.") # mostrar mensaje si dataframe es nulo
        return None

    print("\n--- iniciar limpieza y preparacion de datos ---") # mostrar inicio de proceso

    #manejar valores nulos
    initial_rows = df.shape[0] # obtener numero inicial de filas
    df_cleaned = df.dropna().copy() # eliminar filas con nulos y crear copia
    rows_after_dropna = df_cleaned.shape[0] # obtener numero de filas despues de eliminar nulos

    if initial_rows > rows_after_dropna:
        print(f"eliminar {initial_rows - rows_after_dropna} fila(s) con valores nulos.") # mostrar filas eliminadas
    else:
        print("no encontrar filas con valores nulos para eliminar.") # mostrar mensaje si no hay nulos

    # verificar nulos restantes
    null_after_drop = df_cleaned.isnull().sum().sum() # contar nulos totales
    if null_after_drop == 0:
        print("el dataframe ahora estar libre de valores nulos!") # confirmar ausencia de nulos
    else:
        print(f"advertencia: aun quedar {null_after_drop} valores nulos despues de la limpieza basica.") # advertir sobre nulos restantes

    #generar columna de tiempo
    # agrupar por 'profile_id' y generar contador para cada elemento
    df_cleaned['Tiempo_Segundos'] = df_cleaned.groupby('profile_id').cumcount() / 2
    print("columna 'tiempo_segundos' generar para cada sesion de prueba.") # mostrar confirmacion de columna generada
    print(f"primeros 5 valores de 'tiempo_segundos':\n{df_cleaned['Tiempo_Segundos'].head()}") # mostrar primeros valores
    print(f"ultimos 5 valores de 'tiempo_segundos':\n{df_cleaned['Tiempo_Segundos'].tail()}") # mostrar ultimos valores

    print("\n--- limpieza y preparacion completadas ---") # mostrar finalizacion de proceso

    return df_cleaned # devolver dataframe limpio