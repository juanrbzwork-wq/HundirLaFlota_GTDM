import tablero

def test_crear_tablero():
    tab = tablero.crear_tablero(5, 5)
    assert len(tab) == 5
    assert len(tab[0]) == 5
    assert tab[0][0] == '~'

def test_imprimir_tablero_visible(capsys):
    tab = tablero.crear_tablero(2, 2)
    tab[0][0] = 'B'
    tablero.imprimir_tablero(tab, ocultar_barcos=False)
    salida = capsys.readouterr().out
    assert "A" in salida
    assert "B" in salida
    assert "1" in salida
    assert "B ~" in salida # El barco debe verse

def test_imprimir_tablero_oculto(capsys):
    tab = tablero.crear_tablero(2, 2)
    tab[0][0] = 'B'
    tablero.imprimir_tablero(tab, ocultar_barcos=True)
    salida = capsys.readouterr().out
    assert "~ ~" in salida # El barco debe estar oculto como agua