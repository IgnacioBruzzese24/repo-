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
    datos = cargar_datos(ruta)

    print("Datos cargados correctamente\n")

    
    id_buscado = int(input("Ingrese ID del participante: "))

    participante = filtrar_por_participante(datos, id_buscado)

    
    if participante == None:
        print("Participante no encontrado")
        return

    
    hits_totales = calcular_hits_totales(participante)
    primer_hit = calcular_tiempo_primer_hit(participante)

    
    print("\n--- RESULTADOS ---")
    print(f"Participante: {id_buscado}")
    print(f"Condición: {participante['condicion'][0]}")
    print(f"Hits totales: {hits_totales}")

    if primer_hit != None:
        print(f"Tiempo del primer hit: {primer_hit} segundos")
    else:
        print("No hubo hits")



main()