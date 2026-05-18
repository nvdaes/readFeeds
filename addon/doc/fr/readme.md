# Read Feeds

- Auteurs : Noelia Ruiz Martínez, Mesar Hameed
- Compatible avec NVDA 2021.1
- Download [stable version][1]
- Download [development version][2]

Cette extension fournit un moyen simple de lire les flux aux formats Atom ou
RSS à l'aide de NVDA.
Les flux ne sont pas actualisés automatiquement.
Ci-dessous lorsque nous mentionnons flux, nous voulons dire que les deux
signifient flux RSS et ATOM.

## Installation or Update:

If you used a previous version of this addon, and there is an RSS or personalFeeds folder in your personal NVDA configuration folder,
when installing the current version, a dialog will ask if you want to upgrade or install.
Choose update to preserve your saved feeds and to continue using them in the new installed version of readFeeds.

## Commandes

### Dialogue Read Feeds

Vous pouvez accéder au dialogue Read Feeds depuis le menu NVDA, sous-menu
Outils, élément Flux.

#### Feeds...

Opens a dialog with the following controls:

- Filtrer par : Une zone d'édition pour rechercher des flux précédemment
  enregistrés.
- A list of the saved feeds.
- Liste des articles : Ouvre une boîte de dialogue qui présente la liste des
  articles de vos flux actuel. Sélectionnez l'article que vous souhaitez
  lire et appuyer sur Entrée ou Ouvrir la page Web du bouton de l'article
  sélectionné pour ouvrir la page correspondante dans votre
  navigateur. Appuyez sur le bouton À propos de l'article pour ouvrir une
  boîte de dialogue affichant le titre et le lien de l’article sélectionné ;
  dans cette boîte de dialogue, vous serez en mesure de copier ces
  informations dans le presse-papiers.
- Ouvrir le flux : Ouvre le flux sélectionné dans l'application par défaut.
- Nouveau : Ouvre une boîte de dialogue avec une zone d'édition pour entrer
  l'adresse d'un nouveau flux. Si l'adresse est valide et que le flux peut
  être enregistré, son nom, basé sur le titre du flux, apparaît au bas de la
  liste des flux.
- Renommer : Ouvre une boîte de dialogue avec une zone d'édition pour
  renommer le flux sélectionné.
- Supprimer : Ouvre une boîte de dialogue pour supprimer le flux sélectionné
  après confirmation.
- Définir par défaut : Définit le flux sélectionné comme valeur par défaut,
  afin que ses articles soient accessibles avec les gestes de NVDA.
- Open folder containing a backup of feeds: Opens a folder which may contain a backup of feeds. This can be useful to explore and delete feeds which shouldn't be imported when the add-on is updated.
- Fermer : Ferme la boîte de dialogue Flux.

##### Notes

- If a feed named tempFeed is created, please rename it, as this file could be replaced when needed to create a feed whose name already exists.
- The feed set as the default can't be removed. The addressFile feed will be use as the default when the configuration is reset, so it can't be deleted.

\####Copy feeds folder... ####

Opens a dialog to choose a folder where you can save the personalFeeds directory of your feeds. By default the selected folder is the NVDA's configuration directory, which will create the personalFeeds directory.

#### Restore feeds...

Opens a dialog to select a folder which replaces your feeds in the personalFeeds folder. Make sure you load a folder containing feeds URLs.

### Commandes clavier

- Ctrl+Maj+NVDA+Espace : Annonce l'URL de l'article actuel. En appuyant deux
  fois ouvrira la page web.
- Ctrl+Maj+NVDA+8 : Actualise le flux sélectionné et annonce son plus récent
  titre.
- Ctrl+Maj+NVDA+I : Annonce le titre et le lien du flux actuel. En appuyant
  deux fois copie le titre et le lien associée dans le presse-papiers.
- Ctrl+Maj+NVDA+U : Annonce le titre du flux précédent.
- Ctrl+Maj+NVDA+O : Annonce le titre du flux suivant.

## Notifications

- Lorsque le titre ou l'URL ont été copiés.
- Lorsqu'il est Impossible de se connecter/actualiser un flux, ou l'URL ne
  correspond pas à un flux valide.
- NVDA affichera un message d'erreur si un nouveau flux ne peut pas être
  créé.
- La boîte de dialogue affiche Le titre de la Liste de l'article le nom de
  flux sélectionné et le nombre d'éléments disponibles.

## Changements pour la version 8.0

- Lorsque l'extension est mise à jour, les flux enregistrés dans la version
  précédente de l'extension seront automatiquement copiés dans la nouvelle
  version, à moins que vous ne préfériez importer les flux enregistrés dans
  le dossier de configuration principal de NVDA.
- Lors de l'utilisation de la boîte de dialogue pour copier des flux, si le
  dossier choisi n'est pas nommé personalFeeds, un sous-dossier portant ce
  nom sera créé pour empêcher la suppression des répertoires contenant des
  données importantes, telles que Documents ou Téléchargements.

## Changements pour la version 7.0

- La boîte de dialogue Flux comprend un bouton pour ouvrir un dossier
  pouvant contenir une sauvegarde des flux.
- Lorsque vous utilisez la zone d'édition pour filtrer les flux, si aucun
  résultat n'est trouvé, la liste des flux et autres contrôles sont
  désactivés, afin que NVDA ne signale pas "inconnu" dans la liste vide.
- Si la boîte de dialogue de la liste des articles ne peut pas être
  affichée, par exemple en raison d'erreurs dans le flux, NVDA générera une
  erreur, afin que la boîte de dialogue des flux puisse être utilisée sans
  redémarrer NVDA.

## Changements pour la version 6.0

- Lorsque le flux par défaut a été mis à jour et qu'il cesse de fonctionner
  en raison de problèmes de serveur, les articles précédents ne sont pas
  supprimés et peuvent être lus à l'aide des frappes correspondantes.
- Correction de la régression : Le flux par défaut peut être mis à jour deux
  fois.

## Changements pour la version 5.0

- La boîte de dialogue Liste des articles a été améliorée.
- Compatible avec NVDA 2018.3 ou version ultérieure (requis).
- Compatible avec NVDA 2023.1.

## Changements pour la version 4.0

- Ajout d'un bouton pour ouvrir le flux sélectionné dans la boîte de
  dialogue Flux.

## Changements pour la version 3.0

- Les boîtes de dialogue pour gérer les fichiers de flux ont été
  supprimées. Maintenant, leur fonctionnalité est incluse dans la boîte de
  dialogue Flux.
- La présentation visuelle des dialogues a été améliorée, en respectant
  l'apparence des dialogues présentés dans NVDA.
- Le flux par défaut est sauvegardé dans la configuration NVDA. Par
  conséquent, il est possible de définir des flux différents par défaut dans
  les profils de configuration.
- Nécessite NVDA 2016.4.

## Changements pour la version 2.0

- L'aide de l'extension est disponible à partir du Gestionnaire
  d'extensions.

## Changements pour la version 1.0

- Première version.

[1]: http://addons.nvda-project.org/files/get.php?file=rf
[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev
[3]: http://addons.nvda-project.org/files/get.php?file=rf-o
