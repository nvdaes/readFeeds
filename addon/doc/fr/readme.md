# Read Feeds #

* Auteurs : Noelia Ruiz Martínez, Mesar Hameed
* NVDA compatibility: 2018.3 to 2019.2
* Télécharger [version stable][1]
* Télécharger [version de développement][2]

Cette extension fournit un moyen simple de lire les flux aux formats Atom ou
RSS à l'aide de NVDA. Les flux ne sont pas actualisés automatiquement.
Ci-dessous lorsque nous mentionnons flux, nous voulons dire que les deux
signifient flux RSS et ATOM.

## Installation ou Mise à jour : ##

Si vous utilisiez une version antérieure de cette extension, il y a un
dossier RSS ou personalFeeds dans votre dossier de configuration personnel
de NVDA, lorsque vous installez la version actuelle, une boîte de dialogue
vous demandera si vous souhaitez mettre à jour ou installer.  Choisissez
mise à jour pour préserver vos flux enregistrés et pour continuer à les
utiliser dans la nouvelle version installée de readFeeds.

## Commandes : ##

### Menu Read Feeds ###

Vous pouvez accéder au sous-menu Read Feeds depuis le menu NVDA, sous-menu
Outils, où les suivantes  options du menu sont disponibles :

#### Flux... ####

Ouvre une boîte de dialogue avec les contrôles suivants :

* Filtrer par : Une zone d'édition pour rechercher des flux précédemment
  enregistrés.
* Une liste des flux enregistrés.
* Liste des articles : Ouvre une boîte de dialogue qui présente la liste des
  articles de vvos flux actuel. Sélectionnez l'article que vous souhaitez
  lire et appuyer sur Entrée ou Ouvrir la page Web du bouton de l'article
  sélectionné pour ouvrir la page correspondante dans votre
  navigateur. Appuyez sur le bouton À propos de l'article pour ouvrir une
  boîte de dialogue affichant le titre et le lien de l’article sélectionné ;
  dans cette boîte de dialogue, vous serez en mesure de copier ces
  informations dans le presse-papiers.
* Ouvrir le flux : Ouvre le flux sélectionné dans l'application par défaut.
* Nouveau : Ouvre une boîte de dialogue avec une zone d'édition pour entrer
  l'adresse d'un nouveau flux. Si l'adresse est valide et que le flux peut
  être enregistré, son nom, basé sur le titre du flux, apparaît au bas de la
  liste des flux.
* Renommer : Ouvre une boîte de dialogue avec une zone d'édition pour
  renommer le flux sélectionné.
* Supprimer : Ouvre une boîte de dialogue pour supprimer le flux sélectionné
  après confirmation.
* Définir par défaut : Définit le flux sélectionné comme valeur par défaut,
  afin que ses articles soient accessibles avec les gestes de NVDA.
* Open folder containing a backup of feeds: Opens a folder which may contain
  a backup of feeds. This can be useful to explore and delete feeds which
  shouldn't be imported when the add-on is updated.
* Fermer : Ferme la boîte de dialogue Flux.

##### Notes #####

* Si un flux nommé tempFeed est créé, renommez-le, car ce fichier pourrait
  être remplacé si nécessaire pour créer un flux dont le nom existe déjà.
* Le flux défini par défaut ne peut pas être supprimé. Le flux addressFile
  sera utilisé comme valeur par défaut lors de la réinitialisation de la
  configuration, donc il ne peut pas être supprimé.

####Copier le dossier des flux... ####

Ouvre une boîte de dialogue pour choisir un dossier dans lequel vous pouvez
enregistrer le dossier personalFeeds de vos flux. Par défaut, le dossier
sélectionné est dans la configuration de NVDA, qui créera le répertoire
personalFeeds.

#### Restaurer les flux... ####

Ouvre une boîte de dialogue pour sélectionner un dossier qui remplace vos
flux dans le dossier personalFeeds. Assurez-vous de charger un dossier
contenant des URL de flux.

### Commandes clavier : ###

* Ctrl+Maj+NVDA+Espace : Annonce l'URL de l'article actuel. En appuyant deux
  fois ouvrira la page web.
* Ctrl+Maj+NVDA+8 : Actualise le flux sélectionné et annonce son plus récent
  titre.
* Ctrl+Maj+NVDA+I : Annonce le titre et le lien du flux actuel. En appuyant
  deux fois copie le titre et le lien associée dans le presse-papiers.
* Ctrl+Maj+NVDA+U : Annonce le titre du flux précédent.
* Ctrl+Maj+NVDA+O : Annonce le titre du flux suivant.

## Notifications : ##

* Lorsque le titre ou l'URL ont été copiés.
* Lorsqu'il est Impossible de se connecter/actualiser un flux, ou l'URL ne
  correspond pas à un flux valide.
* NVDA affichera un message d'erreur s'Il n'était pas possible de
  sauvegarder ou de restaurer le dossier personalFeeds.
* La boîte de dialogue affiche Le titre de la Liste de l'article le nom de
  flux sélectionné et le nombre d'éléments disponibles.

## Changes for 8.0 ##

* When the add-on is updated, feeds saved in the previous version of the
  add-on will be automatically copied to the new version, unless you prefer
  to import feeds saved in the main configuration folder of NVDA.
* When using the dialog to copy feeds, if the chosen folder is not named
  personalFeeds, a subfolder with this name will be created to prevent the
  deletion of directories containing important data, such as Documents or
  Downloads.

## Changes for 7.0 ##

* The Feeds dialog includes a button to open a folder which may contain a
  backup of feeds.
* When using the edit box to filter feeds, if no results are found, the list
  of feeds and other controls are disabled, so that NVDA doesn't report
  "unknown" in the empty list.
* If the list of articles dialog can't be shown, for example due to errors
  in the feed, NVDA will raise an error, so that the feeds dialog can be
  used without restarting NVDA.

## Changements pour la version 6.0 ##

* Lorsque le flux par défaut a été mis à jour et qu'il cesse de fonctionner
  en raison de problèmes de serveur, les articles précédents ne sont pas
  supprimés et peuvent être lus à l'aide des frappes correspondantes.
* Correction de la régression : Le flux par défaut peut être mis à jour deux
  fois.

## Changements pour la version 5.0 ##

* La boîte de dialogue Liste des articles a été améliorée.
* Compatible avec NVDA 2018.3 ou version ultérieure (requis).
* Si nécessaire, vous pouvez télécharger la [dernière version compatible
  avec NVDA 2017.3][3].

## Changements pour la version 4.0 ##

* Ajout d'un bouton pour ouvrir le flux sélectionné dans la boîte de
  dialogue Flux.

## Changements pour la version 3.0 ##

* Les boîtes de dialogue pour gérer les fichiers de flux ont été
  supprimées. Maintenant, leur fonctionnalité est incluse dans la boîte de
  dialogue Flux.
* La présentation visuelle des dialogues a été améliorée, en respectant
  l'apparence des dialogues présentés dans NVDA.
* Le flux par défaut est sauvegardé dans la configuration NVDA. Par
  conséquent, il est possible de définir des flux différents par défaut dans
  les profils de configuration.
* Nécessite NVDA 2016.4.


## Changements pour la version 2.0 ##

* L'aide de l'extension est disponible à partir du Gestionnaire
  d'extensions.

## Changements pour la version 1.0 ##

* Première version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rf

[2]: https://addons.nvda-project.org/files/get.php?file=rf-dev

[3]: https://addons.nvda-project.org/files/get.php?file=rf-o
