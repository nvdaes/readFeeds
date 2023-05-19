# Read Feeds #

* Auteurs : Noelia Ruiz Martínez, Mesar Hameed
* Télécharger [version stable][1] (compatible avec NVDA 2019.3 et au-delà)
* Télécharger [version béta][2] (compatible avec NVDA 2019.3 et au-delà)

Cette extension fournit un moyen simple de lire les flux aux formats Atom ou
RSS à l'aide de NVDA. Les flux ne sont pas actualisés automatiquement.
Ci-dessous lorsque nous mentionnons flux, nous voulons dire que les deux
signifient flux RSS et ATOM.

## Commandes ##

### Dialogue Read Feeds ###

Vous pouvez accéder au dialogue Read Feeds depuis le menu NVDA, sous-menu
Outils, élément Flux.

Il contient les contrôles suivants :

* Filtrer par : Une zone d'édition pour rechercher des flux précédemment
  enregistrés.
* Une liste des flux enregistrés, a le focus lorsque la boîte de dialogue
  est ouverte.
* Liste des articles : Ouvre une boîte de dialogue qui présente la liste des
  articles de vos flux actuel. Sélectionnez l'article que vous souhaitez
  lire et appuyer sur Entrée ou Ouvrir la page Web du bouton de l'article
  sélectionné pour ouvrir la page correspondante dans votre
  navigateur. Appuyez sur le bouton À propos de l'article pour ouvrir une
  boîte de dialogue affichant le titre et le lien de l’article sélectionné ;
  dans cette boîte de dialogue, vous serez en mesure de copier ces
  informations dans le presse-papiers.
* Ouvrir le flux : Ouvre le flux sélectionné dans l'application par défaut.
* Ouvrir le flux au format HTML : ouvre le flux sélectionné dans le
  navigateur Web par défaut. Vous pourrez afficher ou masquer les dates de
  publication et les boutons pour copier les informations sur les articles
  dans le presse-papiers.
* Copier l'adresse du flux : ouvre une boîte de dialogue pour confirmer si
  vous souhaitez copier l'adresse du flux dans le presse-papiers.
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
* Importer les flux depuis un fichier OPML : ouvre une boîte de dialogue
  pour ajouter de nouveaux flux à partir d'un fichier OPML.
* Enregistrer les flux dans un fichier OPML : ouvre une boîte de dialogue
  pour enregistrer les flux disponibles à partir de la boîte de dialogue
  Flux  dans un fichier OPML.
* Préférences : Ouvre la boîte de dialogue des paramètres pour readFeeds,
  également disponible dans le menu de NVDA, Préférences, paramètres,
  catégorie readFeeds.
* Fermer : Ferme la boîte de dialogue Flux.

### Notes #####

* Le champ d'édition Filtrer par peut être placée après le bouton Ouvrir
  l'article dans le menu de NVDA, Préférences, Paramètres, Catégorie Lire
  les flux, ou en appuyant sur le bouton Préférences de la boîte de dialogue
  Flux.
* Ce panneau a une option pour afficher les dates des articles dans le
  dialogue Liste des articles.


### Commandes clavier ###

* Ctrl+Maj+NVDA+Espace : Annonce l'URL de l'article actuel. En appuyant deux
  fois ouvrira la page web.
* Ctrl+Maj+NVDA+8 : Actualise le flux sélectionné et annonce son plus récent
  titre.
* Ctrl+Maj+NVDA+I : Annonce le titre et le lien du flux actuel. En appuyant
  deux fois copie le titre et le lien associée dans le presse-papiers.
* Ctrl+Maj+NVDA+U : Annonce le titre du flux précédent.
* Ctrl+Maj+NVDA+O : Annonce le titre du flux suivant.

## Notifications ##

* Lorsque le titre ou l'URL ont été copiés.
* Lorsqu'il est Impossible de se connecter/actualiser un flux, ou l'URL ne
  correspond pas à un flux valide.
* NVDA affichera un message d'erreur si un nouveau flux ne peut pas être
  créé.
