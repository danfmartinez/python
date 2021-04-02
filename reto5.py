# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 18:36:24 2020

@author: Daniel
"""
import pandas as pd
import os.path

def caso_who(ruta_archivo_csv: str)-> dict:
    # se valida la extension del archivo, debe ser .csv
    nombre_archivo, extension = os.path.splitext(ruta_archivo_csv)
    if extension != ".csv":
        return ("Extensión inválida.")
    try:
        covid = pd.read_csv(ruta_archivo_csv)
        covid["date"] = pd.to_datetime(covid["date"])
        # razón entre el número total de casos de COVID-19 y el número total de camas de hospital disponibles
        covid["razon"]= (covid["total_cases_per_million"] * covid["population"] / 1_000_000) \
            / (covid["hospital_beds_per_thousand"] * covid["population"] / 1000 )
        # se agrupan los datos por continentes y dias, y se halla el promedio de la razon
        grafica = covid.groupby(by=["continent","date"])["razon"].mean().reset_index()
        grafica = grafica.pivot(index ="date", columns = "continent", values = "razon" )
        #grafica.plot()
        # respuesta en forma de diccionario
        return (grafica.to_dict())
    # Error al leer el archivo
    except:
        return ("Error al leer el archivo de datos.")


print(caso_who("owid-covid-data.csv"))