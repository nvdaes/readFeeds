# Čitaj feedove (Read Feeds) #

* Autori: Noelia Ruiz Martínez, Mesar Hameed
* Preuzmi [stabilnu verziju][1] (kompatibilna s NVDA 2019.3 i novijom)
* Preuzmi [beta verziju][2] (kompatibilna s NVDA 2019.3 i novijom)

Ovaj dodatak pruža najbolji način za čitanje feedova u Atom ili RSS formatu
koristeći NVDA. Feedovi se neće automatski aktualizirati. U daljnjem tekstu,
kad govorimo o feedovima, podrazumijevamo RSS i ATOM feedove.

## Naredbe ##

### Dijaloški okvir „Čitaj feedove” ###

Dijaloški okvir „Čitaj feedove” se nalazi u NVDA izborniku, u podizborniku
„Alati”, stavka „Feedovi”.

Sadrži sljedeće kontrole:

* Filtriraj prema: Uređivačko polje za pretraživanje prethodno spremljenih
  feedova.
* Popis spremljenih feedova, fokusiran kad se otvori dijaloški okvir.
* Popis članaka: Otvara dijaloški okvir koji prikazuje popis članaka iz
  trenutačnog feeda. Odaberi članak koji želiš čitati i pritisni „Enter” ili
  gumb „Otvori web stranicu odabranog članka”. Time se otvara odgovarajuća
  stranica u tvom pregledniku. Pritiskom gumba „O članku”, otvara se
  dijaloški okvir koji sadrži naslov i poveznicu odabranog članka. U ovom
  dijaloškom okviru možeš kopirati te informacije u međuspremnik.
* Otvori feed: Otvara odabrani feed u zadanoj aplikaciji.
* Otvori feed kao HTML: otvara odabrani feed u zadanom web pregledniku. Moći
  ćeš prikazati ili sakriti datume objavljivanja i gumbe za kopiranje
  informacija o člancima u međuspremnik.
* Kopiraj adresu feeda: otvara dijaloški okvir za potvrđivanje kopiranja
  adrese feeda u međuspremnik.
* Novi: Otvara dijaloški okvir s uređivačkim poljem za unos adrese novog
  feeda. Ako je adresa ispravna i ako se feed može spremiti, njegov naziv
  (izveden iz naslova feeda) će se pojavit na dnu popisa feedova.
* Preimenuj: Otvara dijaloški okvir s uređivačkim poljem za preimenovanje
  odabranog feeda.
* Izbriši: Otvara dijaloški okvir za brisanje odabranog feeda nakon
  potvrđivanja.
* Postavi kao zadani: Postavlja odabrani sažetak kao zadani, tako da se tim
  člancima može pristupiti koristeći NVDA geste.
* Uvezi feedove iz OPML datoteke: Otvara dijaloški okvir za dodavanje novih
  sažetaka iz OPML datoteke.
* Spremi feedove u OPML datoteku: Otvara dijaloški okvir za spremanje
  sažetaka dostupnih iz dijaloškog okvira „Feedovi” u OPML datoteci.
* Postavke: otvara dijaloški okvir postavki za „Čitaj feedove”, također
  dostupan u NVDA izborniku, Postavke, postavke, kategorija readFeeds.
* Zatvori: Zatvara dijaloški okvir „Feedovi”.

### Bilješke #####

* Polje za uređivanje „Filtriraj prema”, može se smjestiti nakon gumba
  „Otvori članak” u NVDA izborniku, „Postavke”, „Postavke”, kategorija
  „Čitaj feedove” ili pritisni gumb „Postavke” u dijaloškom okviru
  „Feedovi”.
* Ova ploča ima opciju za prikaz datuma članaka u dijaloškom okviru popisa
  članaka.


### Tipkovnički prečaci ###

* Kontrol+šift+NVDA+razmaknica: Najavljuje adresu trenutačnog
  članka. Dvostrukim pritiskom otvorit će se web stranica.
* Kontrol+šift+NVDA+8: Aktualizira odabrani feed i najavljuje njegov
  najnoviji naslov.
