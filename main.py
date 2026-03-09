import tablero
import barcos
import mecanicas
import interfaz

def main():

    # INICIALIZACIÓN Y CONFIGURACIÓN

    interfaz.mostrar_mensaje_bienvenida()
    modo_juego = interfaz.mostrar_menu_inicial()  # Jugador vs PC o jugador vs jugador
    
    # estructuras de datos (tableros 10x10)
    # Cada jugador necesita su tablero (donde están sus barcos) y su "radar" (donde anota sus tiros)
    tablero_j1 = tablero.crear_tablero(10, 10)
    radar_j1 = tablero.crear_tablero(10, 10)
    flota_j1 = {}  # Diccionario vacío que se llenará con los barcos

    tablero_j2 = tablero.crear_tablero(10, 10)
    radar_j2 = tablero.crear_tablero(10, 10)
    flota_j2 = {}
    
    # colocar las flotas
    # se colocan aleatoriamente.
    configuracion_barcos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1] # tamaños de los barcos
    
    barcos.generar_flota_aleatoria(tablero_j1, flota_j1, configuracion_barcos)
    barcos.generar_flota_aleatoria(tablero_j2, flota_j2, configuracion_barcos)

    # variables para controlar el bucle
    juego_activo = True
    turno_jugador_1 = True  # si es True, juega el J1. Si es False, juega el J2/PC.

    # BUCLE PRINCIPAL DEL JUEGO

    while juego_activo:
        
        if turno_jugador_1:
            # TURNO DEL JUGADOR 1
            interfaz.mostrar_turno("Jugador 1")
            tablero.imprimir_tablero(radar_j1, ocultar_barcos=False)
            
            # Pedir coordenadas, disparar y se actualizan tableros
            fila, columna = interfaz.pedir_coordenadas()
            resultado = mecanicas.procesar_disparo(tablero_j2, flota_j2, fila, columna)
            
            tablero.actualizar_celda(radar_j1, fila, columna, resultado)
            interfaz.mostrar_mensaje_disparo(resultado)
            
            # Comprobar si ha ganado el j1
            if mecanicas.verificar_fin_juego(flota_j2):
                ganador = "Jugador 1"
                juego_activo = False
            else:
                # Si falla o da en agua, pasa el turno
                turno_jugador_1 = False
                
        else:
            #TURNO DEL JUGADOR 2 (O PC)
            interfaz.mostrar_turno("Jugador 2 / Ordenador")
            
            # Si es PC, generar_coordenada_aleatoria(). Si es J2, pedir_coordenadas()
            if modo_juego == 1: 
                fila, columna = mecanicas.generar_disparo_ia(radar_j2) # Función extra para el PC
            else:
                tablero.imprimir_tablero(radar_j2, ocultar_barcos=False)
                fila, columna = interfaz.pedir_coordenadas()
                
            resultado = mecanicas.procesar_disparo(tablero_j1, flota_j1, fila, columna)
            
            tablero.actualizar_celda(radar_j2, fila, columna, resultado)
            interfaz.mostrar_mensaje_disparo(resultado)
            
            # comprobar si ha ganado
            if mecanicas.verificar_fin_juego(flota_j1):
                ganador = "Jugador 2 / Ordenador"
                juego_activo = False
            else:
                turno_jugador_1 = True

    # RESOLUCIÓN Y FIN DE PARTIDA
   
    interfaz.mostrar_victoria(ganador)
    tablero.imprimir_tablero(tablero_j1, ocultar_barcos=False)
    tablero.imprimir_tablero(tablero_j2, ocultar_barcos=False)
    
main()
