import pandas as pd 
import numpy as np 

def analyze_correlations(df: pd.DataFrame):
    """
    calcular y mostrar matriz de correlacion para variables numericas.

    args:
        df (pd.DataFrame): dataframe limpio y con columna de tiempo.
    """
    if df is None:
        print("no poder calcular correlaciones, el dataframe es nulo.")
        return

    print("\n--- analisis de correlacion entre variables ---")

    # calcular matriz de correlacion
    # excluir columnas de identificacion y tiempo
    correlation_matrix = df.drop(columns=['profile_id', 'Tiempo_Segundos']).corr()

    print("\nmatriz de correlacion completa:")
    # usar to_string para mostrar matriz completa
    print(correlation_matrix.to_string())

    print("\ninterpretacion de la matriz de correlacion:")
    print("   - valores variar de -1 a 1.")
    print("   - valores cercanos a 1 indicar fuerte correlacion positiva.")
    print("   - valores cercanos a -1 indicar fuerte correlacion negativa.")
    print("   - valores cercanos a 0 indicar poca correlacion lineal.")

    # enfocar en correlacion con 'pm' (temperatura del rotor)
    print("\ncorrelacion con la temperatura del rotor (pm):")
    # ordenar para ver las mas fuertes primero
    pm_correlations = correlation_matrix['pm'].sort_values(ascending=False)
    print(pm_correlations.to_string())

    print("\nanalisis clave de la correlacion con 'pm' (temperatura del rotor):")
    # identificar variables mas fuertemente correlacionadas
    top_correlated_pm = pm_correlations[1:4] # excluir 'pm' consigo mismo
    print(f"   las variables mas fuertemente correlacionadas positivamente con 'pm' son:")
    for index, value in top_correlated_pm.items():
        print(f"     - {index}: {value:.4f}")

    print("\nesta seccion ayuda a identificar variables relacionadas con la temperatura del rotor.")


def analyze_descriptive_statistics(df: pd.DataFrame):
    """
    calcular y mostrar estadisticas descriptivas para columnas numericas.

    args:
        df (pd.DataFrame): dataframe limpio.
    """
    if df is None:
        print("no poder calcular estadisticas, el dataframe es nulo.")
        return

    print("\n--- estadisticas descriptivas del dataset ---")
    # transponer tabla para mejor lectura
    print(df.describe().T)
    print("\nestas estadisticas resumen cada variable: promedio, desviacion, valores minimos y maximos, y distribucion.")

def analyze_profile_ids(df: pd.DataFrame):
    """
    analizar cantidad y duracion de sesiones de prueba (profile_id).

    args:
        df (pd.DataFrame): dataframe limpio.
    """
    if df is None:
        print("no poder analizar los id de perfil, el dataframe es nulo.")
        return

    print("\n--- analisis de sesiones de prueba (profile_id) ---")

    # contar numero de sesiones unicas
    num_profiles = df['profile_id'].nunique()
    print(f"numero total de sesiones de prueba unicas: {num_profiles}")

    # obtener id de las sesiones
    profile_ids = df['profile_id'].unique()
    print(f"los id de las sesiones son: {np.sort(profile_ids)}") # ordenar para mejor legibilidad

    # calcular duracion de cada sesion
    # agrupar por profile_id y obtener tiempo maximo
    # considerar tiempo_segundos como duracion
    profile_duration = df.groupby('profile_id')['Tiempo_Segundos'].max().reset_index()
    profile_duration.columns = ['profile_id', 'duracion_segundos']

    print("\nduracion de cada sesion de prueba (en segundos):")
    print(profile_duration)
    print("\nentender la duracion de cada sesion es crucial para la cantidad de datos disponibles por perfil.")

    avg_duration = profile_duration['duracion_segundos'].mean() # calcular duracion promedio
    min_duration = profile_duration['duracion_segundos'].min() # calcular duracion minima
    max_duration = profile_duration['duracion_segundos'].max() # calcular duracion maxima
    print(f"\nduracion promedio de las sesiones: {avg_duration:.2f} segundos")
    print(f"duracion minima de una sesion: {min_duration:.2f} segundos")
    print(f"duracion maxima de una sesion: {max_duration:.2f} segundos")