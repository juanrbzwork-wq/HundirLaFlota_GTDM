import tablero

def pedir_coordenadas(size=10):
    """Pide coordenadas al jugador y comprueba que no den error de formato"""
    while True: 
        try:
            entrada = input("Introduce coordenadas de ataque (fila columna) ej: '3 4': ")
            partes = entrada.split() # Divide el texto en una lista
            
            if len(partes) != 2:
                print("Formato inválido. Usa dos números separados por un espacio.")
                continue # Vuelve al inicio del while
            
            f = int(partes[0])
            c = int(partes[1])
            
            if 0 <= f < size and 0 <= c < size:
                return f, c
            print("Coordenadas fuera de rango. Recuerda que el tablero es de 0 a 9.")
        except ValueError:
            print("Formato inválido. Recuerda usar números enteros.")

def verificar_hundido(flota, f, c):
    """Revisa si al golpear la coordenada (f, c) se hunde algún barco completo"""
    for nombre_barco, coords in flota.items():
        if (f, c) in coords:
            coords.remove((f, c))
            if len(coords) == 0:
                return nombre_barco # El barco no tiene más casillas intactas
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
            
    print(f"> {nombre_jugador} dispara en ({f}, {c})...")
    
    # Comprobar el disparo
    if tablero_defensor[f][c] == 'B':
        print("¡TOCADO! 💥")
        tablero_defensor[f][c] = 'X'
        radar_atacante[f][c] = 'X'
        
        barco_hundido = verificar_hundido(flota_defensora, f, c)
        if barco_hundido:
            print("¡HUNDIDO! 🚢💥")
            del flota_defensora[barco_hundido] # Eliminamos el barco hundido
            
    else:
        print("¡AGUA! 🌊")
        tablero_defensor[f][c] = 'O'
        radar_atacante[f][c] = 'O'
        
    # Comprobar si se ha ganado
    if len(flota_defensora) == 0:
        return True
    
    return False