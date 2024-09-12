diaSemanas = {
    1: "Lunes",
    2: "Martes",
    3: "Miercoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sabado"
}

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