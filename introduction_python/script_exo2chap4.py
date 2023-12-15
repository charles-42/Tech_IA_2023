""" print("Si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?")
reponse = input()
while reponse == "repète":
    print("Si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?")
    reponse = input()
else:
    while reponse != "tu es lourd":
        print("Mais non tu comprends pas, si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste ")
        reponse = input()
 """

#correction
print("Si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?")
resultat = input()
while resultat != "tu es lourd":
    if resultat == "repète":
        resultat = input("Si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?\n")
    else:
        resultat = input("Mais non tu comprends pas, si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?\n")