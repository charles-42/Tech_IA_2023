list_course = ['tomatoes', 'pasta', 'tuna', 'poulet']

def menu(option):
    
    input(print(f"Quelle est votre {choix}?"))
    choix = option1 | option2 | option3 | option4 |option5
    print(choix)
     
    if option1:
        input(print("Ajoutez un élément"))
        return list_course.insert('')
        print(list_course)
 
    if option2:
        input(print('Retirer un élément de la liste'))
        return list_course.remove('')
        print(list_course)
 
    if option3:
        input('Afficher la liste y/n:')
        if input == 'y':
            return list_course
        else:
            return
        print(list_course)
        
    if option4:
        input('Vider la liste y/n:')
        if input == 'y':
            return list_course.clear()
           
        else:
            return
        print(list_course)
  
    if option5:
        input('Quitter: y/n')
        if input == 'y':
            return 
           
        else:
            return menu
    
    

# METHOD PROPOSER PAR Seng
# shopping_list = list()

# # Functions
# def add_item():
#     item = input("Saisir un produit : ")
#     shopping_list.append(item)
    
# def delete_item():
#     item = input("Quel produit supprimer ? : ")
#     shopping_list.remove(item)

# def show_shopping_list():
#     if shopping_list:
#         print("\nProduits dans votre liste")
#         for item in shopping_list:
#             print(f"- {item}")
#     else:
#         print("\nLa liste de courses est vide")
    
# def empty_shopping_list():
#     shopping_list.clear()
    
# # Main loop
# while True:
    
#     print("\nChoisissez parmi les options suivantes : ")
#     print("1: Ajouter un élément à la liste")
#     print("2: Retirer une élément de la liste")
#     print("3: Afficher la liste")
#     print("4: Vider la liste")
#     print("5: Quitter")

#     choice = input("\nQuel est votre choix ? : ")

#     if choice == "1":
#         add_item()
#     elif choice == "2":
#         delete_item()
#     elif choice == "3":
#         show_shopping_list()
#     elif choice == "4":
#         empty_shopping_list()
#     else:
#         print("À bientôt\n")
#         break
        
# print("Fin du programme")
    

    


    