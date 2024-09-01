import re

# Funciones matemáticas básicas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("División por cero")
    return a / b

# Calculadora principal
def calculate(operacion):
    # Limpiar la operación para evitar posibles riesgos de seguridad
    operacion = operacion.strip()
    
    if operacion == "":
        raise ValueError("Entrada vacía")
    
    # Validar si la operación contiene caracteres válidos
    if not re.match(r'^[0-9\+\-\*/\(\)\.\s]+$', operacion):
        raise ValueError("Caracter inválido encontrado en la operación")

    try:
        # Evaluar la operación usando eval de forma segura
        resultado = eval(operacion, {"__builtins__": None}, {
            "suma": suma,
            "resta": resta,
            "multiplicacion": multiplicacion,
            "division": division
        })
        
        return resultado

    except ZeroDivisionError:
        raise ZeroDivisionError("División por cero")
    except SyntaxError:
        raise SyntaxError("Operación inválida")
    except Exception as e:
        raise ValueError(f"Error: {str(e)}")

# Ejecución principal
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
                resultado = calculate(operacion)
                print(f"Resultado: {resultado}")

        except (KeyboardInterrupt, EOFError):
            print("\nSaliendo...")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
