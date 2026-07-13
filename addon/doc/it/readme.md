# Read Feeds

- Authors: Noelia Ruiz Martínez, Mesar Hameed
- Compatibile con NVDA 2021.1
- Download [stable version][1]
- Download [development version][2]

Questo componente aggiuntivo fornisce un modo semplice per leggere i feed
nel formato Atom o RSS usando NVDA.
I feed non verranno aggiornati
automaticamente.
Nel seguito, quando menzioneremo i feed, intenderemo sia i
feed RSS che i feed ATOM.

## Installation or Update:

If you used a previous version of this addon, and there is an RSS or personalFeeds folder in your personal NVDA configuration folder,
when installing the current version, a dialog will ask if you want to upgrade or install.
Choose update to preserve your saved feeds and to continue using them in the new installed version of readFeeds.

## Commands:

### La finestra Read Feeds

Si può accedere alla finestra  Read Feeds dal menu di NVDA, Strumenti,
Feeds.

#### Feeds...

Opens a dialog with the following controls:

- Filtra per: un campo editazione per la ricerca tra i feed salvati.
- A list of the saved feeds.
- Elenco articoli: apre una finestra che presenta l'elenco degli articoli
  del feed selezionato. Selezionate l'articolo che vi interessa leggere,
  quindi premete Invio o il pulsante Apri feed per aprire l'articolo con il
  vostro browser predefinito. Premendo il pulsante Informazioni Articolo è
  possibile visualizzare il link ed il titolo dell'articolo
  selezionato. Queste informazioni possono essere copiate negli appunti.
- Apri feed: apre il feed selezionato nell'applicazione predefinita.
- Nuovo: apre una finestra didialogo con un campo editazione per inserire
  l'indirizzo  di un nuovo feed. Se l'indirizzo è valido ed il feed può
  essere salvato, il nome del  feed, basato sul titolo, apparirà in fondo
  all'elenco dei feed.
- Rinomina: apre una finestra con un campo editazione per rinominare il feed
  selezionato.
- Elimina: apre una finestra che consente di eliminare il feed selezionato,
  dopo conferma.
- Imposta come predefinito: permette di impostare il feed selezionato come
  predefinito, in modo che si possa accedere ai suoi articoli con i comandi
  di NVDA.
- Open folder containing a backup of feeds: Opens a folder which may contain a backup of feeds. This can be useful to explore and delete feeds which shouldn't be imported when the add-on is updated.
- Chiudi: chiude la finestra dei feed.

##### Note

- If a feed named tempFeed is created, please rename it, as this file could be replaced when needed to create a feed whose name already exists.
- The feed set as the default can't be removed. The addressFile feed will be use as the default when the configuration is reset, so it can't be deleted.

\####Copy feeds folder... ####

Opens a dialog to choose a folder where you can save the personalFeeds directory of your feeds. By default the selected folder is the NVDA's configuration directory, which will create the personalFeeds directory.

#### Restore feeds...

Opens a dialog to select a folder which replaces your feeds in the personalFeeds folder. Make sure you load a folder containing feeds URLs.

### Comandi da tastiera

- Ctrl+Shift+NVDA+Spazio: Legge il link dell'articolo selezionato. Se
  premuto due volte apre la pagina web dell'articolo.
- Ctrl+Shift+NVDA+8: Aggiorna il feed selezionato e legge il titolo
  dell'articolo più recente.
- Ctrl+Shift+NVDA+I: legge il titolo e il link del feed selezionato. Se
  premuto due volte, copia queste informazioni negli appunti.
- Ctrl+Shift+NVDA+U: legge il titolo del feed precedente.
- Ctrl+Shift+NVDA+O: legge il titolo del feed successivo.

## Notifications:

- Quando un titolo o un link sono stati copiati.
- Quando non è possibile connettersi o aggiornare un feed, o l'URL non
  corrisponde ad un feed valido.
- NVDA visualizzerà un messaggio di errore se non è possibile creare un
  nuovo feed.
- Nel titolo della finestra elenco articoli viene indicato il nome del feed
  selezionato ed il numero di elementi disponibili.

## Novità nella versione 8.0

- Quando l'add-on viene aggiornato, i feed salvati nella versione precedente
  saranno automaticamente copiati nella nuova versione, a meno che non si
  preferisca importare i feed salvati nella cartella di configurazione di
  NVDA.
- Quando si usa la finestra per copiare i feeds, se la cartella scelta non
  si chiama personalFeeds, verà creata una sottocartella con questo nome,
  per evitare la cancellazione di cartelle contenenti dati importanti, quali
  Documenti o Downloads.

## Novità nella versione 7.0

- Aggiunto un pulsante Nella finestra Feed che consente di aprire una
  cartella di backup.
- Quando non si trova nessun risultato dal campo editazione per filtrare i
  feeds, l'elenco Feed e gli altri controlli vengono disattivati. In questo
  modo NVDA non annuncierà più "sconosciuto" in elenchi vuoti.
- Risolto un errore per il quale le scorciatoie per gli elementi del menu
  degli strumenti di NVDA non funzionavano come previsto.

## Novità nella versione 6.0

- Quando il feed predefinito è stato aggiornato, ma per problemi sul server
  smette di funzionare, gli articoli precedenti non vengono eliminati e
  possono essere letti con i comandi corrispondenti.
- Il feed predefinito può essere nuovamente aggiornato due volte (Fix
  regression).

## Changes for 15.0

- Migliorata la finestra per l'elenco articoli.
- Compatibile con NVDA 2018.3 o versioni successive (richiesto).
- Richiede NVDA 2019.3 o versioni successive.

## Novità nella versione 4.0

- Aggiunto un pulsante per aprire il feed selezionato dalla finestra Feeds.

## Novità nella versione 3.0

- Le finestre per gestire i file dei feed sono state rimosse. Questa
  funzione verrà eseguita dalla finestra Feeds.
- La rappresentazione grafica dell'interfaccia per le finestre di dialogo è
  stata migliorata, in conformità con il layout delle finestre di dialogo di
  NVDA.
- Il feed predefinito viene salvato nella cartella di configurazione di
  NVDA. E' quindi possibile impostare feed predefiniti diversi nei profili
  di configurazione.
- Richiede NVDA 2016.4.

## Changes for 21.0

- Nel gestore componenti aggiuntivi è disponibile la guida dell'add-on.

## Novità nella versione 1.0

- Versione iniziale.

[1]: http://addons.nvda-project.org/files/get.php?file=rf
[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev
[3]: http://addons.nvda-project.org/files/get.php?file=rf-o
