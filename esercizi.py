#Creare una classe Persona che abbia i seguenti attributi: nome, età, sesso. Aggiungi un metodo “presentati” che stampi una frase di presentazione della persona, ad esempio “Ciao, mi chiamo Marco e ho 32 anni.


'''class Persona:
    def __init__(self,nome,età):

        self.nome=nome
        self.età=età
        
    def presentazione(self):
        print("Ciao sono ",self.nome," e ho ", self.età," anni" )

persona1=Persona("Marco","32")

persona1.presentazione()'''







#Creare una classe Animale che abbia gli attributi “nome” e “specie”. Aggiungi un metodo “emetti_suono” che stampi un suono specifico per ogni specie. Ad esempio, se l’animale è un gatto dovrebbe stampare “Miao!”, se è un cane “Bau!”ù


'''class Animale:
    def __init__(self,nome,specie):

        self.nome=nome

        self.specie=specie
    
    def suono(self):
        if self.specie=="gatto":
            print("Miao!")
        
        elif self.specie=="cane":
            print("Bau!")
        
        else:
         print("Suono sconosciuto")




animale1=Animale("daghi","gatto")

animale2=Animale("cat","cane")


animale1.suono()

animale2.suono()'''


#Creare una classe Automobile che abbia gli attributi “marca”, “modello” e “anno”. Aggiungi un metodo “descrivi” che stampi una descrizione dell’automobile, ad esempio “Questa è una Toyota Corolla del 2017”.



'''class Automobile:
    def __init__(self,marca,modello,anno):
        self.marca=marca
        self.modello=modello
        self.anno=anno

    def descrizione(self):
        print(f"Questa è una {self.marca} {self.modello} del {self.anno}")


auto1=Automobile("Toyota","Corolla","2017")

auto1.descrizione()'''


#Creare una classe Impiegato che abbia gli attributi “nome”, “cognome”, “matricola” e “stipendio”. Aggiungere un metodo “aumenta_stipendio” che aumenti lo stipendio dell’impiegato del 10% e un metodo “stampa_dettagli” che stampi tutti i dettagli dell’impiegato, ad esempio “Impiegato: Marco Rossi, matricola 12345, stipendio: 3000 Euro”.



'''class Impiegato:
    def __init__(self,nome,cognome,matricola,stipendio):
        
        self.nome=nome

        self.cognome=cognome

        self.matricola=matricola

        self.stipendio=stipendio
    
    def aumenta_stipendio(self):
        self.stipendio *= 1.1
    
    def stampa_dettagli(self):

        print("Impiegato: "+ self.nome,self.cognome,", matricola",self.matricola,"stipendio: ",float(self.stipendio),"Euro.")



impiegato1=Impiegato("Mario","Rossi",12345,3000)

impiegato1.aumenta_stipendio()
impiegato1.stampa_dettagli()'''





#Crea una classe GestoreMagazzino che gestisca un magazzino di prodotti. La classe dovrà avere i seguenti attributi:
#Un dizionario “prodotti” che mappa i nomi dei prodotti ai rispettivi oggetti “Prodotto” (che descriverai in seguito)
#Una variabile “costo_magazzinaggio” che indica il costo per magazzinare ogni prodotto per un mese

#La classe dovrà avere i seguenti metodi:
#Un metodo “aggiungi_prodotto” che aggiunga un nuovo prodotto al magazzino
#Un metodo “rimuovi_prodotto” che rimuova un prodotto dal magazzino
#Un metodo “calcola_costi_magazzinaggio” che calcoli i costi di magazzinaggio per tutti i prodotti presenti nel magazzino
#Crea inoltre una classe Prodotto che abbia gli attributi “nome”, “prezzo” e “scorta”.


class Prodotto:
    def __init__(self,nome,prezzo,scorta):
        self.nome=nome
        self.prezzo=prezzo
        self.scorta=scorta

class GestoreMagazzino:
    def __init__(self,costo_magazzinaggio):
        self.prodotti={}
        self.costo_magazzinaggio=costo_magazzinaggio

    def aggiungi_prodotto(self,prodotto):
            self.prodotti = 

        

            self.prodotti

    def rimuovi_prodotto(self):

        self.prodotti.pop

    def calcola_costi_magazzinaggio(self):
         

prodotto = Prodotto("telefono",500,20)

