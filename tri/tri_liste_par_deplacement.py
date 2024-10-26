def trie(tab) :
    for _ in range(len(tab)) :
        for i in range(len(tab)) :
            if i > 0 and tab[i-1] > tab[i] :
                tab[i-1], tab[i] = tab[i], tab[i-1]
            elif i < len(tab) - 1 and i >= 0 :
                tab[i], tab[i+1] = tab[i+1], tab[i]
    
    return tab

T = [5, 7, 2, 1, 3, 6]
print(trie(T))
print(T)
