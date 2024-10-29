import csv
import random
import string
import datetime

types_places = ["camion", "voiture","moto", "handicape","total"]
nombre_places = [20,100,40,40,200]

def calcul_places(nom_fichier):
with open(nom_fichier,mode='r') as file:
    reader = csv.DictReader(file)
    places=(0,0,0,0,0)
    for row in reader:
        if (row['Occupation']=='oui'):
            match row['Numero de place']:
                case a<20 : places[0]+=1
                case a>=20 && a< 120:places[1]+=1
                case a>=120 && a< 160:places[2]+=1
                case a>=160 :places[3]+=1
            places[4]+=1
    return places

def csv_places(nom_fichier):
    # Nom des colonnes
    colonnes = [
        "Categorie",
        "Places disponibles",
        "Places totales"
    ]

    with open("places.csv", mode='w', newline='', encoding='utf-8') as fichier:
        writer = csv.DictWriter(fichier, fieldnames=colonnes)
        writer.writeheader()  # Écrire l'en-tête du CSV

        for i in range(5):
            donnees= calcul_places(nom_fichier)
            writer.writerow("Categorie":type_places[i], "Places disponibles":donnees[i],"Places totales": nombre_places[i])


def csv_infra(nombre_vehicules):
    # Nom des colonnes
    colonnes = [
        "Plaque",
        "Categorie"
    ]

    with open("infraction.csv", mode='w', newline='', encoding='utf-8') as fichier:
        writer = csv.DictWriter(fichier, fieldnames=colonnes)
        writer.writeheader()  # Écrire l'en-tête du CSV

        for _ in range(nombre_vehicules):
            writer.writerow(donnees_vehicule)
