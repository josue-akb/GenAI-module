from mcp.server.fastmcp import FastMCP
from tools import get_disk_usage, get_weather

mcp = FastMCP("mon-serveur-mcp")


@mcp.tool()
def get_disk_usage(path: str) -> str:
    """Calcule la taille d'un dossier en mégaoctets."""
    return get_disk_usage(path)

@mcp.tool()
def get_weather_tool(latitude: float, longitude: float) -> str:
    """Retourne la météo actuelle."""
    return get_weather(latitude, longitude)


if __name__ == "__main__":
    mcp.run()