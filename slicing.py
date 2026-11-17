from pydub import AudioSegment  # Importe l'outil de manipulation audio de la bibliothèque pydub
import json                     # Importe le module pour lire et manipuler les fichiers au format JSON
import os                       # Importe le module pour interagir avec le système d'exploitation (dossiers, chemins)
import re                       # Importe le module pour nettoyer les noms de fichiers

def time_to_ms(time_str):
    """Convertit un temps au format texte 'MM:SS' en millisecondes."""
    parts = time_str.split(':')  # Sépare les minutes et les secondes au niveau du caractère ':'
    minutes = int(parts[0])      # Convertit la partie minutes en nombre entier
    seconds = int(parts[1])      # Convertit la partie secondes en nombre entier
    return (minutes * 60 + seconds) * 1000  # Calcule le total en millisecondes

def decouper_audio(fichier_mp3, fichier_json, dossier_sortie="extraits"):
    """Lit un fichier JSON de minutages et découpe le fichier MP3 source en conséquence."""
    
    # 1. Ouverture et lecture du fichier JSON externe contenant la playlist
    with open(fichier_json, "r", encoding="utf-8") as f:
        playlist = json.load(f)  # Convertit le contenu du JSON en une liste de dictionnaires Python

    # 2. Création du dossier de destination s'il n'existe pas et chargement de l'audio source
    os.makedirs(dossier_sortie, exist_ok=True)  # Crée le dossier pour ranger les extraits découpés
    sound = AudioSegment.from_file(fichier_mp3)  # Charge le fichier audio source complet en mémoire

    # 3. Boucle pour parcourir chaque élément de la playlist et procéder au découpage
    for piste in playlist:
        piste_id = piste["id"]                 # Récupère l'identifiant unique de la piste
        start_ms = time_to_ms(piste["time"])     # Convertit le temps de début en millisecondes
        end_ms = time_to_ms(piste["timeNext"])   # Convertit le temps de fin en millisecondes
        
        # Découpe la portion audio correspondante entre le début et la fin
        extrait = sound[start_ms:end_ms]
        
        # Formate le nom du fichier de sortie en incluant l'id, le temps et le nom de la piste
        # Ajouté par Copilot car ":" est interdit dans un nom de fichier
        temps_fichier = piste["time"].replace(":", "-")
        nom_piste = re.sub(r'[<>:"/\\|?*]', "-", piste["nom"]).strip(" .")
        nom_fichier = os.path.join(
            dossier_sortie, 
            f"{piste_id}_{temps_fichier}_{nom_piste}.mp3"
        )
        
        # Exporte l'extrait découpé au format MP3
        extrait.export(nom_fichier, format="mp3")
        print(f"Exporté : {nom_fichier}")  # Affiche un message de confirmation dans la console

    print("\nDécoupage terminé avec succès !")

# Point d'entrée principal du script
if __name__ == "__main__":
    decouper_audio(
        fichier_mp3="BLIND TEST Musique classique.mp3",  # Nom du fichier audio d'origine
        fichier_json="musiquesMp3/MusicQuiz2027.json"     # Nom du fichier JSON contenant les données
    )