import interfaz

def test_mostrar_mensaje_bienvenida(capsys):
    interfaz.mostrar_mensaje_bienvenida()
    salida = capsys.readouterr().out
    assert "BIENVENIDO A HUNDIR LA FLOTA" in salida

def test_pedir_modo_colocacion_valido(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    resultado = interfaz.pedir_modo_colocacion("Jugador 1")
    assert resultado == 1

def test_pedir_modo_colocacion_invalido_luego_valido(monkeypatch, capsys):
    # Simulamos que falla la primera vez ("3") y acierta la segunda ("2")
    entradas = ["3", "2"]
    
    # Creamos un mock de input que SÍ imprima el texto en la consola para que capsys lo lea
    def mock_input(texto_del_input):
        print(texto_del_input) 
        return entradas.pop(0) 
        
    monkeypatch.setattr('builtins.input', mock_input)
    resultado = interfaz.pedir_modo_colocacion("Jugador 2")
    
    salida = capsys.readouterr().out
    assert "Opción inválida" in salida
    assert resultado == 2

def test_mostrar_victoria(capsys):
    interfaz.mostrar_victoria("Jugador 1")
    salida = capsys.readouterr().out
    assert "JUGADOR 1" in salida