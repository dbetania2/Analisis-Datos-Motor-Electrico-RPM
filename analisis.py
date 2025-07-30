import pandas as pd
import numpy as np
from data_exporter import export_powerbi_ready_data
from data_cleaner import clean_and_prepare_data
from data_analyzer import analyze_descriptive_statistics, analyze_profile_ids, analyze_correlations
from data_visualizer import (
    plot_and_summarize_temperature_trends,
    plot_and_summarize_operational_trends,
    plot_and_summarize_correlation_heatmap 
)

# --- Configuración de Nombres de Archivo y Rutas ---
FILE_NAME = 'Electric_Motor_Temperature.csv'
FILE_PATH = FILE_NAME

def load_data(file_path: str) -> pd.DataFrame:
    """
    cargar datos desde un archivo csv.
    """
    try:
        df = pd.read_csv(file_path) # leer archivo csv
        print(f"dataset '{file_path}' cargar exitosamente.") 
        return df # devolver dataframe
    except FileNotFoundError:
        # mostrar error si archivo no se encuentra
        print(f"error: el archivo '{file_path}' no encontrar. asegurar que este en la misma carpeta o revisar la ruta.")
        return None # devolver nulo en caso de error
    except Exception as e:
        # mostrar error general al cargar dataset
        print(f"ocurrir un error al cargar el dataset: {e}")
        return None # devolver nulo en caso de error

def inspect_data(df: pd.DataFrame):
    """
    inspeccionar estructura y contenido de dataframe.
    """
    if df is None:
        print("no poder inspeccionar un dataframe nulo.") # mostrar mensaje si dataframe es nulo
        return

    print("\n--- columnas y tipos de datos (despues de la limpieza) ---")
    df.info() # mostrar informacion de dataframe

    print("\n--- primeras 5 filas del dataframe (despues de la limpieza) ---")
    print(df.head()) # mostrar primeras filas

    print("\n--- ultimas 5 filas del dataframe (despues de la limpieza) ---")
    print(df.tail()) # mostrar ultimas filas

# --- ejecucion principal ---
if __name__ == "__main__":
    df_motor = load_data(FILE_PATH) # cargar datos del motor
    if df_motor is not None: # verificar si datos fueron cargados
        df_motor_cleaned = clean_and_prepare_data(df_motor) # limpiar y preparar datos
        if df_motor_cleaned is not None: # verificar si datos fueron limpiados
            inspect_data(df_motor_cleaned) # inspeccionar datos limpios
            analyze_descriptive_statistics(df_motor_cleaned) # analizar estadisticas descriptivas
            analyze_profile_ids(df_motor_cleaned) # analizar ids de perfil

            profiles_to_visualize = [11.0, 29.0, 6.0] # definir perfiles a visualizar
            plot_and_summarize_temperature_trends(df_motor_cleaned, profiles_to_visualize) # graficar tendencias de temperatura
            plot_and_summarize_operational_trends(df_motor_cleaned, profiles_to_visualize) # graficar tendencias operacionales

            analyze_correlations(df_motor_cleaned) # analizar correlaciones (mostrar matriz textual)

            #generar el mapa de calor de correlacion
            plot_and_summarize_correlation_heatmap(df_motor_cleaned) # graficar mapa de calor de correlacion
            export_powerbi_ready_data(df_motor_cleaned, file_path='motor_data_powerbi_ready.csv') # exportar datos para powerbi