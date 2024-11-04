import csv
import random
import string
import datetime

# Types de places et tarifs horaires
types_places = ["moto", "voiture", "camion", "handicape"]
tarifs_horaire = {
    "moto": 1.5,     # Tarif par heure pour les motos
    "voiture": 3.0,  # Tarif par heure pour les voitures
    "camion": 5.0,   # Tarif par heure pour les camions
    "handicape": 2.0 # Tarif par heure pour les places handicapées
}

# Générer une plaque d'immatriculation aléatoire
def generer_plaque():
    lettres = ''.join(random.choices(string.ascii_uppercase, k=2))
    chiffres = ''.join(random.choices(string.digits, k=4))
    return f"{lettres}-{chiffres}"

def generer_type_place(place):
    if place < 20:
        return types_places[3]  # handicapé
    elif place < 120:
        return types_places[1]  # voiture
    elif place < 160:
        return types_places[2]  # camion
    else:
        return types_places[0]  # moto

# Générer les informations d'un véhicule garé
def generer_donnees_vehicule(place):
    occupe = random.choice(["oui", "non"])
    if occupe == "oui":
        type_vehicule = generer_type_place(place)
        plaque = generer_plaque()
        
        # Générer une durée de stationnement aléatoire pouvant dépasser un jour
        jours = random.randint(0, 2)  # 0 à 2 jours
        heures = random.randint(0, 23)  # 0 à 23 heures
        minutes = random.randint(0, 59)  # 0 à 59 minutes
        seconds = random.randint(0, 59)  # 0 à 59 secondes
        
        temps_paye = datetime.timedelta(days=jours, hours=heures, minutes=minutes, seconds=seconds)
        horaire_debut = datetime.datetime(2024, 10, 1, random.randint(0, 23), random.randint(0, 59), random.randint(0, 59), 0)
        horaire_fin = horaire_debut + temps_paye
        
        # Calculer le prix basé sur le temps passé et le tarif horaire
        tarif = tarifs_horaire[type_vehicule]
        # Calculer le nombre total d'heures
        total_heures = temps_paye.total_seconds() / 3600  # Convertir les secondes en heures
        prix = tarif * total_heures  # Prix total basé sur le temps passé
        prix = round(prix, 1)  # Arrondir le prix à une seule décimale
        
    else:
        type_vehicule = None
        temps_paye = None
        prix = None
        horaire_debut = None
        horaire_fin = None
        plaque = None

    return {
        "Numero de place": place,
        "Type de place": generer_type_place(place),
        "Occupation": occupe,
        "Plaque d'immatriculation": plaque,
        "Categorie de vehicule": type_vehicule,
        "Temps paye": temps_paye,
        "Prix paye": prix,
        "Horaire d'arrive": horaire_debut,
        "Horaire de depart prevu": horaire_fin,
    }

# Générer un CSV avec des véhicules aléatoires
def generer_csv(nombre_vehicules, fichier_csv):
    # Nom des colonnes
    colonnes = [
        "Numero de place",
        "Type de place",
        "Occupation",
        "Plaque d'immatriculation",
        "Categorie de vehicule",
        "Temps paye",
        "Prix paye",
        "Horaire d'arrive",
        "Horaire de depart prevu"
    ]

    # Générer des données et les écrire dans le fichier CSV
    with open(fichier_csv, mode='w', newline='', encoding='utf-8') as fichier:
        writer = csv.DictWriter(fichier, fieldnames=colonnes)
        writer.writeheader()  # Écrire l'en-tête du CSV

        for _ in range(nombre_vehicules):
            donnees_vehicule = generer_donnees_vehicule(_)
            writer.writerow(donnees_vehicule)

# Exemple d'utilisation pour générer un fichier CSV avec 200 véhicules
generer_csv(200, "vehicules_gare.csv")
