import pytest
from AStar import *
import random


def test_zanahorias_restantes():
    tablero = [["C", " ", " ", "\n"], [" ", "Z", "Z", "\n"]]
    result = zanahorias_restantes(tablero)
    assert result == 2


def test_on_non_list_arguments_zanahorias_restantes():
    with pytest.raises(TypeError):
        zanahorias_restantes("abc")


def test_mover_conejo():
    movimiento = ["DERECHA", 0, 1]
    tablero = [["C", " ", " ", "\n"], [" ", "Z", "Z", "\n"]]
    zanahorias = 2
    result = mover_conejo(movimiento, tablero, zanahorias)
    assert result == ([[' ', 'C', ' ', '\n'], [' ', 'Z', 'Z', '\n']], 2)


def test_on_non_list_arguments_mover_conejo():
    with pytest.raises(TypeError):
        mover_conejo("abc", "tablero", [1, 2, 3])


def test_menor_costo():
    costos = [["DERECHA", 10], ["ARRIBA", 8]]
    result = menor_costo(costos)
    assert result == ["ARRIBA", 8]


def test_on_non_list_arguments_menor_costo():
    with pytest.raises(TypeError):
        menor_costo([1, 2, 3])


def test_direccion_aleatoria():
    lista = [["DERECHA", 10], ["IZQUIERDA", 10]]
    random.seed(10)
    result = direccion_aleatoria(lista)
    assert result == ["IZQUIERDA", 10]


def test_on_non_list_arguments_direccion_aleatoria():
    with pytest.raises(TypeError):
        direccion_aleatoria([1, 2, 3])


def test_probabilidades_acumuladas():
    result = probabilidades_acumuladas(0.2, 5)
    assert result[4] == 1


def test_on_non_list_arguments_probabilidades_acumuladas():
    with pytest.raises(TypeError):
        probabilidades_acumuladas([1, 2, 3], 10)


def test_movimientos_conejo():
    result = movimientos_conejo([["", "C", " ", "\n"], [" ", "Z", "Z", "\n"]],
                                [0, 1])

    assert result == [["IZQUIERDA", 0, 0],
                      ["DERECHA", 0, 2],
                      ["ABAJO", 1, 1]]


def test_on_non_list_arguments_probabilidades_acumuladas():
    with pytest.raises(TypeError):
        movimientos_conejo([1, 2, 3], 10)


def test_posicion_conejo():
    result = posicion_conejo([["", "C", " ", "\n"], [" ", "Z", "Z", "\n"]])
    assert result == [0, 1]


def test_rango_vision_conejo():
    result = rango_vision_conejo([["", "C", " ", "\n"], [" ", "Z", "Z", "\n"]],
                                 [0, 1],
                                 2)
    assert result == [[0, 0], [0, 2],
                      [1, 0], [1, 1], [1, 2]]
