def calcular_derivada(formula, h, valores_predefinidos):
    """
    Calcula la derivada basada en una fórmula proporcionada por el usuario.

    Parámetros:
    - formula (str): Fórmula ingresada por el usuario en términos de xi+2, xi+1, xi, xi-1, xi-2.
    - h (float): Paso o altura proporcionada por el usuario.
    - valores_predefinidos (dict): Diccionario con los valores predefinidos de xi y f(x).

    Retorna:
    - float: El resultado de la derivada calculada.
    """
    # Validar que los términos de la fórmula existen en los valores predefinidos
    for termino in ['xi+2', 'xi+1', 'xi', 'xi-1', 'xi-2']:
        if termino in formula and termino not in valores_predefinidos:
            raise ValueError(f"El término {termino} no está en los valores predefinidos.")

    # Reemplazar los valores predefinidos en la fórmula
    for key, value in valores_predefinidos.items():
        formula = formula.replace(key, str(value['f(x)']))

    # Evaluar la fórmula
    try:
        resultado = eval(formula)  # Evaluar la fórmula con los valores reemplazados
    except Exception as e:
        raise ValueError(f"Error al evaluar la fórmula: {e}")

    return resultado
