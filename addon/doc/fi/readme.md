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

* Filter by: An edit box to search previously saved feeds.
* A list of the saved feeds.
* List of articles: Opens a dialog which presents the articles list from
  your current feed. Select the article you want to read and press OK button
  to open the corresponding page in your browser.
* New: Opens a dialog with an edit box to enter the address of a new
  feed. If the address is valid and the feed can be saved, its name, based
  on the feed title, will appear at the bottom of the feeds list.
* Rename: Opens a dialog with an edit box to rename the selected feed.
* Delete: Opens a dialog to delete the selected feed after confirmation.
* Set default: Sets the selected feed as the default, so that its articles
  can be accessed with NVDA's gestures.
* Close: Closes the Feeds dialog.

##### Huomautuksia #####

* If a feed named tempFeed is created, please rename it, as this file could
  be replaced when needed to create a feed whose name already exists.
* The feed set as the default can't be removed. The addressFile feed will be
  use as the default when the configuration is reset, so it can't be
  deleted.

####Kopioi syötekansio... ####

Avaa valintaikkunan, josta voit valita, minne syötteesi sisältävä
personalFeeds-kansio luodaan. Kansiona on oletusarvoisesti NVDA:n
asetushakemisto.

#### Palauta syötteet... ####

Avaa valintaikkunan, josta voit valita kansion, jonka sisältämillä
syötteillä personalFeeds-kansion syötteet korvataan. Varmista, että valitset
vain syötteiden URL-osoitteita sisältävän kansion.

### Näppäinkomennot: ###

* Ctrl+Shift+NVDA+Space: Announces current article's URL. Pressing twice
  will open the web page.
* Ctrl+Shift+NVDA+8: Refreshes the selected feed and announces its most
  recent title.
* Ctrl+Shift+NVDA+I: Announces current feed title and link. Pressing twice
  will copy the title and related link to clipboard.
* Ctrl+Shift+NVDA+U: Announces previous feed title.
* Ctrl+Shift+NVDA+O: Announces next feed title.

## Ilmoitukset: ##

* When the title or URL have been copied.
* When unable to connect/refresh a feed, or the URL does not correspond to a
  valid feed.
* NVDA will display an error message if it was not possible to backup or
  restore the personalFeeds folder.
* The title of the articles list dialog displays the selected feed name and
  number of items available.


## Muutokset versiossa 3.0 ##

* The dialogs to manage feed files have been removed. Now their
  functionality is included in the Feeds dialog.
* The visual presentation of the dialogs has been enhanced, adhering to the
  appearance of the dialogs shown in NVDA.
* The default feed is saved on the NVDA's configuration. Therefore, it's
  possible to set different default feeds in configuration profiles.
* Requires NVDA 2016.4.


## Muutokset versiossa 2.0 ##

* Add-on help is available from the Add-ons Manager.

## Muutokset versiossa 1.0 ##

* Initial version.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf

[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev
