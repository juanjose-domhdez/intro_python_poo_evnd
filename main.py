def main():
    print("Hello, Word!")
    print("Hola de nuevo, Mundo!")
    resultado = suma()
    print(f"La suma de los dos numeros es {resultado}")

def suma():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    return num1 + num2

if __name__ == "__main__":
    main()