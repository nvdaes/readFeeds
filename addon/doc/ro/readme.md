# Citirea  Feedurilor #

* Autori: Noelia Ruiz Martínez, Mesar Hameed
* Descărcați [versiunea stabilă][2]
* Descărcați [versiunea în dezvoltare][1]

Acest add-on oferă o modalitate simplă de a citi feed-uri în format Atom sau
RSS folosind NVDA. Feed-urile nu vor fi actualizate în mod automat. Atunci
când menționăm feed-uri, ne referim atât la fluxuri RSS cât și la cele Atom.

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

- Lista de articole...  Prezintă lista de articole din feed-ul dumneavoastră
curent. Selectați articolul pe care vreți să-l citiți și apăsați butonul OK
pentru a deschide pagina corespunzătoare în navigatorul dumneavoastră.  -
Adresă feed temporară... control + NVDA + shift + enter: Deschide un dialog
pentru tastarea unui nou URL pentru a selecta un alt feed. Feed-ul curent va
fi afișat în acest dialog.  - Încărcarea adresei feed-ului din
filă. NVDA+control+enter: Deschide un dialog pentru a selecta un feed
dintr-o filă salvată care conține un URL feed.  - Salvare adresa feed-ului
curent într-o filă. NVDA+shift+enter: Deschide un dialog pentru a selecta o
filă unde va fi salvat URL-ul feed-ului curent.  Dacă salvați la fila
specială addressFile.txt, acest feed particular va fi utilizat ca feed-ul
dumneavoastră implicit.  - reîmprospătare feed curent: control+shift+NVDA+8:
Reîmprospătează feed-ul curent. Feed-urile nu vor fi actualizate automat
când add-onul Read Feeds este pornit.  - Dosarul Backup feeds. Deschide un
dialog pentru a alege un dosar unde puteți salva directorul de feed-uri
personale din feed-urile dumneavoastră. În mod implicit, folderul selectat
este cel al configurării NVDA, care va crea directorul de feed-uri
personale.  - Restaurare feed-uri. Deschide un dialog pentru a selecta un
dosar care înlocuiește feed-urile dumneavoastră în folderul feed-uri
personale. Asigurați-vă că încărcați un dosar care conține URL-uri ale
feed-urilor.

Notă: Dacă doriți să ștergeți o adresă URL salvată anterior, trebuie doar să
eliminați fișierul corespunzător.

### Comenzi de taste: ###

- Ctrl+Shift+NVDA+Spațiu: Anunță URL-ul articolului curent. Apăsând de două
ori va deschide pagina web.  - Ctrl+Shift+NVDA+8: Reîmprospătează feed-ul
selectat și anunță cel mai recent titlu al său.  - Ctrl+Shift+NVDA+I: Anunță
titlul feed-ului curent. Apăsând de două ori va copia titlul și link-ul
relatat pe planșetă.  - Ctrl+Shift+NVDA+U: Anunță titlul feed-ului
anterior.  - Ctrl+Shift+NVDA+O: Anunță titlul feed-ului următor.

## Notificări: ##

- Când au fost copiate titluri sau URL-uri. - Când în imposibilitatea de a
conecta/reîmprospăta un flux, sau adresa URL nu corespunde unui feed
valid. - NVDA va afișa un mesaj de eroare în cazul în care nu a fost posibil
să facă backup de rezervă la dosarul feed-uri personale. - Titlul dialogului
listă de articol afișează numele selectat și numărul de articole
disponibile.

## Modificări în 2.0 ##
*	 Ghidul add-on-ului este disponibil în managerul de add-on-uri.

## Modificări în 1.0 ##
*	 Versiunea inițială.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

