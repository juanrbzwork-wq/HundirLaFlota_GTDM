"""
Módulo mecanicas.py
Contiene la lógica de disparos, comprobación de victoria y turno del PC.
"""
import random

def procesar_disparo(tablero_enemigo, flota_enemiga, fila, columna):
    """
    Evalúa el disparo. Modifica el diccionario de la flota si hay impacto.
    Devuelve "Agua", "Tocado", "Hundido" o "Repetido".
    """
    celda = tablero_enemigo[fila][columna]
    
    if celda == 'O' or celda == 'X':
        return "Repetido"
        
    elif celda == '~':
        return "Agua"
        
    elif celda == 'B':
        # Buscamos a qué barco le ha dado
        for id_barco, datos in flota_enemiga.items():
            if (fila, columna) in datos["posiciones"]:
                datos["impactos"] += 1
                if datos["impactos"] == datos["tamaño"]:
                    return "Hundido"
                else:
                    return "Tocado"

def verificar_fin_juego(flota):
    """
    Comprueba si todos los barcos de una flota han sido hundidos.
    """
    for datos in flota.values():
        if datos["impactos"] < datos["tamaño"]:
            return False # Hay al menos un barco vivo
    return True

def generar_disparo_ia(radar):
    """
    Genera unas coordenadas aleatorias para el ordenador que no hayan sido disparadas antes.
    """
    filas_totales = len(radar)
    columnas_totales = len(radar[0])
    
    while True:
        fila = random.randint(0, filas_totales - 1)
        columna = random.randint(0, columnas_totales - 1)
        # Si en el radar del PC hay agua ('~'), es una casilla virgen
        if radar[fila][columna] == '~':
            return fila, columna