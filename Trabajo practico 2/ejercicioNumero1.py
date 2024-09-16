def buscaMayor(num1:int, num2:int, num3:int):
    numMayor = num1
    if (num1 == num2 == num3):
        print("Los numeros son iguales.")
    else:
        if num3 > numMayor:
            numMayor = num3
        if num2 > numMayor:
            numMayor = num2
        print(numMayor)

num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese un numero entero: "))
num3 = int(input("Ingrese un numero entero: "))

buscaMayor(num1, num2, num3)


