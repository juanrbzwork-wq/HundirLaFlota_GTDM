import tablero
import barcos
import mecanicas
import interfaz

def main():

    # INICIALIZACIÓN Y CONFIGURACIÓN
    interfaz.mostrar_mensaje_bienvenida()
    modo_juego = interfaz.mostrar_menu_inicial() 
    
    tablero_j1 = tablero.crear_tablero(10, 10)
    radar_j1 = tablero.crear_tablero(10, 10)
    flota_j1 = {}  

    tablero_j2 = tablero.crear_tablero(10, 10)
    radar_j2 = tablero.crear_tablero(10, 10)
    flota_j2 = {}
    
    configuracion_barcos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1] 
    
    barcos.generar_flota_aleatoria(tablero_j1, flota_j1, configuracion_barcos)
    barcos.generar_flota_aleatoria(tablero_j2, flota_j2, configuracion_barcos)

    juego_activo = True
    turno_jugador_1 = True  

    # BUCLE PRINCIPAL DEL JUEGO
    while juego_activo:
        
        if turno_jugador_1:
            # Llamamos a mecanicas.ejecutar_turno
            ha_ganado = mecanicas.ejecutar_turno(
                nombre_jugador="Jugador 1", 
                radar_atacante=radar_j1, 
                tablero_defensor=tablero_j2, 
                flota_defensora=flota_j2, 
                es_pc=False
            )
            
            if ha_ganado:
                ganador = "Jugador 1"
                juego_activo = False
            else:
                turno_jugador_1 = False
                
        else:
            es_ordenador = (modo_juego == 1)
            nombre_j2 = "Ordenador" if es_ordenador else "Jugador 2"
            
            # Llamamos a mecanicas.ejecutar_turno
            ha_ganado = mecanicas.ejecutar_turno(
                nombre_jugador=nombre_j2, 
                radar_atacante=radar_j2, 
                tablero_defensor=tablero_j1, 
                flota_defensora=flota_j1, 
                es_pc=es_ordenador
            )
            
            if ha_ganado:
                ganador = nombre_j2
                juego_activo = False
            else:
                turno_jugador_1 = True

    # RESOLUCIÓN Y FIN DE PARTIDA
    interfaz.mostrar_victoria(ganador)
    tablero.imprimir_tablero(tablero_j1, ocultar_barcos=False)
    tablero.imprimir_tablero(tablero_j2, ocultar_barcos=False)

main()