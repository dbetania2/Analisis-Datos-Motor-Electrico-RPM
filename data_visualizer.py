import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 


def plot_and_summarize_temperature_trends(df: pd.DataFrame, profile_ids_to_plot: list):
    """
    generar graficos de linea para temperaturas clave y resumir hallazgos.

    args:
        df (pd.DataFrame): dataframe limpio con columna de tiempo.
        profile_ids_to_plot (list): lista de profile_id para visualizar.
    """
    if df is None:
        print("no poder generar visualizaciones, el dataframe es nulo.") # mostrar mensaje si dataframe es nulo
        return

    print("\n--- generar visualizaciones de tendencias de temperatura ---") # mostrar inicio de proceso

    temp_cols = ['pm', 'stator_winding', 'stator_tooth', 'stator_yoke', 'coolant', 'ambient'] # definir columnas de temperatura

    for profile_id in profile_ids_to_plot: # iterar sobre cada id de perfil
        df_profile = df[df['profile_id'] == profile_id].copy() # filtrar datos por profile_id

        if df_profile.empty:
            print(f"advertencia: no encontrar datos para el profile_id {profile_id}. saltar.") # mostrar advertencia si no hay datos
            continue

        print(f"\n--- analisis visual y resumen para profile id: {profile_id} ---") # mostrar resumen por perfil

        plt.figure(figsize=(12, 6)) # crear figura para grafico
        sns.lineplot(data=df_profile, x='Tiempo_Segundos', y='pm', label='temperatura_rotor (pm)', color='red') # graficar temperatura rotor
        sns.lineplot(data=df_profile, x='Tiempo_Segundos', y='stator_winding', label='temperatura_devanado_estator', color='blue') # graficar temperatura devanado estator
        sns.lineplot(data=df_profile, x='Tiempo_Segundos', y='stator_tooth', label='temperatura_diente_estator', color='green') # graficar temperatura diente estator
        sns.lineplot(data=df_profile, x='Tiempo_Segundos', y='stator_yoke', label='temperatura_yugo_estator', color='purple') # graficar temperatura yugo estator
        sns.lineplot(data=df_profile, x='Tiempo_Segundos', y='coolant', label='temperatura_refrigerante', color='cyan') # graficar temperatura refrigerante
        sns.lineplot(data=df_profile, x='Tiempo_Segundos', y='ambient', label='temperatura_ambiente', color='gray') # graficar temperatura ambiente

        plt.title(f'tendencias de temperatura para profile id: {profile_id}') # establecer titulo de grafico
        plt.xlabel('tiempo (segundos)') # establecer etiqueta eje x
        plt.ylabel('temperatura (°c)') # establecer etiqueta eje y
        plt.grid(True) # mostrar rejilla
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1)) # colocar leyenda fuera del grafico
        plt.tight_layout() # ajustar layout
        plt.show() # mostrar grafico

        # --- resumen de resultados del grafico en terminal ---
        print(f"resumen de temperaturas para profile id {profile_id}:") # mostrar resumen de temperaturas
        for col in temp_cols: # iterar sobre columnas de temperatura
            min_temp = df_profile[col].min() # obtener temperatura minima
            max_temp = df_profile[col].max() # obtener temperatura maxima
            mean_temp = df_profile[col].mean() # obtener temperatura promedio
            print(f"  {col}: min={min_temp:.2f}°c, max={max_temp:.2f}°c, promedio={mean_temp:.2f} °c") # mostrar estadisticas de temperatura

        initial_pm = df_profile['pm'].iloc[0] # obtener temperatura rotor inicial
        final_pm = df_profile['pm'].iloc[-1] # obtener temperatura rotor final
        max_pm = df_profile['pm'].max() # obtener temperatura rotor maxima
        time_at_max_pm = df_profile['Tiempo_Segundos'].loc[df_profile['pm'].idxmax()] # obtener tiempo en temperatura rotor maxima

        print(f"\n  temperatura del rotor (pm) - inicio: {initial_pm:.2f}°c, final: {final_pm:.2f}°c") # mostrar temperaturas inicial y final
        print(f"  temperatura maxima del rotor (pm): {max_pm:.2f}°c (alcanzar en {time_at_max_pm:.2f} segundos)") # mostrar temperatura maxima y tiempo

        if final_pm > initial_pm * 1.05: # verificar aumento significativo
            print(f"  observacion: la temperatura del rotor (pm) en este perfil tender a aumentar significativamente ({final_pm - initial_pm:.2f}°c de cambio neto).")
        elif final_pm < initial_pm * 0.95: # verificar disminucion significativa
            print(f"  observacion: la temperatura del rotor (pm) en este perfil tender a disminuir significativamente ({initial_pm - final_pm:.2f}°c de cambio neto).")
        else:
            print(f"  observacion: la temperatura del rotor (pm) en este perfil mantenerse relativamente estable.")


