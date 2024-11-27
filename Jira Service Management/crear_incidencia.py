import requests
from requests.auth import HTTPBasicAuth
import json

# URL
jira_url = "https://javier-de-la-paz.atlassian.net/rest/api/3/issue"

# Autenticación con email y API Token
email = ""
api_token = ""

# Headers
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Datos de la incidencia
issue_data = {
    "fields": {
        "project": {
            "key": "MDS"  # Clave del proyecto
        },
        "summary": "Creado con python",
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Incidencia creada desde pyyhon"
                        }
                    ]
                }
            ]
        },
        "issuetype": {
            "name": "Incidentes"
        }
    }
}

# Enviar la solicitud POST
response = requests.post(
    jira_url,
    headers=headers,
    auth=HTTPBasicAuth(email, api_token),
    data=json.dumps(issue_data)
)

# Verificar si la incidencia se creó exitosamente
if response.status_code == 201:
    print("Incidencia creada exitosamente.")
    print(f"Detalles: {response.json()}")
else:
    print(f"Error al crear la incidencia: {response.status_code}")
    print(f"Respuesta: {response.text}")
