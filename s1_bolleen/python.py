#coding:utf-8

def truth_table():
    print("Table de vérité pour (A and B) or (not B and C) or (A and not C) :")
    print("A\tB\tC\t¬A\t¬B\t¬C\t(A and B)\t(not B and C)\t(A and not C)\tOutput")
    canonical_form_1 = []
    canonical_form_2 = []
    for A in [False, True]:
        for B in [False, True]:
            for C in [False, True]:
                not_A = not A
                not_B = not B
                not_C = not C
                output = (A and B) or (not B and C) or (A and not C)  # Fonction logique
                print(f"{int(A)}\t{int(B)}\t{int(C)}\t{int(not_A)}\t{int(not_B)}\t{int(not_C)}\t{int(A and B)}\t\t{int(not B and C)}\t\t{int(A and not C)}\t\t{int(output)}")
                if output == 1:
                    canonical_form_1.append(f"(A and B and {not_C})")
                    canonical_form_2.append(f"({not_A} and {B} and {C})")
    print("\nPremière forme canonique :", " or ".join(canonical_form_1))
    print("Deuxième forme canonique :", " or ".join(canonical_form_2))

truth_table()