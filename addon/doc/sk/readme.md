# RSS čítačka #

* Autori: Noelia Ruiz Martínez, Mesar Hameed
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

- Zoznam článkov... Zobrazí zoznam článkov z aktuálneho zdroja. Vyberte
článok, ktorý chcete čítať a stlačte OK, čím otvoríte článok v predvolenom
webovom prehliadači. - Dočasná adresa zdroja... ctrl + NVDA + shift + enter:
Otvorí dialóg na zadanie novej adresy zdroja alebo vybratie zdroja. V
dialógu sa zobrazí aktuálna adresa. - Načítať adresu zdroja zo
súboru... NVDA+ctrl+enter: Otvorí dialóg, v ktorom môžete vybrať súbor s
adresou zdroja. - Uložiť adresu aktuálneho zdroja do
súboru... NVDA+shift+enter: Otvorí dialóg, v ktorom môžete vybrať súbor, kam
sa uloží adresa aktuálneho zdroja. Ak súbor pomenujete addressfile.txt,
adresa z tohto súboru sa použije ako adresa pre predvolený kanál. - Načítať
nové články: ctrl+shift+NVDA+8: Načíta nové články zo zdroja. Články sa
nenačítavajú automaticky po spustení doplnku. - Zálohovať priečinok s
dátami... Umožňuje vybrať priečinok, do ktorého sa uložia zdroje
informačných kanálov. Predvolený priečinok je priečinok s používateľskými
dátami NVDA, kde sa vytvorí priečinok personalFeeds. - Obnoviť zdroje zo
zálohy... Nahradí adresy z vybratého priečinka. Uistite sa, že ste vybrali
priečinok, ktorý skutočne obsahuje adresy zdrojov.

### Klávesové skratky: ###

- Ctrl+Shift+NVDA+medzera: Oznámy adresu článku. Stlačené dvakrát otvorí
odkaz vo webovom prehliadači. - Ctrl+Shift+NVDA+8: Načíta nové články z
aktuálneho zdroja a oznámy názov najnovšieho článku. - Ctrl+Shift+NVDA+I:
Oznámy názov aktuálneho zdroja. Stlačené dvakrát skopíruje názov do
schránky. - Ctrl+Shift+NVDA+U: Oznámy názov predchádzajúceho článku. -
Ctrl+Shift+NVDA+O: Oznámy názov nasledujúceho článku.

## Oznámenia: ##

- Ak je skopírovaný názov alebo adresa. - Ak sa nepodarilo získať nové
články alebo adresa odkazuje na neplatný zdroj. - NVDA zobrazí chybu, ak sa
nepodarilo vytvoriť zálohu. - Titulok okna s článkami zobrazuje názov zdroja
a počet článkov.

## Zmeny pre verziu 1.0 ##
*	 Prvé vydanie.

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

