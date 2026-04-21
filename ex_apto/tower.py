class Tower:
    def __init__(self, number, adress):
        self.number = number
        self.adress = adress
        self.apts = []

    def __str__(self):
        txt = " - Tower: " + self.number + ", adress: " + self.adress + ", QTD of apartments:" + len(self.apts)
        return txt    

    def adress_apt(self, apt):
        apt.tower = self
        self.apts.append(apt)
        print (" The apartment '{apt.number}' belongs to the tower '{tower.number}'.")


