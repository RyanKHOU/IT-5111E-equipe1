import csv
import random
import string
from datetime import datetime, timedelta

# Définir les catégories de véhicules et les prix par heure à partir de la grille tarifaire
grille_tarifaire = {}

# Lire la grille tarifaire depuis le fichier CSV
def lire_grille_tarifaire(fichier_grille):
    with open(fichier_grille, newline='', encoding='utf-8') as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv, delimiter=';')
        next(lecteur_csv)  # Ignorer l'en-tête
        for ligne in lecteur_csv:
            categorie = ligne[0]
            duree = ligne[1]
            tarif_str = ligne[2].replace('€', '').strip().replace(',', '.')  # Nettoyer et convertir le tarif

            # Vérifier si le tarif est bien un nombre
            try:
                tarif = float(tarif_str)
            except ValueError:
                # Ignorer la ligne si le tarif n'est pas un nombre
                print(f"Tarif non valide pour la ligne: {ligne}")
                continue

            if categorie not in grille_tarifaire:
                grille_tarifaire[categorie] = {}
            grille_tarifaire[categorie][duree] = tarif

# Types de places
types_places = ["moto", "voiture", "camion", "handicape"]

# Générer une plaque d'immatriculation aléatoire
def generer_plaque():
    lettres = ''.join(random.choices(string.ascii_uppercase, k=2))
    chiffres = ''.join(random.choices(string.digits, k=4))
    return f"{lettres}-{chiffres}"

# Générer un horaire d'arrivée et un horaire de départ prévu
def generer_horaires():
    horaire_arrivee = datetime.now() - timedelta(hours=random.randint(1, 24))
    temps_paye = round(random.uniform(0.5, 24), 2)
    horaire_depart = horaire_arrivee + timedelta(hours=temps_paye)
    return horaire_arrivee, horaire_depart, temps_paye

# Calculer le prix payé à partir de la grille tarifaire
def calculer_prix(categorie, temps_paye):
    if categorie not in grille_tarifaire:
        return 0
    # Rechercher le tarif correspondant à la durée la plus proche
    tarif = 0
    for duree, prix in grille_tarifaire[categorie].items():
        if float(duree.replace('H', '').strip()) >= temps_paye:
            tarif = prix
            break
    return tarif

# Générer les informations d'un véhicule garé
def generer_donnees_vehicule(place):
    if place < 20:
        type_place = types_places[3]
    elif place < 120:
        type_place = types_places[2]
    elif place < 160:
        type_place = types_places[1]
    else:
        type_place = types_places[0]

    occupe = random.choice(["oui", "non"])
    if occupe == "oui":
        type_vehicule = types_places[random.randint(0, 2)]  # Assigner une catégorie de véhicule
        plaque = generer_plaque()
        horaire_arrivee, horaire_depart, temps_paye = generer_horaires()
        prix_paye = calculer_prix(type_vehicule, temps_paye)
        
        return {
            "Numero de place": place,
            "Type de place": type_place,
            "Occupation": occupe,
            "Plaque d'immatriculation": plaque,
            "Catégorie de véhicule": type_vehicule,
            "Temps payé": temps_paye,
            "Prix payé (€)": prix_paye,
            "Horaire d'arrivée": horaire_arrivee.strftime("%Y-%m-%d %H:%M"),
            "Horaire de départ prévu": horaire_depart.strftime("%Y-%m-%d %H:%M"),
        }
    else:
        return {
            "Numero de place": place,
            "Type de place": type_place,
            "Occupation": occupe,
            "Plaque d'immatriculation": "",
            "Catégorie de véhicule": "",
            "Temps payé": "",
            "Prix payé (€)": "",
            "Horaire d'arrivée": "",
            "Horaire de départ prévu": "",
        }

# Générer un CSV avec des véhicules aléatoires
def generer_csv(nombre_places, fichier_csv):
    # Nom des colonnes
    colonnes = [
        "Numero de place",
        "Type de place",
        "Occupation",
        "Plaque d'immatriculation",
        "Catégorie de véhicule",
        "Temps payé",
        "Prix payé (€)",
        "Horaire d'arrivée",
        "Horaire de départ prévu"
    ]

    # Générer des données et les écrire dans le fichier CSV
    with open(fichier_csv, mode='w', newline='', encoding='utf-8') as fichier:
        writer = csv.DictWriter(fichier, fieldnames=colonnes)
        writer.writeheader()  # Écrire l'en-tête du CSV

        for place in range(1, nombre_places + 1):
            donnees_vehicule = generer_donnees_vehicule(place)
            writer.writerow(donnees_vehicule)

# Lire la grille tarifaire avant de générer le CSV
lire_grille_tarifaire('Database_Generation/grille_tarifaire_parking.csv')

# Exemple d'utilisation pour générer un fichier CSV avec 100 places de parking
generer_csv(100, "vehicules_gare.csv")
