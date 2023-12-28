import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo CSV
game_name = "Aerlik"
archivo_csv = f'matches/{game_name}/analisis_partidas.csv'

# Cargar el archivo CSV
df = pd.read_csv(archivo_csv)

# Filtrar las partidas donde la posición es BOTTOM y EarlySurrender es False
# Utilizar .copy() para evitar la advertencia
df_bottom = df[(df['Posicion'] == 'BOTTOM') & (df['EarlySurrender'] == False)].copy()

# Convertir la columna 'FechaCreacionPartida' a datetime y ordenar
df_bottom['FechaCreacionPartida'] = pd.to_datetime(df_bottom['FechaCreacionPartida'], unit='ms')
df_bottom = df_bottom.sort_values(by='FechaCreacionPartida')

# Calcular la media de la duración de las partidas y CS promedio por minuto
media_duracion = df_bottom['TiempoJugado'].mean()
media_cs = df_bottom['CS'].mean()
media_cs_por_minuto = (df_bottom['CS'] / df_bottom['TiempoJugado']).mean()

# Gráfico de línea del CS a lo largo del tiempo para BOTTOM
plt.figure(figsize=(10, 6))
plt.plot(df_bottom['FechaCreacionPartida'], df_bottom['CS'], marker='o')
plt.axhline(y=media_cs, color='r', linestyle='-', label=f'Media de CS: {media_cs:.2f}')
plt.title(f'CS  para {game_name} ')
plt.xlabel('Fecha')
plt.ylabel('CS')
plt.grid(True)

texto_estadisticas = (f"Duración media de las partidas: {media_duracion:.2f} minutos\n"
                      f"CS promedio por minuto: {media_cs_por_minuto:.2f}")
plt.text(df_bottom['FechaCreacionPartida'].min(), df_bottom['CS'].max(), texto_estadisticas, fontsize=9, va='top')

plt.show()