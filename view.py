import datetime
import flet as ft

class View(object):
    def __init__(self, page):
        self._page = page
        
        
    def caricaInterfaccia(self):
        # Riga 0 (Titolo)
        self._titolo = ft.Text(value="Libretto voti ++", color="blue", size=20)
        row0 = ft.Row([self._titolo], alignment=ft.MainAxisAlignment.CENTER)

        # Riga 1
        self._txtEsame = ft.TextField(label="Inserisci esame", width=300)
        self._txtCFU = ft.TextField(label="CFU", width=100)
        self._ddVoto = ft.Dropdown(label="Voto", width=100)
        self.fillddVotoOptions()

        self._datePicker = ft.DatePicker(first_date=datetime.datetime(2020, 1, 1), 
                                         last_date=datetime.datetime(2025, 12, 31))

        self._btnCalendar = ft.ElevatedButton(
            'Pick Date',
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self._datePicker.pick_date())
        
        self._page.overlay.append(self._datePicker)

        row1 = ft.Row([self._txtEsame, self._txtCFU, self._ddVoto, self._btnCalendar], spacing=10, alignment=ft.MainAxisAlignment.CENTER)

        # Riga 2
        self._btnAdd = ft.ElevatedButton(text='Add', on_click=self._controller.handleAdd)
        self._btnPrint = ft.ElevatedButton(text='Print', on_click=self._controller.handlePrint)

        row2 = ft.Row([self._btnAdd, self._btnPrint], spacing=10, alignment=ft.MainAxisAlignment.CENTER)

        # Riga 3
        self._lvOut = ft.ListView()
        row3 = ft.Row([self._lvOut])

        self._page.add(row0, row1, row2, row3) 

    def setController(self, controller):
        self._controller = controller

    def fillddVotoOptions(self):
        for i in range(18, 31):
            self._ddVoto.options.append(ft.dropdown.Option(f'{i}'))
        self._ddVoto.options.append(ft.dropdown.Option('30L'))
    
    def update(self):
        self._page.update()
        

    