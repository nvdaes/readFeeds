# RSS Čítačka #

* Autori: Noelia Ruiz Martínez, Mesar Hameed
* NVDA compatibility: 2018.3 to 2019.2
* Stiahnuť [stabilná verzia][1]
* Stiahnúť [Vývojovú verziu ][2]

Tento doplnok poskytuje jednoduchý spôsob čítania kanálov vo formátoch Atom
alebo RSS pomocou NVDA. Kanály sa neobnovia automaticky. Nižšie, keď
spomíname informačné kanály, máme na mysli informačné kanály RSS aj ATOM.

## Inštalácia alebo aktualizácia: ##

Ak ste použili predchádzajúcu verziu tohto doplnku a vo vašom osobnom
konfiguračnom priečinku NVDA sa nachádza priečinok RSS alebo personalFeeds,
pri inštalácii aktuálnej verzie sa zobrazí dialógové okno s otázkou, či
chcete aktualizovať alebo nainštalovať. Vyberte aktualizáciu, aby ste
zachovali uložené kanály a pokračovali v ich používaní v novej
nainštalovanej verzii readFeeds.

## Príkazy: ##

### Menu RSS čítačky ###

Menu RSS čítačky je dostupné z menu NVDA (nvda+n) a obsahuje tieto možnosti:

#### Informačné kanály... ####

Otvorí dialógové okno s nasledujúcimi ovládacími prvkami:

* Filtrovať podľa: Editačné pole na vyhľadávanie predtým uložených kanálov.
* Zoznam uložených informačných kanálov.
* Zoznam článkov: Otvorí sa dialógové okno, ktoré predstavuje zoznam článkov
  z vášho aktuálneho informačného kanála. Vyberte článok, ktorý si chcete
  prečítať, a stlačte kláves Enter alebo Otvoriť webovú stránku tlačidla
  vybraného článku, aby ste otvorili príslušnú stránku v
  prehliadači. Stlačením tlačidla Informácie o článku otvoríte dialógové
  okno s názvom a odkazom na vybraný článok; z tohto dialógového okna budete
  môcť tieto informácie skopírovať do schránky.
* Otvoriť informačný kanál: Otvorí vybraný informačný kanál v predvolenej
  aplikácii.
* Nové: otvorí dialógové okno s editovaním zadajte adresu nového
  informačného kanála. Ak je adresa platná a informačný kanál je možné
  uložiť, v spodnej časti zoznamu informačných kanálov sa zobrazí jeho názov
  na základe názvu informačného kanála.
* Premenovať: Otvorí dialógové okno s editovaným na premenovanie vybraného
  informačného kanála.
* Odstrániť: Otvorí sa dialógové okno, ktoré po potvrdení odstráni vybraný
  informačný kanál.
* Nastaviť predvolené: Nastaví vybraný informačný kanál ako predvolený, aby
  k jeho článkom bolo možné pristupovať pomocou gesta NVDA.
* Otvoriť priečinok obsahujúci zálohu zdrojov: Otvorí priečinok, ktorý môže
  obsahovať zálohu zdrojov. To môže byť užitočné pri skúmaní a odstraňovaní
  informačných kanálov, ktoré by sa po aktualizácii doplnku nemali
  importovať.
* Zatvoriť: Zatvorí dialógové okno informačné kanály

##### Poznámky #####

* Ak sa vytvorí informačný kanál s názvom tempFeed, premenujte ho, pretože v
  prípade potreby je možné tento súbor nahradiť a vytvoriť informačný kanál,
  ktorého názov už existuje.
* Zdroj nastavený ako predvolený nie je možné odstrániť. Informačný kanál
  AddressFile sa použije ako predvolený pri resetovaní konfigurácie, takže
  ho nemožno odstrániť.

Skopýrovať priečinok informačného kanála...

Otvorí dialógové okno pre výber priečinka, do ktorého si môžete uložiť
priečinok personalFeeds vašich informačných kanálov. V predvolenom nastavení
je vybratý priečinok konfiguračným adresárom NVDA, ktorý vytvorí adresár
personalFeeds.

#### Obnoviť informačné kanály... ####

