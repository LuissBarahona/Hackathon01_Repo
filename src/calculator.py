import re
import ast
import operator

# Definición de operadores válidos
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}

# Evaluador seguro utilizando AST
def safe_eval(node):
    if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
        left = safe_eval(node.left)
        right = safe_eval(node.right)
        op_type = type(node.op)
        
        # Evitar división por cero
        if op_type == ast.Div and right == 0:
            raise ZeroDivisionError("Error: División por cero")
        
        result = OPERATORS[op_type](left, right)
        
        # Redondear a un decimal de precisión
        return round(result, 1)

    elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -safe_eval(node.operand)
    
    elif isinstance(node, ast.Constant):
        return node.value
    else:
        raise ValueError("Error: Operación inválida")


# Función de cálculo
def calculate(operacion):
    try:
        # Verificar si la operación está vacía o contiene solo espacios en blanco
        if not operacion.strip():
            raise ValueError("Error: Operación inválida - entrada vacía")

        # Limpiar la operación para evitar posibles riesgos de seguridad
        operacion = re.sub(r'[^0-9\+\-\*/\(\)\.\s]', '', operacion)
        
        # Parsear la operación usando ast
        node = ast.parse(operacion, mode='eval').body
        return safe_eval(node)

    except ZeroDivisionError as e:
        raise e
    except SyntaxError:
        raise SyntaxError("Error: Operación inválida")
    except Exception as e:
        raise ValueError(f"Error: {e}")


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

if __name__ == "__main__":
    main()
