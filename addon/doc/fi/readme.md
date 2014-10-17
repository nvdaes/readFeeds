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

## Changes for 2.0 ##
*	 Add-on help is available from the Add-ons Manager.

## Muutokset versiossa 1.0 ##
*	 Ensimmäinen versio.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

