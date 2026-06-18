"""
Pruebas unitarias para el módulo calculadora.
"""
from calculadora import suma, resta

def test_suma():
    """Valida que la suma funcione correctamente."""
    assert suma(5, 3) == 8

def test_resta():
    """Valida que la resta funcione correctamente."""
    assert resta(10, 4) == 6