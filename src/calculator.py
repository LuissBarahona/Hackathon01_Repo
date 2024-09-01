import ast
import operator as op
import re

# Mapa de operadores permitidos
OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg
}

def evaluate(node):
    if isinstance(node, ast.Num):  # <number>
        return node.n
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        left = evaluate(node.left)
        right = evaluate(node.right)
        return OPERATORS[type(node.op)](left, right)
    elif isinstance(node, ast.UnaryOp):  # <operator> <operand>
        operand = evaluate(node.operand)
        return OPERATORS[type(node.op)](operand)
    else:
        raise TypeError(node)

def calculate(expression):
    # Limpiar la operación para evitar caracteres no permitidos
    expression = expression.strip()
    if expression == "":
        raise ValueError("Entrada vacía")

    if not re.match(r'^[0-9\+\-\*/\(\)\.\s]+$', expression):
        raise ValueError("Caracter inválido encontrado en la operación")

    try:
        # Parsear la expresión
        node = ast.parse(expression, mode='eval').body
        return evaluate(node)

    except ZeroDivisionError:
        raise ZeroDivisionError("División por cero")
    except SyntaxError:
        raise SyntaxError("Operación inválida")
    except Exception as e:
        raise ValueError(f"Error: {str(e)}")

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
