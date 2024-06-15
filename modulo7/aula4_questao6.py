import csv

filename = 'spotify-2023.csv'

try:
    with open(filename, mode='r', encoding='latin-1') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  

        top_songs_by_year = {}

        for line in csv_reader:
            try:
                track_name = line[0].strip()
                artists = line[1].strip()
                artist_count = int(line[2])
                released_year = int(line[3])
                streams = int(line[8])

                if 2012 <= released_year <= 2022 and artist_count == 1:
                    if line[0][0] == '"' or line[1][0] == '"':
                        continue

                    if released_year not in top_songs_by_year:
                        top_songs_by_year[released_year] = [track_name, artists, released_year, streams]
                    else:
                        if streams > top_songs_by_year[released_year][3]:
                            top_songs_by_year[released_year] = [track_name, artists, released_year, streams]
            except ValueError:
                continue  

        top_songs_list = [top_songs_by_year[year] for year in sorted(top_songs_by_year.keys())]

        print(top_songs_list)

except FileNotFoundError:
    print(f"Arquivo '{filename}' não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro durante a leitura do arquivo: {e}")
