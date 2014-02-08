# Lue syötteet #

* Tekijät: Noelia Ruiz Martínez, Mesar Hameed
* Lataa [vakaa versio][2]
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

*	 Artikkelilista...: Näyttää listan nykyisen syötteen
   artikkeleista. Valitse artikkeli, jota haluat lukea, ja paina
   OK-painiketta avataksesi kyseisen artikkelin verkkosivun selaimessa.
*	 Tilapäinen syötteen osoite...: Control+NVDA+Shift+Enter: Avaa
   valintaikkunan, jossa voit kirjoittaa uuden URL-osoitteen toisen syötteen
   valitsemiseksi. Nykyinen URL-osoite näytetään tässä valintaikkunassa.
*	 Lataa syötteen osoite tiedostosta...: NVDA+Control+Enter: Avaa
   valintaikkunan, jossa voit valita syötteen sen osoitteen sisältävästä
   tiedostosta.
*	 Tallenna nykyisen syötteen osoite tiedostoon...: NVDA+Shift+Enter: Avaa
   valintaikkunan, jossa voit valita tiedoston, johon nykyisen syötteen
   URL-osoite tallennetaan. Jos tallennat addressFile.txt-nimiseen
   erikoistiedostoon, syötettä käytetään oletussyötteenä.
*	 Päivitä nykyinen syöte: Control+Shift+NVDA+8: Päivittää nykyisen
   syötteen. Syötteitä ei päivitetä automaattisesti Lue syötteet lisäosaa
   käynnistettäessä.
*	 Varmuuskopioi syötekansio...: Avaa valintaikkunan, jossa voit valita
   kansion, johon personalFeeds-kansion sisältö
   tallennetaan. Oletusarvoisesti on valittuna NVDA:n asetushakemisto, johon
   personalFeeds-kansio luodaan.
*	 Palauta syötteet...: Avaa valintaikkunan, jossa voit valita kansion, joka
   korvaa personalFeeds-kansiossa olevat syötteet. Varmista, että valitset
   syötteiden URL-osoitteita sisältävän kansion.

### Näppäinkomennot: ###

*	 Ctrl+Shift+NVDA+välilyönti: Ilmoittaa nykyisen artikkelin
   URL-osoitteen. Kahdesti painaminen avaa kyseisen verkkosivun.
*	 Ctrl+Shift+NVDA+8: Päivittää nykyisen syötteen ja ilmoittaa sen
   viimeisimmän otsikon.
*	 Ctrl+Shift+NVDA+I: Ilmoittaa syötteen nykyisen otsikon. Kahdesti
   painaminen kopioi otsikon ja sen osoitteen leikepöydälle.
*	 Ctrl+Shift+NVDA+U: Ilmoittaa syötteen edellisen otsikon.
*	 Ctrl+Shift+NVDA+O: Ilmoittaa syötteen seuraavan otsikon.

## Ilmoitukset: ##

*	 Kun otsikko tai URL-osoite on kopioitu.
*	 Kun syötteen osoitteeseen ei saada yhteyttä/syötettä ei voi päivittää,
   tai URL-osoitteessa ei ole kelvollista syötettä.
*	 NVDA näyttää virheilmoituksen, mikäli personalFeeds-kansion
   varmuuskopiointi ei ollut mahdollista.
*	 Artikkelilista-valintaikkunan nimi näyttää valitun syötteen nimen ja
   artikkelien lukumäärän.

## Muutokset versiossa 1.0 ##
*	 Ensimmäinen versio.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

