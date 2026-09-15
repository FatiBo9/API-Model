---

## 5. Dépôt : `Modèle API`

```markdown
# 🐱🐶 API de Classification d'Images (TensorFlow)

## 📌 Présentation
Développement d'une API web en Python embarquant un modèle de Deep Learning sous TensorFlow/Keras spécialisé dans la classification d'images (Chats vs Chiens). L'API expose des endpoints sécurisés permettant le traitement de requêtes unitaires et d'inférences par lots (*batch processing*), accompagnés d'un script client Python.

## 🚀 Fonctionnalités
- Prétraitement automatisé des images en entrée (redimensionnement, normalisation).
- Endpoint `/predict` pour la classification individuelle d'une image.
- Endpoint `/predict-batch` pour l'inférence simultanée sur plusieurs fichiers.
- Client Python autonome démontrant la consommation des endpoints.

## 🛠️ Technologies & Outils
- **Deep Learning :** TensorFlow / Keras
- **Framework API :** FastAPI / Flask
- **Prétraitement d'Image :** OpenCV, PIL, NumPy
- **Environnement :** Python, Jupyter Notebook

## ⚙️ Installation & Lancement

```bash
# 1. Cloner le dépôt
git clone [https://github.com/FatiBo9/Mod-le-API.git](https://github.com/FatiBo9/Mod-le-API.git)
cd Mod-le-API

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer le notebook ou l'API Python
app (2).py
