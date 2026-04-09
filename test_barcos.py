import barcos
import tablero

def test_generar_flota_aleatoria():
    tab = tablero.crear_tablero(5, 5)
    flota = {}
    configuracion = [3, 2] # 5 casillas en total
    
    barcos.generar_flota_aleatoria(tab, flota, configuracion)
    
    # Contar cuántas 'B' hay en el tablero
    casillas_ocupadas = sum(fila.count('B') for fila in tab)
    assert casillas_ocupadas == 5
    assert len(flota) == 2

def test_colocar_flota_manual_exito(monkeypatch, capsys):
    tab = tablero.crear_tablero(5, 5)
    flota = {}
    configuracion = [2]
    
    # Colocar en A 1, orientación horizontal
    entradas = ["A 1", "h"]
    monkeypatch.setattr('builtins.input', lambda _: entradas.pop(0))
    
    barcos.colocar_flota_manual(tab, flota, configuracion)
    
    assert tab[0][0] == 'B' # Fila 0, Columna 0 (A1)
    assert tab[0][1] == 'B' # Horizontal
    assert "barco_0_2casillas" in flota

def test_colocar_flota_manual_errores(monkeypatch, capsys):
    tab = tablero.crear_tablero(3, 3)
    tab[0][1] = 'B' # Ponemos un barco estorbo para forzar colisión
    flota = {}
    configuracion = [2]
    
    entradas = [
        "A",      # Formato inválido
        "Z 1",    # Letra inválida
        "A 9",    # Fila fuera de rango
        "A 1", "h", # Colisión con el barco en (0,1)
        "A 1", "x", # Orientación inválida (asume horizontal, chocará de nuevo)
        "A 2", "v"  # Posición válida (B2 hacia abajo)
    ]
    monkeypatch.setattr('builtins.input', lambda _: entradas.pop(0))
    
    barcos.colocar_flota_manual(tab, flota, configuracion)
    salida = capsys.readouterr().out
    
    assert "Formato inválido" in salida
    assert "El barco se sale del tablero o choca" in salida
    assert "Orientación no válida" in salida
    assert tab[1][0] == 'B' # Comprobamos que finalmente se colocó en A2 (v)