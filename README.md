# Superstore — EDA + Insights en Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jaimehdzgt/superstore_project/blob/main/SuperStore.ipynb)

Un proyecto sencillo y presentable para explorar el dataset **Sample – Superstore**, generar **insights** claros (segmentos, regiones, categorías, envíos, rentabilidad) y mostrar un **informe bonito** dentro del notebook (con bookmarks y KPIs).

---

## 🧠 ¿Qué hace este proyecto?

- **Integra GitHub con Google Colab** para que cualquiera pueda abrir y correr el notebook desde el navegador.
- **Carga el Excel desde Google Drive** (ruta flexible para evitar errores de espacios en el nombre).
- Realiza un **Análisis Exploratorio de Datos (EDA)**:
  - Tipifica columnas, normaliza nombres y **cuenta vacíos** por columna.
  - Reporta **duplicados** y estadísticos generales.
  - Muestra **distribuciones**, **correlaciones** y **posibles outliers**.
- **Imputa Ship_Date** como **Order_Date + 5 días** (sin perder el reporte de nulos original para auditar el cambio).
- **Genera un informe con estilo** (HTML/Markdown) que resume hallazgos:
  - Segmento con más órdenes y segmento más rentable.
  - Regiones/estados con mejor/peor desempeño.
  - Categorías y subcategorías top.
  - Modos de envío más usados y con mejor utilidad.
  - % de órdenes rentables y margen global.
- Exporta **artefactos** útiles:
  - `eda_outputs/missing_report.csv` (reporte de nulos)
  - `eda_outputs/describe_all.csv` (descriptivos)
  - `eda_outputs/superstore_sample_clean.csv` (muestra limpia)

> Si quieres mostrar screenshots del informe, súbelos a `assets/` y agrégalos aquí:
> 
> ![Insights & Conclusiones — Superstore](assets/Insights_1.png)
> 
> ![Insights & Conclusiones — Superstore (continuación)](assets/Insights_2.png)



