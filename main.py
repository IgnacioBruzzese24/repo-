# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:12:34 2026

@author: nacho
"""

from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import (
    calcular_hits_totales,
    calcular_tiempo_primer_hit
)

def main():
    ruta = "datos/datos_proyecto.csv"

    try:
        datos = cargar_datos(ruta)
    except FileNotFoundError:
        print("Error: no se encontró el archivo de datos.")
        return
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return

    print("Datos cargados correctamente\n")

    try:
        id_buscado = int(input("Ingrese ID del participante: "))
    except ValueError:
        print("Error: el ID debe ser un número entero.")
        return

    participante = filtrar_por_participante(datos, id_buscado)

    if participante == None:
        print("Error: participante no encontrado.")
        return

    try:
        hits_totales = calcular_hits_totales(participante)
        primer_hit = calcular_tiempo_primer_hit(participante)
    except Exception as e:
        print(f"Error al calcular métricas: {e}")
        return

    print("\n--- RESULTADOS ---")
    print(f"Participante: {id_buscado}")
    print(f"Condición: {participante['condicion'][0]}")
    print(f"Hits totales: {hits_totales}")

    if primer_hit != None:
        print(f"Tiempo del primer hit: {primer_hit}")
    else:
        print("No hubo hits")

main()