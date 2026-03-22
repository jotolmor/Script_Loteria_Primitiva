import openpyxl

# =====================================================================
# PON AQUÍ EL NOMBRE EXACTO DE TU ARCHIVO EXCEL
# =====================================================================
ARCHIVO_EXCEL = 'datos.xlsx' 
ARCHIVO_XML = 'porcentajes_primitiva.xml'

print("--- INICIANDO CONVERSIÓN DE EXCEL (XLSX) A XML ---\n")

try:
    # Cargamos el archivo de Excel
    print(f"Cargando el archivo '{ARCHIVO_EXCEL}'...")
    libro = openpyxl.load_workbook(ARCHIVO_EXCEL, data_only=True)
    hoja = libro.active # Seleccionamos la primera pestaña del Excel

    with open(ARCHIVO_XML, mode='w', encoding='utf-8') as f_xml:
        f_xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f_xml.write('<estadisticas>\n')
        
        filas_procesadas = 0
        hay_reintegros = False
        
        # Recorremos todas las filas del Excel (empezando por la 2 para saltar los títulos)
        for fila in hoja.iter_rows(min_row=2, values_only=True):
            # En tu Excel: Columna B (índice 1) es Número, Columna D (índice 3) es Porcentaje
            if len(fila) >= 4:
                numero_celda = fila[1]
                frecuencia_celda = fila[3]
                
                # Si la celda está vacía, pasamos a la siguiente
                if numero_celda is None or frecuencia_celda is None:
                    continue
                    
                try:
                    # Convertimos a números por si Excel los detectó como texto
                    numero = int(numero_celda)
                    frecuencia = float(frecuencia_celda)
                except ValueError:
                    continue # Si hay algún texto raro, lo saltamos
                    
                # Escribimos en el XML según si es bola o reintegro
                if 1 <= numero <= 49:
                    f_xml.write(f'    <bola numero="{numero}" frecuencia="{frecuencia}" />\n')
                    filas_procesadas += 1
                elif 0 <= numero <= 9:
                    f_xml.write(f'    <reintegro numero="{numero}" frecuencia="{frecuencia}" />\n')
                    hay_reintegros = True
                    filas_procesadas += 1

        # Si tu Excel no tenía reintegros, creamos unos genéricos
        if not hay_reintegros:
            for r in range(10):
                f_xml.write(f'    <reintegro numero="{r}" frecuencia="0.10" />\n')
            print("ℹ️ No se detectaron reintegros en el Excel. Se han generado neutrales automáticamente.")

        f_xml.write('</estadisticas>\n')
        
    print(f"\n✅ ¡Éxito! Se han procesado {filas_procesadas} números.")
    print(f"📁 Tu archivo '{ARCHIVO_XML}' ha sido creado y está listo para el simulador.")

except FileNotFoundError:
    print(f"\n❌ Error: No encuentro el archivo '{ARCHIVO_EXCEL}'.")
    print("Asegúrate de que está en esta misma carpeta y que el nombre está bien escrito.")
except Exception as e:
    print(f"\n❌ Error inesperado: {e}")