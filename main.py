import cv2

# Chemin vers votre vidéo
video_path = 'C:\\Users\\userfl\\Desktop\\V project\\Extraction-d-images-cl-s-d-une-vid-o\\video.mp4'

# Charger la vidéo
cap = cv2.VideoCapture(video_path)

# Vérifiez si la vidéo s'est bien chargée
if not cap.isOpened():
    print("Erreur lors de l'ouverture de la vidéo")
else:
    print("Vidéo chargée avec succès")

import os

# Créer un répertoire pour stocker les images clés
output_dir = 'images_cles'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Paramètres pour définir un seuil de changement
frame_interval = 30  # Intervalle d'analyse des frames (saute 30 frames)
previous_frame = None
image_count = 0

while True:
    # Lire la frame actuelle
    ret, frame = cap.read()

    # Si la lecture échoue (fin de la vidéo), on sort de la boucle
    if not ret:
        break

    # Convertir la frame en niveaux de gris pour simplifier l'analyse
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Comparer avec la frame précédente
    if previous_frame is not None:
        # Calculer la différence absolue entre les deux frames
        diff = cv2.absdiff(previous_frame, gray_frame)
        # Calculer la moyenne des différences (plus elle est élevée, plus il y a de changement)
        mean_diff = diff.mean()

        # Si la différence dépasse un certain seuil, on considère qu'il y a un changement
        if mean_diff > 30:  # Ce seuil peut être ajusté
            # Sauvegarder la frame comme une image clé
            image_count += 1
            image_name = f"{output_dir}/image_{image_count}.jpg"
            cv2.imwrite(image_name, frame)
            print(f"Image clé {image_count} extraite à la frame {cap.get(cv2.CAP_PROP_POS_FRAMES)}")

    # Mettre à jour la frame précédente
    previous_frame = gray_frame

    # Avancer de l'intervalle défini
    cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) + frame_interval)

# Libérer la vidéo et fermer les fenêtres
cap.release()
cv2.destroyAllWindows()