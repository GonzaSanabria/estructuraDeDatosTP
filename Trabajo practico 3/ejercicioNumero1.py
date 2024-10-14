def palabraInvertida(palabra: str):
    if palabra.lower != palabra[::-1].lower:
        print("Es palindromo.")
    else:
        print("No es palindromo.")

prueba = palabraInvertida("neuquen")



