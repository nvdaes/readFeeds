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

- Article list...  Presents the article list from your current feed. Select
the article you want to read and press OK button to open the corresponding
page in your browser.  - Temporary feed address... control + NVDA + shift +
enter: Opens a dialog for typing a new URL to select another feed. The
current URL will be shown in this dialog.  - Load feed address from
file... NVDA+control+enter: Opens a dialog to select a feed from a saved
file containing a feed URL.  - Save current feed address to
file... NVDA+shift+enter: opens a dialog for selecting the file where
current feed URL will be saved.  If you save to the special file
addressFile.txt, this particular feed will be used as your default feed.  -
Refresh current feed: control+shift+NVDA+8: Refresh selected feed. The feeds
will not be updated automatically when Read Feeds addon is started.  -
Backup feeds folder...  opens a dialog to choose a folder where you can save
the personalFeeds directory of your feeds. By default the selected folder is
the NVDA's configuration directory, which will create the personalFeeds
directory.  - Restore feeds...  Opens a dialog to select a folder which
replaces your feeds in the personalFeeds folder. Make sure you load a folder
containing feeds URLs.

Note: If you want to delete a previously saved feed URL, just remove the
corresponding file.

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

## Changes for 2.0 ##
*	 Add-on help is available from the Add-ons Manager.

## Zmeny pre verziu 1.0 ##
*	 Prvé vydanie.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

