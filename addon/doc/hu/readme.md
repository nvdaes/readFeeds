# Hírcsatorna-olvasó #

* Készítők: Noelia Ruiz Martínez, Mesar Hameed
* Letöltés [stabil verzió][2]
* Letöltés [Fejlesztői verzió][1]

Ez a kiegészítő lehetővé teszi, hogy az NVDA használatával közvetlenül is
lehessen Atom, és RSS hírcsatornákat olvasni. A hírcsatornák nem frissülnek
automatikusan. Az alábbiakban a hírcsatorna megnevezés egyaránt utal az
Atom, és RSS hírcsatornákra is.

## Telepítés, vagy frissítés: ##

Amennyiben a kiegészítő egy korábbi verzióját használta, és már van a
személyes NVDA konfigurációs mappájában egy RSS, vagy personalFeeds mappa, a
6.0 vagy későbbi verziók telepítése során a program meg fogja kérdezni, hogy
frissíteni, vagy telepíteni szeretné-e a kiegészítőt. Válassza a frissítés
lehetőséget, amennyiben szeretné a korábban használt hírcsatornáit a
legújabb verzióban is változatlanul használni.

## Parancsok: ##

### Hírcsatorna-olvasó menü ###

A Hírcsatorna-olvasó almenü elérhető az NVDA menüjéből (NVDA+N), ahol az
alábbi menüpontokat érheti el:. 

*	 Cikkek listája... megjeleníti az aktuális hírcsatorna cikkeit. Válassza
   ki az elolvasni kívánt cikket, majd nyomja meg az Igen gombot a megfelelő
   weboldal böngészőben való megjelenítéséhez.
*	 Átmeneti hírcsatorna címek... (control+NVDA+shift+enter): Megnyit egy
   ablakot, ahol begépelheti az új hírcsatorna URL címét. Ebben az ablakban
   az aktuális hírcsatorna URL címe látható.
*	 Hírcsatorna betöltése fájlból... (NVDA+control+enter): megnyit egy
   ablakot ahol kiválasztható egy hírcsatorna az URL címét tartalmazó
   fájlból.
*	 Az aktuális hírcsatorna címének mentése fájlba... (NVDA+shift+enter):
   Megnyit egy ablakot, ahol kiválasztható az a fájl, amibe a program az
   aktuális hírcsatorna URL címét elmentheti. Amennyiben az addressFile.txt
   nevű speciális fájlba ment, ez a hírcsatorna lesz az alapértelmezett
   hírcsatorna.
*	 Az aktuális hírcsatorna frissítése (control+shift+NVDA+8): Frissíti az
   aktuális hírcsatornát. A hírcsatornák nem frissülnek automatikusan,
   amikor a Hírcsatorna Olvasó bővítmény elindul.
*	 Személyes hírcsatornák mappájának elmentése... megnyit egy ablakot, ahol
   kiválasztható az a mappa, ahová a program a személyes hírcsatornáit
   tartalmazó personalFeeds mappát elmentheti. Alapértelmezés szerint az
   NVDA konfigurációs mappája van kiválasztva, ami létrehoz egy
   personalFeeds mappát.
*	 Saját hírcsatornák visszaállítása... megnyit egy ablakot, ahol
   kiválasztható az a mappa, ami felülírja a personalFeeds mappában
   található hírcsatornákat. Győződjön meg róla, hogy hírcsatorna URL
   címeket tartalmazó mappát választ ki.

### Billentyűparancsok: ###

*	 Ctrl+Shift+NVDA+Szóköz: Bemondja az aktuális cikk URL címét, kétszeri
   megnyomásra megnyitja a hivatkozott weboldalt.
*	 Ctrl+Shift+NVDA+8: Frissíti a kijelölt hírcsatornát, és bemondja az
   aktuális nevét.
*	 Ctrl+Shift+NVDA+I: Bemondja az aktuális hírcsatorna nevét, kétszeri
   megnyomásra a hírcsatorna nevét és linkjét a vágólapra másolja.
*	 Ctrl+Shift+NVDA+U: Bemondja az előző hírcsatorna nevét. 
*	 Ctrl+Shift+NVDA+O: Bemondja a következő hírcsatorna nevét.

## Figyelmeztetések: ##

*	 Ha a név, vagy az URL másolásra került.
*	 Ha nem lehet elérni/frissíteni egy hírcsatornát, vagy ha az URL nem egy
   létező hírcsatornára mutat.
*	 Az NVDA egy hibaüzenetet jelenít meg, amennyiben nem lehetséges elmenteni
   a személyes hírcsatornák mappáját.
*	 A Cikkek listája ablakának címsorában megjelenik a kiválasztott
   hírcsatorna neve, valamint az elérhető elemek száma.

## Az 1.0 verzió változásai: ##
*	 Kezdeti verzió

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

