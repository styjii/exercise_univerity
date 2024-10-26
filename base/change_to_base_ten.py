from pathlib import Path
import Base


# Enter base 10 in this parameter
def ChangeBase2Or16(number : str) :
    choice = ["base2", "base16"]
    user_choice = ""
    user = Base.baseChoice(user_choice, choice)
    base : int = user.get("base")
    user_choice = user.get("choice")

    all_element : list = [int(element) if element.isdigit() else element for element in number]
    float_number : list = all_element.copy()

    int_number = []
    # Adding integer in int number
    for element in all_element :
        if element != "." :
            int_number.append(element)
            float_number.remove(element)
        else :
            break
    
    all_reste = calcRest(int("".join([str(element) for element in int_number])), base)
    all_reste = reverse(all_reste)
    
    if len(float_number) != 0 :
        all_reste.append(".")

        float_number.insert(0, "0")
    
        # Calculate the decimal number (loading...)
        float_rest = "".join([str(element) for element in float_number])
        if base == 2 :
            for i in range(3) :
                if float_rest == ["0.25", "0.5", "0.75"][i] :
                    all_reste.append(["01", "1", "11"][i])
        else :
            result = 0
            i = 1
            while True :
                result += 1 / pow(base, i)
                all_reste.append(1)
                if str(result) == float_rest :
                    break
        # conv_base = changeToBaseTen(float_rest)
        # for i in range(1000000000000) :
        #     n = "".join(["0.", str(i)])
        #     if conv_base == n :
        #         pass
    all_reste = ''.join([str(element) for element in all_reste])
    # Convert all number greater than 10 to letter in base 16
    if base == 16 :
        all_reste = Base.setToCharacter(all_reste)
    
    with open(file, "a") as f :
        f.write(f"base10 : {number} = {user_choice} : {all_reste}\n")

    return f"{user_choice} : {all_reste}"
# Enter base 16 or base 2 in this parameter
def changeToBaseTen(number : str) :
    choice = ["base2", "base16"]
    user_choice = ""
    user = Base.baseChoice(user_choice, choice)
    base = user.get("base")
    user_choice = user.get("choice")

    elements = [element for element in number if not element.isdigit()]
    if (base == 2 and len(elements) > 1) or (base == 2 and not (number.isdigit() or "." in elements)) :
        return "Impossible to solve because your number contains characters !"
    else :
        base_ten = 0
        if "." in [element for element in number] :
            all_element = [int(element) if element.isdigit() else element for element in number]
            all_element = [Base.setToNumber(element) if element in ['A', 'B', 'C', 'D', 'E', 'F'] else element for element in all_element]

            float_number = all_element.copy()
            int_number = []
            base_ten : float = 0

            for element in all_element :
                if element != "." :
                    int_number.append(element)
                    float_number.remove(element)
                else :
                    break
            
            base_ten = Base.calcBase(int_number, base, base_ten)
            base_ten = Base.calcBase(float_number, base, base_ten)
        else :
            all_element = [int(element) if element.isdigit() else Base.setToNumber(element) for element in number]
            base_ten = Base.calcBase(all_element, base, base_ten)

    with open(file, "a") as f :
        f.write(f"{user_choice} : {number} = base10 : {base_ten}\n")

    return f"base 10 : {base_ten}"

def calcRest(number : int, base : int) :
    liste = []
    while number != 0 :
        reste = number % base
        liste.append(reste)
        number = number // base
    return liste

def reverse(liste) :
    # reversed the list
    liste_reverse = []
    i = len(liste) - 1
    while i >= 0 :
        liste_reverse.append(liste[i])
        i -= 1
    return liste_reverse

file = Path.cwd() / "base.txt"
content = ""
if file.exists :
    with open(file, "r") as f :
        content = f.read()
else :
    file.touch()
    

MENU = "MENU : \n1 - Enter a base10 -> return base2 or base16 \n2 - Enter a base2 or base16 -> return base10 \n3 - View content \n4 - delete all content \n👉 "
CHOICE = ['1', '2', '3', '4']

USER_CHOICE = ""
while USER_CHOICE not in CHOICE :
    USER_CHOICE = input(MENU)
    if USER_CHOICE not in CHOICE :
        print("Your choice is invalid !")

if USER_CHOICE in ['1', '2'] :
    with open(file, "a") as f :
        f.write(f"\n{'-'*10} DEBUT {'-'*10}\n")
    while True :
        user = Base.enterBase(USER_CHOICE)

        if USER_CHOICE == '1' :
            result = ChangeBase2Or16(user)
        else :
            result = changeToBaseTen(user)
        print(result)

        continue_or_exit = ""
        while continue_or_exit not in ['1', '2'] :
            continue_or_exit = input("What do you want ? \n1 - Continue \n2 - Exit \n👉 ")
            if continue_or_exit not in ['1', '2'] :
                print("Your choice is invalid !")

        if continue_or_exit == '2' :
            break
elif USER_CHOICE == '3' and content == "" :
    print("No content.")
elif USER_CHOICE == '4' and content != "" :
    with open(file, "w") as f :
        f.write("")
        print("All content has been deleted !")
elif USER_CHOICE == '4' and content == "" :
    print("impossible to delete content because file is empty !")
else :
    print(content)