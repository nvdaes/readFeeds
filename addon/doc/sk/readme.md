# RSS Čítačka #

* Autori: Noelia Ruiz Martínez, Mesar Hameed
* Funguje s NVDA od verzie 2019.3.
* Stiahnuť [stabilnú verzia][1]
* Stiahnúť [Vývojovú verziu ][2]

Poskytuje jednoduchý spôsob čítania kanálov vo formátoch Atom alebo RSS
pomocou NVDA. Kanály sa neobnovia automaticky. Nižšie, keď spomíname
informačné kanály, máme na mysli informačné kanály RSS aj ATOM.

## Inštalácia alebo aktualizácia: ##

Ak ste používali predchádzajúcu verziu tohto doplnku a v priečinku s
nastaveniami NVDA sa nachádza priečinok RSS alebo personalFeeds, pri
inštalácii aktuálnej verzie sa zobrazí dialógové okno s otázkou, či chcete
aktualizovať alebo nainštalovať. Vyberte aktualizáciu, aby ste zachovali
uložené kanály a pokračovali v ich používaní v novej nainštalovanej verzii
doplnku.

## Príkazy: ##

### Menu RSS čítačky ###

Menu RSS čítačky je dostupné z menu NVDA > nástroje a obsahuje tieto
možnosti:

#### Informačné kanály... ####

Otvorí dialógové okno s nasledujúcimi možnosťami:

* Filter: Editačné pole na vyhľadávanie uložených kanálov.
* Zoznam uložených informačných kanálov.
* Zoznam článkov: Otvorí zoznam článkov z vášho aktuálneho informačného
  kanála. Vyberte článok, ktorý si chcete prečítať, a stlačte kláves Enter
  alebo tlačidlo Otvoriť webovú stránku, aby ste otvorili príslušnú stránku
  v prehliadači. Stlačením tlačidla Informácie o článku otvoríte dialógové
  okno s názvom a odkazom na vybraný článok; z tohto dialógového okna budete
  môcť tieto informácie skopírovať do schránky.
* Otvoriť informačný kanál: Otvorí vybraný informačný kanál v predvolenej
  aplikácii.
* Nový: otvorí dialógové okno, kde môžete vložiť adresu informačného
  kanála. Ak je adresa platná a informačný kanál je možné uložiť, Kanál je
  pridaný na koniec zoznamu kanálov.
* Premenovať: Otvorí dialógové okno v ktorom môžete zadať nový názov kanála.
* Odstrániť: Umožní odstrániť vybratý informačný kanál.
* Nastaviť predvolené: Nastaví vybraný informačný kanál ako predvolený, aby
  k jeho článkom bolo možné pristupovať pomocou klávesových skratiek.
* Otvoriť priečinok so zálohou zdrojov: Otvorí priečinok, ktorý môže
  obsahovať zálohu zdrojov. To môže byť užitočné pri skúmaní a odstraňovaní
  informačných kanálov, ktoré by sa po aktualizácii doplnku nemali
  importovať.
* Zatvoriť: Zatvorí dialógové okno informačné kanály.

##### Poznámky #####

* Ak sa vytvorí informačný kanál s názvom tempFeed, premenujte ho a prideľte
  mu zmysluplný názov. V opačnom prípade môže byť tento kanál prepísaný pri
  pridaní nasledujúceho kanála.
* Zdroj nastavený ako predvolený nie je možné odstrániť. Informačný kanál
  AddressFile sa použije ako predvolený pri resetovaní konfigurácie, takže
  ho nemožno odstrániť.

####Skopírovať informačné kanály...####

Otvorí dialógové okno pre výber priečinka, do ktorého si môžete uložiť vaše
informačné kanály. V predvolenom nastavení je vybratý priečinok s
nastaveniami NVDA. Kanály sa vždy ukladajú do adresára personalfeeds.

#### Obnoviť informačné kanály... ####

