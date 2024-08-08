import pandas as pd
import glob
import os
import json


def cargar_datos_csv() :

    carpeta_actual = os.path.dirname(__file__)  
    carpeta_csv = os.path.join(carpeta_actual, 'starwars', 'csv')
    archivos_csv = glob.glob(os.path.join(carpeta_csv, '*.csv'))


    if not archivos_csv:

        print("No se encontraron archivos CSV en la carpeta especificada.")

    else:
        diccionarios_csv = {os.path.basename(archivo): pd.read_csv(archivo).to_dict(orient='records') for archivo in archivos_csv}

        db={}
        for nombre_archivo, diccionario in diccionarios_csv.items():
            if nombre_archivo=='characters.csv' or nombre_archivo=='planets.csv' or nombre_archivo=='starships.csv' or nombre_archivo=='weapons.csv' :
                lista_diccionarios=[]
                for registro in diccionario:
                    lista_diccionarios.append(registro)
                db[nombre_archivo.replace('.csv','')]=lista_diccionarios
        
    return db

#db es una base de datos creada a partir de los csv de characters, planets, starships y weapons. 
#cada una de estas es una llave del diccionario, y sus valores son una lista de characters, una lista de planets, una lista de starship y una lista de weapons respectivamente
#cada elemento de esta lista es de tipo diccionario y contiene caracateristicas referentes a los personajes, planetas, neves o armas.
















        





        