
matriz_prueba= [['C',' ',' ',' '],
                [' ',' ','Z',' '],
                [' ',' ',' ','Z']]

m = [['C', ' ', 'V', ' '],
     [' ', ' ', 'Z', ' '],
     [' ', ' ', '>', 'Z']]

m_bucle = [['C','>','V', ' '],
           [' ',' ','Z', ' '],
           [' ','A','<', 'Z']]

#fitness(m,'derecha')
#algortimo_genetico("",'>',4,10)
#algortimo_genetico("",'>',4,100)

import random
import copy
import time

def algortimo_genetico(tablero_inicial,direccion,cant_individuos,generaciones):
    matriz_tablero=matriz_prueba
    mutacion_agregar_signal = 20
    mutacion_cambiar_direccion = 25
    mutacion_quitar_signal = 15
    #matriz_tablero=convertir_tablero_inicial(tablero_inicial)
    
    individuos=[]
    x=cant_individuos
    while(x>0):
        individuos.append(copy.deepcopy(matriz_tablero))
        x-=1
    
    cant = 0

    while(cant<generaciones):
        #print('\n')
        #print(cant)

        for i in individuos:
            i_aux = mutacion(i, mutacion_agregar_signal,mutacion_cambiar_direccion,
                            mutacion_quitar_signal)
        
        n =  len (individuos)

        next_gen = copy.deepcopy(individuos)

        while(n>0):
            random.seed(time.clock())

            i1 =  random.randint(0,len(individuos)-1)
            i2 =  random.randint(0,len(individuos)-1)
        
            hijos = cruce(individuos[i1],individuos[i2],0)
    
            next_gen.extend(hijos)
            n-=1
        
        individuos = elegir_mejores(next_gen,len(individuos),direccion)

        
        
        cant += 1

    for i in individuos:
        print(i)

def elegir_mejores(gen, cantidad, direccion):
    indiviuos  = copy.deepcopy(gen)
    for i in indiviuos:
        puntuacion = fitness(i,direccion)
        i.append(puntuacion)

    gen =  sorted(indiviuos, key=lambda point : point[-1])

    gen = gen[-cantidad:]
    next_gen=[]

    for i in gen:
        i = i[:-1]
        next_gen.append(i)
    
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
        h1 =  copy.deepcopy(individuo1)
        h2 =  copy.deepcopy(individuo2)
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


def mutacion(individuo,m_agregar,m_cambiar,m_quitar):
    mutacion = random.randint(0, 100)
    m_cambiar += m_agregar
    m_quitar += m_cambiar
    signals = ['<','>','A','V']

    if mutacion<m_agregar:
        random.seed(time.clock())
        add = True
        n=0
        dimension = len(individuo) * len(individuo[0])
        while(add and n<dimension):
            i = random.randint(0,len(individuo)-1)
            j = random.randint(0,len(individuo[0])-1)
            x = random.randint(0,3)
            
            if individuo[i][j] == ' ':
                individuo[i][j] = signals[x]
                add = False

            n+=1
            

    elif mutacion<m_cambiar:
        random.seed(time.clock())
        signals_position = []
        for i in range(len(individuo)):
            for j in range(len(individuo[0])):
                if (individuo[i][j]=='<' or individuo[i][j]=='>' or 
                    individuo[i][j]=='A' or individuo[i][j]=='V'):
                    signals_position.append([i,j])

        if(len(signals_position)>0):
            x = random.randint(0,len(signals_position)-1)
            pos = signals_position[x]
            x = random.randint(0,3)
            individuo[pos[0]][pos[1]]=signals[x]


    elif mutacion<m_quitar:
        random.seed(time.clock())
        signals_position = []
        for i in range(len(individuo)):
            for j in range(len(individuo[0])):
                if (individuo[i][j]=='<' or individuo[i][j]=='>' or 
                    individuo[i][j]=='A' or individuo[i][j]=='V'):
                    signals_position.append([i,j])

        if(len(signals_position)>0):
            x = random.randint(0,len(signals_position)-1)
            pos = signals_position[x]
            individuo[pos[0]][pos[1]]=" "
    
    return individuo


