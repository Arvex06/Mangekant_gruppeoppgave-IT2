class Mangekant:
    def __init__(self, sider):
        self.sider = sider
        self.lengde = []

    def sidelengde(self):
        for i in range(self.sider):
            lengde = int(input("Skriv inn lengden på side: "))
            self.lengde.append(lengde)
        
    def omkrets(self):
        return sum(self.lengde) 
    
    def visInfo(self):
        print(f"Mangekanten har {self.sider} sider med sidelengde {self.lengde}."
              f"Omkretsen er {self.omkrets()}")

mangekant = Mangekant(4)     # Oppretter en instans (et objekt) av klassen Mangekant med 5 sider
mangekant.sidelengde()       # Kaller metoden `sidelengde` for å samle inn lengden på hver side fra brukeren
mangekant.visInfo()          # Kaller metoden `visInfo` for å vise antall sider, sidelengdene og omkretsen