# Informe de proyecto corto #2-3 - Inteligencia Artificial: Buscador de Zanahorias
#### Realizado Por:
1. José Miguel Mora Rodríguez
2. Dylan Rodríguez Barboza
3. Karina Zeledón Pinell
#### Profesor:
Juan Manuel Esquivel Rodríguez, Ph. D.

# Problema planteado
El problema planteado para el desarrollo del proyecto se basa en el desarrollo de algoritmos de búsquedas relacionados a la búsqueda y recorrido en laberintos. Se pretende desarrollar una algoritmo de búsqueda A* y un algoritmo genético los cuáles brinden la solución óptima al problema planteado. Cada instancia del problema se vera presentada en un tablero de NxM dimensiones en el cuál se representa un conejo en busca de zanahorias colocadas en distintas partes del tablero. A continuación se brinda una breve explicación de la representación del problema en formato de archivos de texto.

## Representación del Tablero

En aras de enfocar el desarrollo del proyecto en los algoritmos de búsqueda, se utilizará una
interfaz rudimentaria para manejar las entradas y salidas de los programas. El tablero será un
archivo de texto de N líneas y M columnas y cada caracter podrá ser únicamente:
- C: en mayúscula, identifica la posición del conejo. Sólo podrá haber uno por tablero.
- Z: en mayúscula, identifica la posición de una zanahoria. Puede haber múltiples
zanahorias por tablero.
- Espacio en blanco: El caracter de espacio no tiene ningún efecto secundario pero sí
debe estar presente para indicar una posición en el tablero por la que el conejo puede
transitar.
- <: símbolo menor que, indica un cambio de dirección hacia la izquierda.
- \>: símbolo mayor que, indica un cambio de dirección hacia la derecha.
- A: letra A mayúscula, indica un cambio de dirección hacia arriba.
- V: letra V mayúscula, indica un cambio de dirección hacia abajo.
- Cambio de línea: No tiene ninguna interpretación en el programa más que separar las
distintas filas.

Un ejemplo se muestra a continuación:

| C |   |   |   | Z  |
|---|---|---|---|---|
|   | Z | Z |   |   |
|   |   |   |  Z |   |
|   |   |   | Z |   |

# Búsqueda A*

El primer algoritmo implementado consiste en una búsqueda A*. El problema consiste en crear el algoritmo de tal manera que mueva al conejo a través del tablero, una casilla a la vez, utilizando A*. Se diseñó una función de costo para guiar la búsqueda A* la cual considera el costo acumulado y un heurístico para aproximar el costo futuro. 
## Función de costo
La función de costo f con la cuál se guía la búsqueda es la siguiente: 

f(n) = g(n) + h(n), donde
g(n): costo acumulado
h(n): heurístico de búsqueda

Cabe resaltar que el costo acumulado hasta un punto específico en la ejecución del algoritmo será simplemente la cantidad de pasos que ha dado el conejo. El heurístico diseñado es el siguiente:

