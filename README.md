
## ⚠️ Aviso muy importante (Descargo de responsabilidad)

¡Escucha con atención! Aunque este robot es muy inteligente y usa matemáticas avanzadas, hay algunas cosas que debes saber:

* **Es un juego de azar:** La lotería es como lanzar una moneda al aire; nadie puede saber con un 100% de seguridad qué va a salir. 
* **El robot no es adivino:** El script usa la historia para "adivinar" lo que es más probable, pero **no es exacto**. Los números que salen son solo sugerencias basadas en estadísticas.
* **No garantiza premios:** Usar este programa **no significa que vayas a ganar dinero**. A veces la IA acierta y muchas otras veces no.
* **Juego Responsable:** Este programa es solo para **divertirse y aprender** programación. Nunca gastes dinero que necesites para cosas importantes. ¡La suerte es caprichosa!

# 🚀 Mi Súper Máquina de Adivinar Lotería (con IA)

¡Hola! Bienvenido a bordo. Esta es una herramienta mágica que usa **Inteligencia Artificial** (un robot muy listo) para estudiar los números de la Primitiva desde hace muchísimos años.

El robot lee un "libro de recuerdos" (`historico_limpio.csv`) con todos los sorteos que han salido y te ayuda a elegir los números que tienen más "posibilidades" de salir en el próximo. ¡Es como tener un detective privado para la lotería!

---

## 🎮 Cómo usarlo (Paso a paso para valientes)

Sigue estos cinco pasos para poner en marcha el motor de la IA. ¡Es más fácil que montar un mueble de LEGO!

### Paso 1: ¡Prepara tu mochila! 🎒
Para que el programa funcione, necesitas tener instalada una herramienta llamada **Python**. Piensa en Python como el motor de un coche: ¡sin él no arranca!