def plot_and_summarize_operational_trends(df: pd.DataFrame, profile_ids_to_plot: list):
    """
    generar graficos de linea para variables operacionales y resumir hallazgos.

    args:
        df (pd.DataFrame): dataframe limpio con columna de tiempo.
        profile_ids_to_plot (list): lista de profile_id para visualizar.
    """
    if df is None:
        print("no poder generar visualizaciones, el dataframe es nulo.") # mostrar mensaje si dataframe es nulo
        return

    print("\n--- generar visualizaciones de tendencias operacionales ---") # mostrar inicio de proceso

    op_cols = ['motor_speed', 'torque', 'i_d', 'i_q', 'u_d', 'u_q'] # definir columnas operacionales

    for profile_id in profile_ids_to_plot: # iterar sobre cada id de perfil
        df_profile = df[df['profile_id'] == profile_id].copy() # filtrar datos por profile_id

        if df_profile.empty:
            print(f"advertencia: no encontrar datos para el profile_id {profile_id}. saltar.") # mostrar advertencia si no hay datos
            continue

        print(f"\n--- analisis visual y resumen operacional para profile id: {profile_id} ---") # mostrar resumen por perfil

        # grafico de velocidad y torque
        plt.figure(figsize=(12, 6)) # crear figura para grafico
        sns.lineplot(data=df_profile, x='Tiempo_Segundos', y='motor_speed', label='velocidad del motor (rpm)', color='orange') # graficar velocidad motor
        sns.lineplot(data=df_profile, x='Tiempo_Segundos', y='torque', label='torque (nm)', color='brown', linestyle='--') # graficar torque
        plt.title(f'velocidad y torque del motor para profile id: {profile_id}') # establecer titulo de grafico
        plt.xlabel('tiempo (segundos)') # establecer etiqueta eje x
        plt.ylabel('valor') # establecer etiqueta eje y
        plt.grid(True) # mostrar rejilla
        plt.legend() # mostrar leyenda
        plt.show() # mostrar grafico

        # grafico de corrientes y voltajes
        plt.figure(figsize=(12, 6)) # crear figura para grafico
        sns.lineplot(data=df_profile, x='Tiempo_Segundos', y='i_d', label='corriente i_d', color='darkgreen') # graficar corriente i_d
        sns.lineplot(data=df_profile, x='Tiempo_Segundos', y='i_q', label='corriente i_q', color='darkblue') # graficar corriente i_q
        sns.lineplot(data=df_profile, x='Tiempo_Segundos', y='u_d', label='voltaje u_d', color='red', linestyle=':') # graficar voltaje u_d
        sns.lineplot(data=df_profile, x='Tiempo_Segundos', y='u_q', label='voltaje u_q', color='purple', linestyle=':') # graficar voltaje u_q
        plt.title(f'corrientes y voltajes de control para profile id: {profile_id}') # establecer titulo de grafico
        plt.xlabel('tiempo (segundos)') # establecer etiqueta eje x
        plt.ylabel('valor') # establecer etiqueta eje y
        plt.grid(True) # mostrar rejilla
        plt.legend() # mostrar leyenda
        plt.show() # mostrar grafico

        # --- resumen de resultados del grafico en terminal ---
        print(f"resumen de variables operacionales para profile id {profile_id}:") # mostrar resumen de variables operacionales
        for col in op_cols: # iterar sobre columnas operacionales
            min_val = df_profile[col].min() # obtener valor minimo
            max_val = df_profile[col].max() # obtener valor maximo
            mean_val = df_profile[col].mean() # obtener valor promedio
            print(f"  {col}: min={min_val:.2f}, max={max_val:.2f}, promedio={mean_val:.2f}") # mostrar estadisticas

        avg_speed = df_profile['motor_speed'].mean() # obtener velocidad promedio
        max_speed = df_profile['motor_speed'].max() # obtener velocidad maxima
        avg_torque = df_profile['torque'].mean() # obtener torque promedio
        max_torque = df_profile['torque'].abs().max() # obtener torque maximo absoluto

        print(f"\n  velocidad del motor - promedio: {avg_speed:.2f} rpm, maximo: {max_speed:.2f} rpm") # mostrar estadisticas velocidad
        print(f"  torque - promedio: {avg_torque:.2f} nm, maximo absoluto: {max_torque:.2f} nm") # mostrar estadisticas torque
        print(f"  observacion: la velocidad y el torque mostrar patrones que indicar la carga de trabajo del motor.")
        if df_profile['torque'].min() < 0: # verificar torque negativo
            print("  nota: observar valores de torque negativos, sugerir frenado o regeneracion de energia.")


