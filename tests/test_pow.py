"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Cualquier número elevado a 0 (resultado: 1)
#   - Número elevado a 1 (resultado: el mismo número)
#   - Base negativa con exponente par (resultado positivo)
#   - Exponente decimal, ej: 9 ** 0.5 (raíz cuadrada)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.


@pytest.mark.parametrize("base, exponente, esperado", [
    (5, 0, 1),           # (X ^ 0) = 1
    (5, 1, 5),           # (X ^ 1) = X
    (-2, 4, 16),         # X>=0 y E%2=0 => X^E >= 0
    (9, 0.5, 3),         # E<1 => X^E  = raíz(E) de X
])
def testPow(X, E, esperado):
    assert pow_(X, E) == esperado
    
    