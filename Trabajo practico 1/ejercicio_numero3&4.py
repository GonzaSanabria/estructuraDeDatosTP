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