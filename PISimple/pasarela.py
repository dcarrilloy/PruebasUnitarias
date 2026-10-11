import requests  # Librería que hace peticiones HTTP a internet

def cobrar_tarjeta(tarjeta: str, monto: float) -> bool:
    """Función que en la vida real hace una petición HTTP a un banco externo."""
    respuesta = requests.post("https://api.banco.com/v1/cobrar", json={"tarjeta": tarjeta, "monto": monto})
    return respuesta.status_code == 200

def procesar_orden(id_orden: str, monto: float, tarjeta: str) -> str:
    """Lógica de negocio que depende del cobro con tarjeta."""
    if monto <= 0:
        return "RECHAZADO_MONTO_INVALIDO"
    
    # Llamada al servicio externo
    exito = cobrar_tarjeta(tarjeta, monto)
    
    if exito:
        return "ORDEN_PROCESADA"
    else:
        return "ERROR_PAGO"