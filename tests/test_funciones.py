import pytest
from src.funciones import factorial

def test_factorial_1_falla():
    assert factorial(1) == 1 # Falla
    
def test_tipo_falla():
    with pytest.raises(TypeError):
        factorial("hola")  # No se puede calcular factorial de un string
        
def test_tipo_pasa():
    assert factorial(1) == 1  # Probamos que funciona con enteros
    
def test_negativo_falla():
    with pytest.raises(ValueError):
        factorial(-5)  # No se puede calcular factorial de números negativos
        
def test_negativo_pasa():
    with pytest.raises(ValueError):
        factorial(-1)  # Otro caso negativo que también debe fallar

def test_positivo_falla():
    assert factorial(5) == 120  # Probamos con un caso positivo
    
def test_positivo_falla():
    assert factorial(6) == 720  # Probamos con un caso positivo