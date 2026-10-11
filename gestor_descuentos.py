def calcular_precio_final(precio_base: float, porcentaje_descuento: float) -> float:
    """
    Calcula el precio final aplicando un porcentaje de descuento.
    
    Reglas de negocio:
    - El precio base debe ser mayor a 0.
    - El porcentaje de descuento debe estar entre 0 y 100.
    """
    if precio_base <= 0:
        raise ValueError("El precio base debe ser mayor a cero.")
    
    if not (0 <= porcentaje_descuento <= 100):
        raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
    
    monto_descuento = precio_base * (porcentaje_descuento / 100)
    precio_final = precio_base - monto_descuento
    
    return round(precio_final, 2)