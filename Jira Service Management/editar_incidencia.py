import requests
from requests.auth import HTTPBasicAuth
import json

# Tu URL de Jira Cloud
issue_key = "MDS-120"  # Reemplaza con la clave de la incidencia que quieres editar
jira_url = f"https://javier-de-la-paz.atlassian.net/rest/api/3/issue/{issue_key}"

# Autenticación básica con tu email y API Token
email = ""
api_token = ""

# Cabeceras
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Datos de la incidencia con ADF en la descripción
update_data = {
    "fields": {
        "summary": "Editado con python",
        "description": {
            "type": "doc",  # Formato ADF
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Incidencia editada desde pyhton"
                        }
                    ]
                }
            ]
        }
    }
}

# Enviar la solicitud PUT para editar la incidencia
response = requests.put(
    jira_url,
    headers=headers,
    auth=HTTPBasicAuth(email, api_token),
    data=json.dumps(update_data)
)

# Verificar si la incidencia se editó exitosamente
if response.status_code == 204:
    print("Incidencia ADF editada exitosamente.")
else:
    print(f"Error al editar la incidencia: {response.status_code}")
    print(f"Respuesta: {response.text}")
