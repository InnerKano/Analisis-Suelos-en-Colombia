import pandas as pd
from sodapy import Socrata

def queries(nombre_departamento, nombre_municipio, nombre_cultivo, limite_registro):
    client = Socrata("www.datos.gov.co", None)
    results = client.get("ch4u-f3i5", departamento = nombre_departamento.upper(), municipio= nombre_municipio.upper(), 
    cultivo = nombre_cultivo,limit = limite_registro)
    results_df = pd.DataFrame.from_records(results)
    results_df.rename(columns= {"departamento": "Departamento", "municipio":"Municipio", "cultivo":"Cultivo",
     "topografia":"Topografia", "ph_agua_suelo_2_5_1_0":"pH", "f_sforo_p_bray_ii_mg_kg":"Fosforo(P)",
     "potasio_k_intercambiable_cmol_kg":"Potasio(K)"}, inplace = True)
    results_df["pH_mediana"] = results_df["pH"].median()
    results_df["Fosforo(P)_mediana"] = results_df["Fosforo(P)"].median()
    results_df["Potasio(K)_mediana"] = results_df["Potasio(K)"].median()

    return results_df[["Departamento", "Municipio", "Cultivo", "Topografia","pH_mediana","Fosforo(P)_mediana","Potasio(K)_mediana"]]
