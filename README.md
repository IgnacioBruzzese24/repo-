# repo- 
Integrantes: Ignacio Bruzzese, Juan Bautista Klein Larroude, Tobias Leonard

---

Este repositorio corresponde a un proyecto de la materia Programación (Ciencias del Comportamiento, Universidad de San Andrés).

El objetivo es trabajar con datos simulados de una tarea motora, aplicando conceptos de procesamiento de datos, organización del código y manejo de errores.

---

## Contexto del problema

Se estudia cómo los participantes realizan movimientos para alcanzar una zona objetivo bajo distintas condiciones:

* competencia
* cooperación

Durante la tarea:

* se registra la posición del movimiento (x, y)
* se mide el tiempo transcurrido
* se detecta si ocurre un evento relevante (hit)
* cada participante genera múltiples registros en el tiempo

Los datos se almacenan en un archivo CSV sin encabezado, donde cada fila representa un instante temporal.

---

## Objetivo del proyecto

Desarrollar un sistema que permita:

* procesar los datos registrados
* organizar la información por participante
* analizar el comportamiento motor en el tiempo
* calcular métricas básicas de desempeño

---

## Estructura de los datos

Cada registro contiene:

* id_participante
* tiempo
* x, y
* hit (True / False)
* condicion (competencia o cooperacion)

---

## Métricas

El sistema calcula:

1. Hits totales
   Cantidad de veces que el participante alcanza el objetivo

2. Tiempo del primer hit
   Momento en que ocurre el primer evento

---

## Enfoque del trabajo

El proyecto permite practicar:

* lectura de archivos
* procesamiento de datos
* uso de listas y diccionarios
* diseño modular de funciones
* validación de datos y manejo de errores

---

## Nota

Los datos utilizados son simulados y tienen fines exclusivamente educativos.

---

