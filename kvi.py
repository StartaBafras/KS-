import sqlite3
#kalkış=input("Kalkış İskelesi: ")
#varış=input("Varış İskelesi: ")
kalkış="İzmit"
varış="Karamürsel"
geçici= []
istasyondan_geçen=[]
dere=sqlite3.connect("rıhtım.db")
im=dere.cursor()
im.execute("create table if not exists hatlar('hat','durak1','durak2','durak3','durak4','durak5')")
im.execute("select * from hatlar")
tablo=im.fetchall()
for hat in tablo:
    for duraklar in hat:
        if duraklar == kalkış:
            geçici.append(hat)

