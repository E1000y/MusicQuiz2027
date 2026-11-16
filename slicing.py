from pydub import AudioSegment
import os

# Charger le fichier audio source complet
audio_source = "musiquesMp3/BLIND TEST Musique classique.mp3"  # Remplace par le nom de ton fichier source

# Convertir un temps "MM:SS" en millisecondes pour pydub
def time_to_ms(time_str):
    parts = time_str.split(':')
    minutes = int(parts[0])
    seconds = int(parts[1])
    return (minutes * 60 + seconds) * 1000

# Ta liste brute de morceaux
rawPlaylist = [
    { "time": "0:00", "nextTime": "0:29", "reponse": "Wolfgang Amadeus Mozart - Sérénade n°13 “Une petite musique de nuit”" },
    { "time": "0:29", "nextTime": "0:57", "reponse": "Franz Schubert - Quintette en la majeur “La Truite”" },
    { "time": "0:57", "nextTime": "1:26", "reponse": "Giuseppe Verdi - Aïda “La Marche des trompettes”" },
    { "time": "1:26", "nextTime": "1:55", "reponse": "Wolfgang Amadeus Mozart - Requiem en ré mineur “Lacrimosa”" },
    { "time": "1:55", "nextTime": "2:24", "reponse": "Johann Strauss II - Le Beau Danube bleu" },
    { "time": "2:24", "nextTime": "2:51", "reponse": "Johann Pachelbel - Canon" },
    { "time": "2:51", "nextTime": "3:20", "reponse": "Claude Debussy - Suite Bergamasque “Claire de lune”" }
]

# Créer le dossier de sortie s'il n'existe pas
os.makedirs("extraits", exist_ok=True)

# Charger l'audio source en mémoire
sound = AudioSegment.from_file(audio_source)

# Découpage automatique
for index, item in enumerate(rawPlaylist, start=1):
    start_ms = time_to_ms(item["time"])
    end_ms = time_to_ms(item["nextTime"])
    
    # Extraire le morceau
    extrait = sound[start_ms:end_ms]
    
    # Nommer le fichier de sortie proprement
    nom_fichier = f"extraits/morceau_{index:02d}.mp3"
    
    # Exporter
    extrait.export(nom_fichier, format="mp3")
    print(f"Exporté : {nom_fichier} ({item['reponse']})")

print("Découpage terminé !")