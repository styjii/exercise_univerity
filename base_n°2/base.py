class Base:
    def __init__(self, number : str) :
        self.number = number
    
    def __repr__(self) :
        return f"Base({self.number})"
    
    def _set_to_number(element) :
        c = ['A', 'B', 'C', 'D', 'E', 'F']
        n = [10, 11, 12, 13, 14, 15]
        n_list = []
        
        
        for i in range(len(c)) :
            if element == c[i] :
                n_list.append(n[i])
            else :
                n_list.append(element)
                 
        return n_list
    
    def _check(self) :
        pass
    
    def _conversion(self) :
        return [element for element in str(self.number)]
        
    def base_10_base_2(self) :
        rest = []
        while self.number != 0 :
            rest.append(self.number % 2)
            self.number = self.number // 2
        
        return [element for element in reversed(rest)]
    



if __name__ == "__main__" :
    base_10 = Base("4A")
    print(base_10._set_to_number())