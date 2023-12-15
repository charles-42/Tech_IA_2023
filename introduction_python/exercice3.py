#Exercice 3: 
#Reprenez votre programme en utilisant l'instruction break

print("Si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?")

resultat = input()

while True:
    if resultat == "tu es lourd":
        break
    elif resultat == "répète":
        resultat = input("Si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?")
    else:
        resultats = input("Mais non tu comprends Si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?")
print("le jeu est fini")
