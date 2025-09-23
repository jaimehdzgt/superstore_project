# Superstore Analytics — EDA & Model

Repositorio demostrativo con **Python + Jupyter** para el dataset *Sample - Superstore*.
Ejecutable en **Google Colab**. Incluye EDA y un modelo de clasificación (orden rentable).

## Estructura
```
superstore_project/
├─ data/
│  ├─ superstore_sample.csv
│  └─ (Sample - Superstore.xlsx)   # opcional (no se versiona por .gitignore)
├─ notebooks/
│  ├─ 01_EDA_Superstore.ipynb
│  └─ 02_Modeling_Superstore.ipynb
├─ src/
│  └─ utils.py
├─ requirements.txt
├─ .gitignore
├─ LICENSE
└─ README.md
```

## Colab (rápido)
1. Sube `notebooks/*.ipynb` a Colab.
2. Si quieres usar el Excel completo, monta Drive y pon la ruta en `excel_path`:
   ```python
   from google.colab import drive; drive.mount('/content/drive')
   excel_path = '/content/drive/MyDrive/Sample - Superstore.xlsx'
   ```
3. Si no, se usará `data/superstore_sample.csv`.

---
© 2025 MIT
