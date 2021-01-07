# Read Feeds #

* Autori: Noelia Ruiz Martínez, Mesar Hameed
* Compatibilità con NVDA: versione 2019.3 o successive
* Scarica la [versione stabile][1]
* Scarica la [versione in sviluppo][2]


Questo componente aggiuntivo fornisce un modo semplice per leggere i feed
nel formato Atom o RSS usando NVDA. I feed non verranno aggiornati
automaticamente. Nel seguito, quando menzioneremo i feed, intenderemo sia i
feed RSS che i feed ATOM.

## Installazione o aggiornamento ##

Se avete installato una versione precedente di questo componente aggiuntivo
e nella cartella di configurazione di NVDAsono presenti le sottocartelle
personalFeed o RSS , quando installerete la versione corrente una finestra
di dialogo vi chiederà se volete aggiornare o installare. Scegliete Aggiorna
per conservare i feed memorizzati e continuare ad utilizzarli nella nuova
versione di ReadFeed.

## Comandi ##

### Il Menu di Read Feeds ###

Si può accedere al sottomenu Read Feeds dal menu di NVDA, Strumenti.  Le
voci del sottomenu sono:

#### Feeds ####

Apre una finestra con i seguenti controlli:

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
* Cartella backup: apre una cartella che contiene un backup dei feed. Ciò
  può essere utile per esplorare e cancellare feed che non si vogliono
  importare durante l'aggiornamento del componente.
* Preferenze: apre la finestra impostazioni di ReadFeeds, disponibile anche
  dal menu di NVDA->Preferenze->Impostazioni, categoria Read Feeds.
* Chiudi: chiude la finestra dei feed.

##### Note #####

* Se è presente un feed chiamato tempFeed, si consiglia di rinominarlo,
  visto che il feed potrà essere sostituito quando si ha bisogno di creare
  un feed il cui nome esiste già.
* Il feed impostato come predefinito non può essere rimosso. Il feed
  addressFile  sarà usato come predefinito quando si ripristina la
  configurazione iniziale, perciò anch'esso non può essere rimosso.
* Il campo editazione "Filtra per" può essere collocato dopo il pulsante
  "Apri articolo" andando nel menu di NVDA->Preferenze->Impostazioni,
  categoria Read feeds, oppure attivando il pulsante "Preferenze" della
  finestra Feeds.

#### Copia cartella feed ####

Apre una finestra da cui è possibile scegliere il percorso per salvare la
cartella dei vostri feed. Il percorso predefinito è la cartella di
configurazione di NVDA,  dove verrà salvata una cartella nominata
personalFeeds.

#### Ripristina feed ####

Apre una finestra che consente di selezionare una cartella di feed
precedentemente salvati e che sostituiranno i feed nella cartella
personalFeeds. Assicurarsi di selezionare una cartella che contiene file con
l'URL dei feed.

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
* NVDA mostrerà un messaggio di errore se non è stato possibile copiare o
  ripristinare la cartella personalFeeds e se non è possibile creare un
  nuovo feed.
* Nel titolo della finestra elenco articoli viene indicato il nome del feed
  selezionato ed il numero di elementi disponibili.

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

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev

[3]: https://addons.nvda-project.org/files/get.php?file=rf-o
