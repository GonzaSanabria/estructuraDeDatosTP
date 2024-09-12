diaSemanas = {
    1: "Lunes",
    2: "Martes",
    3: "Miercoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sabado"
}

print("============================= AULAS ==============================")
try:
    num = int(input("Ingrese el numero del dia: 1 (Lunes) a 6 (Sabado): "))

    if num in diaSemanas:
        
        if num % 2 == 0:
            
            print("A-300")
            
        else:
            
            print("A-315")
            
    else:
        
        print("Numero invalido. Por favor, ingrese un numero entre 1 y 6 .")
        
except ValueError:
    
    print("Entrada no valida. Por favor, ingrese un numero entero.")


print("================= Descuento y estacionamientos =================")

turnos: {
    "maniana",
    "mañana",
    "tarde",
    "noche"
}

materiasCursadas = int(input("Ingrese la cantidad de materias a las que desearia anotarse."))

cuota = 12000

try:
    turno = input("Ingrese el turno: mañana, tarde o noche. ")
    inputMinuscula = turno.lower()
    
    if inputMinuscula in turnos:
        if inputMinuscula == "tarde" and materiasCursadas == 3:
            descuento = 0.25
            cuotaDescuento = cuota * (1 - descuento)
        else:
            descuento = 0.05
            cuotaDescuento = cuota * (1 - descuento)
    else:
        print("El turno ingresado es incorrecto.")
except ValueError:
    print("Debe ingresar uno de los siguientes turnos: mañana, tarde o noche.")