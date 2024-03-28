# from dataclasses import dataclass

import dataclasses

@dataclasses.dataclass
class Voto:
    esame: str
    cfu: int
    punteggio: int
    lode: bool
    data: str

    def str_punteggio(self):
        """
        Costruisce la stringa che rappresenta in forma leggibile il punteggio,
        tenendo conto della possibilità di lode
        :return: "30 e lode" oppure il punteggio (senza lode), sotto forma di stringa
        """
        if self.punteggio == 30 and self.lode:
            return "30 e lode"
        else:
            return f"{self.punteggio}"
            # return self.punteggio  NOOO
    
    def copy(self):
        return Voto(self.esame, self.cfu, self.punteggio, self.lode, self.data)

    def __str__(self):
        return f"Esame {self.esame} ({self.cfu}): voto {self.str_punteggio()} il {self.data}"

class Libretto:
    def __init__(self):
        self._voti = []

    def append(self, voto):
        if self.has_voto(voto)==False and self.has_conflitto(voto)==False:
            self._voti.append(voto)
        else:
            raise ValueError("Voto non valido")

    def media(self):
        if len(self._voti)==0:
            raise ValueError("Elenco voti vuoto")
        punteggi = [v.punteggio for v in self._voti]
        return sum(punteggi)/len(punteggi)

    def findByPunteggio(self, punteggio, lode):
        """
        Seleziona tutti e soli i soli voti che hanno un punteggio definito.
        :param punteggio: numero intero che rappresenta il punteggio
        :param lode: booleano che indica la presenza della lode
        :return: lista di oggetti di tipo Voto che hanno il punteggio specificato (può anche essere vuota)
        """
        corsi = []
        for v in self._voti:
            if v.punteggio == punteggio and v.lode == lode:
                corsi.append(v)
        return corsi

    def findByEsame(self, esame):
        """
        Cerca il voto a partire dal nome dell'esame.
        :param esame: Nome dall'esame da ricercare
        :return: l'oggetto Voto corrispondente al nome trovato, oppure None se non viene trovato
        """
        for v in self._voti:
            if v.esame == esame:
                return v
        return None

    def findByEsame2(self, esame):
        """
        Cerca il voto a partire dal nome dell'esame.
        :param esame: Nome dall'esame da ricercare
        :return: l'oggetto Voto corrispondente al nome trovato, oppure un'eccezione ValueError se
        l'elemento non viene trovato
        """
        for v in self._voti:
            if v.esame == esame:
                return v
        raise ValueError(f"Esame '{esame}' non presente nel libretto")


    def has_voto(self, voto):
        """
        Ricerca se nel libretto esiste già un esame con lo stesso nome e lo stesso punteggio
        :param voto: oggetto Voto da confrontare
        :return: True se esiste, False se non esiste
        """
        for v in self._voti:
            if v.esame == voto.esame and v.punteggio == voto.punteggio and v.lode == voto.lode:
                return True
        return False

    def has_conflitto(self, voto):
        """
        Ricerca se nel libretto esiste già un esame con lo stesso nome ma punteggio diverso
        :param voto: oggetto Voto da confrontare
        :return: True se esiste, False se non esiste
        """
        for v in self._voti:
            if v.esame == voto.esame and not(v.punteggio == voto.punteggio and v.lode == voto.lode):
            # if v.esame == voto.esame and (v.punteggio != voto.punteggio or v.lode != voto.lode):
                    return True
        return False
    
    def copy(self):
        nuovo_libretto = Libretto()
        for v in self._voti:
            nuovo_libretto.append(v.copy())
        return nuovo_libretto

    def sortByEsame(self):
        # voti_sort_ByEsame = list(self._voti)
        voti_sort_ByEsame = self.copy()
        voti_sort_ByEsame._voti.sort(key=lambda v: v.esame)
        return voti_sort_ByEsame
    
    def sortByPunteggio(self):
        # voti_sort_ByPunteggio = list(self._voti)
        voti_sort_ByPunteggio = self.copy()
        # voti_sort_ByPunteggio._voti.sort(key=lambda v: v.punteggio+1 
        #                                 if v.lode else v.punteggio, 
        #                                 reverse=True)
        voti_sort_ByPunteggio._voti.sort(key=lambda v: (v.punteggio, v.lode), reverse=True) # verificia prima il punteggio, se è uguale, va a verificare la lode per stabilire chi è maggiore o minore
        return voti_sort_ByPunteggio
    
    def removeVoto(self, punteggio):
        voti_pulito = [v for v in self._voti if v.punteggio >= punteggio]
        self._voti = voti_pulito
        return self
    
    def libretto_migliorato(self): # aggiungo questo metodo se non voglio creare la classe Libretto_migliorato che eredita da Libretto  
        nuovo_libretto = self.copy()
        for v in nuovo_libretto._voti:
            if 18 <= v.punteggio <= 23:
                v.punteggio += 1
            elif 24 <= v.punteggio <= 28:
                v.punteggio += 2
            elif v.punteggio == 29:
                v.punteggio += 3
    
        return nuovo_libretto
    
    def stampa(self):
        print(f"Hai {len(self._voti)} voti:")
        for v in self._voti:
            print(v)
        print(f"La media: {self.media():.2f}")

    def stampaGUI(self):
        outList = []
        outList.append(f"Hai {len(self._voti)} voti:")
        for v in self._voti:
            outList.append(v)
        outList.append(f"La media: {self.media():.2f}")
        
        return outList


# Creazione libretto migliorato creando un nuova classe Libretto_migliorato che eredita da Libretto        
# class Libretto_migliorato(Libretto):
#     # def __init__(self):
#     #     super().__init__()
    
#     def append(self, voto):
#         voto_migliorato = copy.deepcopy(voto)
#         if 18 <= voto_migliorato.punteggio <= 23:
#             voto_migliorato.punteggio += 1       
#         elif 24 <= voto_migliorato.punteggio <= 28:
#                 voto_migliorato.punteggio += 2
#         elif voto_migliorato.punteggio == 29:
#                 voto_migliorato.punteggio = 30
#         super().append(voto_migliorato)

def _test_voto():
    print(__name__)
    v1 = Voto("nome esame", 8, 28, False, '2024-03-11')
    l1 = Libretto()
    l1.append(v1)
    print(l1.media())

if __name__ == "__main__":
    _test_voto()
