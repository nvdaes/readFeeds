# Read Feeds #

* Autori: Noelia Ruiz Martínez, Mesar Hameed
* Scarica la [versione stabile][1] (compatibile con NVDA 2019.3 e
  successive)
* Download [beta version][2] (compatible with NVDA 2019.3 and beyond)

Questo componente aggiuntivo fornisce un modo semplice per leggere i feed
nel formato Atom o RSS usando NVDA. I feed non verranno aggiornati
automaticamente. Nel seguito, quando menzioneremo i feed, intenderemo sia i
feed RSS che i feed ATOM.

## Comandi ##

### La finestra Read Feeds ###

Si può accedere alla finestra  Read Feeds dal menu di NVDA, Strumenti,
Feeds.

Contiene  i seguenti controlli:

* Filtra per: un campo editazione per la ricerca tra i feed salvati.
* Un elenco dei feed salvati, che viene focalizzato quando la finestra viene
  aperta.
* Elenco articoli: apre una finestra che presenta l'elenco degli articoli
  del feed selezionato. Selezionate l'articolo che vi interessa leggere,
  quindi premete Invio o il pulsante Apri feed per aprire l'articolo con il
  vostro browser predefinito. Premendo il pulsante Informazioni Articolo è
  possibile visualizzare il link ed il titolo dell'articolo
  selezionato. Queste informazioni possono essere copiate negli appunti.
* Apri feed: apre il feed selezionato nell'applicazione predefinita.
* Apri feed come HTML. Apre il feed selezionato nel vostro browser
  predefinito. Potrete mostrare o nascondere la data di pubblicazione e il
  pulsante per copiare negli appunti le informazioni sull'articolo.
* Copia indirizzo feed. Apre una finestra che vi consente di cfonfermare se
  volete copiare negli appunti l'indirizzo del feed.
* Nuovo: apre una finestra didialogo con un campo editazione per inserire
  l'indirizzo  di un nuovo feed. Se l'indirizzo è valido ed il feed può
  essere salvato, il nome del  feed, basato sul titolo, apparirà in fondo
  all'elenco dei feed.
* Rinomina: apre una finestra con un campo editazione per rinominare il feed
  selezionato.
* Elimina: apre una finestra che consente di eliminare il feed selezionato,
  dopo conferma.
* Imposta come predefinito: permette di impostare il feed selezionato come
  predefinito, in modo che si possa accedere ai suoi articoli con i comandi
  di NVDA.
* Importa feeds da file OPML: Apre una finestra di dialogo per aggiungere
  nuovi feed da file OPML.
* Salva i  feed in file  OPML: Apre una finestra di dialogo per salvare i
  feed disponibili dalla finestra di dialogo Feed in file OPML.
* Preferenze: apre la finestra impostazioni di ReadFeeds, disponibile anche
  dal menu di NVDA->Preferenze->Impostazioni, categoria Read Feeds.
* Chiudi: chiude la finestra dei feed.

### Note #####

* Il campo editazione "Filtra per" può essere collocato dopo il pulsante
  "Apri articolo" andando nel menu di NVDA->Preferenze->Impostazioni,
  categoria Read feeds, oppure attivando il pulsante "Preferenze" della
  finestra Feeds.
* Questo riquadro  ha un'opzione per mostrare le date degli articoli nella
  finestra di dialogo Elenco degli articoli.


### Comandi da tastiera ###

* Ctrl+Shift+NVDA+Spazio: Legge il link dell'articolo selezionato. Se
  premuto due volte apre la pagina web dell'articolo.
* Ctrl+Shift+NVDA+8: Aggiorna il feed selezionato e legge il titolo
  dell'articolo più recente.
* Ctrl+Shift+NVDA+I: legge il titolo e il link del feed selezionato. Se
  premuto due volte, copia queste informazioni negli appunti.
* Ctrl+Shift+NVDA+U: legge il titolo del feed precedente.
* Ctrl+Shift+NVDA+O: legge il titolo del feed successivo.

## Avvisi vocali ##

* Quando un titolo o un link sono stati copiati.
* Quando non è possibile connettersi o aggiornare un feed, o l'URL non
  corrisponde ad un feed valido.
* NVDA visualizzerà un messaggio di errore se non è possibile creare un
  nuovo feed.
* Nel titolo della finestra elenco articoli viene indicato il nome del feed
  selezionato ed il numero di elementi disponibili.

## Changes for 21.0

* Feeds with untitled articles can be presented in the Articles dialog, and
  opened as HTML.

## Changes for 20.0

* universalFeedParser is updated to 5.0.1, adding support for more feeds.

## Novità nella versione 14.0

* Risolto un errore che rendeva impossibile aggiungere alcuni feed.

