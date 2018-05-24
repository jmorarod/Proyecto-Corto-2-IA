# Proyecto-Corto-2-IA
# Cómo ejecutar las funcionalidades
Para ejecutar las funcionalidades de este proyecto, se debe dirigir a la siguiente carpeta: tec/ic/ia/pc y hacer lo siguiente:
* Utilizar el archivo main.py, el cual se puede utilizar en cualquier directorio del computador, este archivo ya contiene la importación que se necesita para ejecutar las funcionalidades, en este caso: from tec.ic.ia.pc2.g05 import a_star_search, algortimo_genetico
* Se debe abrir la línea de comandos en el mismo directorio en el que se encuentre el archivo main.py
* Para ejecutar el algoritmos de A*, se utilizará este comando como ejemplo (se pueden cambiar los valores de los parámetros al gusto): python main.py --tablero-inicial ejemplo1.txt --a-estrella --vision 2 --zanahorias 2
* Para ejecutar el algoritmos genético, se utilizará este comando como ejemplo (se pueden cambiar los valores de los parámetros al gusto): python main.py --tablero-inicial ejemplo1.txt --genetico --derecha --individuos 5 --generaciones 3 --mutacion-agregar 40 --mutacion-cambiar 40 --mutacion-quitar 20 --tipo-cruce 1
* Se debe tomar en cuenta que ejemplo1.txt es un archivo de entrada que se encontrará en la misma carpeta que el archivo main.py, de otra forma, el programa no reconocerá el archivo y no se ejecutará.
