# Hírcsatorna-olvasó #

* Készítők: Noelia Ruiz Martínez, Mesar Hameed
* Letöltés [stabil verzió][2]
* Letöltés [Fejlesztői verzió][1]

Ez a kiegészítő lehetővé teszi, hogy az NVDA használatával közvetlenül is
lehessen Atom és RSS hírcsatornákat olvasni. A hírcsatornák nem frissülnek
automatikusan. Az alábbiakban a hírcsatorna megnevezés egyaránt utal az Atom
és RSS hírcsatornákra is.

## Telepítés vagy frissítés: ##

Amennyiben a kiegészítő egy korábbi verzióját használta, és már van a
személyes NVDA konfigurációs mappájában egy RSS vagy personalFeeds mappa, a
6.0 vagy későbbi verziók telepítése során a program meg fogja kérdezni, hogy
frissíteni vagy telepíteni szeretné-e a kiegészítőt. Válassza a frissítés
lehetőséget, amennyiben szeretné a korábban használt hírcsatornáit a
legújabb verzióban is változatlanul használni.

## Parancsok: ##

### Hírcsatorna-olvasó menü ###

A Hírcsatorna-olvasó almenü elérhető az NVDA menüjéből (NVDA+N), ahol az
alábbi menüpontokat érheti el: 

- Cikkek Listája: a kiválasztott hírcsatorna cikkeit tartalmazza. Válassza
ki az olvasni kívánt cikket, majd az Igen gomb lenyomásával a cikkhez
tartozó weboldal megnyílik a böngészőben.  - Átmeneti hírcsatorna
címek... control + NVDA + shift + enter: Megnyit egy párbeszédablakot új
hírcsatorna URL megadásához, az aktuális cím látszik a szerkesztőmezőben.  -
Hírcsatorna betöltése fájlból... NVDA+control+enter: Megnyit egy
párbeszédablakot a hírcsatorna URL címét tartalmazó fájl megnyitásához.  -
Az Aktuális hírcsatorna címének mentése fájlba... NVDA+shift+enter: Megnyit
egypárbeszédablakot, ahol kiválasztható az a fájl, ahová az aktuális
hírcsatorna címét menteni lehet. Az addressFile.txt speciális fájlba
elmentett URL az alapértelmezett hírcsatorna.  - Az aktuális hírcsatorna
frissítése control+shift+NVDA+8: Frissíti az aktuális hírcsatornát. A
hírcsatornák nem frissülnek automatikusan a readFeeds bővítmény futásakor.
- Személyes hírcsatornák mappájának elmentése... Megnyit egy
párbeszédablakot, ahol megadható a personalFeeds mappa mentési
helye. Alapértelmezés szerint az NVDA konfigurációs mappájában jön létre egy
personalFeeds mappa.  - Saját hírcsatornák visszaállítása... Megnyit egy
párbeszédablakot, ahol kiválasztható az a mappa, amiből felülírásra kerül a
personalFeeds könyvtár tartalma. Győződjön meg róla, hogy a kiválasztott
mappa hírcsatornák URL-címét tartalmazza!

Megjegyzés: Elmentett hírcsatorna URL törléséhez törölni kell a hozzá
tartozó fájlt.

### Billentyűparancsok: ###

- Ctrl+Shift+NVDA+Space: Az aktuális cikk URL-címének bemondása. Kétszeri
lenyomásra megnyitja a weboldalt.  - Ctrl+Shift+NVDA+8: Frissíti az aktuális
hírcsatornát, és bemondja a legfrissebb cikk címét.  - Ctrl+Shift+NVDA+I:
Bemondja az aktuális hírcsatorna nevét. Kétszeri megnyomásra a vágólapra
másolja a nevét, és a hozzá tartozó URL-t.  - Ctrl+Shift+NVDA+U: Bemondja az
előző hírcsatorna nevét.  - Ctrl+Shift+NVDA+O: Bemondja a következő
hírcsatorna nevét.

## Figyelmeztetések: ##

- Amikor a cím vagy az URL másolásra kerül.  - Amikor nem lehet kapcsolódni,
vagy frissíteni a hírcsatornát, vagy épp az URL nem tartozik egy létező
hírcsatornához.  - Az NVDA hibaüzenetet jelenít meg, ha nem sikerült
elmenteni a personalFeeds mappát.  - A cikkek listája megjeleníti a
kiválasztott hírcsatorna nevét és az elérhető elemek számát.

## A 2.0 verzió változásai: ##
*	 A kiegészítő súgója elérhető a bővítmények kezelése párbeszédablakról is.

## Az 1.0 verzió változásai: ##
*	 Kezdeti verzió

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

