import re

#LUIS
def suma(a, b):
    return a + b

#RONAL


#ISAAC
def multiplicacion(a, b):
    return a * b

#CAMILO




#INICIO LUIS
def calcular_operacion(operacion):
    try:
        # Usar una expresión regular para dividir la operación en operandos y operador
        match = re.match(r"(\d+\.?\d*)([\+\-\/])(\d+\.?\d)", operacion)
        if not match:
            return "Error: Operación inválida"

        a = float(match.group(1))
        operador = match.group(2)
        b = float(match.group(3))

        # Seleccionar la operación según el operador
        if operador == '+':
            return suma(a, b)
        elif operador == '-':
            return resta(a, b)
        elif operador == '*':
            return multiplicacion(a, b)
        elif operador == '/':
            return division(a, b)
        else:
            return "Error: Operador inválido"
    except ValueError:
        return "Error: Operación inválida"
    except Exception as e:
        return f"Error: {e}"


def main():
    print("Calculadora en línea de comandos")
    print("Escribe una operación (por ejemplo, 2 + 2 o 2+2) y presiona Enter")
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



if _name_ == "_main_":
    main()