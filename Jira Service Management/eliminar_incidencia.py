import requests
from requests.auth import HTTPBasicAuth

# Tu URL de Jira Cloud
issue_key = "MDS-121"  # Reemplaza con la clave de la incidencia que deseas eliminar
jira_url = f"https://javier-de-la-paz.atlassian.net/rest/api/3/issue/{issue_key}"


# Autenticación básica con tu email y API Token
email = ""
api_token = ""

# Cabeceras
headers = {
    "Accept": "application/json"
}

# Enviar la solicitud DELETE para eliminar la incidencia
response = requests.delete(
    jira_url,
    headers=headers,
    auth=HTTPBasicAuth(email, api_token)
)

# Verificar si la incidencia se eliminó exitosamente
if response.status_code == 204:
    print("Incidencia eliminada exitosamente.")
elif response.status_code == 404:
    print("Incidencia no encontrada.")
else:
    print(f"Error al eliminar la incidencia: {response.status_code}")
    print(f"Respuesta: {response.text}")
