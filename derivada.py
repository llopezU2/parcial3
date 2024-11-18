def primera_derivada(f_values, h):
    """
    Calcula la primera derivada utilizando la fórmula:
    f'(xi) = (-f(xi+2) + 8*f(xi+1) - 8*f(xi-1) + f(xi-2)) / (12*h)

    Parámetros:
    - f_values (dict): Diccionario con los valores de la función en los puntos.
    - h (float): Paso o altura.

    Retorna:
    - float: Valor de la derivada.
    """
    # Validar que todas las claves están presentes
    if not all(key in f_values for key in ['xi+2', 'xi+1', 'xi-1', 'xi-2']):
        raise ValueError("El diccionario 'f_values' debe contener las claves: 'xi+2', 'xi+1', 'xi-1', 'xi-2'")
    
    # Calcular la derivada
    derivada = (-f_values['xi+2'] + 8*f_values['xi+1'] - 8*f_values['xi-1'] + f_values['xi-2']) / (12 * h)
    return derivada
