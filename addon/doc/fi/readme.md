# Lue syötteet #

* Tekijät: Noelia Ruiz Martínez, Mesar Hameed
* Yhteensopivuus: NVDA 2019.3 tai uudempi
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]


Tämä lisäosa tarjoaa suoraviivaisen tavan lukea Atom -tai RSS-syötteitä
NVDA:ta käyttäen.  Syötteitä ei päivitetä automaattisesti.  Alla mainitut
syötteet tarkoittavat sekä Atom- että RSS-syötteitä.

## Asennus tai päivitys ##

Mikäli olet käyttänyt tämän lisäosan aiempaa versiota ja jos
käyttäjäkohtaisessa NVDA:n asetushakemistossa on RSS- tai
personalFeeds-niminen kansio, versiota 6.0 tai uudempaa asennettaessa
kysytään, haluatko suorittaa päivityksen vai asennuksen.  Säilytä
tallentamasi syötteet ja jatka niiden käyttöä uudessa lisäosan versiossa
valitsemalla  päivitys.

## Komennot ##

### Lue syötteet -valikko ###

Pääset Lue syötteet -alavalikkoon NVDA-valikon Työkalut-alavalikosta, jossa
ovat käytettävissä seuraavat vaihtoehdot:

#### Syötteet ####

Avaa valintaikkunan, jossa on seuraavat säätimet:

* Suodata: Muokkauskenttä aiemmin tallennettujen syötteiden etsimiseen.
* Tallennettujen syötteiden luettelo, aktiivisena kun valintaikkuna avataan.
* Artikkeliluettelo: Avaa valintaikkunan, joka näyttää luettelon nykyisen
  syötteen artikkeleista. Valitse artikkeli, jonka haluat lukea, ja paina
  Enter tai Avaa valitun artikkelin verkkosivu -painiketta avataksesi
  vastaavan sivun selaimessa. Paina Tietoa artikkelista -painiketta
  avataksesi valintaikkunan, jossa näytetään valitun artikkelin otsikko ja
  linkki. Tiedot on myös mahdollista kopioida leikepöydälle.
* Avaa syöte: Avaa valitun syötteen oletussovelluksessa.
* Avaa syöte HTML-muodossa: Avaa valitun syötteen oletusselaimessa. Voit
  näyttää tai piilottaa julkaisupäivämäärät sekä artikkeleiden tiedot
  leikepöydälle kopioivat painikkeet.
* Kopioi syötteen osoite: Avaa valintaikkunan, jossa kysytään vahvistus
  syötteen osoitteen kopioinnista leikepöydälle.
* Uusi: Avaa muokkausruudun sisältävän valintaikkunan, johon voit kirjoittaa
  uuden syötteen osoitteen. Mikäli syöte on kelvollinen ja se voidaan
  tallentaa, sen otsikkoon pohjautuva nimi ilmestyy artikkeliluettelon
  alaosaan.
* Nimeä uudelleen: Avaa muokkausruudun sisältävän valintaikkunan, jossa voit
  uudelleennimetä valitun syötteen.
* Poista: Avaa vahvistuksen pyytävän valintaikkunan, jossa voit poistaa
  valitun syötteen.
* Aseta oletukseksi: Asettaa valitun syötteen oletukseksi, jotta sen
  artikkeleihin pääsee NVDA:n syötekomennoilla.
* Avaa syötteiden varmuuskopiokansio: Avaa kansion, joka saattaa sisältää
  syötteiden varmuuskopion. Tästä voi olla hyötyä sellaisten syötteiden
  tutkimisessa ja poistamisessa, joita ei haluta tuotavan lisäosaa
  päivitettäessä.
* Asetukset: Avaa Lue syötteet -lisäosan asetusvalintaikkunan. Löytyy myös
  NVDA-valikosta kohdasta Asetukset / Asetukset / Lue syötteet -kategoria.
* Sulje: Sulkee Syötteet-valintaikkunan.

##### Huomautuksia #####

* Mikäli tempFeed-niminen syöte luodaan, nimeä se uudelleen, sillä tämä
  tiedosto saatetaan korvata, kun samannimisen syötteen luominen on tarpeen.
* Oletukseksi asetettua syötettä ei voi poistaa. AddressFile-nimistä
  syötettä käytetään oletuksena asetuksia nollattaessa, joten sitä ei voi
  poistaa.
* Suodata-muokkauskenttä voidaan sijoittaa Avaa artikkeli -painikkeen
  jälkeen NVDA-valikosta kohdasta Asetukset / Asetukset Lue syötteet
  -kategoria tai painamalla Syötteet-valintaikkunan Asetukset-painiketta.

#### Kopioi syötekansio ####

Avaa valintaikkunan, josta voit valita, minne syötteet sisältävä
personalFeeds-kansio luodaan. Kansiona on oletusarvoisesti NVDA:n
asetushakemisto.

#### Palauta syötteet ####

Avaa valintaikkunan, josta voit valita kansion, jonka sisältämillä
syötteillä personalFeeds-kansion syötteet korvataan. Varmista, että valitset
vain syötteiden URL-osoitteita sisältävän kansion.

### Näppäinkomennot ###

* Ctrl+Vaihto+NVDA+Väli: Ilmoittaa nykyisen artikkelin
  URL-osoitteen. Kahdesti painettaessa avataan sen verkkosivu.
