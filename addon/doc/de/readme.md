# Feeds lesen #

* Authors: Noelia Ruiz Martínez, Mesar Hameed
* NVDA-Kompatibilität: 2018.3 bis 2019.2
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]

Diese Erweiterung bietet eine einfache Möglichkeit, RSS-Feeds in den
Formaten Atom oder RSS mit NVDA zu lesen. Die Feeds werden nicht automatisch
aktualisiert. Wenn wir weiter unten  von Feeds sprechen, dann meinen wir
sowohl RSS- als auch  ATOM-Feeds.

## Installation oder Aktualisierung: ##

Wenn Sie eine frühere Version dieser Erweiterung verwendet haben und in
Ihrem persönlichen NVDA-Konfigurationsordner ein RSS- oder
personalFeeds-Ordner vorhanden ist, wird bei der Installation der aktuellen
Version ein Dialogfeld angezeigt. In diesem Dialog werden Sie gefragt, ob
Sie eine Aktualisierung oder eine Installation durchführen möchten.  Wählen
Sie aktualisieren, um Ihre gespeicherten Feeds zu behalten und sie in der
neu installierten Version von RSS-Feed-Reader weiter zu verwenden.

## Befehle: ##

### Feed-Reader-Menü ###

Sie können auf das Untermenü RSS-Feed-Reader aus dem NVDA-Menü, Untermenü
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
* Backup Ordner öffnen: Öffnet einen Ordner, in welchem Sicherungsdateien
  der RSS Feeds enthalten sein können. In diesem Ordner können die Feeds
  gelöscht werden, welche bei einer Aktualisierung der Erweiterung nicht
  importiert werden sollen.
* Schließen: Schließt den Dialog.

##### Hinweise #####

* Wenn ein Feed namens tempFeed erstellt wird, benennen Sie ihn bitte
  um. Andernfalls könnte er ersetzt werden, wenn erneut ein Ordner mit
  diesem Namen erstellt wird.
* Der als Standard eingestellte Feed kann nicht entfernt werden. Der
  AddressFile-Feed wird als Standard verwendet, wenn die Konfiguration
  zurückgesetzt wird. Daher kann dieser Ordner nicht gelöscht werden.

####Artikelordner kopieren...####

Öffnet einen Dialog, in dem Sie einen Ordner auswählen können, um Ihre
persönlichen RSS Feed Artikel zu speichern. Standardmäßig ist der
ausgewählte Ordner das Konfigurationsverzeichnis von NVDA und der Ordner
heißt personalFeeds.

#### RSS-Feeds wiederherstellen... ####

Öffnet einen Dialog um einen Ordner zu wählen, der ihren Ordner mit
persönlichen FEEDS ersetzt. Stellen Sie sicher, dass Sie einen Ordner
wählen, der URLs von RSS Feeds enthält.

### Tastenkombinationen: ###

* STRG+Umschalt+NVDA+Leertaste: Sagt die aktuelle Adresse des Artikels
  an. Zweimaliges Drücken öffnet die Webseite des Artikels.
* STRG+Umschalt+NVDA+8: Der ausgewählte RSS-Feed wird neu geladen und der
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

## Änderungen in 8.0 ##

* Bei der Aktualisierung dieser Erweiterung werden die in der vorherigen
  Version gespeicherten Feeds automatisch in die neue Version kopiert, es
  sei denn, Sie möchten ausdrücklich, dass Feeds aus dem
  Hauptkonfigurationsordner von NVDA importiert werden.
* Wenn Sie den Dialog zum Kopieren von Feeds verwenden und der ausgewählte
  Ordner nicht "personalFeeds" heißt, wird ein Unterordner mit diesem Namen
  erstellt, um das Löschen von Verzeichnissen mit wichtigen Daten wie
  Dokumente oder Downloads zu verhindern.

## Änderungen bis 7.0 ##

* Der RSS Feeds Dialog wird mit einen Schalter erweitert, um einen
  Backup-Ordner zu öffnen, der die Sicherungsdateien der Feeds enthalten
  kann.
* Wenn die Eingabe in der Filterfunktion keine Ergebnisse liefert, werden
  die Liste der Feeds und andere Dialogelemente nicht mehr angezeigt. Somit
  meldet NVDA nicht mehr "unbekannt" in der leeren Liste.
* Wenn die Liste der Artikel nicht angezeigt werden kann, beispielsweise
  wegen Fehlern beim Rss Feed, wird NVDA einen Fehler auslösen. Dadurch
  können Sie den RSS Feed Dialog nutzen, ohne NVDA neu starten zu müssen.

## Änderungen bis 6.0 ##

* Wenn der Standardfeed aktualisiert wurde und er aufgrund von
  Serverproblemen nicht mehr funktioniert, werden die vorherigen Artikel
  nicht gelöscht und können mit den entsprechenden Tastenkombinationen
  gelesen werden.
* Fehler behoben: Der Standardfeed kann noch zweimal aktualisiert werden.

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
* NVDA 2016.4 oder höher ist erforderlich.


## Änderungen in 2.0 ##

* Hilfe zur Erweiterung ist über den Dialog "Erweiterungen verwalten"
  verfügbar.

## Änderungen in 1.0 ##

* Ehrstveröffentlichung.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev

[3]: https://addons.nvda-project.org/files/get.php?file=rf-o
