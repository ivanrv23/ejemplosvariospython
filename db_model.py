from db_client import execute_query
from datetime import datetime

class PrismaModel:
    @staticmethod
    def create_table():
        """Crea la tabla prismas si no existe"""
        query = """
        CREATE TABLE IF NOT EXISTS prismas (
            id_prisma INT AUTO_INCREMENT PRIMARY KEY,
            state_prisma INT NOT NULL,
            estado_prisma INT NOT NULL,
            nombre_prisma TEXT NOT NULL,
            perfil_prisma TEXT,
            hora_prisma DATETIME NOT NULL,
            angulo_horizontal DECIMAL(15,5),
            angulo_vertical DECIMAL(15,5),
            distancia_prisma DECIMAL(15,5) DEFAULT 0,
            tipoppm_prisma TEXT,
            ppm_prisma DECIMAL(15,5) DEFAULT 0,
            presion_prisma DECIMAL(15,5) DEFAULT 0,
            temperatura_prisma DECIMAL(15,5) DEFAULT 0,
            constante_prisma DECIMAL(15,5) DEFAULT 0,
            este_target DECIMAL(15,5) NOT NULL,
            norte_target DECIMAL(15,5) NOT NULL,
            elevacion_target DECIMAL(15,5) NOT NULL,
            altura_reflector DECIMAL(15,5) DEFAULT 0,
            altura_instrumento DECIMAL(15,5) DEFAULT 0,
            este_estacion DECIMAL(15,5) DEFAULT 0,
            norte_estacion DECIMAL(15,5) DEFAULT 0,
            altura_estacion DECIMAL(15,5) DEFAULT 0,
            medicion_prisma DECIMAL(15,5) DEFAULT 0,
            diferencia_tiempocorto DECIMAL(15,5) DEFAULT 0,
            diferencia_tiempolargo DECIMAL(15,5) DEFAULT 0,
            diferencia_limitevelocidad DECIMAL(15,5) DEFAULT 0,
            distancia_horizontal DECIMAL(15,5) DEFAULT 0,
            diferencia_atipica DECIMAL(15,5) DEFAULT 0,
            desplaza_longitudinal DECIMAL(15,5) DEFAULT 0,
            desplaza_transversal DECIMAL(15,5) DEFAULT 0,
            desplaza_altura DECIMAL(15,5) DEFAULT 0,
            grupo_puntos TEXT
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """
        return execute_query(query)
    
    @staticmethod
    def insert_prisma(data):
        """Inserta un nuevo prisma"""
        query = """
        INSERT INTO prismas (
            state_prisma, estado_prisma, nombre_prisma, perfil_prisma, hora_prisma,
            angulo_horizontal, angulo_vertical, este_target, norte_target, elevacion_target
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        return execute_query(query, params=data)
    
    @staticmethod
    def insert_batch_prismas(batch_data):
        """Inserta múltiples prismas en un lote"""
        query = """
        INSERT INTO prismas (
            state_prisma, estado_prisma, nombre_prisma, perfil_prisma, hora_prisma,
            angulo_horizontal, angulo_vertical, este_target, norte_target, elevacion_target
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        return execute_query(query, batch_data=batch_data)
    
    @staticmethod
    def get_prisma_by_id(prisma_id):
        """Obtiene un prisma por su ID"""
        query = "SELECT * FROM prismas WHERE id_prisma = ?"
        return execute_query(query, params=[prisma_id])
    
    @staticmethod
    def get_all_prismas(limit=10):
        """Obtiene todos los prismas con límite opcional"""
        query = "SELECT * FROM prismas LIMIT ?"
        return execute_query(query, params=[limit])
    
    @staticmethod
    def update_prisma(prisma_id, data):
        """Actualiza un prisma existente"""
        query = """
        UPDATE prismas SET
            state_prisma = ?, estado_prisma = ?, nombre_prisma = ?, perfil_prisma = ?, hora_prisma = ?,
            angulo_horizontal = ?, angulo_vertical = ?, este_target = ?, norte_target = ?, elevacion_target = ?
        WHERE id_prisma = ?
        """
        # Agregar el ID al final de los datos
        data.append(prisma_id)
        return execute_query(query, params=data)
    
    @staticmethod
    def delete_prisma(prisma_id):
        """Elimina un prisma por su ID"""
        query = "DELETE FROM prismas WHERE id_prisma = ?"
        return execute_query(query, params=[prisma_id])
    
    @staticmethod
    def search_prismas_by_name(name):
        """Busca prismas por nombre"""
        query = "SELECT * FROM prismas WHERE nombre_prisma LIKE ?"
        return execute_query(query, params=[f"%{name}%"])
    
    @staticmethod
    def get_prismas_by_date_range(start_date, end_date):
        """Obtiene prismas en un rango de fechas"""
        query = "SELECT * FROM prismas WHERE hora_prisma BETWEEN ? AND ?"
        return execute_query(query, params=[start_date, end_date])
    
    @staticmethod
    def get_prismas_by_coordinates(min_e, max_e, min_n, max_n):
        """Obtiene prismas dentro de un área geográfica"""
        query = """
        SELECT * FROM prismas 
        WHERE este_target BETWEEN ? AND ? 
        AND norte_target BETWEEN ? AND ?
        """
        return execute_query(query, params=[min_e, max_e, min_n, max_n])
    
    @staticmethod
    def custom_query(query, params=None):
        """Ejecuta una consulta personalizada"""
        return execute_query(query, params=params)
    
    @staticmethod
    def obtener_celdas():
        """Obtiene todos los prismas con límite opcional"""
        query = "SELECT * FROM celdas"
        return execute_query(query)