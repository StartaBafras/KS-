import sqlite3
import denemeler #Böyle yapınca global değişken nedense çalışmıyor fonksiyonu buraya kopyalamak gerekti
#kalkış=input("Kalkış İskelesi: ")
#varış=input("Varış İskelesi: ")
kalkış="Gölcük"
varış="Tütünçiftlik"
gidenler= []


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
                print(i)
                print(geçen_trenler[sayaç][0],"ile doğrudan gidilir")
                print("Kalkış istasyonu:{} \n Varış istasyonu: {}".format(kalkış,varış))
                del geçen_trenler[sayaç]
                #sayaç=len(geçen_trenler)-1
                print(geçen_trenler)
            if i == NameError:
                sayaç -= 1 
            #else:
                #print(sayaç)
                #print(i)
                #print(geçen_trenler[sayaç][0],"ile doğrudan gidilmez")
        #sayaç -= 1
        #print(sayaç)
    del i


ilk_durak = []
ilk_durak = geçenler(kalkış)


def aktarma(aktarma_yapabilecekler):
    for i in aktarma_yapabilecekler:
        for duraklar in i:
            durak_2 = []
            durak_2 = geçenler(duraklar)
            doğrudan(durak_2,varış)

def doğrudan2(geçen_trenler,varış):
    for hat in geçen_trenler:
        for duraklar in hat:
            if duraklar == varış:
                print(hat[0],"doğrudan gider")



doğrudan2(ilk_durak,varış)



