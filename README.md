# Contrôle du Volume par Détection des Doigts 🖐️

Cette application utilise la détection des mains en temps réel via la webcam pour contrôler le volume du système Windows. Elle utilise OpenCV pour la capture vidéo, MediaPipe pour la détection des mains, et pycaw pour le contrôle du volume système.

## 🎯 Fonctionnalités

- Détection en temps réel des mains via la webcam
- Contrôle du volume système basé sur le nombre de doigts levés :
- Contrôle précis du volume système :
  - 5 doigts ➡️ 100% du volume
  - 4 doigts ➡️ 80% du volume
  - 3 doigts ➡️ 60% du volume
  - 2 doigts ➡️ 40% du volume
  - 1 doigt ➡️ 20% du volume
  - 0 doigt ➡️ 0% du volume (muet)
- Affichage en temps réel du pourcentage de volume

## 🛠️ Prérequis

- Python 3.7+
- Webcam fonctionnelle
- Système d'exploitation Windows
- Git (optionnel)

## 📦 Installation

1. Clonez le dépôt (ou téléchargez-le) :
```bash
git clone https://github.com/votre-username/Detection_doigt.git
cd Detection_doigt
```

2. Créez un environnement virtuel (recommandé) :
```bash
python -m venv venv
venv\Scripts\activate
```

3. Installez les dépendances requises :
```bash
pip install -r requirements.txt
```

## 🚀 Utilisation

1. Lancez l'application :
```bash
python main.py
```

2. Une fenêtre s'ouvrira montrant le flux de votre webcam
3. Placez votre main devant la caméra
4. Levez ou baissez vos doigts pour ajuster le volume
5. Pour quitter l'application, appuyez sur la touche 'q'

## 📝 Notes d'utilisation

- Assurez-vous d'avoir une bonne luminosité pour une meilleure détection
- Gardez votre main à une distance raisonnable de la caméra (environ 30-50 cm)
- Évitez les mouvements trop rapides
- La main doit être bien visible et non obstruée

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## ✨ Auteur

Steventog

## 🙏 Remerciements

- OpenCV pour la capture vidéo
- MediaPipe pour la détection des mains
- pycaw pour le contrôle du volume Windows
