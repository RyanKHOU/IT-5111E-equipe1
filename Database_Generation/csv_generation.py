import csv
import random
import string

# Définir les catégories de véhicules et les prix par heure
categories_vehicules = {
    "moto": 1.5,  # prix par heure
    "voiture": 2.5,
    "camion": 5.0
}

# Types de places
types_places = ["place moto", "place voiture", "place camion"]

# Générer une plaque d'immatriculation aléatoire
def generer_plaque():
    lettres = ''.join(random.choices(string.ascii_uppercase, k=2))
    chiffres = ''.join(random.choices(string.digits, k=4))
    return f"{lettres}-{chiffres}"

# Générer les informations d'un véhicule garé
def generer_donnees_vehicule():
    categorie = random.choice(list(categories_vehicules.keys()))
    plaque = generer_plaque()
    numero_place = random.randint(1, 100)  # Numéro de place aléatoire
    type_place = f"place {categorie}"
    temps_stationnement = round(random.uniform(0.5, 24), 2)  # Entre 30 min et 24 heures
    prix = round(temps_stationnement * categories_vehicules[categorie], 2)
    paiement_effectue = random.choice(["oui", "non"])
    
    return {
        "Plaque d'immatriculation": plaque,
        "Numéro de place": numero_place,
        "Type de place": type_place,
        "Catégorie de véhicule": categorie,
        "Temps de stationnement (h)": temps_stationnement,
        "Prix (€)": prix,
        "Paiement effectué": paiement_effectue
    }

# Générer un CSV avec des véhicules aléatoires
def generer_csv(nombre_vehicules, fichier_csv):
    # Nom des colonnes
    colonnes = [
        "Plaque d'immatriculation", 
        "Numéro de place", 
        "Type de place", 
        "Catégorie de véhicule", 
        "Temps de stationnement (h)", 
        "Prix (€)", 
        "Paiement effectué"
    ]
    
    # Générer des données et les écrire dans le fichier CSV
    with open(fichier_csv, mode='w', newline='', encoding='utf-8') as fichier:
        writer = csv.DictWriter(fichier, fieldnames=colonnes)
        writer.writeheader()  # Écrire l'en-tête du CSV
        
        for _ in range(nombre_vehicules):
            donnees_vehicule = generer_donnees_vehicule()
            writer.writerow(donnees_vehicule)

# Exemple d'utilisation pour générer un fichier CSV avec 100 véhicules
generer_csv(100, "vehicules_gare.csv")