* Ctrl+Vaihto+NVDA+8: Päivittää valitun syötteen ja ilmoittaa sen uusimman
  artikkelin otsikon.
* Ctrl+Vaihto+NVDA+I: Ilmoittaa nykyisen syötteen otsikon ja
  linkin. Kahdesti painettaessa ne kopioidaan leikepöydälle.
* Ctrl+Vaihto+NVDA+U: Ilmoittaa edellisen syötteen otsikon.
* Ctrl+Vaihto+NVDA+O: Ilmoittaa seuraavan syötteen otsikon.

## Ilmoitukset ##

* Kun otsikko tai URL-osoite on kopioitu.
* Kun yhdistäminen/syötteen päivittäminen ei onnistu, tai annetussa
  URL-osoitteessa ei ole kelvollista syötettä.
* NVDA näyttää virheilmoituksen, mikäli personalFeeds-kansion
  varmuuskopiointi tai palautus ei ollut mahdollista ja jos uutta syötettä
  ei voi luoda.
* Valitun syötteen nimi ja saatavilla olevien artikkeleiden määrä näytetään
  Artikkeliluettelo-valintaikkunan otsikossa.

## Muutokset versiossa 10.0 ##

* Lisätty painike valitun syötteen avaamiseen HTML-muodossa
  oletusselaimessa.
* Mikäli uutta syötettä ei voi luoda, siitä näytetään virheilmoitus.
* Parannettu artikkeleiden järjestystä ja näyttämistä.
* Tuetaan mahdollisesti useampia syötteitä.
* Syöteluettelo on aktiivisena hakukentän sijaan, kun Syötteet-valintaikkuna
  avataan.
* Voit valita, sijoitetaanko hakukenttä syöteluettelon jälkeen, jolloin
  luettelo tulee aktiiviseksi jopa vaihdettaessa toisesta ikkunasta
  sulkematta Syötteet-valintaikkunaa.
* Syötteet-valintaikkunaan lisätty painike syötteen osoitteen kopioimiseen
  leikepöydälle.

## Muutokset versiossa 9.0 ##

* Edellyttää NVDA 2019.3:a tai uudempaa.

## Muutokset versiossa 8.0 ##

* Kun lisäosa päivitetään, aiemmassa versiossa tallennetut syötteet
  kopioidaan  automaattisesti uuteen versioon, paitsi jos haluat tuoda ne
  NVDA-asetusten pääkansiosta.
* Jos valitulle kansiolle ei ole Syötteidenkopiointivalintaikkunassa annettu
  nimeksi personalFeeds, sen niminen alikansio luodaan, jotta estetään
  tärkeää dataa sisältävien hakemistojen, kuten Tiedostot tai Ladatut
  tiedostot, poistaminen.

## Muutokset versiossa 7.0 ##

* Syötteet-valintaikkunassa on painike, jolla voidaan avata mahdollisen
  syöttteiden varmuuskopion sisältävä kansio.
* Kun muokkauskenttää käytetään syötteiden suodattamiseen ja jos
  hakutuloksia ei löydy, syötteiden luettelo sekä muut säätimet poistetaan
  käytöstä, jottei NVDA sano "tuntematon" kohdistuksen siirtyessä tähän
  tyhjään luetteloon.
* Mikäli Artikkeliluettelo-valintaikkunaa ei voida näyttää, esim. syötteessä
  olevien virheiden vuoksi, NVDA ilmoittaa virheestä, jotta
  Syötteet-valintaikkunaa voidaan käyttää ilman NVDA:n
  uudelleenkäynnistystä.

## Muutokset versiossa 6.0 ##

* Kun oletussyöte on päivitetty ja se lakkaa toimimasta palvelinongelmien
  vuoksi, aiempia artikkeleita ei poisteta, vaan niitä voidaan lukea
  tarkoitukseen varatuilla näppäinkomennoilla.
* Oletussyöte voidaan taas päivittää kahdesti.

## Muutokset versiossa 5.0 ##

* Artikkeliluettelovalintaikkunaa on paranneltu.
* Yhteensopiva NVDA 2018.3:n tai uudemman kanssa (vaaditaan).
* Viimeisen NVDA 2017.3:n kanssa yhteensopivan version voi ladata
  [tästä. ][3]

## Muutokset versiossa 4.0 ##

* Syötteet-valintaikkunaan lisätty painike valitun syötteen avaamiseen.

## Muutokset versiossa 3.0 ##

* Syötetiedostojen hallintavalintaikkunat on poistettu. Niiden
  toiminnallisuus on nyt sisällytetty Syötteet-valintaikkunaan.
* Valintaikkunoiden visuaalista esitystä on paranneltu noudattamaan NVDA:n
  ikkunoiden ulkoasua.
* Oletussyöte tallennetaan NVDA:n asetushakemistoon. Tämän ansiosta
  asetusprofiileissa on mahdollista asettaa eri oletussyötteitä.
* Edellyttää NVDA:n 2016.4-versiota.

## Muutokset versiossa 2.0 ##

* Ohje on käytettävissä Lisäosien hallinnasta.

## Muutokset versiossa 1.0 ##

* Ensimmäinen versio.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev

[3]: https://addons.nvda-project.org/files/get.php?file=rf-o
