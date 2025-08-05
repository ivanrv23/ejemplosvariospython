from db_model import PrismaModel
from datetime import datetime, timedelta
import time

def test_all_operations():
    result = PrismaModel.obtener_celdas()
    print(result)

if __name__ == "__main__":
    print("="*70)
    print("PRUEBA COMPLETA DE OPERACIONES DE BASE DE DATOS")
    print("="*70)
    
    start_time = time.time()
    test_all_operations()
    
    duration = time.time() - start_time
    print(f"\nPrueba completada en {duration:.2f} segundos")