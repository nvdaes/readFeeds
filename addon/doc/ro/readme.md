# Read Feeds #

* Autori: Noelia Ruiz Martínez, Mesar Hameed
* NVDA compatibility: 2019.3 or later
* Descărcați [versiunea stabilă][1]
* Descărcați [versiunea în dezvoltare][2]


Acest supliment oferă o modalitate simplă de a citi feed-uri în format Atom
sau RSS folosind NVDA. Feed-urile nu vor fi actualizate în mod
automat. Atunci când menționăm feed-uri, ne referim atât la fluxuri RSS cât
și la cele Atom.

## Installation or Update ##

Dacă ați utilizat o versiune anterioară a acestui add-on și există un dosar
RSS sau un dosar de feed-uri personale în dosarul dumneavoastră de
configurare al NVDA, când se instalează versiunea 6.0 sau mai nou, un dialog
vă va întreba dacă vreți să upgradați sau instalați. Alegeți actualizare
pentru a păstra feed-urile salvate și pentru a continua să le folosiți în
noua versiune instalată a cititorului de feed-uri.

## Commands ##

### Meniul Read Feeds  ###

Puteți accesa submeniul Read Feeds din meniul NVDA, NVDA+N, unde sunt
disponibile următoarele opțiuni:

#### Feeds ####

Deschide un dialog cu următoarele controale:

* Filtrează după: O casetă de editare pentru căutarea fluxurilor salvate
  anterior.
* A list of the saved feeds, focused when the dialog is opened.
* Lista articolelor: Deschide un dialog care  prezintă lista articolelor de
  la fluxul curent. Selectați articolul pe care vreți să îl citiți și
  apăsați Enter sau butonul „Deschide pagina web a articolului selectat”
  pentru a deschide pagina corespunzătoare în navigatorul web. Apăsați
  butonul „Despre articol” pentru a deschide un dialog care arată titlul și
  link-ul articolului selectat; din acest dialog, veți putea să copiați
  aceste informații pe planșetă.
* Deschide flux: Deschide fluxul selectat in aplicația standard
  corespunzătoare.
* Open feed as HTML: Opens the selected feed in the default web browser. You
  will be able to show or hide publication dates and buttons to copy
  information about articles to clipboard.
* Copy feed address: Opens a dialog to confirm if you want to copy the feed
  address to clipboard.
* Nou: Deschide un dialog cu o casetă de editare pentru introducerea adresei
  unui nou flux. Dacă adresa este validă și fluxul poate fi salvat, numele
  său bazat pe titlul acestuia va apărea la sfârșitul listei de fluxuri.
* Redenumire: Deschide un dialog cu o casetă de editare pentru redenumirea
  fluxului selectat.
* Ștergere: Deschide un dialog pentru ștergerea fluxului selectat după
  confirmare.
* Setare ca implicit: Setează fluxul selectat ca implicit, așa că articolele
  sale pot fi accesate cu gesturile NVDA-ului.
* Open folder containing a backup of feeds: Opens a folder which may contain
  a backup of feeds. This can be useful to explore and delete feeds which
  shouldn't be imported when the add-on is updated.
* Preferences: Opens the settings dialog for readFeeds, also available in
  NVDA's menu, Preferences, settings, readFeeds category.
* Închidere: Închide dialogul fluxurilor.

##### Note #####

* Dacă se creează un flux numit tempFeed, vă rugăm să-l redenumiți, deoarece
  acest fișier ar putea fi înlocuit atunci când este necesar pentru a crea
  un flux al cărui nume deja există.
* Fluxul setat ca implicit nu poate fi șters. Fluxul addressFile va fi
  utilizat ca implicit atunci când configurația este resetată, deci nu poate
  fi șters.
* The Filter by edit box can be placed after the Open article button from
  NVDA's menu, Preferences, Settings, Read feeds category, or pressing the
  Preferences button of the Feeds dialog.

#### Copy feeds folder ####

