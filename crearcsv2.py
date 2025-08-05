import csv

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

# Nombre del archivo CSV
nombre_archivo = "datos_mediciones.csv"

# Escribir el archivo CSV con los encabezados
with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
    writer = csv.writer(archivo, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerow(encabezados)

print(f"Archivo CSV '{nombre_archivo}' creado exitosamente.")