class Persona:
    def __init__(self,nome,cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print("ciao sono "+ self.nome)

persona1 = Persona("Mario","Pero")
persona2 = Persona("Luca", "Rossi")


persona1.saluta()



