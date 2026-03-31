def crear_tablero(filas, columnas):
    """Crea una matriz 2D llena de agua ('~')"""
    return [['~' for _ in range(columnas)] for _ in range(filas)]

def imprimir_tablero(tablero, ocultar_barcos=False):
    """Imprime el tablero por pantalla con cabeceras de columnas y filas"""
    # Imprimir números de las columnas
    cabecera = "   " + " ".join([str(i) for i in range(len(tablero[0]))])
    print(cabecera)
    
    # Imprimir cada fila con su número correspondiente
    for idx, fila in enumerate(tablero):
        fila_str = []
        for celda in fila:
            if ocultar_barcos and celda == 'B':
                fila_str.append('~')
            else:
                fila_str.append(celda)
        print(f"{idx:2d} {' '.join(fila_str)}")
    print() # Salto de línea por estética