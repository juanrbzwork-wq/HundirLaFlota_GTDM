def mostrar_mensaje_bienvenida():
    print("="*50)
    print("        ¡BIENVENIDO A HUNDIR LA FLOTA!        ")
    print("="*50)

def mostrar_menu_inicial():
    print("Selecciona el modo de juego:")
    print("1. Un jugador (contra el Ordenador)")
    print("2. Dos jugadores (Multijugador local)")
    
    opcion = input("Introduce 1 o 2: ")
    while opcion not in ['1', '2']:
        opcion = input("Opción no válida. Por favor, introduce 1 o 2: ")
    
    return int(opcion)

def pedir_modo_colocacion(nombre_jugador):
    """Pregunta al jugador si quiere colocar barcos manual o aleatoriamente"""
    print(f"\n{'-'*40}")
    print(f"Almirante {nombre_jugador}, ¿cómo desea posicionar su flota?")
    print("1. Manualmente (tú eliges las coordenadas)")
    print("2. Aleatoriamente (posicionamiento automático)")
    
    opcion = input("Elige una opción (1 o 2): ")
    while opcion not in ['1', '2']:
        opcion = input("Opción inválida. Elige 1 (Manual) o 2 (Aleatorio): ")
        
    return int(opcion)

def mostrar_victoria(ganador):
    print("\n" + "*"*50)
    print(f"      ¡FIN DE LA PARTIDA! HA GANADO: {ganador.upper()}      ")
    print("*"*50 + "\n")