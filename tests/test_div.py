"""Tests para la función div(a, b) -> float."""

import pytest

from src.calculator import div


# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - División que da resultado decimal (float)
#   - División con números negativos
#   - División por cero → debe lanzar ZeroDivisionError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_div_por_cero():
#     with pytest.raises(ZeroDivisionError):
#         div(10, 0)
def testDivisionDecimal():
    assert div(5, 2) == 2.5#"Si la evaluo en 5 / 2 debe dar 2.5"

def testDivisionNegativos():
    assert div(-6, 3) == -2.0#"Si la evaluo en -6 / 3 debe dar -2.0"

#Este caso es diferente a los anteriores,
#no se esperan valores correctos, sino un error,
#Es semejante a un "Sintax error" en una calculadora,
#Entonces un correcto funcionamiento se define por lo que se espera
#Sea su capacidad(su alcanse) y sus fallas(sus limites).
#El retorno assert esta diseñado para numeros, no para erroes
#Para  retornar errores, se usa  el with  pytest.[comportamineto del error]([tipo de error])
def testDivisionPorCero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
        
#Analogia en java(mi lenguaje fuerte):
# El "with" es como hacer un catch que retorna implicitamente un assert
# y luego un try.Ej:

# with pytest.raises(ZeroDivisionError):     =    catch(ZeroDivisionError e){return assert}
# div(1,0)                                   =    try{div(1,0)}