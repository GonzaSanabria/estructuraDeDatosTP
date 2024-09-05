import re

nombre = input("Ingrese su nombre: ")

edad = input("Ingrese su edad: ")

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

tituloSecundario = True


valorCuatrimestre = montoMatricula / 4