## Novità nella versione 13.0

* Il componente aggiuntivo non può essere utilizzato in modalità schermo
  protetto.
* I feed sono gestiti con file OPML.
* A causa di modifiche nel sistema di gestione dei feed, sono state
  apportate modifiche al file di configurazione dove è impostato il feed
  predefinito. Usa la finestra di dialogo Feed se vuoi impostarla di nuovo.
* I vecchi file di testo utilizzati nelle versioni precedenti verranno
  automaticamente importati nel nuovo formato OPML all'avvio del componente
  aggiuntivo.
* La funzione di copia e ripristino dei feed è stata sostituita con la
  possibilità di importare e salvare in file OPML.
* I feed con formato incorretto possono essere elaborati prima di essere
  aggiunti per renderli compatibili con il componente aggiuntivo.
* Nelle impostazioni del componente ReadFeeds, una nuova opzione consente di
  visualizzare le date degli articoli nella finestra Elenco articoli.

## Novità nella versione 12.0

* Risolto un errore per il quale le scorciatoie per gli elementi del menu
  degli strumenti di NVDA non funzionavano come previsto.

## Novità nella versione 11.0

* Compatibile con NVDA 2021.1

## Novità nella versione 10.0 ##

* Aggiunto un pulsante per aprire il feed selezionato come HTML nel browser
  preferito.
* Se un nuovo feed non può essere creato, apparirà una finestra di errore.
* Migliorato l'ordine e il layout di alcuni articoli.
* Aggiunto il supporto per nuove tipologie di feeds.
* Quando viene aperta la finestra Feeds, verrà focalizzata la lista dei
  feeds anziché il campo editazione Cerca.
* E' possibile scegliere se il campo editazione "Cerca" sia mostrato dopo la
  lista dei feeds; ciò è utile per focalizzare la lista anche quando di
  viene da un'altra finestra senza chiudere la finestra Feeds.
* Aggiunto un pulsante per copiare l'indirizzo del feed selezionato dalla
  finestra Feeds.

## Novità nella versione 9.0 ##

* Richiede NVDA 2019.3 o versioni successive.

## Novità nella versione 8.0 ##

* Quando l'add-on viene aggiornato, i feed salvati nella versione precedente
  saranno automaticamente copiati nella nuova versione, a meno che non si
  preferisca importare i feed salvati nella cartella di configurazione di
  NVDA.
* Quando si usa la finestra per copiare i feeds, se la cartella scelta non
  si chiama personalFeeds, verà creata una sottocartella con questo nome,
  per evitare la cancellazione di cartelle contenenti dati importanti, quali
  Documenti o Downloads.

## Novità nella versione 7.0 ##

* Aggiunto un pulsante Nella finestra Feed che consente di aprire una
  cartella di backup.
* Quando non si trova nessun risultato dal campo editazione per filtrare i
  feeds, l'elenco Feed e gli altri controlli vengono disattivati. In questo
  modo NVDA non annuncierà più "sconosciuto" in elenchi vuoti.
* Se l'elenco degli articoli non può essere visualizzato, perché per esempio
  c'è un problema nel feed, NVDA mostrerà un messaggio di errore. In questo
  modo non sarà più necessario riavviare NVDA per usare la finestra Feed.

## Novità nella versione 6.0 ##

* Quando il feed predefinito è stato aggiornato, ma per problemi sul server
  smette di funzionare, gli articoli precedenti non vengono eliminati e
  possono essere letti con i comandi corrispondenti.
* Il feed predefinito può essere nuovamente aggiornato due volte (Fix
  regression).

## Novità nella versione 5.0 ##

* Migliorata la finestra per l'elenco articoli.
* Compatibile con NVDA 2018.3 o versioni successive (richiesto).
* Se è necessario, è possibile scaricare l'ultima versione [compatibile con
  NVDA 2017.3][3].

## Novità nella versione 4.0 ##

* Aggiunto un pulsante per aprire il feed selezionato dalla finestra Feeds.

## Novità nella versione 3.0 ##

* Le finestre per gestire i file dei feed sono state rimosse. Questa
  funzione verrà eseguita dalla finestra Feeds.
* La rappresentazione grafica dell'interfaccia per le finestre di dialogo è
  stata migliorata, in conformità con il layout delle finestre di dialogo di
  NVDA.
* Il feed predefinito viene salvato nella cartella di configurazione di
  NVDA. E' quindi possibile impostare feed predefiniti diversi nei profili
  di configurazione.
* Richiede NVDA 2016.4.

## Novità nella versione 2.0 ##

* Nel gestore componenti aggiuntivi è disponibile la guida dell'add-on.

## Novità nella versione 1.0 ##

* Versione iniziale.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds

[2]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=rf-o
