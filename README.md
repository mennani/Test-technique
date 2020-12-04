# Test-technique

Informations générales :
- Ce projet consiste à développer une API avec le framework Django du langage Python. Cette API calcule par défaut le nombre de multiple de 7 dans 100. 
Si ce nombre est infénieur à 5, l'API affiche le nombre de multiple de 7 dans 100, sinon elle affiche "Alter way".
- L'API est paramétré pour permettre à l'utilisateur de définir:
 * La limite de nombres qu'il souhaite parcourir (ex: 50 au lieu de 100).
 * Le nombre à énumérer (ex: 3 au lieu de 7).
 * Le mot qu'il souhaite afficher (ex: "Hello world!" au lieu de "Alter way" ).
 * Le nombre utilisé pour la comparaison (ex: 20 au lieu de 5)
 
Démarrage :
Cette API est développée en Django, ainsi le programmeur doit installer l'ensemble des bibliothèques de ce framework pour pouvoir utiliser l'API 

Auteur :
Hamza MENNANI

License :
Ce projet a été créé par moi même, tout utilisateur peut l'utiliser ou l'adapter pour répondre à son besoin à condition de citer son auteur.

Exécution du code :
La ligne de commande suivante permet d'éxecuter le package contenant l'API : chemain_vers_le_dossier_d_execution_python\python.exe manage.py runserver port_a_utiliser(8080 par exemple)

Déploiement :
Cette API peut être intégré à toute application de type micro-services sous forme d'un composant logiciel indépendant. A titre d'exemple une application d'aide d'apprentissage 
de calcule. Pour simplifier le déploiement, la personne en charge du DevOps peut définir le code du test de cette API. la tester dans un premier temps et s'assurer que son 
fonctionnement correspond au fonctionnement prévu, puis d'utiliser un outil d'intégration continue comme GitLab CI pour tester l'intégration de l'API avec les autres composants 
de l'application. Ensuite, procéder au déploiement de l'API avec L'orcherstrateur Kubernets dans un conteneur Docker par exemple. 

Versionnement :
Version 1.0 (API fonctionnelle)
