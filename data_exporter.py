import pandas as pd 

def export_powerbi_ready_data(df: pd.DataFrame, file_path: str = 'motor_data_powerbi_ready.csv'):
    """
    renombrar columnas de dataframe y exportar a archivo csv o parquet.

    args:
        df (pd.DataFrame): dataframe limpio con columna de tiempo.
        file_path (str): ruta y nombre de archivo de salida.
    """
    if df is None:
        print("error: el dataframe proporcionado es nulo. no poder exportar.") # mostrar error si dataframe es nulo
        return

    print(f"\n--- preparar y exportar datos para power bi ---") # mostrar mensaje de preparacion



    # --- renombrar columnas para claridad en power bi ---
    df_powerbi_ready = df.rename(columns={
        'u_q': 'voltaje_q_v', # renombrar columna de voltaje q
        'coolant': 'temperatura_refrigerante_c', # renombrar columna de temperatura refrigerante
        'stator_winding': 'temperatura_devanado_estator_c', # renombrar columna de temperatura devanado estator
        'u_d': 'voltaje_d_v', # renombrar columna de voltaje d
        'stator_tooth': 'temperatura_diente_estator_c', # renombrar columna de temperatura diente estator
        'motor_speed': 'velocidad_motor_rpm', # renombrar columna de velocidad motor
        'i_d': 'corriente_d_a', # renombrar columna de corriente d
        'i_q': 'corriente_q_a', # renombrar columna de corriente q
        'pm': 'temperatura_rotor_c', # renombrar columna de temperatura rotor
        'stator_yoke': 'temperatura_yugo_estator_c', # renombrar columna de temperatura yugo estator
        'ambient': 'temperatura_ambiente_c', # renombrar columna de temperatura ambiente
        'torque': 'torque_nm', # renombrar columna de torque
        'profile_id': 'id_sesion_prueba', # renombrar columna de id de sesion de prueba
        'Tiempo_Segundos': 'tiempo_sesion_segundos' # renombrar columna de tiempo de sesion
    })

    # --- exportar dataframe con nombres amigables ---
    if file_path.endswith('.csv'):
        # exportar a csv, sin indice y con punto decimal
        df_powerbi_ready.to_csv(file_path, index=False, decimal='.')
        print(f"dataset preparado para power bi exportar como '{file_path}' (csv).") # mostrar mensaje de exportacion csv
    elif file_path.endswith('.parquet'):
        # exportar a parquet, sin indice
        df_powerbi_ready.to_parquet(file_path, index=False)
        print(f"dataset preparado para power bi exportar como '{file_path}' (parquet).") # mostrar mensaje de exportacion parquet
    else:
        # mostrar advertencia por formato de archivo no soportado
        print("advertencia: formato de archivo no soportado. usar '.csv' o '.parquet'.")