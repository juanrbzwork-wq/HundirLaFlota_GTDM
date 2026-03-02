"""
Módulo barcos.py
Gestiona la validación y colocación de la flota en el tablero.
"""
import random

def validar_posicion(tablero, fila, columna, tamaño, orientacion):
    """
    Comprueba si un barco puede colocarse en la posición indicada sin salirse
    del tablero ni pisar otro barco. Devuelve True o False.
    """
    filas_totales = len(tablero)
    columnas_totales = len(tablero[0])

    if orientacion == 'H':
        if columna + tamaño > columnas_totales:
            return False
        for c in range(columna, columna + tamaño):
            if tablero[fila][c] != '~':
                return False
                
    elif orientacion == 'V':
        if fila + tamaño > filas_totales:
            return False
        for f in range(fila, fila + tamaño):
            if tablero[f][columna] != '~':
                return False
                
    return True

def colocar_barco(tablero, flota, fila, columna, tamaño, orientacion, id_barco):
    """
    Dibuja el barco en la matriz ('B') y guarda sus datos en el diccionario de la flota.
    """
    posiciones = []
    
    if orientacion == 'H':
        for c in range(columna, columna + tamaño):
            tablero[fila][c] = 'B'
            posiciones.append((fila, c))
    elif orientacion == 'V':
        for f in range(fila, fila + tamaño):
            tablero[f][columna] = 'B'
            posiciones.append((f, columna))
            
    # Guardamos el barco en el diccionario
    flota[id_barco] = {
        "tamaño": tamaño,
        "impactos": 0,
        "posiciones": posiciones
    }

def generar_flota_aleatoria(tablero, flota, configuracion_barcos):
    """
    Recorre la lista de tamaños y los coloca aleatoriamente en el tablero.
    """
    id_barco = 0
    for tamaño in configuracion_barcos:
        colocado = False
        while not colocado:
            fila = random.randint(0, len(tablero) - 1)
            columna = random.randint(0, len(tablero[0]) - 1)
            orientacion = random.choice(['H', 'V'])
            
            if validar_posicion(tablero, fila, columna, tamaño, orientacion):
                colocar_barco(tablero, flota, fila, columna, tamaño, orientacion, id_barco)
                colocado = True
                id_barco += 1