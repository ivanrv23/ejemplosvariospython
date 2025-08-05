from db_model import PrismaModel
import time

def test_select_operations():
    print("\n=== TEST SELECT ===")
    celdas = PrismaModel.obtener_celdas_total()
    print(celdas)
    
    # Obtener todas las celdas
    # celdas = PrismaModel.obtener_celdas(5)
    # print(f"Total celdas: {len(celdas)}")
    # for i, celda in enumerate(celdas, 1):
    #     print(f"Celta {i}: {celda}")
    
    # # Obtener celda específica
    # if celdas:
    #     celda_id = celdas[0][0]
    #     celda = PrismaModel.obtener_celda_por_id(celda_id)
    #     print(f"\nCelda por ID ({celda_id}): {celda}")
    
    # # Obtener por tipo
    # tipo = celdas[0][2] if celdas else 'TipoEjemplo'
    # celdas_tipo = PrismaModel.obtener_celdas_por_tipo(tipo)
    # print(f"\nCeldas de tipo '{tipo}': {len(celdas_tipo)}")

def test_write_operations():
    print("\n=== TEST WRITE ===")
    
    # Crear nueva celda
    nuevo_id = None
    if PrismaModel.crear_celda("Celda Test", "Temporal"):
        print("Celda creada con éxito")
        # Obtener ID de la nueva celda
        celdas = PrismaModel.obtener_celdas(1)
        if celdas:
            nuevo_id = celdas[0][0]
            print(f"Nueva celda ID: {nuevo_id}")
    else:
        print("Error creando celda")
    
    # Actualizar celda
    if nuevo_id:
        if PrismaModel.actualizar_celda(nuevo_id, "Celda Actualizada", "Permanente"):
            print("Celda actualizada con éxito")
        else:
            print("Error actualizando celda")
    
    # Eliminar celda
    if nuevo_id:
        if PrismaModel.eliminar_celda(nuevo_id):
            print("Celda eliminada con éxito")
        else:
            print("Error eliminando celda")

def test_batch_operations():
    print("\n=== TEST BATCH ===")
    
    # Crear múltiples celdas
    celdas_lote = [
        ("Celda Batch 1", "Lote"),
        ("Celda Batch 2", "Lote"),
        ("Celda Batch 3", "Lote")
    ]
    
    if PrismaModel.crear_celdas_lote(celdas_lote):
        print("Lote de celdas creado con éxito")
        
        # Eliminar celdas de lote
        if PrismaModel.eliminar_celdas_por_tipo("Lote"):
            print("Celdas de lote eliminadas con éxito")
        else:
            print("Error eliminando celdas de lote")
    else:
        print("Error creando lote de celdas")

def test_all_operations():
    test_select_operations()
    # test_write_operations()
    # test_batch_operations()

if __name__ == "__main__":
    print("=" * 70)
    print("PRUEBA COMPLETA DE OPERACIONES DE BASE DE DATOS")
    print("=" * 70)
    
    start_time = time.time()
    test_all_operations()
    
    duration = time.time() - start_time
    print(f"\nPrueba completada en {duration:.2f} segundos")