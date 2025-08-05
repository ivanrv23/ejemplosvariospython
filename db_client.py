import requests
import json
import gzip
from typing import Union, List, Tuple, Optional

API_URL = "https://e-verifylicense.eigha.pe/db_handler.php"
API_TOKEN = "dGhpcyBpcyBhIHZlcnkgc2VjdXJlIGtleSEhIQ=="

def execute_query(
    query: str, 
    params: Optional[tuple] = None, 
    batch_data: Optional[list] = None
) -> Union[List[tuple], bool, None]:
    """
    Ejecuta una consulta SQL a través de la API
    
    Parámetros:
        query: Consulta SQL
        params: Parámetros para consultas preparadas
        batch_data: Datos para operaciones por lotes
    
    Retorna:
        - Para SELECT: Lista de tuplas con resultados o lista vacía
        - Para INSERT/UPDATE/DELETE: True si éxito, False si fallo
        - None para errores
    """
    payload = {"query": query, "api_key": API_TOKEN}
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    
    if params is not None:
        payload["params"] = params
        
    if batch_data is not None:
        payload["batch_data"] = batch_data
    
    try:
        # Manejo de compresión para lotes grandes
        if batch_data and len(json.dumps(payload)) > 1024:
            data = gzip.compress(json.dumps(payload).encode('utf-8'))
            headers["Content-Encoding"] = "gzip"
            response = requests.post(
                API_URL, 
                data=data, 
                headers=headers,
                timeout=30
            )
        else:
            response = requests.post(
                API_URL,
                json=payload,
                headers=headers,
                timeout=30
            )
        
        # Manejo de errores HTTP
        if response.status_code != 200:
            return None
        
        json_data = response.json()
        
        # Verificar estado de la respuesta
        if json_data.get('status') != 'success':
            return None
        
        # Procesar diferentes tipos de respuesta
        if 'data' in json_data:
            # Convertir resultados SELECT a lista de tuplas
            return [tuple(row.values()) for row in json_data['data']]
        
        if 'affected_rows' in json_data:
            # Operaciones de escritura con filas afectadas
            return json_data['affected_rows'] > 0
        
        # Para operaciones que no devuelven filas afectadas (ej: DDL)
        return True
        
    except Exception:
        # Cualquier excepción devuelve None
        return None