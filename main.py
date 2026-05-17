def main():
    print("Hello, Word!")
    print("Hola de nuevo, Mundo!")
    resultado = suma()
    print(f"La suma de los dos numeros es {resultado}")
    resultado = multiplicacion()
    print(f"El resultado de la multiplicacion es {resultado}")

def suma():
    print("Suma de dos numeros")
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    return num1 + num2

def multiplicacion():
    print("Multiplicacion de dos numeros")
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    return num1 * num2

if __name__ == "__main__":
    main()