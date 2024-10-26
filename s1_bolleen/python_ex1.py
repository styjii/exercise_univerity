
#coding:utf-8
def saisie_fonction_logique() :
    nombre_variables = int(input("N : "))
    fonction_logique = input("Entrez la fonction logique du tableau (utilisez 'and', 'or', 'not' pour les opérations logiques et variable : a,b,c...):\n ")
    return nombre_variables, fonction_logique

def verite(nombre_variables, fonction_logique) :
    header = "\t".join([chr(97 + i) for i in range(nombre_variables)])
    header += "\t" + "\t".join(["¬" + chr(97 + i) for i in range(nombre_variables)]) + "\tf(X)"
    print(header)
    form_canonique_1 = []
    form_canonique_2 = []
    for values in generate_truth_values(nombre_variables):
        row = "\t".join([str(int(value)) for value in values])
        negated_values = [not value for value in values]
        row += "\t" + "\t".join([str(int(negated_value)) for negated_value in negated_values])
        
        # Mapping des noms de variables aux valeurs de vérité
        variables = {chr(97 + i): value for i, value in enumerate(values)}
        
        # Évaluation de la fonction logique
        fX = eval(fonction_logique, {}, variables)
        row += "\t" + str(int(fX))
        print(row)
        
        if fX == 1:
            form_canonique_1.append(int(True))
        else:
            form_canonique_2.append(int(False))
    resform_canonique_1 = any(form_canonique_1)
    resform_canonique_2 = any(form_canonique_2)

    operator(nombre_variables)
    
    print(f"1er forme canonique :\n\t\t{form_canonique_1} = {resform_canonique_1}")

    print(f"2em forme canonique :\n\t\t{form_canonique_2} = {resform_canonique_2}")
def generate_truth_values(n) :
    from itertools import product
    return product([False, True], repeat=n)
def operator(nombre_variables) :
    if nombre_variables == 2 :
        print("ab\t\t¬ba")
        for a in [False, True] :
            for b in [False, True] :
                _a = not a
                _b = not b

                ab = a and b
                _ba = not b and a
                _ab = not a and b

                print(f"{int(ab)}\t\t{int(_ba)}")
    if nombre_variables == 3 :
        print("ab\t\t\t¬bc\t\t\ta¬c")
        for a in [False, True] :
            for b in [False, True] :
                for c in [False, True] :
                    _a = not a
                    _b = not b
                    _c = not c
                    
                    ab = a and b
                    _bc = not b and c
                    a_c = a and not c
                    
                    print(f"{int(ab)}\t\t\t{int(_bc)}\t\t\t{int(a_c)}")
nombre_variables, fonction_logique = saisie_fonction_logique()
verite(nombre_variables, fonction_logique)