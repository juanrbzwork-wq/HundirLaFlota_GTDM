def mostrar_mensaje_bienvenida():
    print("="*50)
    print("        ¡BIENVENIDO A HUNDIR LA FLOTA!        ")
    print("        --- Modo 2 Jugadores Local ---        ")
    print("="*50)

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