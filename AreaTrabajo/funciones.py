def calculadora(a,b,calculo = "suma"):
    
    # Validación
    operaciones = ["suma", "resta", "multiplicación", "división"]
    if calculo not in operaciones:
        print("Por favor, elegir una operación válida: suma, resta, multiplicación, división")
        return
    
    # Cálculo
    print("Su resultado es: ")
    if calculo == "suma":
        
        return a + b
    elif calculo == "resta":
        return a-b
    elif calculo == "multiplicación":
        return a*b
    elif calculo == "división":
        return a/b