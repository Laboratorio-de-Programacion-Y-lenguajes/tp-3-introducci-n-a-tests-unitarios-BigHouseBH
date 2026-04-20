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


#Antes de iniciar, aprendí el funcionamiento de @pytest.mark.parametrize.
#No es un método en sí, sino un DECORADOR que aplica METADATA a una función.
#
#Componentes:
#- "@": Operador que declara una metadata.
#- "pytest.mark.parametrize": Tipo de metadata (test parametrizado).
#- La función debajo: Sujeto que recibe la metadata y es modificado por ella.
#
#La metadata altera el comportamiento por defecto de la función:
#en lugar de ejecutarse UNA vez, se ejecuta MÚLTIPLES veces,
#una por cada tupla de valores provista.
#
#En cuanto al operador "@" refiere a metadata, su función es la misma que en Java:
#define un metadato (datos generales que sobrescriben valores por defecto),
#como el <head> en HTML, o @Override en Java.
#
#Explicación de parámetros en @pytest.mark.parametrize("a,b,esperado", [(1,2,3)]):
#- "a,b,esperado": String que nombra los parámetros para identificar cada caso en los reportes.
#- [(1,2,3)]: Colección de tests. Cada tupla es un vector con los valores
#  a cargar en los parámetros de la función.

@pytest.mark.parametrize("a, b, esperado", [
    (0, 1, 0),           # Multiplicar por cero
    (-1, -1, 1),         # Multiplicar dos números negativos (resultado positivo)
    (1, -1, -1),         # Multiplicar un positivo y un negativo (resultado negativo)
    (1, 2, 2),           # Multiplicar por 1 (elemento neutro)
    (1.5, 2.0, 3.0),     # Multiplicar dos decimales (float)
])
def testMultiplicar(a, b, esperado):#Funcion sujeta a la metadata declarada
    assert mul(a, b) == esperado