list_course = ['tomatoes', 'pasta', 'tuna', 'poulet']

def menu(option):
    option = option1 | option2 | option3 | option4 |option5
 
    if option1:
        input(print("Ajoutez un élément"))
        return list_course.insert('')
        print(list_course)
 
    if option2:
        input(print('Retirer un élément de la liste'))
        return list_course.remove('')
        print(list_course)
 
    if option3:
        input('Afficher la liste')
        return list_course
        print(list_course)
        
    if option4:
        input('Vider la liste')
        return list_course.clear()
        print(list_course)
  
    if option5:
        input('Quitter')
        return



    

    

