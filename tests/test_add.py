"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add


# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Sumar dos números negativos
#   - Sumar un número positivo y uno negativo
#   - Sumar con cero
#   - Sumar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
#
# Ejemplo de test parametrizado:
#
# @pytest.mark.parametrize("a,b,expected", [
#     (..., ..., ...),
#     (..., ..., ...),
# ])
# def test_add_parametrizado(a, b, expected):
#     assert add(a, b) == expected



#Segun la ia: el assert es una especie  es un operador que funciona 
# semajnte a un return, cuya funcion es dar unos "casos de prueva"
# (ejemplos de valores) al la funcion y
# verificar si retorna lo esperado en tal caso
#Piensalo como decir: asertas si tal valores retornas tal respuesta
def  testSumarDosNegativos():
    assert add(-1, -2) == -3#"Si la evaluo en -1 + -2 debe dar -3"
    
def testSumarPositivoYNegativo():
    assert add(5, -3) == 2#"Si la evaluo en 5 + -3 debe dar 2"
    
def testSumarConCero():
    assert add(1, 0) == 1#"Si la evaluo en 1 + 0 debe dar 1"
    
def testSumarConDecimales():
    assert    add(1.1,1.1)==2.2;