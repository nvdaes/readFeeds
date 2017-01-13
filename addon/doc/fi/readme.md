# Lue syötteet #

* Tekijät: Noelia Ruiz Martínez, Mesar Hameed
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Tämä lisäosa tarjoaa suoraviivaisen tavan lukea Atom -tai RSS-syötteitä
NVDA:ta käyttäen.  Syötteitä ei päivitetä automaattisesti.  Alla mainitut
syötteet tarkoittavat sekä Atom- että RSS-syötteitä.

## Asennus tai päivitys: ##

Mikäli olet käyttänyt tämän lisäosan aiempaa versiota ja jos
käyttäjäkohtaisessa NVDA:n asetushakemistossa on RSS- tai
personalFeeds-niminen kansio, versiota 6.0 tai uudempaa asennettaessa
sinulta kysytään, haluatko suorittaa päivityksen vai asennuksen.  Valitse
päivitys säilyttääksesi tallentamasi syötteet ja jatkaaksesi niiden käyttöä
uudessa Lue syötteet -lisäosan versiossa.

## Komennot: ##

### Lue syötteet -valikko ###

Pääset Lue syötteet -alavalikkoon NVDA-valikon Työkalut-alavalikosta, jossa
ovat käytettävissä seuraavat vaihtoehdot:

#### Syötteet... ####

Avaa valintaikkunan, jossa on seuraavat säätimet:

- Suodata: Muokkauskenttä aiemmin tallennettujen syötteiden etsimiseen.  -
Tallennettujen syötteiden luettelo.  - Artikkeliluettelo: Avaa
valintaikkunan, jossa näytetään luettelo nykyisen syötteen
artikkeleista. Valitse artikkeli, jota haluat lukea, ja paina OK-painiketta
avataksesi kyseisen syötteen selaimessa.  - Uusi: Avaa valintaikkunan, jossa
olevaan muokkauskenttään kirjoitetaan uuden syötteen osoite. Mikäli osoite
on kelvollinen ja syöte voidaan tallentaa, sen  syötteen otsikkoon
pohjautuva nimi ilmestyy syöteluettelon alimmaiseksi.  - Nimeä uudelleen:
Avaa valintaikkunan, jossa olevan muokkausruudun avulla voidaan nimetä
valittu syöte uudelleen.  - Poista: Avaa valintaikkunan, jossa valittu syöte
voidaan poistaa.  - Aseta oletukseksi: Asettaa valitun syötteen oletukseksi,
jotta sen artikkeleita voi lukea NVDA:n syöte-eleillä.  - Sulje: Sulkee
syötevalintaikkunan.

##### Huomautuksia #####
- Mikäli tempFeed-niminen syöte luodaan, nimeä se uudelleen, sillä tämä
tiedosto saatetaan korvata, kun on tarpeen luoda syöte, jonka nimi on jo
olemassa.  - Oletukseksi asetettua syötettä ei voi
poistaa. AddressFile-nimistä syötettä käytetään oletuksena asetuksia
nollattaessa, joten sitä ei voi poistaa.

####Kopioi syötekansio... ####

Avaa valintaikkunan, josta voit valita, minne syötteesi sisältävä
personalFeeds-kansio luodaan. Kansiona on oletusarvoisesti NVDA:n
asetushakemisto.

#### Palauta syötteet... ####

Avaa valintaikkunan, josta voit valita kansion, jonka sisältämillä
syötteillä personalFeeds-kansion syötteet korvataan. Varmista, että valitset
vain syötteiden URL-osoitteita sisältävän kansion.

### Näppäinkomennot: ###

- Ctrl+Shift+NVDA+Välilyönti: Ilmoittaa nykyisen artikkelin
URL-osoitteen. Kahdesti painaminen avaa artikkelin verkkosivun.  -
Ctrl+Shift+NVDA+8: Päivittää valitun syötteen ja lukee sen uusimman
otsikon.  - Ctrl+Shift+NVDA+I: Lukee nykyisen syötteen otsikon. Kahdesti
painaminen kopioi otsikon ja siihen liittyvän linkin leikepöydälle.  -
Ctrl+Shift+NVDA+U: Lukee edellisen syötteen otsikon.  - Ctrl+Shift+NVDA+O:
Lukee seuraavan syötteen otsikon.

## Ilmoitukset: ##

- Kun otsikko tai URL-osoite on kopioitu.  - Kun yhteyttä ei voi
muodostaa/syötettä päivittää, tai annetussa URL-osoitteessa ei ole
kelvollista syötettä.  - NVDA näyttää virheilmoituksen, mikäli
personalFeeds-kansion varmuuskopiointi tai palautus ei onnistunut.  -
Artikkeliluettelo-valintaikkunan otsikko näyttää valitun syötteen nimen sekä
syötteiden lukumäärän.


## Muutokset versiossa 3.0 ##
- Syötetiedostojen hallintavalintaikkunat on poistettu. Niiden
toiminnallisuus on sisällytetty Syötteet-valintaikkunaan.  -
Valintaikkunoiden visuaalista esittämistä on parannettu noudattamaan NVDA:n
ikkunoiden ulkoasua.  - Oletussyöte tallennetaan NVDA:n asetuksiin. Tämän
ansiosta asetusprofiileissa on mahdollista määrittää eri oletussyötteitä.  -
Edellyttää NVDA:n 2016.4-versiota.


## Muutokset versiossa 2.0 ##
- Ohje on käytettävissä Lisäosien hallinnasta.

## Muutokset versiossa 1.0 ##
- Ensimmäinen versio.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf

[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev
