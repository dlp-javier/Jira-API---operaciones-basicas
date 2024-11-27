import requests
from requests.auth import HTTPBasicAuth

# Tu URL de Jira Cloud
issue_key = "MDS-120"  # Reemplaza con la clave de la incidencia que deseas eliminar
jira_url = f"https://javier-de-la-paz.atlassian.net/rest/api/3/issue/{issue_key}/transitions"
# Autenticación básica con tu email y API Token
email = ""
api_token = ""

# Cabeceras
headers = {
    "Accept": "application/json"
}

# Enviar solicitud GET para obtener las transiciones disponibles
response = requests.get(
    jira_url,
    headers=headers,
    auth=HTTPBasicAuth(email, api_token)
)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    transitions = response.json()['transitions']
    for transition in transitions:
        print(f"ID de transición: {transition['id']}, Nombre: {transition['name']}")
else:
    print(f"Error al obtener las transiciones: {response.status_code}")
    print(f"Respuesta: {response.text}")