Umožní nahradiť aktuálne informačné kanály súbormi so zálohy. Ustite sa, že
ste zvolili priečinok s RSS adresami.

### Klávesové skratky: ###

* Ctrl+Shift+NVDA+Medzera: Oznamuje URL aktuálneho článku. Stlačené dvakrát
  rýchlo za sebou otvorí webovú stránku.
* Ctrl+Shift+NVDA+8: Obnoví vybraný informačný kanál a oznámi názov
  posledného článku.
* Ctrl+Shift+NVDA+I: Oznamuje aktuálny názov informačného kanála a
  odkaz. Stlačené dvakrát rýchlo za sebou skopíruje názov a odkaz do
  schránky.
* Ctrl+Shift+NVDA+U: oznámi predchádzajúci článok.
* Ctrl+Shift+NVDA+O: Oznámi nasledujúci článok.

## Upozornenia: ##

* Po skopírovaní názvu alebo adresy URL do schránky.
* Ak sa nedá pripojiť/obnoviť informačný kanál alebo webová adresa
  nezodpovedá platnému informačnému kanálu.
* NVDA zobrazí chybové hlásenie, ak nebolo možné zálohovať alebo obnoviť
  priečinok personalFeeds.
* Názov dialógového okna so zoznamom článkov obsahuje vybratý názov
  informačného kanála a počet dostupných položiek.

## Zmeny vo verzii 9.0 ##

* Vyžaduje NVDA od verzie 2019.3.

## Zmeny vo verzii 8.0 ##

* Po inštalácii novej verzie doplnku sa automaticky importujú uložené
  kanály, v prípade, že nepreferujete ukladanie do hlavného adresára s
  nastaveniami NVDA.
* Ak kopírujete kanály a nový priečinok sa nevolá personalFeeds, bude takýto
  priečinok vytvorený a do neho budú importované nastavenia, aby nedošlo k
  zmazaniu dôležitých adresárov.

## Zmeny vo verzii 7.0 ##

* Pridané tlačidlo na otvorenie adresára so zálohou.
* Ak ste zadali reťazec na filtrovanie a žiadna položka nezodpovedá filtru,
  ostatné položky v dialógu sa skryjú.
* Ak nie je možné zobraziť zoznam článkov, napríklad z dôvodu chýb v
  informačnom kanáli, NVDA zobrazí chybu, takže dialógové okno informačných
  kanálov sa dá použiť bez reštartovania NVDA.

## Zmeny vo verzii 6.0 ##

* Po aktualizácii predvoleného informačného kanála a jeho nefunkčnosti z
  dôvodu problémov so serverom sa predchádzajúce články neodstránia a dajú
  sa prečítať pomocou klávesových skratiek.
* Predvolený informačný kanál možno znova aktualizovať dvakrát.

## Zmeny vo verzii 5.0 ##

* Vylepšené okno so zoznamom článkov.
* Vyžaduje sa NVDA od verzie 2018.3.
* V prípade potreby si môžete stiahnuť [poslednú verziu kompatibilnú s NVDA
  2017.3] [3].

## Zmeny vo verzii 4.0 ##

* Pridané tlačidlo na otvorenie vybraného informačného kanála v dialógovom
  okne Informačné kanály.

## Zmeny vo verzii 3.0 ##

* Dialógové okná na správu súborov informačného kanála boli
  odstránené. Funkcie sú zahrnuté v dialógovom okne Informačné kanály.
* Vylepšená vizuálna prezentácia dialógov.
* Predvolený informačný kanál je uložený v nastaveniach NVDA. Preto je možné
  mať v rôznych profiloch rôzne predvolené informačné kanály.
* Vyžaduje NVDA 2016.4.


## Zmeny vo verzii 2.0 ##

* Návod k doplnku nájdete v správcovi doplnkov.

## Zmeny vo verzii 1.0 ##

* Prvé vydanie.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev

[3]: https://addons.nvda-project.org/files/get.php?file=rf-o
