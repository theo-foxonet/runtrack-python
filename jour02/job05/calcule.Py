def calcule(num1 , operator , num2):
    if operator == "+":
        resultat = num1 + num2
        print(resultat)
    elif operator == "-":
        resultat = num1 - num2
        print(resultat)
    elif operator == "*":
        resultat = num1 * num2
        print(resultat)
    elif operator == "/":
        resultat = num1 / num2
        print(resultat)
    elif operator == "%":
        resultat = num1 % num2
        print(resultat)
    else:
        print("erreur")


calcule(15,"+",78)