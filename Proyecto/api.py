import pandas as pd
from sodapy import Socrata

def queries(nombre_departamento, nombre_municipio, nombre_cultivo, limite_registro):
    # Crear un cliente para la API de Socrata
    client = Socrata("www.datos.gov.co", None)
    
    # Realizar la consulta a la API de Socrata con los parámetros proporcionados
    results = client.get("ch4u-f3i5", 
                         departamento=nombre_departamento.upper(), 
                         municipio=nombre_municipio.upper(), 
                         cultivo=nombre_cultivo, 
                         limit=limite_registro)
    
    # Convertir los resultados obtenidos de la API a un DataFrame de Pandas
    results_df = pd.DataFrame.from_records(results)
    
    # Renombrar las columnas del DataFrame para que sean más legibles
    results_df.rename(columns={
        "departamento": "Departamento", 
        "municipio": "Municipio", 
        "cultivo": "Cultivo",
        "topografia": "Topografia", 
        "ph_agua_suelo_2_5_1_0": "pH", 
        "f_sforo_p_bray_ii_mg_kg": "Fosforo(P)",
        "potasio_k_intercambiable_cmol_kg": "Potasio(K)"
    }, inplace=True)
    
    
    # Convertir las columnas 'pH', 'Fosforo(P)' y 'Potasio(K)' a valores numéricos
    # Si algún valor no puede ser convertido, se reemplazará con NaN
    results_df["pH"] = pd.to_numeric(results_df["pH"], errors='coerce')
    results_df["Fosforo(P)"] = pd.to_numeric(results_df["Fosforo(P)"], errors='coerce')
    results_df["Potasio(K)"] = pd.to_numeric(results_df["Potasio(K)"], errors='coerce')
    
    # Reemplazar valores NaN en las columnas numéricas con 0
    results_df["pH"] = results_df["pH"].fillna(0)
    results_df["Fosforo(P)"] = results_df["Fosforo(P)"].fillna(0)
    results_df["Potasio(K)"] = results_df["Potasio(K)"].fillna(0)
    
    # Calcular la mediana de las columnas numéricas
    results_df["pH_mediana"] = results_df["pH"].median()
    results_df["Fosforo(P)_mediana"] = results_df["Fosforo(P)"].median()
    results_df["Potasio(K)_mediana"] = results_df["Potasio(K)"].median()
    
    # Retornar un DataFrame con las columnas relevantes, incluyendo las medianas calculadas
    return results_df[["Departamento", "Municipio", "Cultivo", "Topografia", "pH_mediana", "Fosforo(P)_mediana", "Potasio(K)_mediana"]]
