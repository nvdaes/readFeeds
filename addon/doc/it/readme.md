# Read Feeds #

* Autori: Noelia Ruiz Martínez, Mesar Hameed
* NVDA compatibility: 2018.3 to 2019.2
* Scarica la [versione stabile][1]
* Scarica la [versione in sviluppo][2]

Questo componente aggiuntivo fornisce un modo semplice per leggere i feed
nel formato Atom o RSS usando NVDA. I feed non verranno aggiornati
automaticamente. Quando si menzionano i feed, si intendono sia i feed RSS
che feed ATOM.

## Installazione e aggiornamento: ##

Se avete installato una versione precedente di questo componente aggiuntivo,
e sono presenti le cartelle personalFeed o RSS nella cartella di
configurazione di NVDA, un messaggio di dialogo vi chiederà se si vuol
importare le cartelle personali durante l'aggiornamento.

## Comandi rapidi: ##

### Il Menu di Read Feeds ###

Si può accedere al sottomenu Gestore Feed dal menu NVDA, Strumenti.  Le voci
del sottomenu sono:

#### Feeds... ####

Apre una finestra con i seguenti controlli:

* Filtra per: un campo editazione per la ricerca tra i feed salvati.
* Un elenco dei feed salvati.
* Elenco degli articoli: apre una finestra che presenta l'elenco degli
  articoli del feed selezionato. Seleziona l'articolo che ti interessa
  leggere, quindi premere Invio o il pulsante Apri feed per aprire
  l'articolo con il tuo browser predefinito. Premendo il pulsante
  Informazioni Articolo è possibile visualizzare il link ed il titolo
  dell'articolo selezionato. Queste informazioni possono essere copiate
  negli appunti. 
* Apri feed: apre il feed nell'aplicazione predefinita.
* Nuovo: apre una finestra per inserire un nuovo indirizzo feed. Se
  l'indirizzo è valido ed il feed può esser salvato, il nome del  feed
  appare nel fondo dell'elenco feed.
* Rinomina: apre una finestra dove è possibile rinominare il feed.
* Elimina: apre una finestra che consente di eliminare un feed con previa
  converma.
* Imposta predefinito: permette di impostare il feed selezionato come
  predefinito, in modo che il feed selezionato si potrà anche aprire con i
  comandi di NVDA.
* Cartella backup: apre una cartella che contiene feed precedentemente
  salvati. Può essere utile per cancellare feed non più necessari che non si
  vogliono caricare durante l'aggiornamento del componente.
* Chiudi: chiude la finestra dei feed.

##### Nota: #####

* Se è presente un feed chiamato tempFeed, si consiglia di rinominarlo,
  visto che il feed potrà esser sostituito da un feed che ha lo stesso nome.
* Il feed impostato come predefinito non può essere rimosso. Il file
  addressFile  potrà esser usato come predefinito quando si ripristina alla
  configurazione iniziale, in questo caso potrà esser rimosso.

####Cartella Copia feed ####

Apre una finestra dove è possibile scegliere il percorso per salvare la
cartella dei vostri feed. Il percorso predefinito è la cartella di
configurazione di NVDA,  dove verrà salvata una cartella nominata
personalFeeds.

#### Ripristina feed ####

Apre una finestra che consente selezionare una cartella di feed
precedentemente salvati e che sostituiranno i feed nella cartella
personalFeeds. Assicurarsi di selezionare una cartella che contiene file con
l'URL dei feed.

### Comandi da tastiera:  ###

* Ctrl+Shift+NVDA+Space: Legge il link dell'articolo selezionato. Premuto
  due volte apre la pagina web dell'articolo.
* Ctrl+Shift+NVDA+8: Aggiorna il feed selezionato e annuncia l'articolo più
  recente.
* Ctrl+Shift+NVDA+I: legge il titolo del feed e del link
  selezionato. Premendo due volte verrà copiato il titolo e il relativo link
  negli appunti. 
* Ctrl+Shift+NVDA+U: legge il titolo del precedente feed.
* Ctrl+Shift+NVDA+O: legge il titolo del feed successivo.

## Avvisi vocali: ##

* Quando si copia un titolo o un link.
* Quando non è possibile connettersi o aggiornare un feed, o l'URL non
  corrisponde ad un feed valido.
* NVDA visualizza un avviso di errore segnalando che non è stato possibile
  ripristinare o aggiornare la cartella personalFeeds.
* Nel titolo della finestra elenco articoli viene indicato il feed
  selezionato ed il numero di elementi disponibili.

## Changes for 8.0 ##

* When the add-on is updated, feeds saved in the previous version of the
  add-on will be automatically copied to the new version, unless you prefer
  to import feeds saved in the main configuration folder of NVDA.
* When using the dialog to copy feeds, if the chosen folder is not named
  personalFeeds, a subfolder with this name will be created to prevent the
  deletion of directories containing important data, such as Documents or
  Downloads.

## Changes for 7.0 ##

* Aggiunto un pulsante Nella finestra Feed che consente di aprire una
  cartella di backup. 
* Quando non si trova nessun risultato dal campo editazione, l'elenco Feed e
  gli altri controlli vengono disattivati. In questo modo NVDA non
  annuncierà più Sconosciuto in elenchi vuoti.
* Se l'elenco degli articoli non può essere visualizzato, dovuto per esempio
  ad un problema di feed, verrà rilasciato un errore. In questo modo non
  sarà più necessario riavviare NVDA per usare la finestra Feed.

## Changes for 6.0 ##

* Quando il feed predefinito è stato aggiornato, ma per problemi del server
  non si connette, gli articoli precedenti non vengono eliminati e possono
  essere letti con i comandi assegnati.
* Il feed predefinito può essere aggiornato nuovamente (Fix regression).

## Changes for 5.0 ##

* Migliorata la finestra per l'elenco articoli.
* Compatibilità con NVDA 2018.3 o superiore(required).
* Se è necessario, è possibile scaricare la versione [compatibile con NVDA
  2017.3][3].

## Changes for 4.0 ##

* Aggiunto un pulsante per aprire il feed selezionato dalla finestra Feeds. 

## Changes for 3.0 ##

* La finestra per gestire i file dei feed è stata rimossa. Questa funzione
  verrà eseguita dalla finestra Feeds.
* The visual presentation of the dialogs has been enhanced, adhering to the
  appearance of the dialogs shown in NVDA.
* The default feed is saved on the NVDA's configuration. Therefore, it's
  possible to set different default feeds in configuration profiles.
* Requires NVDA 2016.4.


## Changes for 2.0 ##

* Add-on help is available from the Add-ons Manager.

## Changes for 1.0 ##

* Initial version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev

[3]: https://addons.nvda-project.org/files/get.php?file=rf-o
