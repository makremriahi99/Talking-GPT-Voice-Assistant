class Studente:
    ore_settimanali=36
    corpo_studentesco=0
    def __init__(self,nome,cognome,corso_di_studi):
        self.nome=nome
        self.cognome=cognome
        self.corso_di_sudi=corso_di_studi
        Studente.corpo_studentesco += 1
     
    
    def scheda_personale(self):
        print(f"Scheda Studente\n Nome:{self.nome}\n Cognome:{self.cognome}\n Corso Di Studi:{self.corso_di_sudi}\n Ore settimanali:{self.ore_settimanali}")

class Insegnante(Studente):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome,materia)
   


studente_uno = Studente("Py","Mike","Programmazione")
studente_due = Studente("Marta","Stannis","sienze politiche")
insegnante2 = Insegnante("Maria","Rossi","Chimica")

studente_uno.ore_settimanali+=4

studente_uno.scheda_personale()
print(Studente.scheda_personale(studente_due))

print(Insegnante.scheda_personale(insegnante2))

 