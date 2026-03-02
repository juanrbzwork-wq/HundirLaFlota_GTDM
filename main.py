# Importamos los módulos de nuestra arquitectura
import tablero
import barcos
import mecanicas
import interfaz

def main():
    # ==========================================
    # FASE 1: INICIALIZACIÓN Y CONFIGURACIÓN
    # ==========================================
    interfaz.mostrar_mensaje_bienvenida()
    modo_juego = interfaz.mostrar_menu_inicial()  # Ej: 1 = Jugador vs PC
    
    # 1.1 Crear las estructuras de datos (Tableros 10x10)
    # Cada jugador necesita su tablero (donde están sus barcos) y su "radar" (donde anota sus tiros)
    tablero_j1 = tablero.crear_tablero(10, 10)
    radar_j1 = tablero.crear_tablero(10, 10)
    flota_j1 = {}  # Diccionario vacío que se llenará con los barcos

    tablero_j2 = tablero.crear_tablero(10, 10)
    radar_j2 = tablero.crear_tablero(10, 10)
    flota_j2 = {}
    
    # 1.2 Colocar las flotas
    # (Para simplificar este esqueleto, asumimos que ambos se colocan aleatoriamente.
    # Más adelante podéis añadir que el Jugador 1 los coloque a mano mediante interfaz).
    configuracion_barcos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1] # Tamaños de los barcos
    
    barcos.generar_flota_aleatoria(tablero_j1, flota_j1, configuracion_barcos)
    barcos.generar_flota_aleatoria(tablero_j2, flota_j2, configuracion_barcos)

    # Variables de control del bucle
    juego_activo = True
    turno_jugador_1 = True  # Si es True, juega el J1. Si es False, juega el J2/PC.

    # ==========================================
    # FASE 2: BUCLE PRINCIPAL DEL JUEGO
    # ==========================================
    while juego_activo:
        
        if turno_jugador_1:
            # --- TURNO DEL JUGADOR 1 ---
            interfaz.mostrar_turno("Jugador 1")
            tablero.imprimir_tablero(radar_j1, ocultar_barcos=False)
            
            # Pedir coordenadas, disparar y actualizar tableros
            fila, columna = interfaz.pedir_coordenadas()
            resultado = mecanicas.procesar_disparo(tablero_j2, flota_j2, fila, columna)
            
            tablero.actualizar_celda(radar_j1, fila, columna, resultado)
            interfaz.mostrar_mensaje_disparo(resultado)
            
            # Comprobar si ha ganado
            if mecanicas.verificar_fin_juego(flota_j2):
                ganador = "Jugador 1"
                juego_activo = False
            else:
                # Si falla o da en agua, pasa el turno (cambiadlo si jugáis con reglas de repetir turno por acertar)
                turno_jugador_1 = False
                
        else:
            # --- TURNO DEL JUGADOR 2 (O PC) ---
            interfaz.mostrar_turno("Jugador 2 / Ordenador")
            
            # Si es PC, generar_coordenada_aleatoria(). Si es Jugador 2, pedir_coordenadas()
            if modo_juego == 1: 
                fila, columna = mecanicas.generar_disparo_ia(radar_j2) # Función extra para el PC
            else:
                tablero.imprimir_tablero(radar_j2, ocultar_barcos=False)
                fila, columna = interfaz.pedir_coordenadas()
                
            resultado = mecanicas.procesar_disparo(tablero_j1, flota_j1, fila, columna)
            
            tablero.actualizar_celda(radar_j2, fila, columna, resultado)
            interfaz.mostrar_mensaje_disparo(resultado)
            
            # Comprobar si ha ganado
            if mecanicas.verificar_fin_juego(flota_j1):
                ganador = "Jugador 2 / Ordenador"
                juego_activo = False
            else:
                turno_jugador_1 = True

    # ==========================================
    # FASE 3: RESOLUCIÓN Y FIN DE PARTIDA
    # ==========================================
    interfaz.mostrar_victoria(ganador)
    tablero.imprimir_tablero(tablero_j1, ocultar_barcos=False)
    tablero.imprimir_tablero(tablero_j2, ocultar_barcos=False)
    
# Esto asegura que el main solo se ejecuta si lanzamos este archivo directamente
if __name__ == "__main__":
    main()