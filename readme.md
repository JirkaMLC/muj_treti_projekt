##1. Popis projektu

Program sberac.py projde výsledky voleb pro vybraný volební okrsek a uloží do výstupního csv souboru vybrané data pro jednotlivé obce z daného okrsku. Data čerpá z odkazu, který musí směrovat na stránky ČSÚ, viz ukázka projektu.
data, která program sběrač u každé obce načte a uloží do výstupního souboru :

○ kód obce

○ název obce

○ voliči v seznamu

○ vydané obálky

○ platné hlasy

○ počty hlasů pro kandidující strany

#2. Instalace potřebných knihoven

Před spuštěním je třeba stáhnout extra moduly, které program pro běh využívá. 
Jejich seznam je uveden v souboru requirements.txt. Instalace knihoven pomocí tools: Sync Pytho rqurments

´pip install -r requirements.txt´

##3. Ukázka projektu

Výsledky voleb pro okrsek Tábor

1. argument - https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=3107
2. argument - vysledky_tabor.csv

## Stahovaní a ukládaní do .csv souboru. 

Ukazka výstupu:
Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy
563251,Balkova Lhota,102,69,4,0,0,8,0,7,7,0,0,2,0,0,8,0,5,16,0,0,3,0,0,0,0,9,0
563366,Bečice,63,52,10,0,0,5,0,2,2,0,0,1,0,0,11,0,2,3,0,0,1,0,1,0,0,14,0
552054,Bechyně,4405,2774,255,5,3,189,4,103,355,27,18,53,4,8,242,2,230,793,2,9,105,1,31,4,10,283,16