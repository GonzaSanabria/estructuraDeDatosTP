# Esto valida si se ingresa numero validos
while True:
    try:
        nota1 = float(input("Ingrese la primer nota del alumno (0-10): "))
        if nota1 >= 0 and nota1 <= 10:  
            # En el caso de que la primera nota se ingrese correctamente, se procede a pedir la segunda nota. 
            # De lo contrario, se vuelve a pedir que se ingrese un numero nuevamente.
            # El bucle de abajo cumple con la misma funcion que el de arriba. 
            while True:
                try:
                    nota2 = float(input("Ingrese la segunda nota del alumno (0-10)"))
                    if nota2 >= 0 and nota2 <= 10:
                        break
                    else: 
                        print("Por favor, ingrese una nota entre 0 y 10.")
                except ValueError: 
                    print("Entrada no valida. Por favor, ingrese un numero")
            break
        else:
            print("Por favor, ingrese una nota entre 0 y 10.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un numero.")

# Con esta operacion sabemos el promedio de las notas.
prom = (nota1 + nota2) / 2

print(f"El promedio de la notas es: {prom}")
# Condicional que define si aprobo o no el examen.
if nota2 >= 7:
    print("Aprobo el segundo examen.")
else:
    print("Desaprobo el segundo examen.")

# Aca se define su mejoro o empeoro su desempenio.
if nota2 > nota1:
    print("Mejoro su desempenio.")
elif nota1 == nota2:
    print("Matuvo la nota.")
else:
    print("Empeoro su desempenio.")

# Define si promociona la materia, si debe rendir final o si debe recursar.
if prom >= 7:
    print("Promociono la materia.")
elif prom >= 4 and prom < 7:
    print("Debe rendir final.")
else:
    print("Debe recursar.")