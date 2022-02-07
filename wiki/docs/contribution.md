
# Contributions au projet
Pour contribuer à ce projet, vous devez minimalement suivre les consignes indiquées plus bas. Prenez en compte que celles-ci peuvent être sujettes à changement.

## 🌳 Gestion des branches
Ce projet suit une méthodologie git flow simplifié. Pour ajouter une fonctionnalité, il faut créer une branche à partir de la branche `develop` nommée feature/nom_du_feature. Pour être intégré vos changments au projet, il faut créer un pull request sur la branche `develop`. Seuls les pull request acceptés intégré à `develop` puis poussé sur le `master`.


## ⚡/🐞 Features and Bugs
Les échanges d'information par rapport aux demandes changements sont répertoriés comme issues. Les issues en pair avec les tags sont utilisées pour communiquer au contributeur les problèmes et les demandes. Chacune d'elle est identifiée et enregistrée sur le kanban (project).

#### **Création de demandes/issues**

Lorsqu’un issue est créé, qu’il agisse d’un feature ou d’un bug, il faut suivre les *templates* (gabarits) appropriés.

--- **Le template feature est utilisé pour les demandes de changement**

--- **Le template bug est utilisé pour les problèmes et les questions.**

Les issues seront attachés à un milestone en plus d’être ajoutés automatiquement au Kanban (project)



## 🙏 Pull Request
Pour contribuer au projet et finalement intégrer vos modifications au code, vous devez créer une branche feature/[nom du feature] à partir de la branche `develop`. Afin de faire intégrer les changements faits sur votre branche, créez un pull request sur la branche develop.

**Tenez en compte que toutes les pull request doivent être revues avant d'être accepté.** 

Assurez-vous de lier la pull request à un issue ou bien d'intégrer au message le lien vers le issues, par exemple:
  
```md
  Ajout de lecture d'argument au script de remplissage

  **Détails**
  Le scripte de remplissage prend maintenant des paramètres au démarrage du programme. 
  Par exemple, en faisant 
  
  [...]

  closes #[numéro du issue]

```

#### **Création de pull request**
Pour créer un pull request, assurez-vous d’avoir la version la plus à jour du code afin de causer le moins de conflits. Elles devront être attachées à un message suivant le gabarit.


## 🔖 Respect des tags
Chaque *issue* et pull-request est identifié par au moins une étiquette ou bien *tag*.

- block-by
  - Lorsqu’une tâche dépend d’une autre
- bug
  - Lorsqu’il est question d’un comportement non attendu... un *bug*
- documentation
  - Lorsque le changement est fortement lié à la documentation.
- duplicate
  - Lorsque le changement ou une demande est déjà répertorié.
- feature
  - Pour les nouvelles fonctionnalités
- help wanted
  - Lorsque de l’aide est demandée.
- invalid
  - Lorqu'un changement ne respecte par les lignes consignent ou bien la direction du projet
- question
  - Demande d’information supplémentaire
- request
  - pour les suggestions
- wont-fix
  - Lorsque le issue ou la pull request ne sera pas pris en compte pour des raisons qui ne satisfait pas le tag `invalid`


La liste de toutes les étiquettes se trouve sur [ici](https://github.com/KenJoelTL/LOG680-tp01-eq08/labels).
