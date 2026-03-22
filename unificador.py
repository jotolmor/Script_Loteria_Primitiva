import pandas as pd

# Nombre de tu archivo subido
ARCHIVO_ENTRADA = 'datos.xlsx'
ARCHIVO_SALIDA = 'historico_limpio.csv'

print("🧼 Iniciando limpieza profunda de datos históricos...")

try:
    # 1. Cargamos el archivo saltando la primera fila de basura si la hay
    # Usamos low_memory=False para evitar avisos con archivos grandes
    df = pd.read_csv(ARCHIVO_ENTRADA, skiprows=1, low_memory=False)

    # 2. Renombramos las columnas para que Python las entienda bien
    # Tu archivo tiene: Fecha, B1, B2, B3, B4, B5, B6, Comp, Reintegro
    columnas = ['Fecha', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'Complementario', 'Reintegro']
    df.columns = columnas

    # 3. Limpieza de filas críticas
    # Eliminamos filas donde la fecha o la primera bola estén vacías
    df = df.dropna(subset=['Fecha', 'B1'])

    # 4. Convertir columnas a números
    # 'coerce' transforma cualquier texto raro en "NaN" (vacío) y luego lo limpiamos
    cols_numeros = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'Complementario', 'Reintegro']
    for col in cols_numeros:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # 5. Formatear la fecha
    df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')
    
    # 6. Ordenar por fecha de más antiguo a más moderno
    df = df.sort_values(by='Fecha', ascending=True)

    # 7. Guardar el resultado final
    # Guardamos sin el índice para que el CSV sea más puro
    df.to_csv(ARCHIVO_SALIDA, index=False)

    print("-" * 30)
    print(f"✅ ¡LIMPIEZA COMPLETADA!")
    print(f"📊 Sorteos procesados: {len(df)}")
    print(f"📅 Rango: {df['Fecha'].min().date()} hasta {df['Fecha'].max().date()}")
    print(f"📁 Archivo generado: {ARCHIVO_SALIDA}")
    print("-" * 30)

except Exception as e:
    print(f"❌ Error durante la limpieza: {e}")