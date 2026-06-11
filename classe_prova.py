

class Calciatore:
    def __init__(self,nome,cognome,numero):
        self.nome=nome
        self.cognome=cognome
        self.numero=numero

    def saluta(self):
        print("ciao sono "+ self.nome)

class Allenatore(Calciatore):
    def __init__(self, nome, cognome,numero,GOL):
        super().__init__(nome, cognome,numero)
        self.GOL=GOL

calciatore1=Calciatore("Davide","Calabria","2")

calciatore2=Calciatore("Ismael","Bennacer","4")

allenatore1=Allenatore("Sérgio", "Conceição","99","50")

calciatore2.saluta()


