"""
Pruebas unitarias para el módulo calculadora.
"""
from calculadora import suma, resta

<<<<<<< HEAD
def test_suma():
    """Valida que la suma funcione correctamente (Forzando fallo)."""
    assert suma(5, 3) == 99  # <--- Cambia el 8 por 99. Como 5+3 es 8, esto va a fallar.

def test_resta():
    """Valida que la resta funcione correctamente."""
    assert resta(10, 4) == 6
=======
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

print(suma(5, 3))
>>>>>>> 7b0a9917c301c611079dc602fb5470e5585004c7
