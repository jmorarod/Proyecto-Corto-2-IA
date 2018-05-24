import pytest
from AGenetico import *


def test_recorrer_tablero():
    tablero = [['C', ' ', 'V', ' '],
               [' ', ' ', 'Z', ' '],
               [' ', ' ', '>', 'Z']]
    pos_conejo = [0,0]
    direccion = "derecha"
    total_zanahoria = 2
    resultado =  recorrer_tablero(tablero, pos_conejo, direccion, total_zanahoria, 0)
    assert resultado == [5,2]

def test_fitness():
    tablero = [['C', ' ', 'V', ' '],
               [' ', ' ', 'Z', ' '],
               [' ', ' ', '>', 'Z']]
    direccion = "derecha"
    resultado = fitness(tablero,direccion)
    assert resultado == 185

def test_mutacion():
    tablero = [['C', ' ', 'V', ' '],
               [' ', ' ', 'Z', ' '],
               [' ', ' ', '>', 'Z']]
    m_agregar = 20
    m_cambiar = 30
    m_quitar = 15
    resultado = mutacion(tablero,m_agregar,m_cambiar,m_quitar)
    assert isinstance(resultado, list)

def test_cruce_fila():
    parent1 = [['C', ' ', 'V', ' '],
               [' ', ' ', 'Z', ' '],
               [' ', ' ', 'V', 'Z'],
               [' ', 'Z', ' ', ' ']]

    parent2 = [['C', ' ', ' ', 'V'],
               [' ', ' ', 'Z', ' '],
               [' ', ' ', ' ', 'Z'],
               [' ', 'Z', ' ', '<']]

    hijo1 = [['C', ' ', 'V', ' '], 
               [' ', ' ', 'Z', ' '], 
               [' ', ' ', ' ', 'Z'], 
               [' ', 'Z', ' ', '<']]
    
    hijo2 = [['C', ' ', ' ', 'V'], 
             [' ', ' ', 'Z', ' '],
             [' ', ' ', 'V', 'Z'], 
             [' ', 'Z', ' ', ' ']]

    resultado = cruce(parent1,parent2,0)
    assert resultado[0]==hijo1 and resultado[1]==hijo2


def test_cruce_columna():
    parent1 = [['C', ' ', 'V', ' '],
               [' ', ' ', 'Z', ' '],
               [' ', ' ', 'V', 'Z'],
               [' ', 'Z', ' ', ' ']]

    parent2 = [['C', ' ', ' ', 'V'],
               [' ', ' ', 'Z', ' '],
               [' ', ' ', ' ', 'Z'],
               [' ', 'Z', ' ', '<']]

    hijo1 = [['C', ' ', ' ', 'V'], 
             [' ', ' ', 'Z', ' '], 
             [' ', ' ', ' ', 'Z'], 
             [' ', 'Z', ' ', '<']]
    
    hijo2 = [['C', ' ', 'V', ' '], 
             [' ', ' ', 'Z', ' '], 
             [' ', ' ', 'V', 'Z'], 
             [' ', 'Z', ' ', ' ']]

    resultado = cruce(parent1,parent2,1)
    assert resultado[0]==hijo1 and resultado[1]==hijo2

def test_elegir_mejores():
    individuos = []

    gen1 = [['C', ' ', 'V', ' '],
            [' ', ' ', 'Z', ' '],
            [' ', ' ', ' ', 'Z'],
            [' ', 'Z', '<', ' ']]

    gen2 = [['C', ' ', ' ', 'V'],
            ['>', ' ', 'Z', ' '],
            [' ', ' ', ' ', 'Z'],
            ['A', 'Z', ' ', '<']]

    gen3 = [['C', ' ', ' ', 'V'], 
            [' ', ' ', 'Z', ' '], 
            [' ', ' ', ' ', 'Z'], 
            [' ', 'Z', ' ', '<']]
    
    gen4 = [['C', ' ', 'V', ' '], 
            [' ', ' ', 'Z', ' '], 
            [' ', ' ', '>', 'Z'], 
            [' ', 'Z', ' ', ' ']]

    individuos.append(gen1)
    individuos.append(gen2)
    individuos.append(gen3)
    individuos.append(gen4)

    resultado = elegir_mejores(individuos, 2 , "derecha", 0)

    assert resultado[0]==gen4 and resultado[1]==gen2





