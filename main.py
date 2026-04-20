import tablero
import barcos
import mecanicas
import interfaz

def main():
    # INICIALIZACIÓN Y CONFIGURACIÓN
    interfaz.mostrar_mensaje_bienvenida()
    
    # Tableros 10x10 y flotas
    tablero_j1 = tablero.crear_tablero(10, 10)
    radar_j1 = tablero.crear_tablero(10, 10)
    flota_j1 = {}  

    tablero_j2 = tablero.crear_tablero(10, 10)
    radar_j2 = tablero.crear_tablero(10, 10)
    flota_j2 = {}
    
    configuracion_barcos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1] 
    
    # === FASE DE COLOCACIÓN DE BARCOS ===
    
    # Colocar Jugador 1
    opcion_j1 = interfaz.pedir_modo_colocacion("Jugador 1")
    if opcion_j1 == 1:
        barcos.colocar_flota_manual(tablero_j1, flota_j1, configuracion_barcos)
    else:
        barcos.generar_flota_aleatoria(tablero_j1, flota_j1, configuracion_barcos)
        print("Flota del Jugador 1 generada aleatoriamente.")

    # Colocar Jugador 2
    opcion_j2 = interfaz.pedir_modo_colocacion("Jugador 2")
    if opcion_j2 == 1:
        barcos.colocar_flota_manual(tablero_j2, flota_j2, configuracion_barcos)
    else:
        barcos.generar_flota_aleatoria(tablero_j2, flota_j2, configuracion_barcos)
        print("Flota del Jugador 2 generada aleatoriamente.")

    # === BUCLE PRINCIPAL DEL JUEGO ===
    juego_activo = True
    ganador = ""
    turno_actual = 0 # 0 para J1 y 1 para J2

    jugadores = [
        {"nombre": "Jugador 1", "radar": radar_j1, "tab_defensor": tablero_j2, "flota_defensora": flota_j2},
        {"nombre": "Jugador 2", "radar": radar_j2, "tab_defensor": tablero_j1, "flota_defensora": flota_j1}
    ]

    while juego_activo:
        jugador_activo = jugadores[turno_actual % 2]
        
        ha_ganado = mecanicas.ejecutar_turno(
            nombre_jugador=jugador_activo["nombre"], 
            radar_atacante=jugador_activo["radar"], 
            tablero_defensor=jugador_activo["tab_defensor"], 
            flota_defensora=jugador_activo["flota_defensora"]
        )
        
        if ha_ganado:
            ganador = jugador_activo["nombre"]
            juego_activo = False
        else:
            turno_actual += 1

    # RESOLUCIÓN Y FIN DE PARTIDA
    interfaz.mostrar_victoria(ganador)
    print("\n--- Tablero final Jugador 1 ---")
    tablero.imprimir_tablero(tablero_j1, ocultar_barcos=False)
    print("\n--- Tablero final Jugador 2 ---")
    tablero.imprimir_tablero(tablero_j2, ocultar_barcos=False)

main()