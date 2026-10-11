from unittest.mock import patch
from pasarela import procesar_orden

# Usamos @patch para interceptar 'cobrar_tarjeta' dentro del módulo pasarela
@patch("pasarela.cobrar_tarjeta")
def test_procesar_orden_exitosa(mock_cobrar):
    # 1. ARRANGE
    # Le decimos al Mock qué debe responder cuando la función procesar_orden lo llame
    mock_cobrar.return_value = True  # Simulamos que el banco respondió "Éxito"

    # 2. ACT
    resultado = procesar_orden(id_orden="ORD-123", monto=150.0, tarjeta="4557-XXXX-XXXX-1111")

    # 3. ASSERT
    assert resultado == "ORDEN_PROCESADA"
    # Verificamos que nuestro código sí llamó al cobro con los parámetros correctos
    mock_cobrar.assert_called_once_with("4557-XXXX-XXXX-1111", 150.0)


@patch("pasarela.cobrar_tarjeta")
def test_procesar_orden_tarjeta_rechazada(mock_cobrar):
    # Arrange: Simulamos que el banco rebotó la tarjeta
    mock_cobrar.return_value = False

    # Act
    resultado = procesar_orden(id_orden="ORD-124", monto=500.0, tarjeta="4000-XXXX-XXXX-0000")

    # Assert
    assert resultado == "ERROR_PAGO"