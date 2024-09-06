import re

# Solicita al usuario su nombre
nombre = input("Ingrese su nombre completo: ")

# Solicita al usuario su edad
edad = input("Ingrese su edad: ")

# Verifica el formato de la fecha de nacimiento con una expresión regular
# 're' indica que es una expresion regular, mientras que .match es un metodo que indica que el patron que se ponga dentro re.match() debe coincidir con cierto parametros
# En pocas palabras, es una manera de validar que la edad se escriba de una determinada manera. 
#'r' indica una raw string; '^' indica que la busqueda empiece desde el principio del texto; '\d' significa que se debe ingresar un numero
# '{2}' indica que se deben ingresar dos numeros; ' / ' es simplemente la barra que separa las fechas; '$' indica donde termina nuestra busqueda.
while True:
    fecha_nacimiento = input("Ingrese fecha de nacimiento (dd/mm/aa): ")
    if re.match(r'^\d{2}/\d{2}/\d{2}$', fecha_nacimiento): 
        break
    else:
        print("Formato incorrecto. Por favor ingrese la fecha en el formato dd/mm/aa.")

montoMatricula = float(input("Ingrese monto de la matricula: "))

# Variable que indica si el estudiante tiene título secundario
tituloSecundario = True

cuotaMensual = montoMatricula + 1000

pythonUno = 12000

pythonUnoMensual = pythonUno / 4

pagoEfectivo = True

if pagoEfectivo == True:
    pythonValorFinal = pythonUnoMensual * (1 - 0.85)
else:
    pythonValorFinal = pythonUnoMensual

print("========================================================")
print("======== Universidad de Python - Inscripciones =========")
print("========================================================")
print("\nDATOS DE INGRESO:")
print(f"Nombre completo: {nombre}")
print(f"Fecha de nacimiento y edad: {fecha_nacimiento} {edad}")
print(f"Posee titulo?: {tituloSecundario}")
print(f"Matricula: ${montoMatricula}")
print(f"Cuota Mensual: ${cuotaMensual}")
print(f"Arancel mensual materia 'Python I': ${pythonUnoMensual}")
print(f"Arancel mensual materia 'Python I' con descuento: $2550")