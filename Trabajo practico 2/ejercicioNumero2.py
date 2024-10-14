def fechaValida(num1:int, num2:int, num3:int)->bool:
    dias = list(range(1, 31))
    meses = list(range(1, 13))
    
    if num1 in dias and num2 in meses and num3 <= 2024:
        print(True)
    else:
        print(False)
    

fechaValida(20, 3, 2000)

