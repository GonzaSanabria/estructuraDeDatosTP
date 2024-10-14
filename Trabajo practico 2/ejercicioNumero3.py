def caja(montoPagar, dineroRecibido):
    if dineroRecibido >= montoPagar:
        vuelto = dineroRecibido - montoPagar
        print(f"El vuelto de la compra es: ${vuelto}")
        
        
        denominaciones = [1000, 500, 200, 100, 50, 20, 10, 5, 1] # Denominaciones disponibles
        
        # Desglose del vuelto
        for denominacion in denominaciones: #Recorre el array de las denominaciones disponibles
            cantidadBilletes = vuelto // denominacion  # Se realiza esta operacion con cada una de las denomicaciones. Tiene // para que devuelva un numero entero.
            if cantidadBilletes > 0: 
                print(f"{cantidadBilletes} billete(s)/moneda(s) de ${denominacion}") # En el caso de que la cantidad de billetes sea mayor a cero se imprime el siguiente mensaje
            vuelto %= denominacion  # Con esto se define la cantidad de dinero que nos queda por devolver
    else:
        print("El dinero es insuficiente.")


caja(1563, 2000)