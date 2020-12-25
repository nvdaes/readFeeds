# Čitaj feedove (Read Feeds) #

* Autori: Noelia Ruiz Martínez, Mesar Hameed
* NVDA kompatibilnost: 2019.3 i novija
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]


Ovaj dodatak pruža najbolji način za čitanje feedova u Atom ili RSS formatu
koristeći NVDA. Feedovi se neće automatski aktualizirati. U daljnjem tekstu,
kad govorimo o feedovima, podrazumijevamo RSS i ATOM feedove.

## Installation or Update ##

Ako već koristiš prijašnju verziju ovog dodatka i ako postoji mapa „RSS” ili
„personalFeeds” (mapa osobnih feedova) u vašoj mapi NVDA konfiguracije,
tijekom instaliranja aktualne verzije će dijaloški okvir pitati, želiš li
nadograditi ili instalirati dodatak. Odaberi nadogradnju, kako bi se
sačuvali prethodno spremljeni feedovi i nastavili koristiti u novoj
instaliranoj verziji dodatka „Čitaj feedove”.

## Commands ##

### Izbornik „Čitaj feedove” ###

Podizbornik „Čitaj feedove” se nalazi u NVDA izborniku, u podizborniku
Alati, gdje su dostupne sljedeće opcije:

#### Feeds ####

Otvara dijaloški okvir sa sljedećim kontrolama:

* Filtriraj prema: Uređivačko polje za pretraživanje prethodno spremljenih
  feedova.
* A list of the saved feeds, focused when the dialog is opened.
* Popis članaka: Otvara dijaloški okvir koji prikazuje popis članaka iz
  trenutačnog feeda. Odaberi članak koji želiš čitati i pritisni „Enter” ili
  gumb „Otvori web stranicu odabranog članka”. Time se otvara odgovarajuća
  stranica u tvom pregledniku. Pritiskom gumba „O članku”, otvara se
  dijaloški okvir koji sadrži naslov i poveznicu odabranog članka. U ovom
  dijaloškom okviru možeš kopirati te informacije u međuspremnik.
* Otvori feed: Otvara odabrani feed u zadanoj aplikaciji.
* Open feed as HTML: Opens the selected feed in the default web browser. You
  will be able to show or hide publication dates and buttons to copy
  information about articles to clipboard.
* Copy feed address: Opens a dialog to confirm if you want to copy the feed
  address to clipboard.
* Novi: Otvara dijaloški okvir s uređivačkim poljem za unos adrese novog
  feeda. Ako je adresa ispravna i ako se feed može spremiti, njegov naziv
  (izveden iz naslova feeda) će se pojavit na dnu popisa feedova.
* Preimenuj: Otvara dijaloški okvir s uređivačkim poljem za preimenovanje
  odabranog feeda.
* Izbriši: Otvara dijaloški okvir za brisanje odabranog feeda nakon
  potvrđivanja.
* Postavi kao zadani: Postavlja odabrani sažetak kao zadani, tako da se tim
  člancima može pristupiti koristeći NVDA geste.
* Otvori mapu sa sigurnosnim kopijama feedova: Otvara mapu koja može
  sadržavati sigurnosnu kopiju feedova. Ovo može biti korisno za
  istraživanje i brisanje feedova, koje ne treba uvoziti kad se dodatak
  nadogradi.
* Preferences: Opens the settings dialog for readFeeds, also available in
  NVDA's menu, Preferences, settings, readFeeds category.
* Zatvori: Zatvara dijaloški okvir „Feedovi”.

##### Napomene #####

* Ako se stvori feed pod nazivom „tempFeed”, preimenuj ga, kako bi se ta
  datoteka mogla zamijeniti u slučaju da treba stvoriti feed s nazivom koji
  već postojeći.
* Feed koji je postavljen kao zadani se ne može ukloniti. Feed „addressFile”
  će se koristiti kao zadani kad se konfiguracija ponovo postavi, te se
  stoga ne može ukloniti.
* The Filter by edit box can be placed after the Open article button from
  NVDA's menu, Preferences, Settings, Read feeds category, or pressing the
  Preferences button of the Feeds dialog.

#### Copy feeds folder ####

Otvara dijaloški okvir za odabir mape za spremanje „personalFeeds” mape s
osobnim feedovima. Za to se standardno koristi mapa NVDA konfiguracije, gdje
će se stvoriti „personalFeeds” mapa.

