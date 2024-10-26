class Base :
    def __init__(self, number : str) -> None:
        self.number = number.upper()

    def __str__(self) -> str:
        return f"Base({self.number})"
    
    def __repr__(self) -> str:
        return f"Base({self.number})"

    def _check(self):
        """check input

        Raises:
            ValueError: empty value
            ValueError: invalid value
        """
        characters = ['A', 'B', 'C', 'D', 'E', 'F']
        if not self.number:
            raise ValueError("Please enter an values !")
        
        for e in self.number:
            if not (e.isdigit() or e in characters):
                raise ValueError("Please check your input !")
    
    def _check_number(self):
        """check number

        Raises:
            ValueError: number only
        """
        if not self.number.isdigit():
            raise ValueError("Please enter a number !")

    def _check_base_two(self):
        """check value

        Raises:
            ValueError: invalid value
            ValueError: invalid value
        """
        if not self.number.isdigit():
            raise ValueError("Please check your input !")
        
        for e in self.number:
            if e not in ['0', '1']:
                raise ValueError("Please check your input !")

    def _reverse(self, List:list) -> list:
        """reversed list

        Args:
            l (list[int]): number list

        Returns:
            list[int]: reversed list
        """
        n = len(List) - 1
        list_reverse = []
        for i in range(n, -1, -1):
            list_reverse.append(List[i])
        return list_reverse

    def _set_to_number(self, e:str) -> int:
        """convert character to number

        Args:
            e (str): character to convert

        Returns:
            int: number for the character
        """
        characters = ['A', 'B', 'C', 'D', 'E', 'F']
        numbers = [10, 11, 12, 13, 14, 15]
        n = len(characters)
        
        for i in range(n):
            if e == characters[i]:
                return numbers[i]
        return -1

    def _set_to_character(self, e:int) -> str:
        """convert to character

        Args:
            e (int): number to convert

        Returns:
            str: character for the number
        """
        characters = ['A', 'B', 'C', 'D', 'E', 'F']
        numbers = [10, 11, 12, 13, 14, 15]
        n = len(characters)
        
        for i in range(n):
            if e == numbers[i]:
                return characters[i]
        return str(e)


    def base_ten_to_base_two(self) -> str:
        """convert base ten to base two

        Returns:
            str: base two
        """
        self._check_number()
        q = int(self.number)
        base_two = []
        while q != 0:
            r = q % 2
            q = q // 2
            base_two.append(r)
        return "".join([str(e) for e in self._reverse(base_two)])

    def base_two_to_base_ten(self) -> str:
        """convert base two to base ten

        Returns:
            str: base ten
        """
        self._check_base_two()
        n = len(self.number)
        base_ten = 0
        for i in range(n):
            base_ten += int(self.number[i]) * pow(2, n-1)
            n -= 1
        return str(base_ten)

    def base_ten_to_base_sixteen(self) -> str:
        """convert base ten to base sixteen

        Returns:
            str: base sixteen
        """
        self._check_number()
        base_sixteen = []
        q = int(self.number)
        while q != 0:
            r = q % 16
            q = q // 16
            base_sixteen.append(r)
        return "".join([self._set_to_character(e) for e in self._reverse(base_sixteen)])

    def base_sixteen_to_base_ten(self) -> str:
        """convert base sixteen to base ten

        Returns:
            str: base ten
        """
        self._check()
        n, base_ten = len(self.number), 0
        for i in range(n):
            base_ten += int([e if e.isdigit() else self._set_to_number(e) for e in self.number][i]) * pow(16, n-1)
            n -= 1
        return str(base_ten)

if __name__ == "__main__":
    base = Base("5c8")
    print(base.base_sixteen_to_base_ten())