* Kontrol+šift+NVDA+I: Najavljuje naslov trenutačnog feeda i
  poveznicu. Dvostrukim pritiskom kopirat će se naslov i poveznica u
  međuspremnik.
* Kontrol+šift+NVDA+U: Najavljuje naslov prethodnog feeda.
* Kontrol+šift+NVDA+O: Najavljuje naslov sljedećeg feeda.

## Obavijesti ##

* Kad su naslov ili URL adresa kopirani.
* Kad povezivanje ili aktualiziranje feeda nije moguće ili kad URL adresa ne
  odgovara ispravnom feedu.
* NVDA će prikazati poruku greške ako nije moguće stvoriti nov feed.
* Naslov dijaloškog okvira popisa članaka prikazuje odabrani naziv feeda i
  broj dostupnih stavki.

## Promjene u verziji 21.0

* Feedovi s člancima bez naslova mogu se prikazati u dijaloškom okviru
  Članci i otvoriti kao HTML.

## Promjene u verziji 20.0

* universalFeedParser je aktualiziran na 5.0.1, dodajući podršku za više
  feedova.

## Promjene u verziji 14.0

* Ispravljena je greška koja je onemogućavala dodavanje nekih feedova.

## Promjene u verziji 13.0

* Dodatak se ne može koristiti u sigurnim ekranima.
* Feedovima se upravlja iz OPML datoteka.
* Zbog promjena u sustavu upravljanja feedovima dolazi do promjena u
  konfiguracijskoj datoteci u kojoj je postavljen zadani feed. Koristi
  dijaloški okvir „Feedovi” ako ga želiš ponovo postaviti.
* Tvoje stare tekstualne datoteke korištene u prethodnim verzijama
  automatski će se uvesti u novi OPML format kad se dodatak pokrene.
* Funkcija kopiranja i vraćanja feedova zamijenjena je s mogućnošću uvoza iz
  i spremanja u OPML datoteke.
* Loše formatirani feedovi mogu se obraditi prije dodavanja kako bi bili
  kompatibilni s dodatkom.
* Na ploči postavki „Čitaj feedove”, nova opcija omogućuje prikaz datuma
  članaka u dijaloškom okviru popisa članaka.

## Promjene u verziji 12.0

* Ispravljena je greška zbog koje prečaci za stavke izbornika NVDA alata ne
  rade na očekivan način.

## Promjene u verziji 11.0

* Kompatibilno s NVDA 2021.1

## Promjene u verziji 10.0 ##

* Dodan je gumb za otvaranje odabranog feeda kao HTML u standardnom web
  pregledniku.
* Ako se novi feed ne može stvoriti, o tome će se obavijestiti u dijaloškom
  okviru grešaka.
* Poboljšan je redoslijed i prezentacija nekih članaka.
* Moguće je podržati više feedova.
* Kad se otvori dijaloški okvir „Feedovi”, umjesto polja za uređivanje
  pretraživanja, fokusirat će se popis feedova.
* Možeš odabrati, hoće li se polje za uređivanje pretraživanja nalaziti
  nakon popisa feedova. To je korisno za fokusiranje popisa čak i kad se
  prebacuješ iz jednog drugog prozora, bez da zatvoriš dijaloški okvir
  „Feedovi”.
* Dodan je gumb za kopiranje adrese feeda u međuspremnik iz dijaloškog
  okvira „Feedovi”.

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

* Dijaloški okvir „Feedovi” sadrži gumb za otvaranje mape koja može sadržati
  sigurnosnu kopiju feedova.
* Kad se koristi okvir za uređivanje za filtriranje feedova, ako nema
  rezultata, popis feedova i ostale kontrole su deaktivirane. Na taj način
  NVDA ne javlja „nepoznato” u praznom popisu.
* Ako se dijalog s popisom članaka ne može prikazati, primjerice zbog
  grešaka u feedu, NVDA će javiti grešku, tako da se dijaloški okvir
  „Feedovi” može koristiti bez ponovnog pokretanja NVDA čitača.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds

[2]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=rf-o