* La boîte de dialogue affiche Le titre de la Liste de l'article le nom de
  flux sélectionné et le nombre d'éléments disponibles.

## Changements pour la version 21.0

* Les flux avec des articles sans titre peuvent être présentés dans la boîte
  de dialogue des articles et ouverts en HTML.

## Changements pour la version 20.0

* universalFeedParser est mis à jour vers la 5.0.1, ajoutant la prise en
  charge de plus de flux.

## Changements pour la version 14.0

* Correction d'un bug qui rendait impossible d'ajouter des flux.

## Changements pour la version 13.0

* L'extension ne peut pas être utilisée sur des écrans sécurisés.
* Les flux sont gérés à partir des fichiers OPML.
* En raison des modifications du système de gestion des flux, il y a des
  modifications dans le fichier de configuration où le flux par défaut est
  défini. S'il vous plaît, utilisez la boîte de dialogue Flux si vous
  souhaitez le définir à nouveau.
* Vos anciens fichiers texte utilisés dans les versions précédentes seront
  automatiquement importés dans le nouveau format OPML au démarrage de
  l'extension.
* La fonction copier et restaurer les flux a été remplacée par la
  possibilité d'importer et d'enregistrer dans les fichiers OPML.
* Les flux non formés peuvent être traités avant d'être ajoutés pour les
  rendre compatibles avec l'extension.
* Dans le panneau des paramètres Read Feeds, une nouvelle option permet
  d'afficher les dates de l'article dans le dialogue Liste des articles.

## Changements pour la version 12.0

* Correction d'un bug qui faisait que les raccourcis pour les éléments du
  menu Outils de NVDA ne fonctionnaient pas comme prévu.

## Changements pour la version 11.0

* Compatible avec NVDA 2021.1

## Changements pour la version 10.0 ##

* Ajout d'un bouton pour ouvrir le flux sélectionné au format HTML dans le
  navigateur Web par défaut.
* Si un nouveau flux ne peut pas être créé, cela sera notifié par un
  dialogue d'erreur.
* Amélioration de l'ordre et de la présentation de certains articles.
* Davantage de flux peuvent être pris en charge.
* Lorsque la boîte de dialogue des flux est ouverte, la liste des flux aura
  le focus au lieu de la zone d'édition de recherche.
* Vous pouvez choisir si la zone d'édition de recherche est placée après la
  liste des flux, utile pour mettre en focus la liste même lorsque vous
  basculez d'une autre fenêtre sans fermer la boîte de dialogue Flux.
* Ajout d'un bouton pour copier l'adresse du flux dans le presse-papiers à
  partir de la boîte de dialogue des flux.

## Changements pour la version 9.0 ##

* Nécessite NVDA 2019.3 ou ultérieure.

## Changements pour la version 8.0 ##

* Lorsque l'extension est mise à jour, les flux enregistrés dans la version
  précédente de l'extension seront automatiquement copiés dans la nouvelle
  version, à moins que vous ne préfériez importer les flux enregistrés dans
  le dossier de configuration principal de NVDA.
* Lors de l'utilisation de la boîte de dialogue pour copier des flux, si le
  dossier choisi n'est pas nommé personalFeeds, un sous-dossier portant ce
  nom sera créé pour empêcher la suppression des répertoires contenant des
  données importantes, telles que Documents ou Téléchargements.

## Changements pour la version 7.0 ##

* La boîte de dialogue Flux comprend un bouton pour ouvrir un dossier
  pouvant contenir une sauvegarde des flux.
* Lorsque vous utilisez la zone d'édition pour filtrer les flux, si aucun
  résultat n'est trouvé, la liste des flux et autres contrôles sont
  désactivés, afin que NVDA ne signale pas "inconnu" dans la liste vide.
* Si la boîte de dialogue de la liste des articles ne peut pas être
  affichée, par exemple en raison d'erreurs dans le flux, NVDA générera une
  erreur, afin que la boîte de dialogue des flux puisse être utilisée sans
  redémarrer NVDA.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds

[2]: https://www.nvaccess.org/addonStore/legacy?file=readFeeds-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=rf-o