Deschide un dialog pentru a alege un dosar unde să puteți salva dosarul
personalFeeds al fluxurilor dumneavoastră. În mod implicit, folderul
selectat este cel al configurației NVDA, care va crea dosarul personalFeeds.

#### Restore feeds ####

Deschide un dialog pentru selectarea unui dosar care înlocuiește fluxurile
dumneavoastră în dosarul personalFeeds. Asigurați-vă că încărcați un dosar
ce conține URL-urile fluxurilor.

### Keyboard commands ###

* Ctrl+Shift+NVDA+Spațiu: Anunță URL-ul articolului curent. Apăsarea de două
  ori va deschide pagina web.
* Ctrl+Shift+NVDA+8: Reîmprospătează fluxul selectat și anunță cel mai
  recent titlu al său.
* Ctrl+Shift+NVDA+I: Anunță titlul fluxului curent și link-ul
  acestuia. Apăsarea de două ori va copia titlul și link-ul relatat pe
  planșetă.
* Ctrl+Shift+NVDA+U: Anunță titlul fluxului precedent.
* Ctrl+Shift+NVDA+O: Anunță titlul fluxului succedent.

## Notifications ##

* Când titlul sau URL-ul a fost copiat.
* Atunci când nu se poate conecta/reîmprospăta un flux, sau URL-ul nu
  corespunde unui flux valid.
* NVDA will display an error message if it was not possible to backup or
  restore the personalFeeds folder, and if a new feed cannot be created.
* Dialogul titlului listei articolelor afișează numele fluxului selectat și
  numărul elementelor disponibile.

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

## Changes for 9.0 ##

* Requires NVDA 2019.3 or later.

## Changes for 8.0 ##

* When the add-on is updated, feeds saved in the previous version of the
  add-on will be automatically copied to the new version, unless you prefer
  to import feeds saved in the main configuration folder of NVDA.
* When using the dialog to copy feeds, if the chosen folder is not named
  personalFeeds, a subfolder with this name will be created to prevent the
  deletion of directories containing important data, such as Documents or
  Downloads.

## Changes for 7.0 ##

* The Feeds dialog includes a button to open a folder which may contain a
  backup of feeds.
* When using the edit box to filter feeds, if no results are found, the list
  of feeds and other controls are disabled, so that NVDA doesn't report
  "unknown" in the empty list.
* If the list of articles dialog can't be shown, for example due to errors
  in the feed, NVDA will raise an error, so that the feeds dialog can be
  used without restarting NVDA.

## Modificări în 6.0 ##

* Când fluxul implicit a fost actualizat și nu se nu mai funcționează
  datorită problemelor de server, articolele precedente nu sunt șterse și
  pot fi citite cu combinații de taste corespondente.
* rezolvare: fluxul implicit poate fi actualizat de două ori.

## Modificări în 5.0 ##

* A fost îmbunătățit dialogul listei articolelor.
* Compatibil cu NVDA 2018.3 sau mai nou (necesar).
* Dacă e musai, puteți descărca [ultima versiune compatibilă cu NVDA
  2017.3][3].

## Modificări în 4.0 ##

* S-a adaugat un buton pentru deschiderea fluxului selectat din dialogul
  pentru alegerea fluxurilor.

## Modificări în 3.0 ##

* Dialogul pentru administrarea fișierelor fluxurilor a fost eliminat. În
  prezent, funcționalitatea lui este inclusă în dialogul fluxurilor.
* Prezentarea vizuală a dialogurilor a fost îmbunătățită, aderând la
  aspectul dialogurilor afișate în NVDA.
* Fluxul implicit este salvat în configurația NVDA. Prin urmare, este
  posibilă setarea fluxurilor implicite diferite în configurarea
  profilurilor.
* Necesită NVDA 2016.4.

## Modificări în 2.0 ##

* Ghidul suplimentului este disponibil în managerul de add-on-uri.

## Modificări în 1.0 ##

* Versiunea inițială.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev

[3]: https://addons.nvda-project.org/files/get.php?file=rf-o
