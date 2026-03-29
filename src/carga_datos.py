# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:19:57 2026

@author: nacho
"""
def parsear_linea(linea:str)->list:
    """
   Parsea una línea del archivo y convierte cada valor a su tipo correspondiente.

   Parámetros:
   linea (str): línea del archivo en formato CSV

   Retorna:
   list: lista con los valores convertidos
   """
    partes=linea.strip().split(",")
    id_participante=int(partes[0])
    tiempo=float(partes[1])
    x=float(partes[2])
    y=float(partes[3])
    hit = partes[4].strip().lower() == "true"
    condicion=partes[5].split()
    
    return [id_participante, tiempo, x, y, hit, condicion]

def cargar_datos(ruta: str) -> list:
    """
    Carga los datos desde un archivo y los organiza por participante.

    Parámetros:
    ruta (str): ruta del archivo

    Retorna:
    list: lista de diccionarios (uno por participante)
    """
    participantes = {}

    archivo = open(ruta, "r")

    for linea in archivo:
        datos = parsear_linea(linea)

        id_p, tiempo, x, y, hit, condicion = datos

        if id_p not in participantes:
            participantes[id_p] = {
                "id_participante": id_p,
                "tiempo": [],
                "x": [],
                "y": [],
                "hit": [],
                "condicion": []
            }

        participantes[id_p]["tiempo"].append(tiempo)
        participantes[id_p]["x"].append(x)
        participantes[id_p]["y"].append(y)
        participantes[id_p]["hit"].append(hit)
        participantes[id_p]["condicion"].append(condicion)

    archivo.close()

    return list(participantes.values())