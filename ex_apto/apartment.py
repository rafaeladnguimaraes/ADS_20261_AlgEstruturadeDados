from tower import Tower

class Apartment:
    def __init__(self, number, c_space = None):
        self.number = number
        self.c_space = c_space
        self.c_next = None
        self.tower = None

    def __str__(self):
        txt = " - Apartment: " + self.number + ", Tower: " + self.tower.number + ", car space:" + self.c_space 
        return txt 

