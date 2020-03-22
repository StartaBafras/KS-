import sqlite3
#kalkış=input("Kalkış İskelesi: ")
#varış=input("Varış İskelesi: ")
kalkış="İzmit"
varış="Karamürsel"
geçici= []
istasyondan_geçen=[]
dere=sqlite3.connect("/home/beyhan/Belgeler/Python/KDU/rıhtım.db")
im=dere.cursor()
im.execute("create table if not exists hatlar('hat','durak1','durak2','durak3','durak4','durak5')")
im.execute("select * from hatlar")
tablo=im.fetchall()
dere.close()
for hat in tablo:
    for duraklar in hat:
        if duraklar == kalkış:
            geçici.append(hat)#Veri tabanındaki boş hücreleri silmeye gerek var mı ?
sayaç=len(geçici)-1
while sayaç > -1:
    for i in geçici[sayaç]:
        if i == varış:
            print(geçici[sayaç][0],"ile gidilir")
            del geçici[sayaç]
    sayaç -= 1
sayaç=len(geçici)-1
print(i)
print(geçici)