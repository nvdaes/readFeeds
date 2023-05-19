# RSS Čítačka #

* Autori: Noelia Ruiz Martínez, Mesar Hameed
* Download [stable version][1] (compatible with NVDA 2019.3 and beyond)
* Download [beta version][2] (compatible with NVDA 2019.3 and beyond)

Poskytuje jednoduchý spôsob čítania kanálov vo formátoch Atom alebo RSS
pomocou NVDA. Kanály sa neobnovia automaticky. Nižšie, keď spomíname
informačné kanály, máme na mysli informačné kanály RSS aj ATOM.

## Commands ##

### Read Feeds dialog ###

You can access the Read Feeds dialog from the nvda menu, Tools submenu,
Feeds item.

It contains the following controls:

* Filter: Editačné pole na vyhľadávanie uložených kanálov.
* A list of the saved feeds, focused when the dialog is opened.
* Zoznam článkov: Otvorí zoznam článkov z vášho aktuálneho informačného
  kanála. Vyberte článok, ktorý si chcete prečítať, a stlačte kláves Enter
  alebo tlačidlo Otvoriť webovú stránku, aby ste otvorili príslušnú stránku
  v prehliadači. Stlačením tlačidla Informácie o článku otvoríte dialógové
  okno s názvom a odkazom na vybraný článok; z tohto dialógového okna budete
  môcť tieto informácie skopírovať do schránky.
* Otvoriť informačný kanál: Otvorí vybraný informačný kanál v predvolenej
  aplikácii.
* Open feed as HTML: Opens the selected feed in the default web browser. You
  will be able to show or hide publication dates and buttons to copy
  information about articles to clipboard.
* Copy feed address: Opens a dialog to confirm if you want to copy the feed
  address to clipboard.
* Nový: otvorí dialógové okno, kde môžete vložiť adresu informačného
  kanála. Ak je adresa platná a informačný kanál je možné uložiť, Kanál je
  pridaný na koniec zoznamu kanálov.
* Premenovať: Otvorí dialógové okno v ktorom môžete zadať nový názov kanála.
* Odstrániť: Umožní odstrániť vybratý informačný kanál.
* Nastaviť predvolené: Nastaví vybraný informačný kanál ako predvolený, aby
  k jeho článkom bolo možné pristupovať pomocou klávesových skratiek.
* Import feeds from OPML file: Opens a dialog to add new feeds from an OPML
  file.
* Save feeds to OPML file: Opens a dialog to save the feeds available from
  the Feeds dialog in an OPML file.
* Preferences: Opens the settings dialog for readFeeds, also available in
  NVDA's menu, Preferences, settings, readFeeds category.
* Zatvoriť: Zatvorí dialógové okno informačné kanály.

### Notes #####

* The Filter by edit box can be placed after the Open article button from
  NVDA's menu, Preferences, Settings, Read feeds category, or pressing the
  Preferences button of the Feeds dialog.
* This panel has an option to show article dates on the List of articles
  dialog.


### Keyboard commands ###

* Ctrl+Shift+NVDA+Medzera: Oznamuje URL aktuálneho článku. Stlačené dvakrát
  rýchlo za sebou otvorí webovú stránku.
* Ctrl+Shift+NVDA+8: Obnoví vybraný informačný kanál a oznámi názov
  posledného článku.
* Ctrl+Shift+NVDA+I: Oznamuje aktuálny názov informačného kanála a
  odkaz. Stlačené dvakrát rýchlo za sebou skopíruje názov a odkaz do
  schránky.
* Ctrl+Shift+NVDA+U: oznámi predchádzajúci článok.
* Ctrl+Shift+NVDA+O: Oznámi nasledujúci článok.

## Notifications ##

* Po skopírovaní názvu alebo adresy URL do schránky.
* Ak sa nedá pripojiť/obnoviť informačný kanál alebo webová adresa
  nezodpovedá platnému informačnému kanálu.
* NVDA will display an error message if a new feed cannot be created.
* Názov dialógového okna so zoznamom článkov obsahuje vybratý názov
  informačného kanála a počet dostupných položiek.

## Changes for 21.0

* Feeds with untitled articles can be presented in the Articles dialog, and
  opened as HTML.

## Changes for 20.0

* universalFeedParser is updated to 5.0.1, adding support for more feeds.

## Changes for 14.0

* Fixed a bug that made impossible to add some feeds.

## Changes for 13.0

* The add-on cannot be used on secure screens.
* Feeds are managed from OPML files.
* Due to changes in the feeds management system, there are changes in the
  configuration file where the default feed is set. Please, use the Feeds
  dialog if you want to set it again.
* Your old text files used in previous versions will be automatically
  imported into the new OPML format when the add-on is started.
* The copy and restore feeds feature has been replaced with the ability to
  import from and save to OPML files.
* Non well-formed feeds can be processed before being added to make them
  compatible with the add-on.
* In the Read Feeds settings panel, a new option allows to show article
  dates on the List of articles dialog.

## Changes for 12.0

* Fixed a bug which made shortcuts for items of NVDA's tools menu don't work
  as expected.

## Changes for 11.0

* Compatible with NVDA 2021.1

## Changes for 10.0 ##

* Added a button to open the selected feed as HTML in the default web
  browser.
* If a new feed cannot be created, this will be notified in an error dialog.
* Improved order and presentation of some articles.
* More feeds may be supported.
* When the feeds dialog is opened, the list of feeds will be focused instead
  of the search edit box.
* You can choose if the search edit box is placed after the list of feeds,
  useful to focus the list even when switching from another window without
  closing the Feeds dialog.
* Added a button to copy the feed address to clipboard from the feeds
  dialog.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds

[2]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=rf-o
