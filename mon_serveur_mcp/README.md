#  Atelier 2 — Serveur MCP (Model Context Protocol)

##  Description

Ce projet implémente un serveur MCP en Python permettant d’exposer des outils utilisables par un LLM (Cursor). Le serveur permet d’exécuter des fonctions Python locales via le protocole MCP.

##  Architecture

mon_serveur_mcp/
├── server.py   # serveur MCP
├── tools.py    # fonctions Python
└── pyproject.toml

##  Outils exposés

- get_disk_usage -> calcule la taille d’un dossier en mégaoctets  
- get_weather -> donne la meteo via une API externe

##  Installation

pip install mcp requests  

##  Configuration Cursor

Créer le fichier :
C:\Users\<USER>\.cursor\mcp.json

{
  "mcpServers": {
    "mon-serveur": {
      "command": "python",
      "args": [
        "C:/Users/<USER>/GenAI-module/mon_serveur_mcp/server.py"
      ]
    }
  }
}

##  Tests

> Quelle est la taille de mon dossier Downloads ?  
> Combien de fichiers contient mon dossier Downloads ?  

##  Objectif pédagogique

Comprendre MCP, exposer des tools Python, connecter un LLM à des fonctions locales et exécuter du code via Cursor.