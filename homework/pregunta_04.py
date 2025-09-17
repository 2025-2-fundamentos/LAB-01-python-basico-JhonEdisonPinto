"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    with open("files/input/data.csv", "r") as file: #? abrir el archivo en lectura (r)
        lineas = file.readlines()                   #?leer las lineas y guardarlas en la lista lineas
    Contar_Meses = {}                               #?diccionario 
    for linea in lineas:
        partes = linea.strip().split("\t")          #?elimina saltos de linea y divide las tabulaciones
        fecha = partes [2]                          #?la columna con la fecha 
        mes = fecha.split("-")[1]                   #?extrae el mes de la fecha 

        if mes in Contar_Meses:                     #?coneto de cada mes
            Contar_Meses[mes] += 1
        else: 
            Contar_Meses[mes] = 1
    
    Resultado = sorted(Contar_Meses.items())        #?ordernar con sorted() y devolver los pares mes, cantidad 
    return Resultado
print ( pregunta_04())

