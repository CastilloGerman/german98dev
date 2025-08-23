# calculadora.py
# Calculadora básica con historial

historial = []  # Lista para guardar operaciones realizadas

def mostrar_historial():
    if not historial:
        print("No hay operaciones registradas aún.")
    else:
        print("\n📜 Historial de operaciones:")
        for i, operacion in enumerate(historial, 1):
            print(f"{i}. {operacion}")

def suma():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    resultado = a + b
    historial.append(f"{a} + {b} = {resultado}")
    return resultado

def resta():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    resultado = a - b
    historial.append(f"{a} - {b} = {resultado}")
    return resultado

def multiplicacion():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    resultado = a * b
    historial.append(f"{a} * {b} = {resultado}")
    return resultado

def division():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    if b == 0:
        return "Error: División por cero no permitida."
    resultado = a / b
    historial.append(f"{a} / {b} = {resultado}")
    return resultado

def potencia():
    a = int(input("Ingrese la base: "))
    b = int(input("Ingrese el exponente: "))
    resultado = a ** b
    historial.append(f"{a} ^ {b} = {resultado}")
    return resultado

def raiz_cuadrada():
    a = int(input("Ingrese un número: "))
    if a < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."
    resultado = a ** 0.5
    historial.append(f"√{a} = {resultado}")
    return resultado

def porcentaje():
    a = int(input("Ingrese el número: "))
    b = int(input("Ingrese el porcentaje a calcular: "))
    resultado = (a * b) / 100
    historial.append(f"{b}% de {a} = {resultado}")
    return resultado

def menu():
    print("\nSeleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Porcentaje")
    print("8. Ver historial")
    print("9. Salir")
    return int(input("Ingrese el número de la operación: "))

def calculadora():
    while True:
        opcion = menu()
        if opcion == 1:
            print(f"Resultado: {suma()}")
        elif opcion == 2:
            print(f"Resultado: {resta()}")
        elif opcion == 3:
            print(f"Resultado: {multiplicacion()}")
        elif opcion == 4:
            print(f"Resultado: {division()}")
        elif opcion == 5:
            print(f"Resultado: {potencia()}")
        elif opcion == 6:
            print(f"Resultado: {raiz_cuadrada()}")
        elif opcion == 7:
            print(f"Resultado: {porcentaje()}")
        elif opcion == 8:
            mostrar_historial()
        elif opcion == 9:
            print("Saliendo de la calculadora.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
# Ejemplo de uso de la calculadora

if __name__ == "__main__":
    calculadora()