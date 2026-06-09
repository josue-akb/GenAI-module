import os
from pathlib import Path
from datetime import datetime
import requests


def get_current_time() -> str:
    """Renvoie l'heure actuelle."""
    return datetime.now().isoformat()


def list_directory(path: str) -> list[str]:
    """Liste les fichiers d'un dossier."""
    return os.listdir(os.path.expanduser(path))


def read_file(path: str) -> str:
    """Lit un fichier texte."""
    content = Path(os.path.expanduser(path)).read_text(encoding="utf-8")
    return content[:4000]


def get_weather(latitude: float, longitude: float) -> dict:
    """Récupère la météo via Open-Meteo."""
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}&current_weather=true"
    )
    return requests.get(url).json()["current_weather"]


def get_directory_size(path: str) -> str:
    """Calcule la taille d'un dossier."""
    total = 0

    for root, _, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            if os.path.exists(fp):
                total += os.path.getsize(fp)

    return f"{round(total / (1024*1024), 2)} MB"


def search_wikipedia(query: str) -> str:
    """Recherche un résumé Wikipedia."""
    url = "https://fr.wikipedia.org/api/rest_v1/page/summary/" + query
    r = requests.get(url)

    if r.status_code != 200:
        return "Aucun résultat"

    data = r.json()
    return data.get("extract", "Pas de résumé disponible")



TOOLS = {
    "get_current_time": get_current_time,
    "list_directory": list_directory,
    "read_file": read_file,
    "get_weather": get_weather,
    "get_directory_size": get_directory_size,
    "search_wikipedia": search_wikipedia,
}
TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Donne l'heure actuelle",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_directory",
            "description": "Liste un dossier",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"}
                },
                "required": ["path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Lit un fichier texte",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"}
                },
                "required": ["path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Météo actuelle",
            "parameters": {
                "type": "object",
                "properties": {
                    "latitude": {"type": "number"},
                    "longitude": {"type": "number"}
                },
                "required": ["latitude", "longitude"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_directory_size",
            "description": "Taille d'un dossier",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"}
                },
                "required": ["path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_wikipedia",
            "description": "Recherche un résumé sur Wikipedia",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"}
                },
                "required": ["query"]
            }
        }
    }
]