#### Restore feeds ####

Otvara dijaloški okvir za odabir mape koja zamjenjuje feedove u
„personalFeeds” mapi osobnih feedova. Mapa koju učitaš mora sadrži URL
adrese feedova.

### Keyboard commands ###

* Kontrol+šift+NVDA+razmaknica: Najavljuje adresu trenutačnog
  članka. Dvostrukim pritiskom otvorit će se web stranica.
* Kontrol+šift+NVDA+8: Aktualizira odabrani feed i najavljuje njegov
  najnoviji naslov.
* Kontrol+šift+NVDA+I: Najavljuje naslov trenutačnog feeda i
  poveznicu. Dvostrukim pritiskom kopirat će se naslov i poveznica u
  međuspremnik.
* Kontrol+šift+NVDA+U: Najavljuje naslov prethodnog feeda.
* Kontrol+šift+NVDA+O: Najavljuje naslov sljedećeg feeda.

## Notifications ##

* Kad su naslov ili URL adresa kopirani.
* Kad povezivanje ili aktualiziranje feeda nije moguće ili kad URL adresa ne
  odgovara ispravnom feedu.
* NVDA will display an error message if it was not possible to backup or
  restore the personalFeeds folder, and if a new feed cannot be created.
* Naslov dijaloškog okvira popisa članaka prikazuje odabrani naziv feeda i
  broj dostupnih stavki.

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

## Promjene u verziji 9.0 ##

* Zahtijeva NVDA verziju 2019.3 ili noviju.

## Promjene u verziji 8.0 ##

* Kad se dodatak nadogradi, spremljeni feedovi u prethodnoj verziji dodatka,
  automatski će se kopirati u novu verziju, osim ako želoš uvesti feedove
  koji su spremljeni u glavnoj konfiguracijskoj mapi NVDA čitača.
* Kad se koristi dijaloški okvir za kopiranje feedova, ako se odabrana mapa
  ne zove „personalFeeds”, stvorit će se podmapa s tim nazivom, kako bi se
  spriječilo brisanje mapa koje sadrže važne podatke, poput mape Dokumenti
  ili mape Preuzimanja.

## Promjene u verziji 7.0 ##

* Dijalog „Feedovi” sadrži gumb za otvaranje mape koja može sadržati
  sigurnosnu kopiju feedova.
* Kad se koristi okvir za uređivanje za filtriranje feedova, ako nema
  rezultata, popis feedova i ostale kontrole su deaktivirane. Na taj način
  NVDA ne javlja „nepoznato” u praznom popisu.
* Ako se dijalog s popisom članaka ne može prikazati, primjerice zbog
  grešaka u feedu, NVDA će javiti grešku, tako da se dijaloški okvir s
  feedovima može koristiti bez ponovnog pokretanja NVDA čitača.

## Promjene u verziji 6.0 ##

* Kad je zadani feed aktualiziran i prestane raditi zbog problema s
  poslužiteljem, prethodni se članci ne brišu i mogu se pročitati s
  odgovarajućim tičkovničkim prečacima.
* Regresija popravka: Zadani feed se ponovo može aktualizirati dva puta.

## Promjene u verziji 5.0 ##

* Poboljšan je dijaloški okvir popisa članaka.
* Kompatibilno s NVDA 2018.3 i novijim verzijama (obavezno).
* Ako treba, moguće je preuzeti [zadnju verziju kompatibilnu s NVDA
  2017.3][3].

## Promjene u verziji 4.0 ##

* Dodan je gumb za otvaranje odabranog feeda iz dijaloškog okvira „Feedovi”.

## Promjene u verziji 3.0 ##

* Dijaloški okviri za upravljanje datotekama feedova su uklonjeni. Njihova
  funkcionalnost je sada uključena u dijaloški okvir „Feedovi”.
* Poboljšan je vizualni prikaz dijaloških okvira, u skladu s prikazom
  dijaloških okvira u NVDA čitaču.
* Zadani feed se sprema u NVDA konfiguraciju. Na taj način je moguće
  postaviti razne zadane feedove u konfiguracijskim profilima.
* Zahtijeva NVDA 2016.4.

## Promjene u verziji 2.0 ##

* Pomoć za ovaj dodatak je dostupna u upravljaču za dodatke.

## Promjene u verziji 1.0 ##

* Prva verzija.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev

[3]: https://addons.nvda-project.org/files/get.php?file=rf-o
