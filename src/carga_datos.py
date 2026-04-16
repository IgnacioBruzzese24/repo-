# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:19:57 2026

@author: nacho
"""
def parsear_linea(linea: str):
    """
    Procesa una línea del archivo CSV y convierte sus valores al tipo correspondiente.

    Parámetros:
    linea (str): línea del archivo CSV

    Retorna:
    list: lista con los valores convertidos en el siguiente orden:
          [id_participante, tiempo, x, y, hit, condicion]

    Errores:
    - ValueError si el formato es incorrecto
    - ValueError si los tipos de datos no son válidos
    - ValueError si el tiempo es negativo
    """

    if linea.strip() == "":
        return None

    partes = linea.strip().split(",")

    if len(partes) != 6:
        raise ValueError("Formato de línea incorrecto")

    try:
        id_participante = int(partes[0])
        tiempo = float(partes[1])
        x = float(partes[2])
        y = float(partes[3])
    except ValueError:
        raise ValueError("Error de tipo de dato en la línea")

    if tiempo < 0:
        raise ValueError("El tiempo no puede ser negativo")

    hit = partes[4].strip().lower() == "true"
    condicion = partes[5].strip()

    return [id_participante, tiempo, x, y, hit, condicion]


def cargar_datos(ruta: str):
    """
    Lee un archivo CSV y organiza los datos por participante.

    Parámetros:
    ruta (str): ruta del archivo CSV

    Retorna:
    list: lista de diccionarios, donde cada diccionario representa un participante con sus datos



    Errores:
    - Ignora líneas inválidas mostrando un mensaje
    - Continúa procesando el resto del archivo
    """

    archivo = open(ruta, "r")

    participantes = {}

    for linea in archivo:

        try:
            datos = parsear_linea(linea)

            if datos == None:
                continue

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

        except ValueError as e:
            print(f"Error en línea ignorada: {e}")
            continue

    archivo.close()

    return list(participantes.values())