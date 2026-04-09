import random
import tablero 

def generar_flota_aleatoria(tablero_obj, flota, configuracion_barcos):
    """Coloca los barcos aleatoriamente."""
    filas = len(tablero_obj)
    cols = len(tablero_obj[0])
    
    for idx, tamano_barco in enumerate(configuracion_barcos):
        colocado = False
        while not colocado:
            orientacion = random.randint(0, 1) # 0: Horizontal, 1: Vertical
            f = random.randint(0, filas - 1)
            c = random.randint(0, cols - 1)
            
            coordenadas_temp = []
            valido = True
            
            for i in range(tamano_barco):
                nf = f + (i if orientacion == 1 else 0)
                nc = c + (i if orientacion == 0 else 0)
                
                # Comprobamos que no se salga ni colisione
                if nf >= filas or nc >= cols or tablero_obj[nf][nc] == 'B':
                    valido = False
                    break
                coordenadas_temp.append((nf, nc))
            
            if valido:
                for (nf, nc) in coordenadas_temp:
                    tablero_obj[nf][nc] = 'B'
                flota[f"barco_{idx}_{tamano_barco}casillas"] = coordenadas_temp
                colocado = True

def colocar_flota_manual(tablero_obj, flota, configuracion_barcos):
    """Permite al jugador colocar sus barcos introduciendo coordenadas."""
    filas = len(tablero_obj)
    cols = len(tablero_obj[0])
    letras_validas = "ABCDEFGHIJ"
    
    print("\n¡Preparando la colocación manual de la flota!")
    
    for idx, tamano_barco in enumerate(configuracion_barcos):
        colocado = False
        while not colocado:
            print(f"\nTe toca colocar un barco de tamaño: {tamano_barco}")
            tablero.imprimir_tablero(tablero_obj, ocultar_barcos=False)
            
            try:
                entrada = input("Introduce las coordenadas iniciales (letra columna y número fila) ej: 'C 4' o 'B5': ").upper().replace(" ", "")
                if len(entrada) < 2:
                    print("❌ ERROR: Formato inválido.")
                    continue
                
                letra = entrada[0]
                numero = entrada[1:]
                
                if letra not in letras_validas:
                    print("❌ ERROR: La columna debe ser una letra de la A a la J.")
                    continue
                    
                c = letras_validas.index(letra)
                f = int(numero) - 1
                
                if f < 0 or f >= filas:
                    print(f"❌ ERROR: La fila debe ser un número del 1 al {filas}.")
                    continue
                
                orientacion = 0
                if tamano_barco > 1:
                    ori_input = input("Orientación (h para horizontal, v para vertical): ").strip().lower()
                    if ori_input == 'v':
                        orientacion = 1
                    elif ori_input != 'h':
                        print("Orientación no válida. Asumiendo Horizontal (h).")
                        orientacion = 0
                
                coordenadas_temp = []
                valido = True
                
                for i in range(tamano_barco):
                    nf = f + (i if orientacion == 1 else 0)
                    nc = c + (i if orientacion == 0 else 0)
                    
                    if nf < 0 or nf >= filas or nc < 0 or nc >= cols or tablero_obj[nf][nc] == 'B':
                        valido = False
                        break
                    coordenadas_temp.append((nf, nc))
                
                if valido:
                    for (nf, nc) in coordenadas_temp:
                        tablero_obj[nf][nc] = 'B'
                    flota[f"barco_{idx}_{tamano_barco}casillas"] = coordenadas_temp
                    colocado = True
                    print("--> ¡Barco posicionado correctamente!")
                else:
                    print("❌ ERROR: El barco se sale del tablero o choca con otro barco. Intenta de nuevo.")
                    
            except ValueError:
                print("❌ ERROR: Formato inválido. Escribe una letra y un número.")