"""
Módulo interfaz.py
Se encarga de toda la interacción con el usuario por consola.
"""

def mostrar_mensaje_bienvenida():
    print("========================================")
    print("      BIENVENIDO A HUNDIR LA FLOTA      ")
    print("========================================")

def mostrar_menu_inicial():
    """
    Pregunta el modo de juego y devuelve la opción elegida.
    """
    while True:
        print("\nSelecciona un modo de juego:")
        print("1. Jugador contra Ordenador")
        print("2. Jugador contra Jugador (Próximamente)")
        
        opcion = input("Elige una opción (1 o 2): ")
        if opcion == "1":
            return 1
        elif opcion == "2":
            print("Modo 2 jugadores no implementado aún. Jugando contra el PC.")
            return 1
        else:
            print("Error: Por favor introduce 1 o 2.")

def pedir_coordenadas():
    """
    Pide fila (letra) y columna (número) y las traduce a índices numéricos (0-9).
    Aplica control de errores.
    """
    letras_validas = "ABCDEFGHIJ"
    
    while True:
        try:
            entrada = input("Introduce coordenadas (ejemplo: B5): ").upper().strip()
            
            if len(entrada) < 2 or len(entrada) > 3:
                raise ValueError("Longitud incorrecta.")
                
            letra_fila = entrada[0]
            numero_col = int(entrada[1:])
            
            if letra_fila not in letras_validas:
                raise ValueError("La letra de la fila no es válida.")
                
            if numero_col < 1 or numero_col > 10:
                raise ValueError("El número de la columna debe estar entre 1 y 10.")
                
            # Convertimos a índices (0 a 9)
            indice_fila = letras_validas.index(letra_fila)
            indice_columna = numero_col - 1
            
            return indice_fila, indice_columna
            
        except ValueError as e:
            print(f"Entrada inválida. Asegúrate de introducir una letra (A-J) y un número (1-10).")

def mostrar_mensaje_disparo(resultado):
    print("\n------------------------------")
    if resultado == "Agua":
        print("💦 ¡AGUA! 💦")
    elif resultado == "Tocado":
        print("💥 ¡TOCADO! 💥")
    elif resultado == "Hundido":
        print("🚢💥 ¡HUNDIDO! 💥🚢")
    elif resultado == "Repetido":
        print("⚠️ Ya habías disparado ahí. Pierdes el turno. ⚠️")
    print("------------------------------\n")

def mostrar_turno(jugador):
    print(f"\n>>> TURNO DE: {jugador} <<<")

def mostrar_victoria(ganador):
    print("\n========================================")
    print(f" 🎉 ¡FIN DE LA PARTIDA! HA GANADO: {ganador} 🎉 ")
    print("========================================\n")