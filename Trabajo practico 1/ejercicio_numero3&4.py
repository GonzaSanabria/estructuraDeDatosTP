diaSemanas = {
    1: "Lunes",
    2: "Martes",
    3: "Miercoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sabado"
}

print("============================= AULAS ==============================")

while True:
    try:
        num = int(input("Ingrese el número del día: 1 (Lunes) a 6 (Sábado): "))
        if num in diaSemanas:
            
            if num % 2 == 0:
                print("A-300")
            else:
                print("A-315")
            break
        else:
            print("Número inválido. Por favor, ingrese un número entre 1 y 6.")
            
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")


print("================= Descuento y estacionamientos =================")

turnos = {
    "maniana",
    "mañana",
    "tarde",
    "noche"
}

while True:
    try:
        materiasCursadas = int(input("Ingrese la cantidad de materias a las que desearía anotarse: "))
        
        cuota = 12000
        
        turno = input("Ingrese el turno: mañana, tarde o noche: ").lower()
        
        if turno in turnos:
            if turno == "tarde" and materiasCursadas == 3:
                descuento = 0.25
                cuotaDescuento = cuota * (1 - descuento)
            else:
                descuento = 0.05
                cuotaDescuento = cuota * (1 - descuento)
            print(f"La cuota con descuento es: {cuotaDescuento}")
            break
        else:
            print("El turno ingresado es incorrecto.")
    except ValueError:
        print("Debe ingresar un número válido para la cantidad de materias.")


vehiculosDisponibles = {
    "moto", 
    "auto",
    "bicicleta"
}

while True:
    try:
        vehiculoUsado = input("Ingrese el vehículo en el que ingresa: Auto, Moto o Bicicleta: ").lower()

        if vehiculoUsado in vehiculosDisponibles:
            if vehiculoUsado == "moto":
                print("El costo de estacionamiento para moto es: $300.")
            elif vehiculoUsado == "auto":
                print("El costo de estacionamiento para auto es de: $300.")
            else: 
                print("El costo de estacionamiento de la bicicleta es de: $50.")
            break
        else:
            print("Vehículo no encontrado. Por favor ingrese uno de los vehículos disponibles: Auto, Moto o Bicicleta.")
    except ValueError:
        print("Entrada no válida. Por favor ingrese un valor correcto.")

print("Día   Aula")
print("===================")


for dia in range(1, 7):
    
    if dia % 2 == 0:
        aula = "A-300"  
    else:
        aula = "A-315"  

    
    print(f"{dia}    {aula}")

print("Carga de edades.")
contError = 0 
while True:
    try:
        edad = int(input("Ingrese una edad mayor o igual a 18: "))  
        if edad >= 18:
            print(f"La edad ingresada es: {edad}")
            break  
        else:
            print("Debe ingresar una edad mayor o igual a 18.")
            contError += 1
    except ValueError:
        print("Por favor, ingrese un número válido.")

print(f"Se ha ingresado la edad erroneamente: {contError}")

print("\nPROMEDIO DE NOTAS")

sumNotas = 0
prom = 0
for notaNum in range(1, 6):
    while True:
        try:
            nota = int(input("Ingrese una nota del 1 al 10: "))
            if nota > 0 and nota <= 10:
                sumNotas += nota
                break
            else:
                print("Por favor, ingrese un numero del 1 al 10.")
        except ValueError:
            print("Por favor ingrese numeros. Intente nuevamente.")

prom = sumNotas / 5

print(f"El promedio de notas es: {prom}")
print("\nCOSTO DEL COMEDOR.")


print(f"Día   Costo\n{'=' * 20}")


for dia in range(1, 7):
    
    print(f"El costo del comedor en el dia {dia} es de: ${1250 * dia} ")
    