Otvorí dialógové okno pre výber priečinka, ktoré nahradí vaše informačné
kanály v priečinku personalFeeds. Nezabudnite načítať priečinok obsahujúci
adresy URL informačných kanálov.

### Klávesové skratky: ###

* Ctrl+Shift+NVDA+Medzera: Oznamuje URL aktuálneho článku. Stlačené dva-krát
  otvorí webovú stránku.
* Ctrl+Shift+NVDA+8: Obnoví vybraný informačný kanál a oznámi jeho najnovšiu
  aktualizáciu.
* Ctrl+Shift+NVDA+I: Oznamuje aktuálny názov informačného kanála a
  odkaz. Stlačené dva-krát sa skopíruje názov a odkaz do schránky.
* Ctrl+Shift+NVDA+U: Oznamuje predchádzajúci názov informačného kanála.
* Ctrl+Shift+NVDA+O: Oznamuje ďalší názov informačného kanála.

## Oznámenia: ##

* Po skopírovaní názvu alebo adresy URL.
* Ak sa nedá pripojiť/obnoviť informačný kanál alebo webová adresa
  nezodpovedá platnému informačnému kanálu.
* NVDA zobrazí chybové hlásenie, ak nebolo možné zálohovať alebo obnoviť
  priečinok personalFeeds.
* Názov dialógového okna so zoznamom článkov obsahuje vybratý názov
  informačného kanála a počet dostupných položiek.

## Changes for 8.0 ##

* When the add-on is updated, feeds saved in the previous version of the
  add-on will be automatically copied to the new version, unless you prefer
  to import feeds saved in the main configuration folder of NVDA.
* When using the dialog to copy feeds, if the chosen folder is not named
  personalFeeds, a subfolder with this name will be created to prevent the
  deletion of directories containing important data, such as Documents or
  Downloads.

## Zmeny vo verzii 7.0 ##

* Dialógové okno Kanály obsahuje tlačidlo na otvorenie priečinka, ktorý môže
  obsahovať zálohu informačných kanálov.
* Ak sa na filtrovanie kanálov používa editovacie pole, ak sa nenájdu žiadne
  výsledky, zoznam informačných kanálov a ďalších ovládacích prvkov sa
  deaktivuje, takže NVDA v prázdnom zozname nehlási „neznámy“.
* Ak nie je možné zobraziť zoznam článkov, napríklad z dôvodu chýb v
  informačnom kanáli, NVDA vyvolá chybu, takže dialógové okno informačných
  kanálov sa dá použiť bez reštartovania NVDA.

## Zmeny vo verzii 6.0 ##

* Po aktualizácii predvoleného informačného kanála a jeho zastavení z dôvodu
  problémov so serverom sa predchádzajúce články neodstránia a dajú sa
  prečítať pomocou zodpovedajúcich stlačení klávesov.
* Opraviť regresiu: Predvolený informačný kanál možno znova aktualizovať
  dvakrát.

## Zmeny vo verzii 5.0 ##

* Dialógové okno so zoznamom článkov bolo vylepšené.
* Kompatibilné s NVDA 2018.3 alebo novším (povinné).
* V prípade potreby si môžete stiahnuť [poslednú verziu kompatibilnú s NVDA
  2017.3] [3].

## Zmeny vo verzii 4.0 ##

* Pridané tlačidlo na otvorenie vybraného informačného kanála v dialógovom
  okne Informačné kanály.

## Zmeny vo verzii 3.0 ##

* Dialógové okná na správu súborov informačného kanála boli odstránené. Ich
  funkčnosť je teraz zahrnutá v dialógovom okne Informačné kanály.
* Vizuálna prezentácia dialógov bola vylepšená, pričom sa zachovala podoba
  dialógov zobrazených v NVDA.
* Predvolený informačný kanál je uložený v konfigurácii NVDA. Preto je možné
  v konfiguračných profiloch nastaviť rôzne predvolené informačné kanály.
* Vyžaduje NVDA 2016.4.


## Zmeny vo verzii 2.0 ##

* Návod k doplnku nájdete v správcovi doplnkov.

## Zmeny vo verzii 1.0 ##

* Prvé vydanie.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev

[3]: https://addons.nvda-project.org/files/get.php?file=rf-o
