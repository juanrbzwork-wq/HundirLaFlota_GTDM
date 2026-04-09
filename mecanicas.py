import tablero

def pedir_coordenadas(size=10):
    """Pide coordenadas (Letra y Número) al jugador y las traduce a índices de matriz"""
    letras_validas = "ABCDEFGHIJ"[:size]
    
    while True: 
        try:
            # Pedimos entrada, la pasamos a mayúsculas y quitamos espacios
            entrada = input(f"Introduce coordenadas (letra columna y número fila) ej: 'C 4' o 'A1': ").upper().replace(" ", "")
            
            if len(entrada) < 2:
                print("Formato inválido. Debes poner una letra y un número.")
                continue
            
            letra = entrada[0]
            numero = entrada[1:] # Todo lo que va después de la letra
            
            if letra not in letras_validas:
                print(f"❌ La columna debe ser una letra de la A a la {letras_validas[-1]}.")
                continue
            
            # Traducimos: la letra es la columna, el número es la fila
            c = letras_validas.index(letra)
            f = int(numero) - 1
            
            if 0 <= f < size:
                return f, c
            else:
                print(f"❌ La fila debe ser un número del 1 al {size}.")
                
        except ValueError:
            print("❌ Formato inválido. Asegúrate de incluir el número de la fila correctamente.")

def verificar_hundido(flota, f, c):
    """Revisa si al golpear la coordenada (f, c) se hunde algún barco completo"""
    for nombre_barco, coords in flota.items():
        if (f, c) in coords:
            coords.remove((f, c))
            if len(coords) == 0:
                return nombre_barco 
            return None
    return None

def ejecutar_turno(nombre_jugador, radar_atacante, tablero_defensor, flota_defensora):
    print(f"\n{'='*15} Turno de {nombre_jugador} {'='*15}")
    print("Tu Radar de ataques:")
    tablero.imprimir_tablero(radar_atacante)
    
    size = len(tablero_defensor)
    valido = False
    
    # Repetir mientras ataque una coordenada repetida
    while not valido:
        f, c = pedir_coordenadas(size)
        
        if radar_atacante[f][c] in ['X', 'O']:
            print("Ya has disparado en esas coordenadas. Intenta de nuevo.")
        else:
            valido = True
            
    # Para imprimir bonito de nuevo (Letra y luego número)
    letras = "ABCDEFGHIJ"
    print(f"> {nombre_jugador} dispara en {letras[c]}{f + 1}...")
    
    # Comprobar el disparo
    if tablero_defensor[f][c] == 'B':
        print("¡TOCADO! 💥")
        tablero_defensor[f][c] = 'X'
        radar_atacante[f][c] = 'X'
        
        barco_hundido = verificar_hundido(flota_defensora, f, c)
        if barco_hundido:
            print("¡HUNDIDO! 🚢💥")
            del flota_defensora[barco_hundido]
            
    else:
        print("¡AGUA! 🌊")
        tablero_defensor[f][c] = 'O'
        radar_atacante[f][c] = 'O'
        
    if len(flota_defensora) == 0:
        return True
    
    return False