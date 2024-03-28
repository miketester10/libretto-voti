from voto import Libretto, Voto
import flet as ft

class Controller(object):
    def __init__(self, view):
        self._view = view
        self._model = Libretto()
        self.startupLibretto()

    def handleAdd(self, e):
        esame = self._view._txtEsame.value
        if esame == '':
            self._view._lvOut.controls.append(ft.Text('Il campo Esame non può essere vuoto!', color='red'))
            self._view.update()
            return
        
        strCfu = self._view._txtCFU.value
        try:
            intCfu = int(strCfu)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text('Il campo CFU deve essere un numero intero!', color='red'))
            self._view.update()
            return

        strPunteggio = self._view._ddVoto.value
        if strPunteggio == None:
            self._view._lvOut.controls.append(ft.Text('Il campo Punteggio va selezionato!', color='red'))
            self._view.update()
            return
        if strPunteggio == '30L':
            intPunteggio = 30
            lode = True
        else:
            intPunteggio = int(strPunteggio)
            lode = False
        
        data = self._view._datePicker.value
        if data == None:
            self._view._lvOut.controls.append(ft.Text('Il campo Data va selezionato!', color='red'))
            self._view.update()
            return
        
        self._model.append(Voto(esame, intCfu, intPunteggio, lode, f'{data.year}-{data.month}-{data.day}'))
        self._view._lvOut.controls.append(ft.Text('Voto correttamente aggiunto', color='green'))
        self._view.update()
        
    def handlePrint(self, e):
        outList = self._model.stampaGUI()
        for riga in outList:
            self._view._lvOut.controls.append(ft.Text(riga))

        self._view.update()

    def startupLibretto(self):
        self._model.append(Voto("Fisica I", 10, 20, False, '2022-07-12'))
        self._model.append(Voto("Analisi II", 8, 30, False, '2023-02-15'))
        self._model.append(Voto("Informatica", 10, 24, False, '2021-04-30'))
        self._model.append(Voto("Economia I", 6, 22, False, '2020-06-15'))
        self._model.append(Voto("Chimica", 8, 30, True, '2024-01-10'))   
        self._model.append(Voto("Algebra Lineare", 10, 24, False, '2020-06-30'))
