from pathlib import Path


def get_disk_usage(path: str) -> str:
    """Calcule la taille totale d'un dossier."""
    p = Path(path).expanduser()

    if not p.exists():
        return f"Erreur : le chemin {path} n'existe pas."

    total_bytes = sum(
        f.stat().st_size
        for f in p.rglob("*")
        if f.is_file()
    )

    return f"{total_bytes / 1024 / 1024:.1f} Mo"

import requests


def get_weather(latitude: float, longitude: float) -> str:
    """Récupère la météo actuelle via Open-Meteo."""
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}&current_weather=true"
    )

    data = requests.get(url).json()

    weather = data.get("current_weather", {})

    return f"""
Température: {weather.get('temperature')}°C
Vent: {weather.get('windspeed')} km/h
Code météo: {weather.get('weathercode')}
"""