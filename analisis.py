import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo CSV
game_name = "SoyRevi"
archivo_csv = f'matches/{game_name}/analisis_partidas.csv'

# Cargar el archivo CSV
df = pd.read_csv(archivo_csv)

# Filtrar las partidas donde la posición es BOTTOM y EarlySurrender es False
df_bottom = df[(df['Posicion'] == 'BOTTOM') & (df['EarlySurrender'] == False)]

# Convertir la columna 'FechaCreacionPartida' a datetime y ordenar
df_bottom['FechaCreacionPartida'] = pd.to_datetime(df_bottom['FechaCreacionPartida'], unit='ms')
df_bottom = df_bottom.sort_values(by='FechaCreacionPartida')

# Realizar análisis estadístico básico sobre la columna 'CS'
media_cs = df_bottom['CS'].mean()
mediana_cs = df_bottom['CS'].median()
std_cs = df_bottom['CS'].std()

print(f"Media de CS para BOTTOM: {media_cs}")
print(f"Mediana de CS para BOTTOM: {mediana_cs}")
print(f"Desviación estándar de CS para BOTTOM: {std_cs}")

# Gráfico de línea del CS a lo largo del tiempo para BOTTOM
plt.figure(figsize=(10, 6))
plt.plot(df_bottom['FechaCreacionPartida'], df_bottom['CS'], marker='o')
plt.title(F'CS {game_name}')
plt.xlabel('Fecha')
plt.ylabel('CS')
plt.grid(True)
plt.show()
