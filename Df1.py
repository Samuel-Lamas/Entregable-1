import pandas as pd
import numpy as np

np.random.seed(42)

n = 2000

# Fechas base
fechas_consulta = pd.date_range("2023-01-01", periods=n, freq="H")
fechas_inicio = fechas_consulta + pd.to_timedelta(np.random.randint(-300, 800, n), unit="m")
fechas_fin = fechas_inicio + pd.to_timedelta(np.random.randint(30, 300, n), unit="m")

# Dataset
df1 = pd.DataFrame({
    "ORIGEN": np.random.choice(["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao"], n),
    "DESTINO": np.random.choice(["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao"], n),
    "TIPO_TREN": np.random.choice(["AVE", "ALVIA", "MD", "R. EXPRESS", "OUIGO", "ESPECIAL_RARO"], n, p=[0.3,0.25,0.2,0.15,0.09,0.01]),
    "TIPO_TARIFA": np.random.choice(["Flexible", "Promo", "Mesa", "Especial", "UltraRara"], n),
    "CLASE": np.random.choice(["Turista", "Preferente", "Premium", "Rara"], n),
    "PRECIO": np.random.normal(50, 20, n),
    "FECHA_CONSULTA": fechas_consulta,
    "FECHA_INICIO": fechas_inicio,
    "FECHA_FIN": fechas_fin
})

# Introducimos nulos
for col in ["PRECIO", "TIPO_TARIFA", "CLASE"]:
    df1.loc[df1.sample(frac=0.05).index, col] = np.nan

# Introducimos duplicados
df1 = pd.concat([df1, df1.sample(50)], ignore_index=True)

# Outliers extremos
df1.loc[df1.sample(5).index, "PRECIO"] = [500, 600, 700, 800, 1000]

df1.head()
df1.info()
# Análisis
df1.describe(include='object')
df1.head(5)
df1.tail(5)