1. Pide a un adulto que descargue Python desde la web oficial: [python.org/downloads](https://www.python.org/downloads/).
2. **¡MUY IMPORTANTE!** Cuando aparezca la ventana de instalación, busca una casilla que dice **"Add Python to PATH"** y **márcala**. Es como darle las llaves del coche al programa para que pueda conducir.

---

## 🛠️ Paso 2: Cómo instalar los "superpoderes" a mano (Manual)

Si el robot no puede instalar sus libros de estudio solo, puedes ayudarle tú mismo. Es como darle las piezas de LEGO en la mano. Abre la ventana negra (`cmd`) en tu carpeta y escribe estos tres comandos uno por uno:

1.  **Para leer los datos** (Pandas):  
    `pip install pandas`
2.  **Para entender el Excel** (Openpyxl):  
    `pip install openpyxl`
3.  **Para el cerebro de IA** (Scikit-Learn):  
    `pip install scikit-learn`

> **Truco de experto:** Si quieres instalarlo todo de una vez, escribe:  
> `pip install pandas openpyxl scikit-learn`

---

### Paso 3: Pon las piezas en su sitio 🧩
1. Clona o Descarga el repositorio los archivos necesarios `super_creador.py` y `historico_limpio.csv` se encuentran incluidos

### Paso 4: ¡Dale superpoderes! ⚡
El robot es muy listo, pero necesita "estudiar" antes de empezar. Vamos a instalarle sus "libros de estudio" (librerías). No te asustes, es solo escribir una frase mágica:

1.  Abre la carpeta donde tienes los archivos.
2.  En la barra de direcciones de arriba (donde pone la ruta de la carpeta), escribe **`cmd`** y pulsa la tecla **Enter**. Se abrirá una ventana negra.
3.  Escribe esta frase mágica tal cual y pulsa **Enter**:
    ```powershell
    pip install pandas scikit-learn openpyxl
    ```
    *(Verás que empiezan a salir muchas letras y barras de carga. ¡Está descargando sus superpoderes!).*

### Paso 5: ¡A jugar! 🏁
Cuando la ventana negra deje de escribir cosas, ya estás listo.
1. Abre powershell
2. Pon esto en el terminal **python super_creador.py** para ejecutar el script y presiona **Enter**.
3. Recuerda el terminal debe estar en la misma carpeta, para ejecutar el script.


# 🎰 Simulador Primitiva IA Pro v2.0

Este software avanzado utiliza **Machine Learning** y **filtros de exclusión estadística** para generar combinaciones de lotería basadas en el histórico real (1986-2026).

## 🚀 Nuevas Funciones de Inteligencia

### 1. El Algoritmo de Clustering (K-Means)
La IA divide los 49 números en 6 "familias" según su frecuencia. El programa elige un representante de cada familia, garantizando que tu apuesta tenga números "Calientes" (frecuentes) y "Fríos" (que están por salir), evitando jugadas descompensadas.

### 2. La Regla de la Suma (Σ)
Estadísticamente, el **75% de los sorteos ganadores** tienen una suma total de sus 6 números entre **130 y 210**. El simulador descarta automáticamente cualquier combinación que se salga de este rango de probabilidad.

### ⚖️ El Misterio de la Suma (Σ)

¿Te has fijado que al lado de cada jugada pone algo como `Σ:142`? Esa letra rara es el símbolo de la **Suma**. 

Imagina que cada número es una gominola que pesa lo que dice su número. Si eliges el 1, 2, 3, 4 y 5, tu mochila solo pesa **15 gramos**. ¡Es muy ligera! Si eliges el 46, 47, 48, 49 y 50, tu mochila pesa **230 gramos**. ¡Es pesadísima!

El robot ha estudiado miles de sorteos y ha descubierto un secreto: **¡A la suerte no le gustan las mochilas ni muy ligeras ni muy pesadas!** Casi siempre, las mochilas ganadoras pesan entre **95 y 160 gramos**.

<p align="center">
  <img src="curva_suma.jpg" width="500">
  <br>
  <em>La "Montaña de la Suerte": Casi todos los premios caen en el centro (la parte alta).</em>
</p>

### 🕵️‍♂️ ¿Qué significan las etiquetas (3P/2I)?

Al final de cada jugada verás un código extraño como `3P/2I`. ¡No es un mensaje secreto! Es la forma que tiene el robot de decirte que la combinación está **equilibrada**.

* **P = PARES**: Números como el 2, 14, 26, 40...
* **I = IMPARES**: Números como el 1, 15, 27, 49...

**¿Por qué es importante?**
Si miras todos los sorteos de la historia, verás que **casi nunca** salen todos los números pares o todos impares. ¡Es muy raro! Lo más común es que haya una mezcla. 



El robot usa este filtro para que tu apuesta sea realista:
- **3P/2I**: Significa 3 pares y 2 impares.
- **2P/3I**: Significa 2 pares y 3 impares.

Si el robot genera una jugada con "demasiados" pares o impares, ¡la borra y hace una nueva hasta que quede perfecta!

**¿Por qué el robot hace esto?**
Porque hay miles de formas de sumar un número mediano (como 130), pero solo hay una forma de sumar un número muy pequeño. Al quedarnos en el centro de la montaña, ¡tenemos muchas más oportunidades de acertar!

### 3. Filtro de Paridad (NUEVO)
Es extremadamente raro (menos del 2% de los casos) que una combinación ganadora esté formada solo por números pares o solo por impares. 
- **Optimización**: El simulador ahora obliga a que cada apuesta tenga una mezcla equilibrada (ej. 3 pares y 3 impares, o 4 y 2). Esto elimina miles de combinaciones "feas" que casi nunca salen en el bombo real.



## 🛠️ Instalación Rápida
1. Instala Python (marca "Add to PATH").
2. Pon `super_creador.py` y `historico_limpio.csv` en la misma carpeta.
3. Ejecuta el script. Se instalarán automáticamente las librerías necesarias (`pandas`, `scikit-learn`, `openpyxl`).

## 📁 Uso
- Introduce la cantidad de apuestas.
- El sistema te mostrará la combinación, el Reintegro (R), la Suma (Σ) y la distribución de Pares/Impares (P/I).