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
##Errores y Validaciones

El sistema incluye validaciones para garantizar la correcta ejecución:

* Formato de línea: se verifica que cada registro tenga 6 valores
* Tipos de datos: conversión de ID (int) y variables numéricas (float)
* Rango: el tiempo debe ser mayor o igual a 0
* Líneas inválidas: se ignoran mostrando un mensaje de error
* Participante inexistente: se informa al usuario
* Entrada del usuario: se valida que el ID sea numérico

## Nota

Los datos utilizados son simulados y tienen fines exclusivamente educativos.

---

## molde del sistema usando objetos

- El sistema incluye estas clases:

* Clase Registro
--> representa un instante de medicion (una fila del archivo CSV)
Atributos 
id_participante: int
tiempo: float
x: float
y: float
hit: bool
condicion: str

Métodos
es_hit() --> devuelve si ocurrió un hit
es_valido() --> verifica los datos

* Clase Participante
--> analiza los datos de un participante
Atributos
id: int
registros: lista de objetos del tipo Registro

Métodos
agregar_registro(registro)
calcular_hits_totales()
tiempo_primer_hit()
tiene_datos() --> verifica si el participante ya tiene datos cargados

* Clase Archivo
--> lee el archivo CSV
Atributos
ruta: str

Métodos
abrir_archivo() --> verifica si el archivo existe y se puede abrir
leer_datos() 

* Clase Sistema
--> valida los datos del archivo y los almacena
Atributos
participantes: dict {id: participante}

Metodos
validar_linea(linea)
procesar_datos() --> crea registros y los asigna a cada participante
obtener_participante(id)




