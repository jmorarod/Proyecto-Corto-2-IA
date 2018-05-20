import math

#Entrada: Dos listas 
#Salida: Distancia euclideana entre casillas
#Restricciones: Lista = [x, y]
#Descripción: Retorna la distancia entre dos casillas

def distancia_entre_casillas(casilla_1, casilla_2):
    x1 = casilla_1[0]
    y1 = casilla_1[1]
    x2 = casilla_2[0]
    y2= casilla_2[1]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

#Entradas: Un caracter, lista, matriz
#Salida: Entero
#Restricciones: Lista = [x, y], matriz NxM
#Descripción: Dada una casilla retorna la cantidad de veces
#             que se encuentra el caracter en las casillas vecinas

def cantidad_caracter_vecinos_por_casilla(caracter, casilla, tablero):
    numero_caracteres = 0
    for i in range(casilla[0] - 1, casilla[0]+ 1):
        for j in range(casilla[1] - 1, casilla[1] + 1):
            if(i >= 0 and i < len(tablero) and j >= 0 and j < len(tablero[0])):
                if(tablero[i][j] == caracter):
                    numero_caracteres += 1
    return numero_caracteres

#Entrada: Direccion de un archivo
#Salida: Tablero del problema del conejo(Detalle en la documentación)
#Restricciones: Revisar restriciones de formato en la documentación
#Descripción: Lee un archivo de texto con el formato de tablero
#             y retorna una matriz con la estructura del problema
            
def leer_tablero(archivo):
    tablero = inicializar_tablero(archivo)
    if(tablero == []):
        return []
    i = 0
    j = 0
    for line in archivo:
        for char in line:
            tablero[i][j] = char
            j += 1
        i += 1
    return tablero

#Entrada: Direccion de un archivo
#Salida: Matriz de dimensiones N(filas del archivo) x
#        M(Caracteres x fila)
#Restricciones: Revisar restriciones de formato del problema
#               en la documentación
#Descripción: Lee un archivo de texto con el formato de tablero
#             y retorna una matriz N x M

def inicializar_tablero(archivo):
    archivo = open(archivo,'r')
    filas = 0
    columnas = 0
    for line in archivo:
        filas += 1
        for char in line:
            if(validar_caracter(char)):
                if(char != '\n'):
                    columnas += 1
            else:
                return []
    tablero = [[0] * columnas] * filas
    return tablero
    

#Entrada: Tablero del problema del conejo(Matriz NxM)
#Salida: Posicion del conejo en el tablero
#Restricciones: Revisar restriciones de formato del tablero
#               en la documentación
#Descripción: Retorna la posición del conejo en el tablero

def posicion_conejo(tablero):
    for i in tablero:
        for j in tablero:
            if(tablero[i][j] == 'C'):
                return [i, j]
            
#Entradas: Posicion del conejo(Lista = [x, y])
#          Rango de vision(Lista = [x, y]) 
#Salida: Vision del conejo(Matriz [[x1,y1]...[xn, yn]])
#Restricciones:
#Descripción: Retorna una matriz con las casillas visibles
#             por el conejo en el tablero

def rango_vision_conejo(posicion, rango):
    vision = []
    x_conejo = posicion[0]
    y_conejo = posicion[1]
    x_rango = rango[0]
    y_rango = rango[1]
    for i in range(x_conejo - x_rango, x_conejo + x_rango)
        for j in range(y_conejo - y_rango, y_conejo + y_rango):
            if(i >= 0 and i < len(tablero) and j >= 0 and j < len(tablero[0])):
                vision +0 [i,j]
    return vision
            
#Entrada: Caracter
#Salida: True o False
#Restricciones: 
#Descripción: Valida si un caracter es valido en la definición
#             del problema(revisar documentación)

def validar_caracter(char):
    if(char == 'A' or char == 'V'):
        return True
    elif(char == '>' or char == '<'):
        return True
    elif(char == 'Z' or char == 'C'):
        return True
    elif(char == ' ' or char == '\n'):
        return True
    else:
        return False
