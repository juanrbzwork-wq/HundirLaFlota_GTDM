import mecanicas
import tablero

def test_pedir_coordenadas_errores_y_acierto(monkeypatch, capsys):
    # Simulamos todos los errores posibles y finalmente un acierto
    entradas = [
        "A",       # Error: Menos de 2 caracteres
        "Z 1",     # Error: Letra fuera de rango (A-J)
        "A 15",    # Error: Número fuera de rango
        "A B",     # Error: ValueError (no es un número)
        "C 4"      # Acierto: Fila 3, Columna 2
    ]
    monkeypatch.setattr('builtins.input', lambda _: entradas.pop(0))
    
    f, c = mecanicas.pedir_coordenadas(size=10)
    salida = capsys.readouterr().out
    
    assert "Formato inválido" in salida
    assert "La columna debe ser una letra" in salida
    assert "La fila debe ser un número" in salida
    assert f == 3 # El número 4 es el índice 3
    assert c == 2 # La letra C es el índice 2

def test_verificar_hundido():
    flota = {"barco_1": [(0,0), (0,1)]}
    
    # Probamos a golpear pero no hundir
    res1 = mecanicas.verificar_hundido(flota, 0, 0)
    assert res1 is None
    
    # Probamos a dar el golpe de gracia
    res2 = mecanicas.verificar_hundido(flota, 0, 1)
    assert res2 == "barco_1"

def test_ejecutar_turno_agua(monkeypatch, capsys):
    radar = tablero.crear_tablero(3, 3)
    defensor = tablero.crear_tablero(3, 3)
    flota = {"barco_1": [(2, 2)]}
    
    monkeypatch.setattr('builtins.input', lambda _: "A 1") # Dispara al agua (0,0)
    ha_ganado = mecanicas.ejecutar_turno("P1", radar, defensor, flota)
    
    salida = capsys.readouterr().out
    assert "¡AGUA!" in salida
    assert not ha_ganado
    assert radar[0][0] == 'O'

def test_ejecutar_turno_tocado_y_repetido(monkeypatch, capsys):
    radar = tablero.crear_tablero(3, 3)
    defensor = tablero.crear_tablero(3, 3)
    defensor[0][0] = 'B'
    radar[0][1] = 'X' # Simulamos un tiro previo
    flota = {"barco_1": [(0,0), (0,2)]}
    
    # Dispara a uno repetido, luego acierta a un barco
    entradas = ["B 1", "A 1"] 
    monkeypatch.setattr('builtins.input', lambda _: entradas.pop(0))
    
    ha_ganado = mecanicas.ejecutar_turno("P1", radar, defensor, flota)
    salida = capsys.readouterr().out
    
    assert "Ya has disparado en esas coordenadas" in salida
    assert "¡TOCADO!" in salida
    assert not ha_ganado

def test_ejecutar_turno_hundido_y_victoria(monkeypatch, capsys):
    radar = tablero.crear_tablero(3, 3)
    defensor = tablero.crear_tablero(3, 3)
    defensor[0][0] = 'B'
    flota = {"barco_1": [(0,0)]} # Barco de 1 casilla
    
    monkeypatch.setattr('builtins.input', lambda _: "A 1")
    ha_ganado = mecanicas.ejecutar_turno("P1", radar, defensor, flota)
    
    salida = capsys.readouterr().out
    assert "¡HUNDIDO!" in salida
    assert ha_ganado == True