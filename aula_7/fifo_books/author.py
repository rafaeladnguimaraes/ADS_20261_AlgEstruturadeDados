class Author:
    def __init__(self,name, year):
        self._name = name
        self.__year = year

    def setName(self, value):
        # possibilidade de criar critérios 
        if value != "":
            self._name = value
    def getName(self):
        return self._name        
    
    @property
    def year(self):
        # possibilidade de criar critérios 
        return self.__year
    @year.setter
    def year(self, value):
        if value < 2026:
            self.__year = value

    def __str__(self):
        txt = "Author: " + self._name + " - Year: " + str(self.__year)
        return txt