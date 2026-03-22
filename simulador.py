import sys
import subprocess

# =====================================================================
# EL PLAN Z: AUTO-INSTALADOR HACKER (Añadido openpyxl para Excel)
# =====================================================================
def comprobar_e_instalar():
    print("⏳ Comprobando el motor de Inteligencia Artificial y lector de Excel...")
    try:
        import pandas
        import sklearn
        import openpyxl
        print("✅ Motor IA y Lector Excel detectados y listos.")
    except ImportError:
        print("⚠️ Faltan piezas del motor. Instalando automáticamente (esto tardará un minutito)...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "scikit-learn", "openpyxl"])
            print("🎉 ¡Instalación completada con éxito!")
        except Exception as e:
            print(f"❌ Error al intentar auto-instalar: {e}")
            sys.exit()

comprobar_e_instalar()

# =====================================================================
# IMPORTACIONES
# =====================================================================
import pandas as pd
from sklearn.cluster import KMeans
import random
import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# =====================================================================
# CONFIGURACIÓN DEL ARCHIVO
# Pon aquí el nombre exacto de tu archivo Excel (con .xlsx al final)
# =====================================================================
ARCHIVO_DATOS = 'datos.xlsx'

# =====================================================================
# MOTOR DE INTELIGENCIA ARTIFICIAL Y LÓGICA
# =====================================================================
def cargar_datos_para_ia(ruta):
    """Lee el EXCEL directamente usando Pandas para alimentar a la IA."""
    try:
        # Cambiamos read_csv por read_excel
        df = pd.read_excel(ruta)
        
        # En tu Excel: Columna B (índice 1) = Número, Columna D (índice 3) = Porcentaje
        df_bolas = df[df.iloc[:, 1].apply(lambda x: str(x).isdigit() and 1 <= int(x) <= 49)].copy()
        df_bolas['Número'] = df_bolas.iloc[:, 1].astype(int)
        df_bolas['Porcentaje'] = df_bolas.iloc[:, 3].astype(float)
        
        # Intentamos capturar "Semanas sin salir" en Columna F (índice 5)
        try:
            df_bolas['Semanas_Frio'] = df_bolas.iloc[:, 5].astype(float)
            caracteristicas = df_bolas[['Porcentaje', 'Semanas_Frio']]
        except:
            caracteristicas = df_bolas[['Porcentaje']]

        return df_bolas, caracteristicas
    except Exception as e:
        print(f"Error al cargar datos desde Excel: {e}")
        return None, None

def generar_apuesta_ia(df_bolas, caracteristicas):
    """Usa Machine Learning (K-Means) para crear una apuesta equilibrada."""
    modelo_kmeans = KMeans(n_clusters=6, n_init=10, random_state=None)
    df_bolas['Cluster'] = modelo_kmeans.fit_predict(caracteristicas)
    
    apuesta_ia = []
    for i in range(6):
        numeros_del_cluster = df_bolas[df_bolas['Cluster'] == i]['Número'].tolist()
        if numeros_del_cluster:
            eleccion = random.choice(numeros_del_cluster)
            apuesta_ia.append(eleccion)
            
    while len(apuesta_ia) < 6:
        extra = random.choice(df_bolas['Número'].tolist())
        if extra not in apuesta_ia:
            apuesta_ia.append(extra)
            
    reintegro = random.randint(0, 9)
    return sorted(apuesta_ia), reintegro

def generar_apuesta_aleatoria(df_bolas):
    """Genera 1 apuesta basada en pesos aleatorios (Bombo Clásico)."""
    numeros = df_bolas['Número'].tolist()
    pesos = df_bolas['Porcentaje'].tolist()
    
    combinacion = set()
    while len(combinacion) < 6:
        eleccion = random.choices(numeros, weights=pesos, k=1)[0]
        combinacion.add(eleccion)
        
    reintegro = random.randint(0, 9)
    return sorted(list(combinacion)), reintegro

def guardar_en_csv(apuestas, ruta_salida):
    try:
        with open(ruta_salida, mode='w', encoding='utf-8', newline='') as archivo:
            escritor = csv.writer(archivo, delimiter=',')
            escritor.writerow(['Bola 1', 'Bola 2', 'Bola 3', 'Bola 4', 'Bola 5', 'Bola 6', 'Reintegro'])
            for apuesta in apuestas:
                escritor.writerow(apuesta[0] + [apuesta[1]])
        return True
    except:
        return False

# =====================================================================
# INTERFAZ GRÁFICA (GUI)
# =====================================================================
class AplicacionIA:
    def __init__(self, root):
        self.root = root
        self.root.title("Primitiva IA - Machine Learning")
        self.root.geometry("650x700")
        self.root.configure(padx=20, pady=20)

        self.df_bolas, self.caracteristicas = cargar_datos_para_ia(ARCHIVO_DATOS)
        if self.df_bolas is None:
            messagebox.showerror("Error Crítico", f"No se pudo leer '{ARCHIVO_DATOS}'. Revisa que el archivo exista y no esté abierto en Excel.")
            self.root.destroy()
            return

        tk.Label(root, text="🧠 Primitiva IA - Análisis Predictivo", font=("Arial", 18, "bold")).pack(pady=(0, 10))
        tk.Label(root, text="¿Cuántas apuestas deseas generar?", font=("Arial", 12)).pack()

        self.entrada_cantidad = tk.Entry(root, font=("Arial", 14), width=10, justify="center")
        self.entrada_cantidad.insert(0, "5")
        self.entrada_cantidad.pack(pady=10)

        marco_botones = tk.Frame(root)
        marco_botones.pack(pady=15)

        btn_ia = tk.Button(marco_botones, text="Generar con Inteligencia Artificial (K-Means)", 
                           command=self.accion_generar_ia, bg="#9C27B0", fg="white", font=("Arial", 11, "bold"))
        btn_ia.grid(row=0, column=0, padx=10, pady=5, columnspan=2, sticky="ew")

        btn_aleatorio = tk.Button(marco_botones, text="Generar Ponderadas (Bombo Clásico)", 
                                  command=self.accion_generar_aleatorio, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
        btn_aleatorio.grid(row=1, column=0, padx=10, pady=5, columnspan=2, sticky="ew")

        tk.Label(root, text="Resultados de la simulación:", font=("Arial", 12, "bold")).pack(pady=(10, 5))

        marco_texto = tk.Frame(root)
        marco_texto.pack(fill=tk.BOTH, expand=True)
        scroll = tk.Scrollbar(marco_texto)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.caja_resultados = tk.Text(marco_texto, height=15, width=60, yscrollcommand=scroll.set, font=("Courier", 11))
        self.caja_resultados.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.config(command=self.caja_resultados.yview)

    def obtener_cantidad(self):
        try:
            cantidad = int(self.entrada_cantidad.get())
            if cantidad <= 0: raise ValueError
            return cantidad
        except ValueError:
            messagebox.showwarning("Atención", "Introduce un número válido mayor que 0.")
            return None

    def procesar_apuestas(self, apuestas, cantidad, metodo):
        self.caja_resultados.delete(1.0, tk.END)
        self.caja_resultados.insert(tk.END, f"--- MÉTODO: {metodo} ---\n\n")
        
        for i, apuesta in enumerate(apuestas):
            self.caja_resultados.insert(tk.END, f"Apuesta {i+1:03d}: {apuesta[0]} | Reintegro: {apuesta[1]}\n")
            
        fecha = datetime.now().strftime("%Y-%m-%d")
        ruta = f"mis_apuestas_IA_{fecha}.csv"
        if guardar_en_csv(apuestas, ruta):
            self.caja_resultados.insert(tk.END, f"\n💾 Guardado en: {ruta}\n")
            
        self.caja_resultados.insert(tk.END, "-"*45 + "\n📊 RESUMEN FINANCIERO\n" + "-"*45 + "\n")
        self.caja_resultados.insert(tk.END, f"Coste de la jugada : {cantidad * 1.00:,.2f} €\n")

    def accion_generar_ia(self):
        cantidad = self.obtener_cantidad()
        if cantidad:
            apuestas = [generar_apuesta_ia(self.df_bolas, self.caracteristicas) for _ in range(cantidad)]
            self.procesar_apuestas(apuestas, cantidad, "Inteligencia Artificial (Clustering)")

    def accion_generar_aleatorio(self):
        cantidad = self.obtener_cantidad()
        if cantidad:
            apuestas = [generar_apuesta_aleatoria(self.df_bolas) for _ in range(cantidad)]
            self.procesar_apuestas(apuestas, cantidad, "Probabilidad Ponderada")

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = AplicacionIA(ventana_principal)
    ventana_principal.mainloop()