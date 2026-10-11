import pytest
from gestor_descuentos import calcular_precio_final

def test_calcular_precio_final_exitoso():
    # 1. ARRANGE (Preparar): Definir los datos de entrada y el resultado esperado
    precio_inicial = 100.0
    descuento = 20.0
    resultado_esperado = 80.0

    # 2. ACT (Actuar): Invocamos la función bajo prueba
    resultado_obtenido = calcular_precio_final(precio_inicial, descuento)

    # 3. ASSERT (Afirmar): Verificamos que el resultado coincida
    assert resultado_obtenido == resultado_esperado


def test_calcular_precio_final_descuento_cero():
    # Arrange
    precio_inicial = 50.0
    descuento = 0.0

    # Act
    resultado_obtenido = calcular_precio_final(precio_inicial, descuento)

    # Assert
    assert resultado_obtenido == 50.0


def test_calcular_precio_final_precio_invalido_lanza_excepcion():
    # Arrange
    precio_invalido = -10.0
    descuento = 15.0

    # Act & Assert (Usamos pytest.raises para validar que se lance el ValueError)
    with pytest.raises(ValueError) as exc_info:
        calcular_precio_final(precio_invalido, descuento)
    
    # Assert adicional sobre el mensaje de error
    assert str(exc_info.value) == "El precio base debe ser mayor a cero."