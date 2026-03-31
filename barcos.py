import random
import tablero # Importamos tablero para poder mostrarlo al colocar manualmente

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
    
    print("\n¡Preparando la colocación manual de la flota!")
    
    for idx, tamano_barco in enumerate(configuracion_barcos):
        colocado = False
        while not colocado:
            print(f"\nTe toca colocar un barco de tamaño: {tamano_barco}")
            tablero.imprimir_tablero(tablero_obj, ocultar_barcos=False)
            
            try:
                entrada = input("Introduce las coordenadas iniciales (fila columna) ej: '3 4': ")
                f, c = map(int, entrada.split())
                
                # Si el barco ocupa más de 1 casilla, pedimos orientación
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
                print("❌ ERROR: Formato inválido. Escribe dos números separados por un espacio.")