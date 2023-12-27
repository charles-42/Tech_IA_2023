class Voiture:
    def __init__(self,marque,prix):
        """Construction de l'instance de voiture

        Args:
            marque (string): la marque de la voiture
            prix (float): le prix de vente TTC de la voiture
        """
        self.marque = marque
        self.prix = prix
        self.vitesse_kilometre_heure = 0
    
    def calcule_prix(self,pourcentage_reduction):
        """Calcule le prix après l'application d'une réduction

        Args:
            pourcentage_reduction (float): valeur de la réduction entre 0 et 1

        Returns:
            integer: prix TTC après réduction
        """
        
        prix_apres_reduction = (1-pourcentage_reduction)*self.prix
        return prix_apres_reduction

    def accelerer(self,kilometre_acceleres):
        """ Fait accélérer la voiture

        Args:
            kilometre_acceleres (integer): vitesse d'accélération en points
        """
        self.vitesse_kilometre_heure = self.vitesse_kilometre_heure + kilometre_acceleres
        print(f"La {self.marque} roule à présent à {self.vitesse_kilometre_heure} kilomètres heure")

    def freiner(self,kilometre_deceleres):
        """Fait freiner la voiture

        Args:
            kilometre_deceleres (integer): vitesse de décélération en points
        """
        self.vitesse_kilometre_heure = max(self.vitesse_kilometre_heure - kilometre_deceleres, 0)

        print(f"La {self.marque} roule à présent à {self.vitesse_kilometre_heure} kilomètres heure")

class Vendeur:
    def __init__(self, nom, compteur_vente=0):
        """Construction de l'instance de voiture

        Args:
            nom (string): le nom du vendeur
        """
        self.nom = nom
        self.compteur_vente = compteur_vente

    def vente(self):
        self.compteur_vente += 1
    

class Magasin:

    def __init__(self,nom):
        self.nom = nom
        self.inventaire = []
        self.liste_de_vendeurs = []

    def nombre_voiture_par_marque(self,marque_recherchee):
        
        nombre_voiture_de_la_marque_dans_inventaire = 0

        for voiture in self.inventaire:
            if voiture.marque ==marque_recherchee:
                nombre_voiture_de_la_marque_dans_inventaire += 1

        return nombre_voiture_de_la_marque_dans_inventaire


    def ajouter_voiture_inventaire(self,voiture):

        # On vérifie que l'objet voiture est bien une instance de la classe voiture
        if isinstance(voiture,Voiture):
            self.inventaire.append(voiture)
        else:
            print("On ne peut ajouter à l'inventaire que des voitures")

    def retirer_voiture_inventaire(self,voiture):

        # On vérifie que l'objet voiture est bien une instance de la classe voiture
        if isinstance(voiture,Voiture):
            if voiture in self.inventaire:
                self.inventaire.remove(voiture) 
            else:
                 print("Cette voiture ne se trouve pas dans l'inventaire")
        else:
            print("On ne peut retirer que des voitures de l'inventaire")

    def ajouter_vendeur(self,vendeur):

        # On vérifie que l'objet voiture est bien une instance de la classe voiture
        if isinstance(vendeur,Vendeur):
            self.liste_de_vendeurs.append(vendeur)
        else:
            print("On ne peut ajouter que des vendeurs à la liste de vendeur")

    def retirer_vendeur(self,vendeur):

        if isinstance(vendeur,Vendeur):
            if vendeur in self.inventaire:
                self.liste_de_vendeurs.remove(vendeur) 
            else:
                 print("Ce vendeur n'est pas salarié")
        else:
            print("On ne peut retirer que des vendeurs de la liste de vendeur")
      
class Client:

    def __init__(self,nom, email):
        self.nom = nom
        self.email = email


class Vente:

    def __init__(self,magasin,voiture,client,vendeur):
        
        if isinstance(magasin,Magasin):
            self.magasin = magasin
        else:
            print("Le magasin doit appartenir à la classe magasin")
            return "error"
        
        if isinstance(voiture,Voiture) and voiture in magasin.inventaire:
            self.voiture = voiture
        else:  
            print("La voiture n'est pas une voiture ou elle n'est pas en stock")
            return "error"
        
        if isinstance(client,Client) :
            self.client = client
        else:  
            print("La client doit être de type client")
            return "error"
        
        if isinstance(vendeur,Vendeur) and vendeur in magasin.liste_de_vendeurs:
            self.vendeur = vendeur
        else:  
            print("Le vendeur n'est pas un vendeur ou il ne travaille pas dans ce magasin")
            return "error"
        
        # retirer la voiture de l'inventaire
        magasin.retirer_voiture_inventaire(voiture)

        # ajoute une vente au compteur du vendeur
        vendeur.vente()

    def imprimer_pdf(self,reduction):
        print(f"{self.magasin.nom} \n vendeur : {self.vendeur.nom} \n Client : {self.client.nom} \n Voiture vendu : {self.voiture.marque} ,\n reduction = {reduction} \n prix = {self.voiture.calcule_prix(reduction)}")

toyota_1 = Voiture("toyota",20000.0)
toyota_2 = Voiture("toyota",15000.0)
toyota_3 = Voiture("toyota",10000.0)
toyota_4 = Voiture("toyota",5000.0)
toyota_5 = Voiture("toyota",500.0)
ford_1 = Voiture("ford",20000.0)
ford_2 = Voiture("ford",15000.0)
ford_3 = Voiture("ford",10000.0)
ford_4 = Voiture("ford",5000.0)
jimmy_concessionnaire = Magasin("Jimmy Concessionnaire")

for voit in [toyota_1,toyota_2,toyota_3,toyota_4,toyota_5,ford_1,ford_2,ford_3,ford_4]:
    jimmy_concessionnaire.ajouter_voiture_inventaire(voit)

toyota_6 = Voiture("toyota",50.0)

henri = Vendeur("henri")
paul = Vendeur("paul")

jimmy_concessionnaire.ajouter_vendeur(paul)

denis = Client("denis","denis@gmail.com")

ma_vente = Vente(jimmy_concessionnaire,toyota_5,denis,paul)

ma_vente.imprimer_pdf(0.2)
