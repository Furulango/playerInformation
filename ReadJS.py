import json

def analizar_jugador_especifico(file_path, puuid_jugador):
    with open(file_path, 'r') as file:
        data = json.load(file)

    for player in data['info']['participants']:
        if player['puuid'] == puuid_jugador:
            print(f"Jugador: {player['summonerName']}")
            print(f"KDA: {player['kills']}/{player['deaths']}/{player['assists']}")
            print(f"CS: {player['totalMinionsKilled'] + player['neutralMinionsKilled']}")
            print(f"Daño Total a Campeones: {player['totalDamageDealtToChampions']}")
            print(f"Visión: Guardianes Colocados {player['wardsPlaced']}, Guardianes Eliminados {player['wardsKilled']}")
            print(f"Objetivos: Torres {player['turretKills']}, Dragones {player['dragonKills']}")
            # Añade aquí más análisis según lo que necesites
            break

# Uso del script
archivo_json = 'D:\projectsOwo\playerInformation\match_LA1_1468554497.json'
puuid_jugador = 'tozh4WSFrW-js3sTagOEJOZQGfubNFelkHMA_uXnQMhZRasY2JtRR2vFvDQBXdribkdHxn6sFeVE_w'
analizar_jugador_especifico(archivo_json, puuid_jugador)
