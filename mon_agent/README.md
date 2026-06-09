#  Atelier 1 — Agent ReAct from scratch

## 📌 Description

Ce projet consiste à construire un agent IA en Python utilisant une boucle de raisonnement ReAct (Reasoning + Acting). L’agent est capable de comprendre une requête utilisateur, choisir un outil adapté, exécuter des fonctions Python et retourner une réponse finale.

##  Architecture

mon_agent/
├── agent.py      # logique de l’agent (boucle ReAct)
├── tools.py      # fonctions Python utilisables
├── prompts.py    # prompt système
└── main.py       # point d’entrée CLI

##  Outils disponibles

- get_current_time → heure actuelle  
- list_directory → liste les fichiers d’un dossier  
- read_file → lecture de fichier texte  
- get_weather → météo via API Open-Meteo  
- get_directory_size → taille d’un dossier  
- search_wikipedia → résumé Wikipedia  

##  Lancement

cd mon_agent  
python main.py  

##  Exemple d’utilisation

> Quelle heure est-il ?  
> Liste les fichiers de mon dossier Downloads  

L’agent peut enchaîner plusieurs outils pour répondre.

## 🎯 Objectif pédagogique

Comprendre les agents IA, implémenter une boucle ReAct et utiliser des tools Python dynamiques.