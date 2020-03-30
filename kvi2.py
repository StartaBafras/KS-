import sqlite3
#kalkış=input("Kalkış İskelesi: ")
#varış=input("Varış İskelesi: ")
kalkış="İzmit"
varış="Karamürsel"
gidenler= []


def geçenler(istasyon):# istasyondan geçen hatları verir
    import sqlite3
    global bulunulan_durak
    bulunulan_durak = istasyon
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


ilk_durak = []
ilk_durak = geçenler(kalkış)


def aktarma(aktarma_yapabilecekler):
    for i in aktarma_yapabilecekler:
        for duraklar in i:
            durak_2 = []
            durak_2 = geçenler(duraklar)
            doğrudan2(bulunulan_durak,durak_2,varış)

def doğrudan2(bulunulan_durak,geçen_trenler,varış):
    for hat in geçen_trenler:
        for duraklar in hat:
            if duraklar == varış:
                print(hat[0],"Bulunulan durak: {} Varılan durak: {}".format(bulunulan_durak,varış))




doğrudan2(bulunulan_durak,ilk_durak,varış)
aktarma(ilk_durak)


