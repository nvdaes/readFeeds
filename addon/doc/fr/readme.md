# Read Feeds #

* Auteurs : Noelia Ruiz Martínez, Mesar Hameed
* Télécharger [version stable][2]
* Télécharger [version de développement][1]

Ce module complémentaire fournit un moyen simple de lire les flux aux
formats Atom ou RSS à l'aide de NVDA. Les flux ne sont pas actualisées
automatiquement.  Ci-dessous lorsque nous mentionnons flux, nous voulons
dire que les deux signifient flux RSS et ATOM.

## Installation ou Mise à jour : ##

Si vous utilisiez une version antérieure de ce module complémentaire, il y a
un dossier RSS ou personalFeeds dans votre dossier de configuration
personnel de NVDA, lorsque vous installez la version 6.0 ou ultérieure, une
boîte de dialogue vous demandera si vous souhaitez mettre à jour ou
installer.  Choisissez mise à jour pour préserver vos flux enregistrés et
pour continuer à les utiliser dans la nouvelle version installée de
readFeeds.

## Commandes : ##

### Menu Read Feeds ###

Vous pouvez accéder au sous-menu Read Feeds depuis le menu NVDA, NVDA+N, où
les suivantes  options du menu sont disponibles :

*	 Liste de l'article... Affiche la liste de l'article depuis votre flux
   actuelle. Sélectionnez l'article que vous souhaitez lire, puis appuyez
   sur le bouton Accepter pour ouvrir la page de l'article correspondant
   dans votre navigateur.
*	 Adresse du flux temporaire... contrôle + NVDA + Maj + Entrée : Ouvre une
   boîte de dialogue pour taper une nouvelle URL pour sélectionner un autre
   flux. L'URL actuelle sera montré dans cette boîte de dialogue.
*	 Charger l'adresse du flux depuis un fichier... NVDA+contrôle+entrée :
   Ouvre une boîte de dialogue pour sélectionner un flux dans un fichier
   enregistré contenant l'URL du flux.
*	 Enregistrer l'adresse actuelle du flux sur fichier... NVDA+maj+entrée :
   ouvre une boîte de dialogue pour sélectionner le fichier où l'URL du flux
   actuelle sera enregistré.  Si vous enregistrez le fichier spécial
   addressFile.txt, ce flux particulier servira comme votre flux par défaut.
*	 Actualiser le flux actuel : contrôle+maj+NVDA+8 : Actualisez les flux
   sélectionné. Ces flux ne seront pas actualisés automatiquement lorsque
   commence à démarrer le module complémentaire Read Feeds.
*	 Sauvegarde de votre dossier de flux personnelle... ouvre une boîte de
   dialogue pour choisir un dossier où vous pouvez enregistrer le répertoire
   personalFeeds de vos flux. Par défaut, le dossier sélectionné est le
   répertoire de configuration de NVDA, qui créera le répertoire
   personalFeeds.
*	 Restaurer les flux personnels... Ouvre une boîte de dialogue pour
   sélectionner un dossier qui remplace vos flux dans le dossier
   personalFeeds. Assurez-vous que vous chargez un dossier contenant les
   URLs des flux.

### Commandes clavier : ###

*	 Ctrl+Maj+NVDA+Espace : Annonce l'URL de l'article actuel. En appuyant
   deux fois ouvrira la page web.
*	 Ctrl+Maj+NVDA+8 : Actualise le flux sélectionné et annonce son plus
   récent titre.
*	 Ctrl+Maj+NVDA+I : Annonce le titre du flux actuel. En appuyant deux fois
   copie le titre et le lien associée dans le presse-papiers.
*	 Ctrl+Maj+NVDA+U : Annonce le titre du flux précédent.
*	 Ctrl+Maj+NVDA+O : Annonce le titre du flux suivant.

## Notifications : ##

*	 Lorsque le titre ou l'URL ont été copiés.
*	 Lorsqu'il est Impossible de se connecter/actualiser un flux, ou l'URL ne
   correspond pas à un flux valide.
*	 NVDA affiche un message d'erreur s'Il n'était pas possible de sauvegarder
   le dossier personalFeeds.
*	 Dans le titre de la boîte de dialogue liste de l'article affiche le nom
   de flux sélectionné et le nombre d'éléments disponibles.

## Changements pour la version 1.0 ##
*	 Première version.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rf-dev

[2]: http://addons.nvda-project.org/files/get.php?file=rf

