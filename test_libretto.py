from voto import Libretto, Voto #Libretto_migliorato

lib1 = Libretto()

v1 = Voto("Analisi I", 10, 18, False, '2022-01-30')
lib1.append(v1)
v2 = Voto("Fisica I", 10, 20, False, '2022-07-12')
lib1.append(v2)

lib1.append(Voto("Analisi II", 8, 30, False, '2023-02-15'))
lib1.append(Voto("Informatica", 10, 24, False, '2021-04-30'))
lib1.append(Voto("Economia I", 6, 22, False, '2020-06-15'))
lib1.append(Voto("Chimica", 8, 30, True, '2024-01-10'))

voti25 = lib1.findByPunteggio(25, False)
for v in voti25:
    print(v.esame)

voto_analisi2 = lib1.findByEsame("Analisi III")
if voto_analisi2 is None:
    print("Nessun voto trovato")
else:
    print(f'Hai preso {voto_analisi2.str_punteggio()}')

try:
    voto_analisi2 = lib1.findByEsame2("Analisi III")
    print(f'Hai preso {voto_analisi2.str_punteggio()}')
except ValueError:
    print("Nessun voto trovato")

nuovo1 = Voto("Fisica I", 10, 25, False, '2022-07-13')
nuovo2 = Voto("Fisica II", 10, 25, False, '2022-07-13')
print("1)", lib1.has_voto(nuovo1))
print("2)", lib1.has_voto(nuovo2))

# lib_migliorato = Libretto_migliorato()
# lib_migliorato.append(v1)
# lib_migliorato.append(v2)
# print(lib_migliorato._voti)
# print(lib1._voti)
# print(lib1)
# print(lib_migliorato)

print('Libretto Originale')
lib1.stampa() #libretto originale

print('Libretto Migliorato')
migliorato = lib1.libretto_migliorato() #libretto migliorato
migliorato.stampa()

print('Libretto Migliorato ordinato per esame')
migliorato_sortByEsame = migliorato.sortByEsame() #libretto migliorato sortByEsame
migliorato_sortByEsame.stampa()

print('Libretto Migliorato ordinato per punteggio')
migliorato_sortByPunteggio = migliorato.sortByPunteggio() #libretto migliorato sortByPunteggio
migliorato_sortByPunteggio.stampa()

print('Libretto Migliorato senza i voti minori di 24')
migliorato_senza_voti_minori_24 = migliorato.removeVoto(24) #libretto migliorato senza i voti minori di 24
migliorato_senza_voti_minori_24.stampa()