print("Si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?")
resultat = input()
while True:
    if resultat == "tu es lourd":
        break
    elif resultat == "repète":
        resultat = input("Si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?\n")
    else:
        resultat = input("Mais non tu comprends pas, si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?\n")
