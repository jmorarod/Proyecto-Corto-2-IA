import math

def a_star_search(archivo, vision, zanahorias):
    #try:
    tablero = leer_tablero(archivo)
    print(tablero)
    #while(zanahorias > 0):
    costos = calculo_costo(tablero, vision, zanahorias)
    print(costos)
    #except:
       # print("Error al leer el archivo de entrada")

def calculo_costo(tablero, rango, zanahorias_restantes):
    conejo = posicion_conejo(tablero)
    movimientos = movimientos_conejo(tablero, conejo)
    vision_conejo = rango_vision_conejo(tablero, conejo, rango)
    costos = []
    for casilla_movimiento in movimientos:
        costos_movimientos = []
        
        for casilla_vision in vision_conejo:
            
            casilla = tablero[casilla_vision[0]][casilla_vision[1]]
            if(casilla == 'Z'):#Funcion de costo
                #costo = distancia_entre_casillas([casilla_movimiento[1], casilla_movimiento[2]],casilla_vision)Esto es con distancia_euclideana
                costo = abs(casilla_movimiento[1] - casilla_vision[0]) + abs(casilla_movimiento[2] - casilla_vision[1])
                costo -= (zanahorias_restantes - cantidad_caracter_vecinos_por_casilla('Z', casilla_vision, tablero))
                
                if(tablero[casilla_movimiento[1]][casilla_movimiento[2]] == 'Z'):
                    costo -= 1
                costos_movimientos += [costo]
        costo_minimo = float("inf")
        indice_minimo = 0
        indice = 0
        for i in costos_movimientos:
            if(i < costo_minimo):
                costo_minimo = i
                indice_minimo = indice
            indice += 1
        costos += [casilla_movimiento[0], costos_movimientos[indice_minimo]]
    return costos
            

def movimientos_conejo(tablero, conejo):
    movimientos = []
    if(conejo[0] - 1 >= 0):
        movimientos += [["IZQUIERDA",conejo[0] - 1, conejo[1]]]
    if(conejo[0] + 1 < len(tablero[0])):
        movimientos += [["DERECHA",conejo[0] + 1, conejo[1]]]
    if(conejo[1] - 1 >= 0):
        movimientos += [["ARRIBA",conejo[0], conejo[1] - 1]]
    if(conejo[1] + 1 < len(tablero)):
        movimientos += [["ABAJO",conejo[0], conejo[1] + 1]]
    return movimientos
    
            
                

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
    archivo = open(archivo,'r')
    if(tablero == []):
        return []
    i = 0
    j = 0
    for line in archivo:
        j = 0
        for char in line:
            if(validar_caracter(char)):
                tablero[i][j] = char
            j += 1
        i += 1
    archivo.close()
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
        columnas = 0
        for char in line:
                columnas += 1
        
            
    tablero = [[0 for i in range(columnas)] for j in range(filas)]
    print(tablero)
    return tablero
    

#Entrada: Tablero del problema del conejo(Matriz NxM)
#Salida: Posicion del conejo en el tablero
#Restricciones: Revisar restriciones de formato del tablero
#               en la documentación
#Descripción: Retorna la posición del conejo en el tablero

def posicion_conejo(tablero):
    for i in range(0, len(tablero)):
        for j in range(0, len(tablero[0])):
            if(tablero[i][j] == 'C'):
                return [i, j]
            
#Entradas: Posicion del conejo(Lista = [x, y])
#          Rango de vision(Lista = [x, y]) 
#Salida: Vision del conejo(Matriz [[x1,y1]...[xn, yn]])
#Restricciones:
#Descripción: Retorna una matriz con las casillas visibles
#             por el conejo en el tablero

def rango_vision_conejo(tablero, posicion, rango):
    vision = []
    x_conejo = posicion[0]
    y_conejo = posicion[1]
    for i in range(x_conejo - rango, x_conejo + rango):
        for j in range(y_conejo - rango, y_conejo + rango):
            if(i >= 0 and i < len(tablero) and j >= 0 and j < len(tablero[0])):
                if(i != x_conejo and j != y_conejo):
                    vision += [[i,j]]

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
