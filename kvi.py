import sqlite3
#import denemeler #Böyle yapınca global değişken nedense çalışmıyor fonksiyonu buraya kopyalamak gerekti
#kalkış=input("Kalkış İskelesi: ")
#varış=input("Varış İskelesi: ")
kalkış="İzmit"
varış="Karamürsel"
geçici= []
istasyondan_geçen=[]
dere=sqlite3.connect("/home/beyhan/Belgeler/Python/KDU/rıhtım.db")
im=dere.cursor()
#im.execute("create table if not exists hatlar('hat','durak1','durak2','durak3','durak4','durak5')")
im.execute("select * from hatlar")
tablo=im.fetchall()
#dere.close()
for hat in tablo:
    for duraklar in hat:
        if duraklar == kalkış:
            istasyondan_geçen.append(hat)#Veri tabanındaki boş hücreleri silmeye gerek var mı ?
del hat,duraklar,tablo


#############fonksiyon kısmı
sayaç=len(istasyondan_geçen)-1
print(len(istasyondan_geçen))
while sayaç > -1:
    for i in istasyondan_geçen[sayaç]:
        if i == varış:
            print(istasyondan_geçen[sayaç][0],"ile gidilir")
            del istasyondan_geçen[sayaç]
    sayaç -= 1
del i
###############
sayaç = len(istasyondan_geçen)-1
while sayaç > -1:
    gezinme = len(istasyondan_geçen[sayaç])-1
    while gezinme > 1:
        print(istasyondan_geçen[sayaç][gezinme])
        
        gezinme -=1
    sayaç -= 1
    print(istasyondan_geçen[sayaç])
    sayaç -=1
print("Ayrım bölgesi ####################")
del istasyondan_geçen
#denemeler.geçenler("İzmit")
#print(istasyondan_geçen)
def geçenler(istasyon):
    import sqlite3
    dere=sqlite3.connect("/home/beyhan/Belgeler/Python/KDU/rıhtım.db")
    im=dere.cursor()
    #im.execute("create table if not exists hatlar('hat','durak1','durak2','durak3','durak4','durak5')")
    im.execute("select * from hatlar")
    tablo=im.fetchall()
    #dere.close()
    global istasyondan_geçen
    istasyondan_geçen = []    
    for hat in tablo:
        for duraklar in hat:
            if duraklar == istasyon:
                istasyondan_geçen.append(hat)
    del hat,duraklar
    print(istasyondan_geçen)
geçenler("İzmit")
print(istasyondan_geçen)
