#Scrivere una classe Veicolo che abbia le seguenti proprietà: marca, modello e anno. Aggiungi poi i metodi accellera e frena. Creare poi una classe Auto che eredita da Veicolo ma aggiunge la proprietà colore ed il metodo cambia_colore()
# Modifica la classe Auto in modo che erediti anche il metodo __str__() dalla classe Veicolo, in modo da stampare le informazioni sull’auto in questo formato: “Marca: Ferrari, Modello: Enzo, Anno: 2004, Colore: Rosso”


class Veicolo:
    def __init__(self,marca,modello,anno):
        self.marca=marca
        self.modello=modello
        self.anno=anno
    def accellera(self):
        print("Sto accellerando")
    
    def frenata(self):
        print("Sto frenando")
    
    def __str__(self):

     return f"La macchina è una {self.marca} modello {self.modello} dell'annata {self.anno} del colore {self.colore}"

    
   

    
    
class Auto(Veicolo):
    def __init__(self, marca, modello, anno,colore):

        super().__init__(marca, modello, anno)
        self.colore=colore

    def cambio_colore(self,nuovo_colore):
        self.nuovo_colore=nuovo_colore
    
    
        
    
        
veicolo1=Auto("ferrari","F40",2020,"Rossa")

print(veicolo1.__str__())



