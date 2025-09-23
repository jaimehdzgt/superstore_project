import pandas as pd, numpy as np

def load_superstore(excel_path: str|None = None, csv_fallback: str|None = None) -> pd.DataFrame:
    if excel_path:
        try:
            return pd.read_excel(excel_path, engine="openpyxl")
        except Exception as e:
            print(f"[WARN] No se pudo leer el Excel: {e}. Usando CSV fallback...")
    if csv_fallback:
        return pd.read_csv(csv_fallback)
    raise FileNotFoundError("Proporciona 'excel_path' o 'csv_fallback'.")

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().replace(' ', '_').replace('-', '_') for c in df.columns]
    for c in df.columns:
        if 'date' in c.lower():
            try:
                df[c] = pd.to_datetime(df[c])
            except Exception:
                pass
    for c in df.select_dtypes(include='object').columns:
        df[c] = df[c].astype(str).str.strip()
    return df

def add_kpis(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    cols = {c.lower(): c for c in df.columns}
    if 'sales' in cols and 'profit' in cols:
        s, p = cols['sales'], cols['profit']
        df['profit_margin'] = np.where(df[s]!=0, df[p]/df[s], np.nan)
        df['is_profitable'] = (df[p] > 0).astype(int)
    return df
