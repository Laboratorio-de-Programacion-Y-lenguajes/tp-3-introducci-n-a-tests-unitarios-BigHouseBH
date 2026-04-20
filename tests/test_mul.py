"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Multiplicar por cero
#   - Multiplicar dos números negativos (resultado positivo)
#   - Multiplicar un positivo y un negativo (resultado negativo)
#   - Multiplicar por 1 (elemento neutro)
#   - Multiplicar dos decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

#Ante de iniciar, aprendi el funcionamiento de pytest.mark.parametrize
#Al parecer es un  metodo con la estrucutra estandar de un test
#Con los variables listas para cargarles valores del test
#junto al retorno esperado para dicho test,
#de modo que reutiliza el mismo algoritmo multiples veces
# #con la coleccion de test que se le carga en vectores

#Conceptualmente @pytest.mark.parametrize:
#void conceptualPytestMarkParametrize(int a, int b, int esperado) {
#    assert funcionEjemplo(a, b) == esperado;
#}
