def crear_tablero(filas, columnas):
    """Crea una matriz 2D llena de agua ('~')"""
    return [['~' for _ in range(columnas)] for _ in range(filas)]

def imprimir_tablero(tablero, ocultar_barcos=False):
    """Imprime el tablero por pantalla con letras en columnas y números en filas"""
    letras = "ABCDEFGHIJ"
    
    # Imprimir letras de las columnas en la cabecera
    cabecera = "   " + " ".join([letras[i] for i in range(len(tablero[0]))])
    print(cabecera)
    
    # Imprimir cada fila con su número correspondiente (del 1 al 10)
    for idx, fila in enumerate(tablero):
        fila_str = []
        for celda in fila:
            if ocultar_barcos and celda == 'B':
                fila_str.append('~')
            else:
                fila_str.append(celda)
                
        # El número de la fila es el índice + 1
        print(f"{idx + 1:2d} {' '.join(fila_str)}")
    print() # Salto de línea por estética