from modulos.precios import * # Esto lo hice para probar lo que nos mostro la clase anterior, pa eso na mas

# Valor inicial de zapallo
zapallo = 1000

# Diccionario que simula un switch
opciones = {
    1: dolares,
    2: yenes,
    3: guaranies,
    4: pesos,
    5: otraMoneda
}

print(f"El valor del zapallo es de: ${zapallo}")
nombreComprador = input("\nIngrese el nombre del comprador: ")
nombreEmpresa = input("Ingrese el nombre de la empresa: ")

while True: 
    try:
        divisa = int(input("\nSeleccione la denominación con la que desea pagar: \n1. Dólares (5% de descuento) \n2. Yenes (15% de descuento) \n3. Guaraníes (20% de descuento) \n4. Pesos (10% de descuento) \n5. Otra moneda (aumento del 10%) \nOpción seleccionada: "))
        
        if divisa in opciones:  
            if divisa == 5:  # Si la opción seleccionada es "otra moneda"
                monedaPersonalizada = input("Ingrese el tipo de moneda: ")  # Solicita al usuario el tipo de moneda
                tipoMoneda = opciones[divisa](monedaPersonalizada)  # Llama a la función y pasa el tipo de moneda
            else:
                tipoMoneda = opciones[divisa]()
            break  
        else:
            default_case()
    
    except ValueError:
        print("\nPor favor, ingrese un número válido.")

# Imprimir el recibo
print("\n--- Recibo ---")
print(f"Nombre del comprador: {nombreComprador}")
print(f"Nombre de la empresa: {nombreEmpresa}")
print(f"Tipo de moneda: {tipoMoneda}")
print(f"Producto: Zapallo")
print(f"Precio total en pesos: ${zapallo:.2f}")
