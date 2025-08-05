import csv
import math
from sqlite3 import Error
from services.security.apis.conexiones.conexion import Connection

def mdlListarDataPrismasNombre(table, nombres):
    placeholders = ', '.join(['?' for _ in nombres])
    sql = f"""
    SELECT 
        state_prisma,
        nombre_prisma,
        perfil_prisma,
        hora_prisma,
        angulo_horizontal,
        angulo_vertical,
        distancia_prisma,
        tipoppm_prisma,
        ppm_prisma,
        presion_prisma,
        temperatura_prisma,
        constante_prisma,
        este_target,
        norte_target,
        elevacion_target,
        altura_reflector,
        altura_instrumento,
        este_estacion,
        norte_estacion,
        altura_estacion,
        medicion_prisma,
        diferencia_tiempocorto,
        diferencia_tiempolargo,
        diferencia_limitevelocidad,
        distancia_horizontal,
        diferencia_atipica,
        desplaza_longitudinal,
        desplaza_transversal,
        desplaza_altura,
        grupo_puntos
    FROM {table} 
    WHERE state_prisma = 1 
        AND nombre_prisma IN ({placeholders})
    """
    try:
        conn = Connection.connectionDB()
        cur = conn.cursor()
        cur.execute(sql, nombres)
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error al listar prismas: " + str(e))
        return None
    finally:
        if conn:
            conn.close()

# Definir los encabezados
encabezados = [
    'State', 'Point ID', 'Profile Name', 'Time', 'Hz', 'V', 'D [m]',
    'PPM Type', 'PPM', 'Pressure [mBar]', 'Av Temp [°C]', 'Add Const [m]',
    'Target Easting [m]', 'Target Northing [m]', 'Target Elevation [m]',
    'Reflector Height [m]', 'Instrument Height [m]', 'Station Easting [m]',
    'Station Northing [m]', 'Station Height [m]', 'Null Measurement [m]',
    'Short Time Diff [m]', 'Long Time Diff [m]', 'Vel Limit Diff [m]',
    'Horz Distance [m]', 'Difference Outlier Test [m]',
    'Longitudinal Displacement [m]',
    'Transverse Displacement [m]',
    'Height Displacement [m]', 'Point group'
]

# Parámetros configurables
MAX_FILAS_POR_ARCHIVO = 1000000  # Máximo de filas por archivo CSV
table = "prismas1"
nombres_prismas = ['P1', 'P2', 'P3']  # Lista de nombres de prismas

# Obtener datos
datos = mdlListarDataPrismasNombre(table, nombres_prismas)

if datos is None:
    print("No se pudieron obtener datos de la base de datos")
    exit()

total_filas = len(datos)
print(f"Total de filas obtenidas: {total_filas}")

# Calcular número de archivos necesarios
num_archivos = math.ceil(total_filas / MAX_FILAS_POR_ARCHIVO)
print(f"Se crearán {num_archivos} archivo(s) CSV")

# Crear archivos divididos
for i in range(num_archivos):
    # Calcular rango de datos para este archivo
    inicio = i * MAX_FILAS_POR_ARCHIVO
    fin = min((i + 1) * MAX_FILAS_POR_ARCHIVO, total_filas)
    segmento = datos[inicio:fin]
    
    # Generar nombre de archivo con sufijo numérico
    nombre_archivo = f"datos_topografia_parte_{i+1}.csv"
    
    # Escribir archivo CSV
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        # Escribir encabezado en cada archivo
        escritor.writerow(encabezados)
        escritor.writerows(segmento)
    
    print(f" - Archivo '{nombre_archivo}' creado con {len(segmento)} filas")

print("\nProceso completado. Todos los archivos han sido generados.")