from db_client import execute_query
from typing import List, Tuple, Optional, Union

class PrismaModel:
    # Operaciones SELECT
    @staticmethod
    def obtener_celdas_total() -> List[Tuple]:
        """Obtiene TODAS las celdas sin límite"""
        query = "SELECT * FROM dd"
        return execute_query(query) or None
    
    @staticmethod
    def obtener_celdas(limit: int = 100) -> List[tuple]:
        """Obtiene todas las celdas"""
        query = f"SELECT * FROM celdas LIMIT {limit}"
        return execute_query(query) or []
    
    @staticmethod
    def obtener_celda_por_id(celda_id: int) -> Optional[tuple]:
        """Obtiene una celda por ID"""
        query = "SELECT * FROM celdas WHERE id = %s"
        result = execute_query(query, (celda_id,))
        return result[0] if result else None
    
    # Operaciones INSERT
    @staticmethod
    def crear_celda(nombre: str, tipo: str) -> bool:
        """Crea una nueva celda"""
        query = "INSERT INTO celdas (nombre, tipo) VALUES (%s, %s)"
        return execute_query(query, (nombre, tipo)) or False
    
    @staticmethod
    def crear_celdas_lote(datos: List[Tuple[str, str]]) -> bool:
        """Crea múltiples celdas en una sola operación"""
        query = "INSERT INTO celdas (nombre, tipo) VALUES (?, ?)"
        return execute_query(query, batch_data=datos) or False
    
    # Operaciones UPDATE
    @staticmethod
    def actualizar_celda(celda_id: int, nombre: str, tipo: str) -> bool:
        """Actualiza una celda existente"""
        query = "UPDATE celdas SET nombre = %s, tipo = %s WHERE id = %s"
        return execute_query(query, (nombre, tipo, celda_id)) or False
    
    # Operaciones DELETE
    @staticmethod
    def eliminar_celda(celda_id: int) -> bool:
        """Elimina una celda"""
        query = "DELETE FROM celdas WHERE id = %s"
        return execute_query(query, (celda_id,)) or False
    
    @staticmethod
    def eliminar_celdas_por_tipo(tipo: str) -> bool:
        """Elimina celdas por tipo"""
        query = "DELETE FROM celdas WHERE tipo = %s"
        return execute_query(query, (tipo,)) or False
    
    # Operaciones complejas
    @staticmethod
    def obtener_celdas_por_tipo(tipo: str) -> List[tuple]:
        """Obtiene celdas filtradas por tipo"""
        query = "SELECT * FROM celdas WHERE tipo = %s"
        return execute_query(query, (tipo,)) or []