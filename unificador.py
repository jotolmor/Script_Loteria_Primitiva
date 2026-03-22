import pandas as pd
import io
import csv

# Nombre de tu archivo
ARCHIVO_ENTRADA = 'datos.xlsx'
ARCHIVO_SALIDA = 'historico_limpio.csv'

print("🧼 Iniciando limpieza profunda de datos (Modo Manual Blindado)...")

try:
    datos_limpios = []
    
    # 1. Abrimos el archivo como texto puro
    with open(ARCHIVO_ENTRADA, 'r', encoding='latin-1') as f:
        # Usamos el lector de CSV básico de Python que es más flexible con las comas
        lector = csv.reader(f, delimiter=',')
        
        for fila in lector:
            # Una fila válida debe tener al menos 8 o 9 elementos
            if len(fila) >= 7:
                fecha = fila[0].strip()
                # Comprobamos si la primera columna parece una fecha (ej: 2024-10-31 o 31/10/2024)
                # Buscamos que empiece por un número
                if fecha and fecha[0].isdigit():
                    # Nos quedamos solo con las columnas importantes (Fecha + 6 bolas + Comp + R)
                    # Tomamos hasta 9 elementos si existen
                    datos_limpios.append(fila[:9])

    if not datos_limpios:
        # Si no funcionó con comas, probamos con punto y coma (común en Excel español)
        print("💡 Probando con punto y coma...")
        with open(ARCHIVO_ENTRADA, 'r', encoding='latin-1') as f:
            lector = csv.reader(f, delimiter=';')
            for fila in lector:
                if len(fila) >= 7:
                    fecha = fila[0].strip()
                    if fecha and fecha[0].isdigit():
                        datos_limpios.append(fila[:9])

    # 2. Una vez filtrado, lo convertimos en un DataFrame de Pandas para rematar el formato
    df = pd.DataFrame(datos_limpios)
    
    # Nombrar columnas (Aseguramos 9 nombres)
    columnas = ['Fecha', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'Complementario', 'Reintegro']
    # Si el archivo tiene menos columnas (ej: le falta el reintegro), rellenamos
    while len(df.columns) < len(columnas):
        df[len(df.columns)] = ""
    
    df.columns = columnas[:len(df.columns)]

    # 3. Limpieza final de valores
    for col in df.columns:
        if col != 'Fecha':
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # 4. Formatear fecha y ordenar
    df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')
    df = df.dropna(subset=['Fecha', 'B1']) # Solo filas con fecha y al menos la primera bola
    df = df.sort_values(by='Fecha', ascending=True)

    # 5. Guardar el archivo maestro
    df.to_csv(ARCHIVO_SALIDA, index=False)

    print("-" * 35)
    print(f"✅ ¡POR FIN LOGRADO!")
    print(f"📊 Sorteos rescatados: {len(df)}")
    print(f"📅 Desde: {df['Fecha'].min().date()}")
    print(f"📅 Hasta: {df['Fecha'].max().date()}")
    print(f"📁 Archivo listo: {ARCHIVO_SALIDA}")
    print("-" * 35)

except Exception as e:
    print(f"❌ Error crítico inesperado: {e}")