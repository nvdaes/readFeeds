# Čitaj sažetke #

* Autori: Noelia Ruiz Martínez, Mesar Hameed 
* Preuzmi [stabilnu inačicu][1]
* Preuzmi [razvojnu inačicu][2]

Ovaj dodatak pruža najbolji način za čitanje sažetaka u Atom ili RSS formatu
koristeći NVDA. Sažeci se neće automatski iznova učitavati. Kada u daljnjem
tekstu spomenemo sažetke, pritom mislimo i na RSS i na ATOM sažetke.

## Instalacija ili Ažuriranje: ##

Ako ste koristili prethodnu inačicu ovog dodatka i ako postoji mapa RSS ili
osobnih sažetaka u vašoj mapi konfiguracije NVDA, tijekom instalacije
trenutne verzije dijaloški okvir će vas pitati želite li nadograditi ili
instalirati dodatak. Odaberite nadogradnju da biste sačuvali prethodno
spremljene sažetke i nastavili ih koristiti u novoj instaliranoj verziji
readFeeds dodatka.

## Komande: ##

### Read Feeds izbornik  ###

Možete pristupiti podizborniku Read Feeds iz izbornika NVDA, podizbornika
Alati, gdje su dostupne sljedeće opcije:

#### Sažeci... ####

Otvara dijaloški okvir sa sljedećim kontrolama:

* Filtriraj prema: Uređivačko polje za pretraživanje prethodno spremljenih
  sažetaka.
* Popis spremljenih sažetaka.
* Popis članaka: Otvara dijaloški okvir koji prikazuje popis članaka iz
  trenutnog sažetka.Odaberite članak koji želite čitati i pritisnite gumb OK
  kako biste otvorili odgovarajuću stranicu u vašem pregledniku.
* Otvori sažetak: Otvara odabrani sažetak u zadanoj aplikaciji.
* Novi: Otvara dijaloški okvir s uređivačkim poljem za unos adrese novog
  sažetka. Ako je adresa ispravna i sažetak se može pohraniti, njegovo ime,
  bazirano na naslovu sažetka, pojavit će se na dnu popisa sažetaka.
* Preimenuj: Otvara dijaloški okvir s uređivačkim poljem za preimenovanje
  odabranog sažetka.
* Obriši: Otvara dijaloški okvir za brisanje odabranog sažetka nakon potvrde
  brisanja.
* Postavi kao zadani: Postavlja odabrani sažetak kao zadani, tako da se tim
  člancima može pristupiti koristeći NVDA geste.
* Zatvori: Zatvara dijaloški okvir Sažetaka.

##### Napomene #####

* Ako je kreiran sažetak pod nazivom tempFeed, molimo da ga preimenujete,
  kako bi se ta datoteka mogla zamijeniti u slučaju potrebe kako bi se
  kreirao sažetak s već postojećim imenom.
* Sažetak koji je postavljen kao zadani ne može se ukloniti.Datoteka s
  adresom sažetka bit će u uporabi tijekom vraćanja konfiguracije, te se
  stoga ne može ukloniti.

####Kopiraj mapu sažetaka... ####

Otvara dijaloški okvir za odabir mape gdje će se sačuvati mapa osobnih
sažetaka.Prema zadanome, odabrana mapa je mapa NVDA konfiguracije, gdje će
se stvoriti mapa osobnih sažetaka.

#### Vrati sažetke... ####

Otvara dijaloški okvir za odabir mape koja zamjenjuje mapu Osobni
sažeci. Provjerite jeste li učitali mapu koja sadrži adrese sažetaka.

### Tipkovne prečice: ###

* Ctrl+Shift+NVDA+Razmak: Izgovori adresu trenutnog članka. Dvostrukim
  pritiskom otvorit će se web stranica.
* Ctrl+Shift+NVDA+8: Ponovno učitava odabrani sažetak i izgovara najnoviji
  naslov.
* Ctrl+Shift+NVDA+I: Izgovara naslov trenutnog sažetka i link. Dvostrukim
  pritiskom kopirat će se naslov i povezan link u međuspremnik.
* Ctrl+Shift+NVDA+U: Izgovara naslov prethodnog sažetka.
* Ctrl+Shift+NVDA+O: Izgovara naslov sljedećeg sažetka.

## Obavijesti: ##

* Kada je kopiran naslov ili adresa.
* Kada je omogućeno povezivanje/osvježavanje sažetka, ili adresa ne odgovara
  važećem sažetku.
* NVDA će prikazati poruku greške ako nije bilo moguće stvoriti rezernu
  kopiju ili vratiti mapu Osobni sažeci.
* Popis naslova članaka prikazuje ime odabranog sažetka i broj dostupnih
  stavki.



## Promjene u inačici 4.0 ##

* Dodan gumb za otvaranje odabranog sažetka iz dijaloškog okvira Sažeci.

## Promjene u inačici 3.0 ##

* Dijaloški okviri za upravljanje datotekama sažetaka su uklonjeni. Sada je
  njihova funkcionalnost uključena u dijaloški okvir Sažeci.
* Poboljšan je vizualni prikaz dijaloških okvira, u skladu s prikazom
  dijaloških okvira u NVDA.
* Zadani sažetak pohranjen je u NVDA konfiguraciju. Nadalje, moguće je
  postaviti drugi zadani sažetak u Konfiguracijskim profilima.
* Zahtijeva NVDA inačicu 2016.4.


## Promjene u inačici 2.0 ##

* Pomoć za ovaj dodatak dostupna je u Upravitelju dodacima.

## Promjene u inačici 1.0 ##

* Prva inačica.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf

[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev
