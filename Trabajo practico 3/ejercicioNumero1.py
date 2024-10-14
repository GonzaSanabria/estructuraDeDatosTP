def palabraInvertida(palabra: str):
    if palabra.lower != palabra[::-1].lower:
        print("Es palindromo.")
    else:
        print("No es palindromo.")

prueba = palabraInvertida("neuquen")

# Otra manera de hacerlo

def palindromo(palabra: str): 
    palabra = palabra.lower() 
    longitud = len(palabra) # Con esto definimos la longitud de la palabra 

    for i in range(longitud // 2): # Con esto solo analizamos la mitad de la palabra
        if palabra[i] != palabra[longitud - i - 1]: # En esta parte se hacen las comparaciones
            # con palabra[i] analizamos la palabra normalmente y con palabra[longitud - i - 1] analizamos la palabra al revez. 
            print("No es palindromo.")
            return # Si las mitades son iguales de atras para adelante, esta condicional no retorna nada. 
        
    print("Es palindromo X2.")

pruebaFuncion = palindromo("neuquen")

