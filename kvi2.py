import sqlite3
#kalkış=input("Kalkış İskelesi: ")
#varış=input("Varış İskelesi: ")
kalkış="İzmit"
varış="Hereke"
gidenler= []


def geçenler(istasyon):# istasyondan geçen hatları verir
    global bulunulan_durak
    bulunulan_durak = istasyon
    dere=sqlite3.connect("/home/beyhan/Belgeler/Python/KDU/KSI/rıhtım.db")
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


ilk_durak = []
ilk_durak = geçenler(kalkış)


def aktarma(aktarma_yapabilecekler):#Doğrudan gidenlerin ayıklanmasıyla elde kalan hatlar aktarılır
    hatlar_2 = []
    for i in aktarma_yapabilecekler: #Aktarma yapabilecek birden fazla hat olabileceğinden tek tek hatlar ayıklanır
        for duraklar in i:#Ayıklanan hattın durakları ayrılır
            if duraklar != "Hat-1" and duraklar!= "Hat-2" and duraklar!= "Hat-3" and duraklar!= "Hat-4" and duraklar != i[1] and duraklar != "Boş":
                hatlar_2 = geçenler(duraklar)
                #print(i[0],"İle aşağıda bulunulan duraklara gidilip aktarma yapılarak varış yerine gidilebilir.")
                doğrudan2(duraklar,hatlar_2,varış)


def doğrudan2(bulunulan_durak,geçen_trenler,varış):
    for hat in geçen_trenler:
        for duraklar in hat:
            if duraklar == varış:
                print(hat[0],"Bulunulan durak: {} Varılan durak: {}".format(bulunulan_durak,varış))
                bulunma=hat.index(hat[0])#Geçen_trenler listesinin hangi elemanı doğrudan gidiliyor tespiti
                del geçen_trenler[bulunma]#Doğrudan giden hat aktarmayı kontrol edecek fonksiyona soru yaratmaması için siliniyor


doğrudan2(bulunulan_durak,ilk_durak,varış)

aktarma(ilk_durak)