h(n) = min(pasos_hasta_zanahoria~i - (# zanahorias a buscar - zanahorias_vecinas~i)

Donde zanahoria~i es cada zanahoria en el rango de visión del conejo.

La función pasos_hasta_zanahoria se define de la siguiente forma:
abs(casilla_movimiento[1] - casilla_vision[0]) + abs(casilla_movimiento[2] - casilla_vision[1]), donde abs() es una función de balor absoluto, casilla_movimiento = [x, y] es la casilla del sigueinte nodo o paso a evaluar y casilla_vision = [x, y] es la casilla visible por el conejo evaluado en cuestión.
Si varios nodos poseen el mismo costo dado por la función se procede a elegir uno aleatoriamente(ambos siendo equiprobables).

## Análisis de varación de costo

Como parte del análisis se comprobó el funcionamiento del algoritmo en diferentes escenarios. Aspectos tomados en cuenta al plantear el escneario:
- Dimensiones del tablero 25 x 25
- Diferente número de zanahorias
- Diferente rango de visión
- Cúmulos de zanahorias
- Espacios amplios sin zanahorias

El primer tablero probado fue el siguiente: 
![Tablero 1](http://res.cloudinary.com/chaldeacloud/image/upload/v1527127718/Proyecto%20Corto%202%20IA/tablero_1.png)
Con los siguientes parámetros:
- Número de zanahorias: 13
- Visión: 5 espacios
- Zanahorias a recolectar: 10

Para este escenario se realizaron distintas corridas:

Número de corrida |Costo acumulado/número de pasos| Número de pasos tomados de forma aleatoria | 
-----------|---------------|---------------|
1 | 99 | 62 
2 | 83 | 49
3 | 104 | 76
4 | 274 | 248
5 | 73 | 41

Los pasos de forma aleatoriamente se daban cuando el conejo entraba a la zona más baja del tablero donde no habían zanahorias usualmente en el paso #16-17 y se recuperaba cuando encontraba el cúmulo de zanahorias.

Ajustando el parámetro de visión a 10 espacios se obtuvieron los siguientes resultados:
Número de corrida |Costo acumulado/número de pasos| Número de pasos tomados de forma aleatoria | 
-----------|---------------|---------------|
1 | 43 | 0
2 | 43 | 0
3 | 43 | 0
n | 43 | 0

La solución converge debido al aumento en el campo de visión del conejo

El segundo tablero probado fue el siguiente: 
![Tablero 2](http://res.cloudinary.com/chaldeacloud/image/upload/v1527127718/Proyecto%20Corto%202%20IA/tablero_2.png)
Con los siguientes parámetros:
- Número de zanahorias: 19
- Visión: 5 espacios
- Zanahorias a recolectar: 10

Se obtuvieron los siguientes resultados:

Número de corrida |Costo acumulado/número de pasos| Número de pasos tomados de forma aleatoria | 
-----------|---------------|---------------|
1 | 28 | 2 
2 | 32 | 5
3 | 40 | 17
4 | 79 | 40
5 | 34 | 8

Como se podrá suponer observando el tablero, el algoritmo de búsqueda tiende a ir por la fila e hilera de zanahorias luego de recolectar las más cercanas, esto debido a la naturaleza de la función de costo y el desempate aleatorio de soluciones.


# Algoritmo genético
## Definición de problema
El problema consiste en procesar tableros rectangulares, los cuales contiene un conejo representado con C y múltiples zanahorias que se representan con la Z, el objetivo primario es guiar al conejo por el tablero y que recolecte la mayor cantidad de zanahorias posibles. 

Con el algoritmo genético se tiene la particularidad que el conejo se mueve siempre hacia adelante y su dirección cambia con las señales (<, >, A, V), estas señales indican la siguiente dirección en la cual se va a mover el conejo.

## Definición general del algoritmo
Los algoritmos genéticos están inspirados en la evolución biológica. Estos algoritmos hacen evolucionar a una población de individuos (usualmente representado con arreglos) sometiéndola a operaciones aleatorias semejantes a la evolución biológica (mutaciones, cruces). Además, selecciona a los individuos mas aptos con una función que da una puntuación y basándose en esa puntuación se decide si conservar el individuo o descartarlo.

## Implementación
Con lo mencionado en la sección anterior se puede observar 5 elementos generales de los algoritmos genéticos (población inicial, selección de padres, cruces, mutaciones, función de aptitud). La implementación de estos elementos se detallará a continuación.

### Población inicial
Debido a la definición del problema, el algoritmo empieza con copias del tablero original, este tablero cambia por mutaciones.

### Selección de padres
Este elemento se implemento de forma completamente aleatoria, debido a que una de las restricciones es que la función de aptitud no interviniera en esta selección. Por lo tanto, los padres para hacer el cruce se escogen aleatoriamente. 

### Mutación
La mutación son operaciones puntuales y se hacen antes de realizar el cruce entre los padres. Para este problema se decidieron manejar 3 tipos de mutaciones:
* Agregar señales
* Cambiar señales
* Eliminar señales

Estas mutaciones deben tener valores entre 0-100 y la suma de las tres debe ser menor a 100. Cabe destacar que cada vez que un individuo muta solo interviene una de las 4 (agrega una señal, cambia una señal, elimina una señal o no hace nada)

### Cruces
Los cruces evalúan el punto donde se dividen los padres para luego unirlos y crear nuevos individuos (hijos). En este problema se opto por manejar dos tipos de cruces:
* Columnas: Se divide a la mitad utilizando las columnas
* Filas: Se divide a la mitad utilizando las filas

### Función de aptitud
Esta función se encarga de darle una puntuación al individuo y según es puntuación evaluar sin conservarlo o desecharlo. Para este problema la función costa de 4 elementos principales
*Zanahorias recolectadas (ZR)
*Pasos realizados (PR)
*Señales utilizadas (SU)
*Zanahoritas restantes (ZRR)

Además, la función toma en cuenta 4 coeficientes que esta relacionados con cada elemento, los coeficientes utilizados son los siguientes
*C1 : 100
*C2 : 5
*C3: 1
*C3: 2

La función que se utilizo fue la siguiente:
f = C1*ZR –  (C2*SU + C3*PR + C4*ZRR)

## Resultados

En esta seccion se muestra los resultados obtenidos con un tablero 25x25 y otro 4x7.

Para la evaluacion de los siguientes resultados se utilizo en el siguiente tablero. Ademas la direccion de inicio que se utilizo fue "derecha".

![Tablero 2](https://i.imgur.com/w1wUPt7.png)

A continuación se detallan los resultados obtenidos

|Individuos|Generacion|Mutacion Agregar|Mutacion Cambiar|Mutacion Eliminar|Cruce|Mejor Fitness|Generacion con mejor resultado   
|----------|----------|------------|------------|------------|-----------|-------|---------------	
10|100|20|30|15|Fila|46|52
10|100|20|30|15|Fila|35|1
10|100|20|30|15|Columna|35|1
10|100|20|30|15|Columna|35|3
10|1000|20|30|15|Fila|35|1
10|1000|20|30|15|Fila|35|2
10|1000|20|30|15|Columna|121|663
10|1000|20|30|15|Columna|406|454
10|100|30|25|15|Fila|93|84
10|100|30|25|15|Fila|35|1
10|100|30|25|15|Columna|120|92
10|100|30|25|15|Columna|35|1
10|1000|30|25|15|Fila|35|1
10|1000|30|25|15|Fila|35|1
10|1000|30|25|15|Columna|122|560
10|1000|30|25|15|Columna|123|451

Para la evaluacion de los siguientes resultados se utilizo en el siguiente tablero. Ademas la direccion de inicio que se utilizo fue "derecha".

![Tablero 2](https://i.imgur.com/wVGJWar.png)

A continuación se detallan los resultados obtenidos

|Individuos|Generacion|Mutacion Agregar|Mutacion Cambiar|Mutacion Eliminar|Cruce|Mejor Fitness|Generacion con mejor resultado   
|----------|----------|------------|------------|------------|-----------|-------|---------------	
4|100|20|30|15|Fila|56|71
4|100|20|30|15|Fila|222|51
4|100|20|30|15|Columna|277|50
4|100|20|30|15|Columna|81|26
4|1000|20|30|15|Fila|211|92
4|1000|20|30|15|Fila|93|253
4|1000|20|30|15|Columna|178|1000
4|1000|20|30|15|Columna|277|498
4|100|30|25|15|Fila|90|99
4|100|30|25|15|Fila|70|5
4|100|30|25|15|Columna|83|60
4|100|30|25|15|Columna|173|85
4|1000|30|25|15|Fila|89|739
4|1000|30|25|15|Fila|86|348
4|1000|30|25|15|Columna|178|431
4|1000|30|25|15|Columna|277|250

### Conlusiones de los resultados

Con el tablero mas grande los resultados no fueron demasiado favorables, esto se debe a la cantidad de generaciones con el que se hicieron pruebas. Conforme se hicieron las pruebas se noto que el valor del fitness de los individuos se mantenia constante y no cambiante, esto se debe a los valores que se utilizaron para la mutacion.

Ademas se observo que el tablero mas pequeño si se logro encontrar el optimo (donde el fitness es 277). Sin embargo se noto que usualmente despues de cierta cantidad de generaciones la puntuacion del fitness comenzaba a bajar considerablemente. 

Con respecto a los tipos de cruce, el mejor es el que se hace por columna debido a que da resultados mas constantes ademas que el caso del tablero mas pequeño se visualizo que con el cruce por columna fue el unico capaz de encontrar el optimo. 

# Manual de uso

* Se debe abrir la línea de comandos en el mismo directorio en el que se encuentre el archivo main.py
 
* Para ejecutar el algoritmos de A*, se utilizará este comando como ejemplo (se pueden cambiar los valores de los parámetros al gusto): python main.py --tablero-inicial ejemplo1.txt --a-estrella --vision 2 --zanahorias 2
 
* Para ejecutar el algoritmos genético, se utilizará este comando como ejemplo (se pueden cambiar los valores de los parámetros al gusto): python main.py --tablero-inicial ejemplo1.txt --genetico --derecha --individuos 5 --generaciones 3 --mutacion-agregar 40 --mutacion-cambiar 40 --mutacion-quitar 20 --tipo-cruce 1
 
* Se debe tomar en cuenta que ejemplo1.txt es un archivo de entrada que se encontrará en la misma carpeta que el archivo main.py, de otra forma, el programa no reconocerá el archivo y no se ejecutará.

* También se debe tomar en cuenta que el algoritmo genético tiene cuatro parámetros opcionales: --mutacion-agregar, --mutacion-cambiar --mutacion-quitar y --tipo-cruce, es decir, si no se ponen estos parámetros, el programa se ejecutará de igual forma. Los parámetros anteriores a estos son obligatorios. 

