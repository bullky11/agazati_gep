"""II/A, B, C:
           	20*-28*124*166*15*-188*174*243*20*28*-124*166*15*-188*174
II/D, E:
           	Tízzel osztható számok száma: 1.
kimutatas.txt tartalma:
II/F:
Tízzel osztható számok száma: 1.
A.	Írasson ki a konzolra csillag jellel (*) elválasztva 15 számból álló véletlen számsorozatot [-90,500] zárt intervallumon a mintának megfelelően! (4p)
B.	A generált értékeket tárolja lista adatszerkezetben! (1p)
C.	A * jel csak az értékek között szerepeljen (a végén, elején ne)! (2p)
D.	Írjon függvényt oszthatoak_szama néven, amiben számolja meg, hogy hány olyan elem van, ami tízzel osztható. A visszatérési érték legyen egy egész szám, a függvény bemenete a lista! (3p)
E.	Az oszthatoak_szama függvény eredményét írassa ki a mintának megfelelően a konzolra, amit konzolra_ir nevű metódusban fogalmazzon meg! (2p)
F.	Az oszthatoak_szama függvény eredményét írassa ki a mintának megfelelően a kimutatas.txt nevű fájlba, amit fajl_ir nevű metódusban fogalmazzon meg! (2p)
"""
import random
szam_lista=[]
def szamlistazo():
    i=0
    while i<15:
        szam_lista.append(random.randint(-90,500))
        i+=1
    print(szam_lista)
    print("*".join(str(szamok)for szamok in szam_lista))

def oszthatoakszama():
    i = 0
    db = 0
    while i < len(szam_lista):
        if szam_lista[i] % 10 == 0:
            db += 1
        i += 1
    return db
    print(db)
    konzol_kiir(db)
    fajl_ir(db)

def konzol_kiir(db):
    print(f"Tízzel osztható számok száma: {db}")
def fajl_ir(db):
    fajl=open("kimutatas.txt","w",encoding="utf-8")
    fajl.write(f"Tízzel osztható számok száma: {db}")