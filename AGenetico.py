
matriz_prueba = [['C', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', 'Z', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', 'Z', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', 'Z', ' ']]

m = [['C', ' ', 'V', ' '],
     [' ', ' ', 'Z', ' '],
     [' ', ' ', '>', 'Z']]

m_bucle = [['C', '>', 'V', ' '],
           [' ', ' ', 'Z', ' '],
           [' ', 'A', '<', 'Z']]

archivo = 'C:/Users/Karina/Documents/GitHub/Proyecto-Corto-2-IA/tablero1.txt'
# fitness(m,'derecha')
# algortimo_genetico("",'>',4,10)
# algortimo_genetico("",'derecha',4,10,20,30,15,1)

import random
import copy
import time
import os
import shutil

mejor = []


def algortimo_genetico(tablero_inicial, direccion, cant_individuos, generaciones,
                       magregar, mcambiar, mquitar, tipo_cruce):
    #matriz_tablero = matriz_prueba
    mutacion_agregar_signal = magregar
    mutacion_cambiar_direccion = mcambiar
    mutacion_quitar_signal = mquitar
    tablero = leer_tablero(archivo)

    matriz_tablero = []

    for t in tablero:
        t = t[:-1]
        matriz_tablero.append(t)

    individuos = []
    x = cant_individuos
    while(x > 0):
        individuos.append(copy.deepcopy(matriz_tablero))
        x -= 1

    cant = 1
    
    try:
        ruta = "salida_genetico/"+direccion
        shutil.rmtree(ruta)
    except:
        pass

    global mejor
    mejor = []
    
    while(cant <= generaciones):
        print("\n")
        print("GENERACION: "+str(cant).zfill(5))
        for i in individuos:
            i_aux = mutacion(i, mutacion_agregar_signal, mutacion_cambiar_direccion,
                             mutacion_quitar_signal)

        n = len(individuos)

        next_gen = copy.deepcopy(individuos)

        while(n > 0):
            random.seed(time.clock())

            i1 = random.randint(0, len(individuos)-1)
            i2 = random.randint(0, len(individuos)-1)

            hijos = cruce(individuos[i1], individuos[i2], tipo_cruce)

            next_gen.extend(hijos)
            n -= 1

        individuos = elegir_mejores(next_gen, len(individuos), direccion, cant)
        print_tablero_genetico(direccion, cant, individuos)

        cant += 1

    print("\n")
    print("El mejor individuo es: INDIVIDUO " + str(mejor[0]).zfill(5) + " GENERACION " + str(mejor[1]).zfill(5))
    print("\n")


def elegir_mejores(gen, cantidad, direccion, generacion):
    global mejor
    indiviuos = copy.deepcopy(gen)
    for i in indiviuos:
        puntuacion = fitness(i, direccion)
        i.append(puntuacion)

    gen = sorted(indiviuos, key=lambda point: point[-1])

    gen = gen[-cantidad:]
    next_gen = []
    n = 1

    for i in gen:
        if mejor == []:
          mejor.extend([n,generacion,i[-1]])
        elif mejor[2] < i[-1]:
          mejor = []
          mejor.extend([n,generacion,i[-1]])
          
        print("INDIVIDUO " + str(n).zfill(5) + " APTITUD: " + str(i[-1]))
        i = i[:-1]
        next_gen.append(i)
        n += 1

    return next_gen


def cruce(individuo1, individuo2, tipo):
    if tipo == 0:
        n = len(individuo1)
        h1 = individuo1[:n//2]
        h1.extend(individuo2[n//2:])
        h2 = individuo2[:n//2]
        h2.extend(individuo1[n//2:])

        h = []
        h.append(h1)
        h.append(h2)

        return h
    else:
        n = len(individuo1[0])
        h1 = copy.deepcopy(individuo1)
        h2 = copy.deepcopy(individuo2)
        for i in range(0, len(individuo1)):
            h = individuo1[i][:n//2]
            h.extend(individuo2[i][n//2:])
            h1[i] = copy.deepcopy(h)
            h = individuo2[i][:n//2]
            h.extend(individuo1[i][n//2:])
            h2[i] = copy.deepcopy(h)

        h = []
        h.append(h1)
        h.append(h2)

        return h


def mutacion(individuo, m_agregar, m_cambiar, m_quitar):
    random.seed(time.clock())
    mutacion = random.randint(0, 100)
    m_cambiar += m_agregar
    m_quitar += m_cambiar
    signals = ['<', '>', 'A', 'V']

    if mutacion < m_agregar:
        add = True
        n = 0
        dimension = len(individuo) * len(individuo[0])
        while(add and n < dimension):
            i = random.randint(0, len(individuo)-1)
            j = random.randint(0, len(individuo[0])-1)
            x = random.randint(0, 3)

            if individuo[i][j] == ' ':
                individuo[i][j] = signals[x]
                add = False
            n += 1

    elif mutacion < m_cambiar:
        signals_position = []
        for i in range(len(individuo)):
            for j in range(len(individuo[0])):
                if (individuo[i][j] == '<' or individuo[i][j] == '>' or
                        individuo[i][j] == 'A' or individuo[i][j] == 'V'):
                    signals_position.append([i, j])

        if(len(signals_position) > 0):
            x = random.randint(0, len(signals_position)-1)
            pos = signals_position[x]
            x = random.randint(0, 3)
            individuo[pos[0]][pos[1]] = signals[x]

    elif mutacion < m_quitar:
        signals_position = []
        for i in range(len(individuo)):
            for j in range(len(individuo[0])):
                if (individuo[i][j] == '<' or individuo[i][j] == '>' or
                        individuo[i][j] == 'A' or individuo[i][j] == 'V'):
                    signals_position.append([i, j])

        if(len(signals_position) > 0):
            x = random.randint(0, len(signals_position)-1)
            pos = signals_position[x]
            individuo[pos[0]][pos[1]] = " "

    return individuo


def fitness(individuo, direccion):
    total_zanahorias = 0
    cant_signals = 0

    pos_conejo = []

    C1 = 100
    C2 = 5
    C3 = 1
    C4 = 3

    for i in range(len(individuo)):
        for j in range(len(individuo[0])):
            if individuo[i][j] == 'C':
                pos_conejo.extend([i, j])
            elif individuo[i][j] == 'Z':
                total_zanahorias += 1
            elif (individuo[i][j] == '<' or individuo[i][j] == '>' or
                  individuo[i][j] == 'A' or individuo[i][j] == 'V'):
                cant_signals += 1

    if cant_signals == 0:
        return -50

    aux = copy.deepcopy(individuo)

    resultado = recorrer_tablero(
        aux, pos_conejo, direccion, total_zanahorias, 0)

    cant_pasos = resultado[0]
    cant_zanahorias = resultado[1]
    zanahorias_faltantes = total_zanahorias - cant_zanahorias

    fitness = C1*cant_zanahorias - \
        (C2*cant_signals+C3*cant_pasos+C4*zanahorias_faltantes)

    return fitness


def recorrer_tablero(individuo, pos_conejo, direccion, total_zanahoria, num):
    cant_pasos = 0
    cant_zanahorias = 0

    if total_zanahoria == 0:
        return [0, 0]

    if num >= 10:
        return [150, cant_zanahorias]

    if direccion == 'derecha' or direccion == '>':
        i = pos_conejo[0]
        for j in range(pos_conejo[1], len(individuo[0])):
            if j >= len(individuo[0]):
                break
            elif j == pos_conejo[1]:
                continue

            cant_pasos += 1
            if individuo[i][j] == 'Z':
                cant_zanahorias += 1
                individuo[i][j] = ' '
            elif individuo[i][j] == '<':
                return [100, cant_zanahorias]
            elif (individuo[i][j] == 'A' or individuo[i][j] == 'V'):
                zanahorias = total_zanahoria - cant_zanahorias
                resultado = recorrer_tablero(
                    individuo, [i, j], individuo[i][j], zanahorias, num+1)
                return [resultado[0]+cant_pasos, resultado[1]+cant_zanahorias]

    elif direccion == 'izquierda' or direccion == '<':
        len_individuo = len(individuo[0])
        i = pos_conejo[0]
        for x in range(pos_conejo[1], len_individuo+1):
            j = len_individuo-x
            if j >= len_individuo:
                break
            elif j == pos_conejo[1]:
                continue

            cant_pasos += 1
            if individuo[i][j] == 'Z':
                cant_zanahorias += 1
                individuo[i][j] = ' '
            elif individuo[i][j] == '>':
                return [100, cant_zanahorias]
            elif (individuo[i][j] == 'A' or individuo[i][j] == 'V'):
                zanahorias = total_zanahoria - cant_zanahorias
                resultado = recorrer_tablero(
                    individuo, [i, j], individuo[i][j], zanahorias, num+1)
                return [resultado[0]+cant_pasos, resultado[1]+cant_zanahorias]

    elif direccion == 'arriba' or direccion == 'A':
        j = pos_conejo[1]
        len_individuo = len(individuo)

        for x in range(pos_conejo[0], len_individuo+1):
            i = len_individuo-x
            if i >= len_individuo:
                break
            elif i == pos_conejo[0]:
                continue

            cant_pasos += 1
            if individuo[i][j] == 'Z':
                cant_zanahorias += 1
                individuo[i][j] = ' '
            elif individuo[i][j] == 'V':
                return [100, cant_zanahorias]
            elif (individuo[i][j] == '<' or individuo[i][j] == '>'):
                zanahorias = total_zanahoria - cant_zanahorias
                resultado = recorrer_tablero(
                    individuo, [i, j], individuo[i][j], zanahorias, num+1)
                return [resultado[0]+cant_pasos, resultado[1]+cant_zanahorias]

    elif direccion == 'abajo' or direccion == 'V':
        j = pos_conejo[1]

        for i in range(pos_conejo[0], len(individuo)):
            if i >= len(individuo):
                break
            elif i == pos_conejo[0]:
                continue

            cant_pasos += 1
            if individuo[i][j] == 'Z':
                cant_zanahorias += 1
                individuo[i][j] = ' '
            elif individuo[i][j] == 'A':
                return [100, cant_zanahorias]
            elif (individuo[i][j] == '<' or individuo[i][j] == '>'):
                zanahorias = total_zanahoria - cant_zanahorias
                resultado = recorrer_tablero(
                    individuo, [i, j], individuo[i][j], zanahorias, num+1)
                return [resultado[0]+cant_pasos, resultado[1]+cant_zanahorias]

    return [cant_pasos, cant_zanahorias]


# Entrada: Direccion de un archivo
# Salida: Tablero del problema del conejo(Detalle en la documentación)
# Restricciones: Revisar restriciones de formato en la documentación
# Descripción: Lee un archivo de texto con el formato de tablero
#             y retorna una matriz con la estructura del problema

def leer_tablero(archivo):
    try:
        tablero = inicializar_tablero(archivo)
        archivo = open(archivo, 'r')
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
    except:
        return []

# Entrada: Direccion de un archivo
# Salida: Matriz de dimensiones N(filas del archivo) x
#        M(Caracteres x fila)
# Restricciones: Revisar restriciones de formato del problema
#               en la documentación
# Descripción: Lee un archivo de texto con el formato de tablero
#             y retorna una matriz N x M


def inicializar_tablero(archivo):
    archivo = open(archivo, 'r')
    filas = 0
    columnas = 0
    for line in archivo:
        filas += 1
        columnas = 0
        for char in line:
            columnas += 1
    tablero = [[0 for i in range(columnas)] for j in range(filas)]
    return tablero


# Entrada: Caracter
# Salida: True o False
# Restricciones:
# Descripción: Valida si un caracter es valido en la definición
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


def print_tablero_genetico(direccion, generacion, indiviuos):
    ruta = "salida_genetico/"+direccion+"/"+str(generacion).zfill(5)
    try:
        os.makedirs(ruta)
    except:
        pass

    try:
        n = 1
        for individuo in indiviuos:
            name = ruta + "/" + str(n).zfill(5) + ".txt"
            string = ""
            file = open(name, "w+")
            for fila in individuo:
                for k in fila:
                    string += k
                string += "\n"
            file.write(string)
            file.close()
            n+=1
    except:
        pass
    
