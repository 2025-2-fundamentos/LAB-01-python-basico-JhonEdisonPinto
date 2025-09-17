"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open('files/input/data.csv', 'r') as file:
        suma = 0
        for linea in file:
            datos = linea.split()
            suma += int(datos[1])

        return suma
pregunta_01()
