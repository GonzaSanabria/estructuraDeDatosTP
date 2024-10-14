def dolares():
    global zapallo  
    zapallo *= 0.95 
    print(f"Nuevo precio de zapallo: ${zapallo:.2f}")
    return "Dólares"  # Devuelve el tipo de moneda

def yenes():
    global zapallo
    zapallo *= 0.85  # Aplicar un 15% de descuento
    print(f"Nuevo precio de zapallo: ${zapallo:.2f}")
    return "Yenes"  # Devuelve el tipo de moneda

def guaranies():
    global zapallo
    zapallo *= 0.80  # Aplicar un 20% de descuento
    print(f"Nuevo precio de zapallo: ${zapallo:.2f}")
    return "Guaraníes"  # Devuelve el tipo de moneda

def pesos():
    global zapallo
    zapallo *= 0.90  # Aplicar un 10% de descuento
    print(f"Nuevo precio de zapallo: ${zapallo:.2f}")
    return "Pesos"  # Devuelve el tipo de moneda

def otraMoneda():
    global zapallo
    zapallo *= 1.10  # Aumentar un 10%
    print(f"Nuevo precio de zapallo: ${zapallo:.2f}")
    return "Otra moneda"  # Devuelve un mensaje o tipo de moneda

def default_case():
    print("Opción no válida. No se aplicará ningún cambio.")