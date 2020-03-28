import sqlite3
import denemeler #Böyle yapınca global değişken nedense çalışmıyor fonksiyonu buraya kopyalamak gerekti
#kalkış=input("Kalkış İskelesi: ")
#varış=input("Varış İskelesi: ")
kalkış="İzmit"
varış="Karamürsel"



def geçenler(istasyon):# istasyondan geçen hatları verir
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
    return istasyondan_geçen




def doğrudan(geçen_trenler,hedef):#Hatların hedefe doğrudan gidip gitmediğini kontrol eder
    sayaç=len(geçen_trenler)-1
    while sayaç > -1:
        for i in geçen_trenler[sayaç]:
            if i == hedef:
                print(geçen_trenler[sayaç][0],"ile gidilir")
                del geçen_trenler[sayaç]
        sayaç -= 1
    del i


ilk_durak = []
ilk_durak = geçenler(kalkış)
print(ilk_durak)
doğrudan(ilk_durak,varış)
print(ilk_durak)
print("###############################")

def aktarma(aktarma_yapabilecekler):
    for i in aktarma_yapabilecekler:
        for duraklar in i:
            durak_2 = []
            durak_2 = geçenler(duraklar)
            doğrudan(durak_2,varış)
aktarma(ilk_durak)

