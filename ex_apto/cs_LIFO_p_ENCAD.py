from apartment import Apartment


class Waiting_apts:
    def __init__(self):
        self.start = None
        self.end = None

    def imp_a_waiting(self):
        # corrigir método
        print(" -------- Condominium Duck Noble: Waiting list --------")
        if self.start is None:
            print(" The waiting list is empty.")
        else: 
            aux = self.start
            number = 1
            txt = ""
            while aux:
                txt += number + aux.__str__ + "\n"
                aux = aux.c_next
                number += 1
            print( txt )
    
    def add_a_waiting(self, apt):
        print(" -------- Condominium Duck Noble: Adding to the waiting list -------- ")
        loop = Apartment(apt)
        if self.start is None:
            self.start = loop
        else:
            self.end.c_next = loop
        self.end = loop

        self.imp_a_waiting()
    
class Parked:

    def imp_a_parked(self):
        pass