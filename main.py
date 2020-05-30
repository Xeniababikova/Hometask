#Python 3
 
 
class Donkey:
    def __init__(self, name, load_int, years_int):
        self.load_int = load_int
        self.years_int = years_int
        self.name = name
 
    def __str__(self):
        return f'Donkey-boy {self.name}, {self.load_int}'
 
    def cry(self):
        return 'Eeyore' * self.years_int
 
    def work_hard(self, amount):
        if amount < 0:
            self.years_int *= 2
        else:
            k = amount // 5
            self.years_int -= k
            if self.years_int < 0:
                self.years_int = 0
 
    def carry(self, load):
        return self.load_int <= load
 
    def __lt__(self, other):
        ret = self.years_int > other.years_int
        if self.load_int != other.load_int:
             ret = ret and (self.load_int < other.load_int)
        if self.name != other.name:
            ret = ret and (self.name > other.name)
 
        return ret
 
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
 
    def __eq__(self, other):
        return (
            self.load_int == other.load_int
            and self.years_int == other.years_int
            and self.name == other.name
        )
 
    def __ne__(self, other):
        return not self.__eq__(other)
 
    def __gt__(self, other):
        ret = self.years_int < other.years_int
        if self.load_int != other.load_int:
            ret = ret and (self.load_int > other.load_int)
        if self.name != other.name:
            ret = ret and (self.name < other.name)
 
        return ret
 
    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)