def fitness(individuo, direccion):
    total_zanahorias=0
    cant_signals=0

    pos_conejo=[] 

    for i in range(len(individuo)):
        for j in range(len(individuo[0])):
            if individuo[i][j]=='C':
                pos_conejo.extend([i,j])
            elif individuo[i][j]=='Z':
                total_zanahorias+=1
            elif (individuo[i][j]=='<' or individuo[i][j]=='>' or 
                individuo[i][j]=='A' or individuo[i][j]=='V'):
                cant_signals+=1
    
    if cant_signals==0:
        return -50

    aux = copy.deepcopy(individuo)
    
    resultado = recorrer_tablero(aux,pos_conejo,direccion,total_zanahorias,0)

    cant_pasos = resultado[0]
    cant_zanahorias = resultado[1] 
    zanahorias_faltantes = total_zanahorias - cant_zanahorias

    fitness = cant_zanahorias*100 - (3*cant_signals+cant_pasos+2*zanahorias_faltantes)


    return fitness


def recorrer_tablero(individuo, pos_conejo,direccion,total_zanahoria,num):
    cant_pasos=0
    cant_zanahorias=0

    if total_zanahoria==0:
        return [0,0]

    if num>=10:
        return [150,cant_zanahorias]

    if direccion=='derecha' or direccion=='>':
        i = pos_conejo[0]
        for j in range (pos_conejo[1], len(individuo[0])):
            if j>=len(individuo[0]):
                break
            elif j == pos_conejo[1]:
                continue
            
            cant_pasos+=1
            if individuo[i][j]=='Z':
                cant_zanahorias+=1
                individuo[i][j]=' '
            elif individuo[i][j]=='<':
                return [100,cant_zanahorias]
            elif (individuo[i][j]=='A' or individuo[i][j]=='V'):
                zanahorias = total_zanahoria - cant_zanahorias
                resultado = recorrer_tablero(individuo,[i,j],individuo[i][j],zanahorias,num+1)
                return [resultado[0]+cant_pasos,resultado[1]+cant_zanahorias]
    
    elif direccion=='izquierda' or direccion=='<':
        len_individuo = len(individuo[0])
        i = pos_conejo[0]
        for x in range (pos_conejo[1], len_individuo+1):
            j = len_individuo-x
            if j>=len_individuo:
                break
            elif j == pos_conejo[1]:
                continue
            
            cant_pasos+=1
            if individuo[i][j]=='Z':
                cant_zanahorias+=1
                individuo[i][j]=' '
            elif individuo[i][j]=='>':
                return [100,cant_zanahorias]
            elif (individuo[i][j]=='A' or individuo[i][j]=='V'):
                zanahorias = total_zanahoria - cant_zanahorias
                resultado = recorrer_tablero(individuo,[i,j],individuo[i][j],zanahorias,num+1)
                return [resultado[0]+cant_pasos,resultado[1]+cant_zanahorias]

    elif direccion=='arriba' or direccion=='A':
        j = pos_conejo[1] 
        len_individuo = len(individuo) 

        for x in range (pos_conejo[0], len_individuo+1):
            i=len_individuo-x
            if i>=len_individuo:
                break
            elif i == pos_conejo[0]:
                continue
            
            cant_pasos+=1
            if individuo[i][j]=='Z':
                cant_zanahorias+=1
                individuo[i][j]=' '
            elif individuo[i][j]=='V':
                return [100,cant_zanahorias]
            elif (individuo[i][j]=='<' or individuo[i][j]=='>'):
                zanahorias = total_zanahoria - cant_zanahorias
                resultado = recorrer_tablero(individuo,[i,j],individuo[i][j],zanahorias,num+1)
                return [resultado[0]+cant_pasos,resultado[1]+cant_zanahorias]

    
    elif direccion=='abajo' or direccion=='V':
        j = pos_conejo[1] 

        for i in range (pos_conejo[0], len(individuo)):
            if i>=len(individuo):
                break
            elif i == pos_conejo[0]:
                continue
            
            cant_pasos+=1
            if individuo[i][j]=='Z':
                cant_zanahorias+=1
                individuo[i][j]=' '
            elif individuo[i][j]=='A':
                return [100,cant_zanahorias]
            elif (individuo[i][j]=='<' or individuo[i][j]=='>'):
                zanahorias = total_zanahoria - cant_zanahorias
                resultado = recorrer_tablero(individuo,[i,j],individuo[i][j],zanahorias,num+1)
                return [resultado[0]+cant_pasos,resultado[1]+cant_zanahorias]


    return [cant_pasos,cant_zanahorias]
        




#def convertir_tablero_inicial(tablero):


