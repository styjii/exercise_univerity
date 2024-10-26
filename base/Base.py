def enterBase(choix) :
    user = ""
    if choix == '1' :
        while not (user.isdigit() or "." in user) :
            user = input("Enter a real number base 10 : ")
            if not (user.isdigit() or "." in user) :
                print("Only numbers are allowed !")
    
        return user
    else :
        while not user.isdigit() :
            user = input("Enter a real number base 16 or 2 : ").upper()
            characters = ['A', 'B', 'C', 'D', 'E', 'F']
            c = ""
            for character in user :
                if character in characters or character.isdigit() or character == ".":
                    continue
                c = character
            if c == "" :
                break
            else :
                print("Only basic characters 16 are allowed !")
                continue
        
        return user

def baseChoice(user_choice : str, choice : list) :
    while user_choice not in choice :
        user_choice = input(f"What do you want? {choice[0]} or {choice[1]} : ")
        if user_choice not in choice :
            print("Please write your choice well !")
            continue
        base = 2 if user_choice == choice[0] else 16

    return {"choice": user_choice, "base": base}

def calcBase(liste : list, base : int, result : float) :
    if "." not in liste :
        i = len(liste) - 1
        for element in liste :
            result += element * pow(base, i)
            i -= 1
    else :
        liste.remove(".")
        i = 1
        for element in liste :
            result += element / pow(base, i)
            i += 1

    return result

def setToNumber(element : str) :
    character = ['A', 'B', 'C', 'D', 'E', 'F']
    number_of_each_character = [10, 11, 12, 13, 14, 15]
    i = 0
    while i < len(character) :
        if element == character[i] :
            return number_of_each_character[i]
        i += 1
        
def setToCharacter(element : str) :
    character = ['A', 'B', 'C', 'D', 'E', 'F']
    number_of_each_character = [10, 11, 12, 13, 14, 15]
    result : str = ""
    i = 0
    for i in range(len(element) - 1) :
        elements = "".join([element[i], element[i + 1]])
        for j in range(len(character)) :
            if elements == str(number_of_each_character[j]) :
                elements = character[j]
        if len(element) % 2 == 0 :
            if i == 0 and elements not in character :
                elements = [e for e in elements]
                elements.remove(elements[1])
                elements = "".join(elements)
            elif i != 0 and elements not in character :
                elements = [e for e in elements]
                elements.remove(elements[0])
                elements = "".join(elements)
            result += elements
        else :
            if i == 0 and elements not in character :
                elements = [e for e in elements]
                elements.remove(elements[1])
                elements = "".join(elements)
            elif i != 0 and i != len(element) - 1 and i % 2 == 0 and elements not in character :
                elements = ""
            elif i != 0 and elements not in character :
                elements = [e for e in elements]
                elements.remove(elements[0])
                elements = "".join(elements)
            result += elements
        
    return result
