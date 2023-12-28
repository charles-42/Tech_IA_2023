# **'Exercice'** 

# Evolution
# - Creer une classe Molusque, qui possède les attributs une taille et un nombre de nageoir ainsi que les méthodes 
#     - se déplacer (il se déplace en nageant)
#     - manger (il mange des algue)
#     - respirer (par des branchies)
# - Créer ensuite une classe poisson qui hérite de molusque. Contrairement aux molusques les poissons mangent de phytoplanctons
# - Créer ensuite une classe singe qui hérite de poisson qui n'a pas de nageoir mais un nombre de pattes égal à 4, qui se déplace en marchant, qui mange des insectes et qui respire avec ses poumons
# - Enfin créer une classe homme qui hérite du singe, qui a deux pattes qui mange de tout et qui a une méthode pour conduire une voiture.


class Molusque:
    def __init__(self,taille,nb_de_nageoirs):
        self.taille = taille
        self.nb_de_nageoirs = nb_de_nageoirs

    def se_deplacer(self):
        print("il se déplace en nageant")

    def manger(self):
        print("il mange des algues")

    def respirer(self):
        print("il respire à l'aide de ses branchies")

class Poisson(Molusque):
   
    def manger(self):
        print("il mange du phytoplacton")

class Singe(Poisson):
    def __init__(self,taille,nb_de_pattes):
        self.taille = taille
        self.nb_de_pattes = nb_de_pattes
    
    def se_deplacer(self):
        print("il se déplace en marchant")

    def manger(self):
        print("il mange des insectes")

    def respirer(self):
        print("il respire à l'aide de ses poumons")

class Homme(Singe):   
    def manger(self):
        print ("il mange de tout")

    def conduire_une_voiture(self):
        print("il conduit des voitures")


un_molusque = Molusque(10,0)
print("le molusque")
print(un_molusque.__dict__)
un_molusque.se_deplacer()
un_molusque.manger()
un_molusque.respirer()

un_poisson = Poisson(15,2)
print("le poisson")
print(un_poisson.__dict__)
un_poisson.se_deplacer()
un_poisson.manger()
un_poisson.respirer()

un_singe = Singe(15,4)
print("le singe")
print(un_singe.__dict__)
un_singe.se_deplacer()
un_singe.manger()
un_singe.respirer()

un_homme = Homme(180,2)
print("l'homme'")
print(un_homme.__dict__)
un_homme.se_deplacer()
un_homme.manger()
un_homme.respirer()
un_homme.conduire_une_voiture()

print(isinstance(un_homme,Molusque))