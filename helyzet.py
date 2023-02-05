"""A gep.txt forrásállomány, gépek adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
A gep.txt állomány szerkezete:
·         id (azonosító): pl: 1
·         hely (terem azonosítója): pl.: T403
·         típus (a gép típusát jelöli): pl.: asztali
·         ipcim (a gép ipcíme): pl.: 192.168.2.1
Az állomány első sora a mezőneveket tartalmazza felkiáltó jellel elválasztva.
A megoldás mintája:
III/A, B:
            	A gépek száma: 76.
III/C:
           A páros teremszámú termek azonosító átlaga: 39.
III/D:
            	A legkisebb asztali gép azonosítója: 1, helye: T403.
A.	Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a gep.txt fájlból a játékosok adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
B.	Írassa ki a gépek számát a mintának megfelelően a konzolra! A metódus neve legyen gepek_szama! (2p)
C.	Határozza meg és írassa ki a konzolra a minta szerint, hogy a páros teremszámú termeknek mi az azonosító átlaga. A metódus neve legyen atlag! (4p)
D.	Írassa ki konzolra a mintának megfelelően a legkisebb azonosítójú asztali gép azonosítóját és helyét (ha több is van, akkor az első legkisebb adatait). A metódus neve legyen legkisebb!  (4p)
"""
from Gepclass import Gepclass
gepek_lista=[]
def beolvas():
    fajlom=open("gep.txt","r",encoding="utf-8")
    fajlom.readline()
    tartalom=fajlom.readlines()
    fajlom.close
    i=0
    while i < len(tartalom):
        sor=tartalom[i].strip().split("!")
        gepek_lista.append(Gepclass(sor))
        i+=1
    print(gepek_lista[1])


def gepekszama():
    print(len(gepek_lista))


def atlag():
    i=0
    parostermek=0
    while i< len(gepek_lista):
        if int(gepek_lista[i].hely[1:])%2==0:
            parostermek+=int(gepek_lista[i].hely[1:])
        i+=1
    print(parostermek/len(gepek_lista))


def legkisebb():



