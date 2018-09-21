# RSS-Feed-Reader #

* Authors: Noelia Ruiz Martínez, Mesar Hameed
* [stabile version][1] herunterladen
* Herunterladen der [Entwickler-Version][2]

Diese Erweiterung bietet eine einfache Möglichkeit, RSS-Feeds in den
Formaten Atom oder RSS mit NVDA zu lesen. Die Feeds werden nicht automatisch
aktualisiert. Wenn wir weiter unten  von Feeds sprechen, dann meinen wir
sowohl RSS- als auch  ATOM-Feeds.

## Installation oder Aktualisierung: ##

Wenn Sie eine frühere Version dieser Erweiterung verwendet haben und in
Ihrem persönlichen NVDA-Konfigurationsordner ein RSS- oder
personalFeeds-Ordner vorhanden ist, wird bei der Installation der aktuellen
Version ein Dialogfeld angezeigt. In diesem Dialog werden Sie gefragt, ob
Sie ein Upgrade oder eine Installation durchführen möchten.  Wählen Sie
update, um Ihre gespeicherten Feeds zu behalten und sie in der neu
installierten Version von RSS-Feed-Reader weiter zu verwenden.

## Befehle: ##

### Feed-Reader-Menü ###

Sie können auf das Untermenü RSS-Feed-Reader aus dem nvda-Menü, Untermenü
Extras zugreifen. Es stehen folgende Menüoptionen zur Verfügung:

#### RSS-Feeds... ####

Öffnet einen Dialog mit den folgenden Steuerelementen:

* Filtern nach: Ein Eingabefeld, um zuvor gespeicherte Feeds zu durchsuchen.
* Eine Liste der gespeicherten RSS-Feeds.
* Liste der Artikel: Öffnet einen Dialog, der die Artikelliste aus Ihrem
  aktuellen Feed anzeigt. Wählen Sie den Artikel, den Sie lesen möchten, und
  drücken Sie die Eingabetaste oder die Schaltfläche Webseite des
  ausgewählten Artikels öffnen, um die entsprechende Seite in Ihrem Browser
  zu öffnen. Klicken Sie auf die Schaltfläche Info-Artikel, um einen Dialog
  mit Titel und Link des ausgewählten Artikels zu öffnen; von diesem Dialog
  aus können Sie diese Informationen in die Zwischenablage kopieren.
* Feed öffnen: Öffnet den ausgewählten Feed in der Standardanwendung.
* Neu: Öffnet einen Dialog mit einem Eingabefeld zur Eingabe der Adresse
  eines neuen RSS-Feeds. Wenn die Adresse gültig ist und der Feed
  gespeichert werden kann, erscheint sein Name, basierend auf dem
  Feed-Titel, am Ende der Liste der RSS-Feeds.
* Umbenennen: Öffnet einen Dialog mit einem Eingabefeld zum Umbenennen des
  ausgewählten Feeds.
* Löschen: Öffnet einen Dialog zum Löschen des ausgewählten Feeds.
* Als standard festlegen: Legt den ausgewählten RSS-Feed als Standard fest,
  so dass auf seine Artikel mit den Tastenkürzel von NVDA zugegriffen werden
  kann.
* Schließen: Schließt den Dialog.

##### Hinweise #####

* Wenn ein Feed namens tempFeed erstellt wird, benennen Sie ihn bitte
  um. Sie könnten diese Datei bei Bedarf ersetzen, um einen Feed zu
  erstellen, dessen Name bereits existiert.
* Der als Standard eingestellte Feed kann nicht entfernt werden. Der
  AddressFile-Feed wird als Standard verwendet, wenn die Konfiguration
  zurückgesetzt wird. Daher kann dieser Ordner nicht gelöscht werden.

####Artikelordner kopieren...####

Öffnet einen Dialog zur Auswahl eines Ordners, in dem Sie das
personalFeeds-Verzeichnis Ihrer Artikel speichern können. Standardmäßig ist
der ausgewählte Ordner das Konfigurationsverzeichnis von NVDA.

#### RSS-Feeds wiederherstellen... ####

Öffnet einen Dialog zur Auswahl eines Ordners, der Ihre Feeds im
personalFeeds-Ordner ersetzt. Stellen Sie sicher, dass Sie einen Ordner mit
Feed-URLs auswählen.

### Tastenkombinationen: ###

* STRG+Umschalt+NVDA+Leertaste: Sagt die aktuelle Adresse des Artikels
  an. Zweimaliges Drücken öffnet die Webseite des Artikels.
* STRG+Umschalt+NVDA+8: Das ausgewählte RSS-Feed wir neugeladen und der
  aktuellste Titel wird angesagt.
* Strg+Umschalt+NVDA+I: Sagt den aktuellen Feed-Titel und -Link an. Durch
  zweimaliges Drücken wird der Titel und der zugehörige Link in die
  Zwischenablage kopiert.
* STRG+Umschalt+NVDA+U: Sagt den Titel des vorherigen RSS-Feeds an.
* STRG+Umschalt+NVDA+O: Sagt den Titel des nächsten RSS-Feeds an.

## Benachrichtigungen werden ausgegeben: ##

* Wenn der Titel oder die URL kopiert wurden.
* Wenn die Verbindung / das Neuladen eines RSS-Feeds fehlgeschlagen ist,
  oder wenn die URL nicht mit einem gültigen Feed übereinstimmt.
* NVDA zeigt eine Fehlermeldung an, wenn die Sicherung oder
  Wiederherstellung des Ordners personalFeeds nicht möglich war.
* Im Titel des Dialogs für die Artikellisten werden der Name des
  ausgewählten Feeds und die Anzahl der verfügbaren Artikel angezeigt.

## Änderungen für 5.0 ##

* Der Dialog der Artikelliste wurde erweitert.
* Kompatibel mit NVDA 2018.3 oder neuer (erforderlich).
* Bei Bedarf können Sie die [letzte Version][3], die mit NVDA 2017.3
  kompatibel ist herunterladen.

## Änderungen in 4.0 ##

* Schaltfläche zum Öffnen des ausgewählten Feeds über den Feed-Dialog
  hinzugefügt.

## Änderungen in 3.0 ##

* Die Dialoge zur Verwaltung von RSS-Feed-Dateien wurden entfernt. Jetzt ist
  ihre Funktionalität im RSS-Feeds-Dialog enthalten.
* Die visuelle Darstellung der Dialoge wurde verbessert und entspricht dem
  Erscheinungsbild der Dialoge in NVDA.
* Der Standard-Feed wird in der NVDA-Konfiguration gespeichert. Daher ist es
  möglich, verschiedene Standard-Feeds in Konfigurationsprofilen
  einzustellen.
* NVDA 2016.4 oder höher ist erforderlich


## Änderungen in 2.0 ##

* Hilfe zur Erweiterung ist über den Dialog "Erweiterungen verwalten"
  verfügbar.

## Änderungen in 1.0 ##

* Ehrstveröffentlichung.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev [3]:
https://github.com/nvdaes/readFeeds/releases/download/4.5/readFeeds-4.5.nvda-addon
