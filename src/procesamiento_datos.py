# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:21:16 2026

@author: nacho
"""
def filtrar_por_participante(datos: list, id_participante: int) -> dict:
    """
    Devuelve los datos de un participante específico.

    Parámetros:
    datos (list): lista de participantes
    id_participante (int): ID buscado

    Retorna:
    dict: datos del participante o None si no existe
    """

    for participante in datos:
        if participante["id_participante"] == id_participante:
            return participante

    return None
