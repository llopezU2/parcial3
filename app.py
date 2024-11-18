from derivada import primera_derivada

def main():
    # Valores de ejemplo para probar
    f_values = {
        'xi+2': 0.2,
        'xi+1': 0.6363,
        'xi-1': 1.1035,
        'xi-2': 1.2
    }
    h = 0.25

    # Calcular la derivada
    resultado = primera_derivada(f_values, h)
    print(f"El resultado de la derivada es: {resultado}")

if __name__ == "__main__":
    main()
