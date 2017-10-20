# Read Feeds #

* Autori: Noelia Ruiz Martínez, Mesar Hameed
* Descărcați [versiunea stabilă][1]
* Descărcați [versiunea în dezvoltare][2]

Acest supliment oferă o modalitate simplă de a citi feed-uri în format Atom
sau RSS folosind NVDA. Feed-urile nu vor fi actualizate în mod
automat. Atunci când menționăm feed-uri, ne referim atât la fluxuri RSS cât
și la cele Atom.

## Instalare sau Actualizare: ##

Dacă ați utilizat o versiune anterioară a acestui add-on și există un dosar
RSS sau un dosar de feed-uri personale în dosarul dumneavoastră de
configurare al NVDA, când se instalează versiunea 6.0 sau mai nou, un dialog
vă va întreba dacă vreți să upgradați sau instalați. Alegeți actualizare
pentru a păstra feed-urile salvate și pentru a continua să le folosiți în
noua versiune instalată a cititorului de feed-uri.

## Comenzi: ##

### Meniul Read Feeds  ###

Puteți accesa submeniul Read Feeds din meniul NVDA, NVDA+N, unde sunt
disponibile următoarele opțiuni:

#### Fluxuri ####

Deschide un dialog cu următoarele controale:

* Filtrează după: O casetă de editare pentru căutarea fluxurilor salvate
  anterior.
* O listă a fluxurilor salvate.
* - Filtrat după: O casetă de editare pentru a căuta fluxurilr salvate
  înainte.  - O listă a fluxurilor salvate.  - listă de articole: Deschide
  un dialog care prezintă lista de articole din fluxul curent. Selectați
  articolul pe care vreți să-l citiți și apăsați butonul OK pentru a
  deschide pagina în navigator.  - Nou: Deschide un dialog cu o casetă de
  editare pentru a introduce adresa unui flux nou. Dacă adresa este validă
  și fluxul poate fi salvat, numele său, bazat pe titlul fluxului, va apărea
  la sfârșitul listei de fluxuri.  -  Redenumire: Deschide un dialog cu o
  casetă de editare pentru a redenumi fluxul selectat.  - Ștergere: Deschide
  un dialog pentru a șterge fluxul selectat după confirmare.  -  Setează
  implicit: Setează fluxul selectat ca implicit, deci articolele sale pot fi
  accesate cu gesturile NVDA-ului.  - Închidere: Închide dialogul
  fluxurilor.
* Nou: Deschide un dialog cu o casetă de editare pentru introducerea adresei
  unui nou flux. Dacă adresa este validă și fluxul poate fi salvat, numele
  său bazat pe titlul acestuia va apărea la sfârșitul listei de fluxuri.
* Redenumire: Deschide un dialog cu o casetă de editare pentru redenumirea
  fluxului selectat.
* Ștergere: Deschide un dialog pentru ștergerea fluxului selectat după
  confirmare.
* Setare ca implicit: Setează fluxul selectat ca implicit, așa că articolele
  sale pot fi accesate cu gesturile NVDA-ului.
* Închidere: Închide dialogul fluxurilor.

##### Note #####

* Dacă se creează un flux numit tempFeed, vă rugăm să-l redenumiți, deoarece
  acest fișier ar putea fi înlocuit atunci când este necesar pentru a crea
  un flux al cărui nume deja există.
* Fluxul setat ca implicit nu poate fi șters. Fluxul addressFile va fi
  utilizat ca implicit atunci când configurația este resetată, deci nu poate
  fi șters.

Copiază dosarul fluxurilor... 

Deschide un dialog pentru a alege un dosar unde să puteți salva dosarul
personalFeeds al fluxurilor dumneavoastră. În mod implicit, folderul
selectat este cel al configurației NVDA, care va crea dosarul personalFeeds.

#### Restaurare fluxuri... ####

Deschide un dialog pentru selectarea unui dosar care înlocuiește fluxurile
dumneavoastră în dosarul personalFeeds. Asigurați-vă că încărcați un dosar
ce conține URL-urile fluxurilor.

### Comenzi de taste: ###

* Ctrl+Shift+NVDA+Spațiu: Anunță URL-ul articolului curent. Apăsarea de două
  ori va deschide pagina web.
* Ctrl+Shift+NVDA+8: Reîmprospătează fluxul selectat și anunță cel mai
  recent titlu al său.
* Ctrl+Shift+NVDA+I: Anunță titlul fluxului curent și link-ul
  acestuia. Apăsarea de două ori va copia titlul și link-ul relatat pe
  planșetă.
* Ctrl+Shift+NVDA+U: Anunță titlul fluxului precedent.
* Ctrl+Shift+NVDA+O: Anunță titlul fluxului succedent.

## Notificări: ##

* Când titlul sau URL-ul a fost copiat.
* Atunci când nu se poate conecta/reîmprospăta un flux, sau URL-ul nu
  corespunde unui flux valid.
* NVDA va afișa un mesaj de eroare dacă nu a fost posibilă crearea unei
  copii de siguranță sau restaurarea dosarului personalFeeds.
* Dialogul titlului listei articolelor afișează numele fluxului selectat și
  numărul elementelor disponibile.


## Modificări în 3.0 ##

* Dialogul pentru administrarea fișierelor fluxurilor a fost eliminat. În
  prezent, funcționalitatea lui este inclusă în dialogul fluxurilor.
* Prezentarea vizuală a dialogurilor a fost îmbunătățită, aderând la
  aspectul dialogurilor afișate în NVDA.
* Fluxul implicit este salvat în configurația NVDA. Prin urmare, este
  posibilă setarea fluxurilor implicite diferite în configurarea
  profilurilor.
* Necesită NVDA 2016.4.


## Modificări în 2.0 ##

* Ghidul suplimentului este disponibil în managerul de add-on-uri.

## Modificări în 1.0 ##

* Versiunea inițială.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev
