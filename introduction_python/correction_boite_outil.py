
# **`Exercice`**
# - Créer des classes: boite à outils, marteau, tournevis, clou, visse 
# - Instanciez une boîte à outils, un tournevis, et un marteau.
# - Placez le marteau et le tournevis dans la boîte à outils.
# - Instanciez une visse, et serrez-la avec le tournevis. Affichez la vis avant et après avoir été serrée.
# - Instanciez un clou, puis enfoncez-le avec le marteau. Affichez le clou avant et après avoir été enfoncé.
# - Une boite à outil possède 5 emplacements. (classe attributs)
# - Régulièrement le constructeur des boites à outils sort un nouveau modèle qui permet d'etendre la capacité des boites à outils de 1 emplacement.

# Pour chaque classe vous devez définir les attributs et les méthodes qui permettront d'éxecuter et de rapporter dans le terminal ces actions et ces états.

class Boite_a_outils:

    nombre_emplacements = 5

    def __init__(self):
        self.liste_outils = []

    def ajouter_outil(self,outil):
        if  isinstance(outil,Marteau) or isinstance(outil,Tournevis) :
            
            if len(self.liste_outils) < self.nombre_emplacements:  
                self.liste_outils.append(outil)
            else:
                print("il n'y a plus de place dans la boite à outil")
        else:
            print("vous essayez d'ajouter autre chose qu'un outil")

    @classmethod
    def mise_a_jour_des_boites(cls):
        cls.nombre_emplacements +=1

class Marteau:

    def __init__(self,couleur="rouge",marque="fisher",taille="petit",poids=2):
        self.couleur = couleur
        self.marque = marque
        self.taille = taille
        self.poids = poids

    def enfoncer_un_clou(self,clou):
        if isinstance(clou,Clou):
            clou.est_cloue = True
        else:
            print("on ne peut clouer que des clous")

class Tournevis:
    def __init__(self,forme="plat",taille="petit",aimente=False):
        self.forme = forme
        self.taille = taille
        self.aimente = aimente
    
    def visser(self,visse):
        if isinstance(visse,Visse):
            if self.forme == visse.forme:
                visse.est_visse = True
            else:
                print("la visse et le tournevis ne sont pas compatibles")
        else:
            print("On ne peut visser que des visse")

class Visse:

    def __init__(self,forme="plat",est_visse = False,type = "a bois"):
        self.forme = forme
        self.est_visse = est_visse
        self.type = type

class Clou:
    def __init__(self,est_cloue=False):
        self.est_cloue = est_cloue




marteau_1 = Marteau("bleu","castorama","grand",8)
marteau_2 = Marteau() 
marteau_3 = Marteau(marque="castorama")
tournevis_1 = Tournevis("cruciforme","grand",True)
tournevis_2 = Tournevis()
tournevis_3 = Tournevis("cruciforme")

# print(f"{marteau_3=}", marteau_3.__dict__)

boite_a_outils_de_paul = Boite_a_outils()
boite_a_outils_de_marc = Boite_a_outils()


boite_a_outils_de_marc.ajouter_outil(marteau_1)
boite_a_outils_de_marc.ajouter_outil(marteau_2)
boite_a_outils_de_marc.ajouter_outil(marteau_3)
boite_a_outils_de_marc.ajouter_outil(tournevis_1)
boite_a_outils_de_marc.ajouter_outil(tournevis_2)
boite_a_outils_de_marc.ajouter_outil(tournevis_3)

boite_a_outils_de_marc.mise_a_jour_des_boites()

boite_a_outils_de_marc.ajouter_outil(tournevis_3)

print(len(boite_a_outils_de_marc.liste_outils))

# print(boite_a_outils_de_marc.liste_outils)

visse = Visse()
clou = Clou()

# tournevis_3.visser(clou)
# tournevis_3.visser(visse)
# tournevis_2.visser(visse)
# print(visse.est_visse)


# print(clou.est_cloue)
# marteau_1.enfoncer_un_clou(clou)
# print(clou.est_cloue)