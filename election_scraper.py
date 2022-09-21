"""
Projekt_3.py: Třetí projekt do Engeto Online Python Akadeie

author: Jiří Mlčkovský
email: jiri.mlckovsky.obchod@obchod.cz
discord:nemám založený profil na discordu
"""


from bs4 import BeautifulSoup as BS
import requests
import sys
import csv

# list
hlavni = ["Kód obce", "Název obce", "Voliči v seznamu","Vydané obálky", "Platné hlasy" ]
hlavni_url = "https://volby.cz/pls/ps2017nss/"

kody_l = []
jmena_l = []
komplet_l = []
strany_k = []

# Funkce na zadaní pomocí 2 argumentů "url" a ".csv"

def overeni_args ():
    argumenty = sys.argv
    if len(argumenty) != 3:
        print(f"Nebyl zadán potřebný počet argumentů. Ukončuji program !")
        quit("Ukončuji")
    elif "https://volby.cz/pls/ps2017nss/" not in argumenty[1]:
        print(f"Zadejte url adresu stránky.")
        quit("Ukončuji")
    elif ".csv" not in argumenty[2]:
        print("Zadejte .CSV vstup.")
        quit("Ukončuji")
    else:
        return argumenty[1], argumenty[2]
    #overeni_args():

# Načtení dat obcí a uložení do listu

def fce_nacti_obce(url):
    r = requests.get(url)
    soup = BS (r.content, "html.parser")
    obce = soup.find_all(class_="cislo")   #  tag číslo obce po otevření url a zvolení územního celku př. Tábor
    obce_jmena = soup.find_all(class_="overflow_name")     # tag pro jména obcí př. Tábor
    for o in obce:
        cont = []
        obec_kod = o.getText()
        url_obce = hlavni_url + o.find("a").get("href")
        cont.append(obec_kod)
        cont.append(url_obce)
        kody_l.append(cont)

    for o in obce_jmena:
        nazev_obce = o.getText()
        jmena_l.append(nazev_obce)

# Funkce pro ziskaní dat pro kazdou obec

def fce_strany (url):
    r = requests.get(url)
    soup = BS(r.content,"html.parser")
    strany = soup. find_all(class_="owerflow_name")    # tag pro názvy politických stran po zvolení obce.
    for s in strany:
        strany_k.append(s.getText())

def fce_data(url):
    cont = []
    r = requests.get(url)
    soup = BS(r.content, "html.parser")

    volici = soup.find(class_="cislo", headers ="sa2").getText()   # tag pro volice v tabulce př. Balkova Lhota
    cont.append(int(volici.replace(u"\xa0", "")))                # metoda replace nahraddí "\xa0" za mezeru, to sáme bude platit i pro obalky a hlasy
    obalky = soup.find(class_="cislo", headers="sa3").getText()
    cont.append(int(obalky.replace(u"\xa0", "")))

    for x in range(1,4):
        try:
            str_pocty = soup.find_all(class_="cislo", headers=f"t{x}sa2 t{x}sb3")
            for sp in str_pocty:
                cislo = sp.getText()
                cont.append(int(cislo.replace(u"\xa0","")))
        except:
            pass
    return cont

# funkce pro stažení dat obcí

def fce_stazeni_dat():
    print(f"Stahuji ...")
    list_obce = []
    fce_strany(kody_l[1][1])
    for i in range(0, len(kody_l)):
        de = []
        list_obce.extend(kody_l[i])
        list_obce.pop(1)

        de = fce_data(kody_l[i][1])
        list_obce.append(jmena_l[i])
        list_obce.extend(de)
        komplet_l.append(list_obce)
        list_obce = []

# funkce pro uložení .CSV souboru

def fce_csv_ulozeni(soubor):
    cont = []
    cont.extend(hlavni)
    cont.extend(strany_k)
    print(f"Ukládám data do {soubor}.")
    with open(soubor, "w", newline='', encoding="utf-8") as file:
        wr = csv.writer(file)

        wr.writerow(cont)
        wr.writerows(komplet_l)
    print(f"Uloženo, konec programu")

# Hlavní funkce pro celý program

def spusteni_dat():
    url, soubor = overeni_args()
    fce_nacti_obce(url)
    fce_stazeni_dat()
    fce_csv_ulozeni(soubor)

if __name__ == "__main__":
    spusteni_dat()

