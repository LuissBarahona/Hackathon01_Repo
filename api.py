import re

# LUIS
def suma(a, b):
    return a + b

# RONAL
def resta(a, b):
    return a - b

# ISAAC
def multiplicacion(a, b):
    return a * b

# CAMILO
def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

# INICIO LUIS
def calcular_operacion(operacion):
    try:
        # Limpiar la operación para evitar posibles riesgos de seguridad
        operacion = re.sub(r'[^0-9\+\-\*/\(\)\.]', '', operacion)
        
        # Evaluar la operación usando eval
        resultado = eval(operacion)
        return resultado

    except ZeroDivisionError:
        return "Error: División por cero"
    except SyntaxError:
        return "Error: Operación inválida"
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Calculadora en línea de comandos")
    print("Escribe una operación (por ejemplo, 2 + 2 o (9+9)) y presiona Enter")
    print("Presiona 'c' para borrar la operación actual o 'q' para salir")

    while True:
        try:
            operacion = input(">> ")

            if operacion.lower() == 'q':
                print("Saliendo...")
                break
            elif operacion.lower() == 'c':
                print("Operación borrada.")
                continue
            else:
                resultado = calcular_operacion(operacion)
                print(f"Resultado: {resultado}")

        except (KeyboardInterrupt, EOFError):
            print("\nSaliendo...")
            break

if __name__ == "__main__":
    main()

# FIN LUIS

