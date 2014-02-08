# RSS čítačka #

* Autori: Noelia Ruiz Martínez, Mesar Hameed
* Stiahnuť [stabilná verzia][2]
* Stiahnúť [Vývojovú verziu ][1]

Tento doplnok umožňuje čítať RSS a atom zdroje priamo v NVDA. Zdroje sa
neobnovujú automaticky. Doplnok podporuje formát RSS a Atom.

## Inštalácia a aktualizácia ##

Ak ste doposiaľ používali tento doplnok a v priečinku s dátami NVDA sú
uložené zdroje, pri inštalácii verzie 6.0 a novšej sa zobrazí dialóg, v
ktorom môžete rozhodnúť, či chcete aktualizovať, alebo novú
inštaláciu. Vyberte aktualizovať, ak chcete naďalej používať uložené zdroje.

## Príkazy: ##

### Menu RSS čítačky ###

Menu RSS čítačky je dostupné z menu NVDA (nvda+n) a obsahuje tieto možnosti:

*	 Zoznam článkov... Zobrazí zoznam článkov pre aktuálny informačný
   kanál. Vyberte požadovaný článok a stlačte tlačidlo OK, aby ste ho
   otvorili v predvolenom prehliadači.
*	 Dočasná adresa zdroja... ctrl + NVDA + shift + enter: V dialógu môžete
   zadať adresu nového informačného kanála. V editačnom poli sa zobrazí
   aktuálna adresa.
*	 Načítať adresu kanála zo súboru... NVDA+ctrl+enter: Umoňuje vybrať súbor,
   v ktorom je uložená adresa informačného kanála.
*	 Uložiť aktuálnu adresu zdroja do súboru... NVDA+shift+enter: Zobrazí
   dialóg, v ktorom môžete uložiť aktuálnu adresu kanála do súboru. Ak súbou
   ložíte pod názvom addressFile.txt, kanál z tohto sboru bude použitý ako
   predvolený zdroj.
*	 Načítať nové články: ctrl+shift+NVDA+8: Skontroluje nové články f
   informačnom kanály. Nové články sa nekontrolujú automaticky po spustení
   doplnku.
*	 Zálohovať priečinok s dátami... Ujožňuje zálohovať priečinok s
   kanálmi. Predvolene je tento priečinok v priečinku s nastaveniami nvda
   pod názvom PersonalFeeds.
*	 obnoviť zdroje zo zálohy... Umožňuje nahradiť aktuálne informačné zdroje
   priečinkom zo zálohy. Uistite sa, že vyberiete priečinok, ktorí obsahuje
   platné adresy zdrojov.

### Klávesové skratky: ###

*	 Ctrl+Shift+NVDA+medzera: Oznámi adresu článku. Stlačené dvakrát otvorí
   článok v predvolenom prehliadači.
*	 Ctrl+Shift+NVDA+8: obnoví zoznam článkov a oznámy najnovší článok.
*	 Ctrl+Shift+NVDA+I: Oznámy názov informačného kanála. Stlačené dvakrát
   skopíruje názov do shránky.
*	 Ctrl+Shift+NVDA+U: Povie n ázov predchádzajúceho článku.
*	 Ctrl+Shift+NVDA+O: Prečíta názov nasledujúceho článku.

## Oznámenia: ##

*	 Keď bola skopírovaná adresa alebo názov článku.
*	 Ak sa nepodarilo pripojiť na adresu alebo obnoviť články, alebo adresa
   neobsahuje platný RSS zdroj.
*	 NVDA zobrazí chybu, ak sa nepodarí zálohovať priečinok s dátami.
*	 V názve okna môžete vidieť názov informačného kanála a počet príspevkov,
   ktoré obsahuje.

## Zmeny pre verziu 1.0 ##
*	 Prvé vydanie.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

