"""
Módulo tablero.py
Gestiona la creación, modificación y visualización de las cuadrículas del juego.
"""

def crear_tablero(filas, columnas):
    """
    Crea una matriz (lista de listas) rellenada con el símbolo de agua '~'.
    """
    tablero = []
    for i in range(filas):
        fila = ['~'] * columnas
        tablero.append(fila)
    return tablero

def imprimir_tablero(tablero, ocultar_barcos=False):
    """
    Muestra el tablero por consola con cabeceras de filas y columnas.
    Si ocultar_barcos es True, las 'B' (barcos) se muestran como '~' (agua).
    """
    columnas_str = "  " + " ".join([str(i) for i in range(1, len(tablero[0]) + 1)])
    print(columnas_str)
    
    letras = "ABCDEFGHIJ"
    for i in range(len(tablero)):
        fila_visual = []
        for celda in tablero[i]:
            if ocultar_barcos and celda == 'B':
                fila_visual.append('~')
            else:
                fila_visual.append(celda)
        
        # Mostramos la letra de la fila seguida de los símbolos
        print(f"{letras[i]} " + " ".join(fila_visual))
    print() # Salto de línea por estética

def actualizar_celda(tablero, fila, columna, resultado_disparo):
    """
    Modifica el símbolo de la matriz según el resultado del disparo.
    """
    if resultado_disparo == "Agua":
        tablero[fila][columna] = 'O'
    elif resultado_disparo in ["Tocado", "Hundido"]:
        tablero[fila][columna] = 'X'