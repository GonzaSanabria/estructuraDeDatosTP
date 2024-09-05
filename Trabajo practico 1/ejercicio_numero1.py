import re

# Solicita al usuario su nombre
nombre = input("Ingrese su nombre: ")

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


valorCuatrimestre = montoMatricula + 1000


arancelPython = 12000


costoMensual = arancelPython / 4


descuento = 0.15
pago_efectivo = True  # Asumimos que el pago es en efectivo

if pago_efectivo:
    cuotaDescuento = valorCuatrimestre * (1 - descuento) # En este caso seria 1 - 0.15, que daria como resultado 0.85
else:
    cuotaDescuento = valorCuatrimestre

print("\nDatos del estudiante:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Fecha de nacimiento: {fecha_nacimiento}")
print(f"Tiene título secundario: {tituloSecundario}")
print(f"Monto de la matrícula: ${montoMatricula}")
print(f"Valor del cuatrimestre (incluyendo matrícula): ${valorCuatrimestre}")
print(f"Costo mensual de la materia 'Python I': ${costoMensual}")
print(f"Cuota con descuento si paga en efectivo: ${cuotaDescuento}")


