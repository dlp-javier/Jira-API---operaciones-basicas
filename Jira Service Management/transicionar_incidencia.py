import requests
from requests.auth import HTTPBasicAuth
import json

# Tu URL de Jira Cloud
issue_key = "MDS-120"  # Reemplaza con la clave de la incidencia que deseas eliminar
jira_url = f"https://javier-de-la-paz.atlassian.net/rest/api/3/issue/{issue_key}/transitions"
# Autenticación básica con tu email y API Token
email = ""
api_token = ""

# Cabeceras
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# ID de la transición que deseas aplicar (obtenido en el paso anterior)
transition_id = "31"  # Reemplaza con el ID correcto de la transición

# Datos para aplicar la transición
transition_data = {
    "transition": {
        "id": transition_id  # Aquí va el ID de la transición
    },
    "fields": {
        "customfield_10102": {  # Reemplaza "customfield_12345" con el ID de "Área resolutora"
            "value": "Ingeniería"
        }
    }
}

# Enviar la solicitud POST para transicionar la incidencia
response = requests.post(
    jira_url,
    headers=headers,
    auth=HTTPBasicAuth(email, api_token),
    data=json.dumps(transition_data)
)

# Verificar si la incidencia fue transicionada exitosamente
if response.status_code == 204:
    print("Transición aplicada exitosamente.")
else:
    print(f"Error al aplicar la transición: {response.status_code}")
    print(f"Respuesta: {response.text}")
