# Lue syötteet #

* Tekijät: Noelia Ruiz Martínez, Mesar Hameed
* Lataa [kehitysversio][1]

Tämä lisäosa tarjoaa suoraviivaisen tavan lukea Atom -tai RSS-syötteitä
NVDA:ta käyttäen.  Syötteitä ei päivitetä automaattisesti.  Alla mainitut
syötteet tarkoittavat sekä Atom- että RSS-syötteitä.

## Asennus tai päivitys: ##

Mikäli olet käyttänyt tämän lisäosan aiempaa versiota ja jos
käyttäjäkohtaisessa NVDA:n asetushakemistossa on RSS- tai
personalFeeds-niminen kansio, versiota 6.0 tai uudempaa asennettaessa
sinulta kysytään, haluatko päivittää vai asentaa.  Valitse päivitys
säilyttääksesi tallentamasi syötteet ja jatkaaksesi niiden käyttöä uudessa
Lue syötteet -lisäosan versiossa.

## Komennot: ##

### Lue syötteet -valikko ###

Pääset Lue syötteet -valikkoon NVDA-valikosta, NVDA+N, jossa ovat käytössä
seuraavat vaihtoehdot:

- Artikkelilista...  Näyttää listan nykyisen syötteen artikkeleista. Valitse
haluamasi artikkeli ja paina OK-painiketta avataksesi sen sivun selaimessa.
- Tilapäissyötteen osoite... Control+NVDA+Shift+Enter: Avaa valintaikkunan,
jossa voit kirjoittaa uuden URL-osoitteen toisen syötteen
valitsemiseksi. Nykyinen URL näytetään tässä valintaikkunassa.  - Lataa
syötteen osoite tiedostosta... NVDA+Control+Enter: Avaa valintaikkunan,
jossa voit valita syötteen sen osoitteen sisältävästä tiedostosta.  -
Tallenna nykyisen syötteen osoite tiedostoon... NVDA+Shift+Enter: Avaa
valintaikkunan, jossa voit valita tiedoston, johon nykyisen syötteen
URL-osoite tallennetaan.  Mikäli tallennat addressFile.txt-nimiseen
erikoistiedostoon, tätä syötettä käytetään oletussyötteenä.  - Päivitä
nykyinen syöte: Control+Shift+NVDA+8: Päivittää valitun syötteen. Syötteitä
ei päivitetä automaattisesti Lue syötteet -lisäosaa käynnistettäessä.  -
Varmuuskopioi syötekansio...  Avaa valintaikkunan, jossa voit valita
kansion, johon syötteidesi personalFeeds-hakemisto tallennetaan. Valittuna
kansiona on oletusarvoisesti NVDA:n asetuskansio, johon
personalFeeds-hakemisto luodaan.  - Palauta syötteet...  Avaa
valintaikkunan, jossa voit valita kansion, joka korvaa
personalFeeds-kansiossa olevat syötteesi. Varmista, että avaamasi kansio
sisältää syötteiden URL-osoitteita.

### Näppäinkomennot: ###

- Ctrl+Shift+NVDA+välilyönti: Ilmoittaa nykyisen artikkelin
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
personalFeeds-kansion varmuuskopiointi ei onnistunut.  -
Artikkelilista-valintaikkunan otsikko näyttää valitun syötteen nimen sekä
syötteiden lukumäärän.

## Muutokset versiossa 1.0 ##
*	 Ensimmäinen versio.

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

