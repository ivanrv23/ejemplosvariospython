import requests
import json
import gzip

# VERIFICA ESTA URL - DEBE SER LA CORRECTA DONDE SUBISTE EL PHP
API_URL = "https://e-verifylicense.eigha.pe/db_handler.php"
API_TOKEN = "dGhpcyBpcyBhIHZlcnkgc2VjdXJlIGtleSEhIQ=="

def execute_query(query, params=None, batch_data=None):
    payload = {
        "query": query,
        "api_key": API_TOKEN  # Mantenemos el token en payload para compatibilidad
    }
    
    if params is not None:
        payload["params"] = params
        
    if batch_data is not None:
        payload["batch_data"] = batch_data
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }
    
    try:
        # Comprimir si hay batch grande
        if batch_data and len(batch_data) > 100:
            data = json.dumps(payload).encode('utf-8')
            compressed = gzip.compress(data)
            response = requests.post(
                API_URL,
                data=compressed,
                headers={**headers, "Content-Encoding": "gzip"},
                timeout=30
            )
        else:
            response = requests.post(
                API_URL,
                json=payload,
                headers=headers,
                timeout=30
            )
        
        if response.status_code == 200:
            return response.json()
        else:
            return {
                'status': 'error',
                'message': f"HTTP Error {response.status_code}",
                'response': response.text[:500]
            }
            
    except Exception as e:
        return {
            'status': 'error',
            'message': f"Connection error: {str(e)}"
        }