# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:22:00 2026

@author: nacho
"""
def calcular_hits_totales(datos: dict) -> int:
    """
    Calcula la cantidad total de hits de un participante.

    Parámetros:
    datos (dict): datos de un participante

    Retorna:
    int: cantidad total de hits
    """

    return sum(datos["hit"])

def calcular_tiempo_primer_hit(datos: dict):
    """
    Devuelve el tiempo en el que ocurre el primer hit.

    Parámetros:
    datos (dict): datos de un participante

    Retorna:
    float o None: tiempo del primer hit o None si no hay hits
    """

    for i in range(len(datos["hit"])):
        if datos["hit"][i]:
            return datos["tiempo"][i]

    return None

