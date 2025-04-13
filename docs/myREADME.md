- Fonctionnalités à implémenter :
    * Avoir une prévisualisation du pdf avant sa génération.
    * Pouvoir échanger avec le LLM afin d'apporter des modifications aux lettres.
    * Avoir une vue générale sur les lettres déjà générées dans la perspective d'établissement d'un dossier administratif donné.
    * Gestion des données :
        - Sauvegarder un certain nombre d'informations répététives dans une base de données.
        - Ne pas sauvegarder les données ponctuelles.

- Informations utiles :
    * session_state est un cache temporaire côté utilisateur.

- Commandes utiles :
    * Création et lancement d'un environnement virtuel :
        - python -m venv venv
        - source venv/bin/activate
    * Sauvegarde des dépendances Python d'un projet donné :
        - pip freeze > requirements.txt
    * Installer les dépendances Python retrouvées dans un fichier requirements.txt :
        - pip install -r requirements.txt

- Liens utiles :
    * https://github.com/markdouthwaite/streamlit-project/blob/master/docs/template-info.md

- Difficultés :
    * Appliquer des styles différents aux boutons.