def plot_and_summarize_correlation_heatmap(df: pd.DataFrame):
    """
    generar mapa de calor de matriz de correlacion y resumir hallazgos.

    args:
        df (pd.DataFrame): dataframe limpio.
    """
    if df is None:
        print("no poder generar el mapa de calor, el dataframe es nulo.") # mostrar mensaje si dataframe es nulo
        return

    print("\n--- generar visualizacion de la matriz de correlacion ---") # mostrar inicio de proceso

    # excluir columnas de identificacion y tiempo para correlacion visual
    df_corr = df.drop(columns=['profile_id', 'Tiempo_Segundos'])
    correlation_matrix = df_corr.corr() # calcular matriz de correlacion

    # crear mascara para parte superior del triangulo (matriz simetrica)
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

    plt.figure(figsize=(14, 10)) # crear figura para grafico
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", # graficar mapa de calor
                linewidths=.5, mask=mask, cbar_kws={"shrink": .8})
    plt.title('mapa de calor de la matriz de correlacion') # establecer titulo de grafico
    plt.xticks(rotation=45, ha='right') # rotar etiquetas eje x
    plt.yticks(rotation=0) # rotar etiquetas eje y
    plt.tight_layout() # ajustar layout
    plt.show() # mostrar grafico

    # --- resumen de resultados del grafico en terminal ---
    print("\n--- resumen del mapa de calor de correlacion ---") # mostrar resumen
    print("el mapa de calor mostrar fuerza y direccion de relacion lineal entre variables.")
    print("  - colores calidos (rojo) indicar correlacion positiva fuerte.")
    print("  - colores frios (azul) indicar correlacion negativa fuerte.")
    print("  - colores cercanos al blanco/cero indicar poca o ninguna correlacion lineal.")

    # enfocar en 'pm'
    pm_correlations = correlation_matrix['pm'].sort_values(ascending=False) # obtener correlaciones con pm
    print("\nlas correlaciones mas relevantes con la temperatura del rotor (pm) son:") # mostrar correlaciones relevantes
    for col, corr_value in pm_correlations.items(): # iterar sobre correlaciones
        if col != 'pm': # excluir correlacion de pm consigo mismo
            print(f"  - {col}: {corr_value:.4f}") # mostrar valor de correlacion
