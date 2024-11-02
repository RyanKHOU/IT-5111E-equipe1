import csv
import random
import string
import datetime
from datetime import datetime

types_places = ["handicape", "voiture","camion", "moto","total"]
nombre_places = [20,100,40,40,200]
maintenant = datetime(2024,10,1,22,00,00,0)

def calcul_places(nom_fichier):
    with open(nom_fichier, mode='r') as file:
        reader = csv.DictReader(file)
        places = [0, 0, 0, 0, 0]
        for row in reader:
            if row['Occupation'] == 'non':
                numero_place = int(row['Numero de place'])
                if numero_place < 20:
                    places[0] += 1  # Handicape
                elif 20 <= numero_place < 120:
                    places[1] += 1  # Voiture
                elif 120 <= numero_place < 160:
                    places[2] += 1  # Camion
                elif numero_place >= 160:
                    places[3] += 1  # Moto
                places[4] += 1  # Total des places non occupées
        return places


def calcul_temps(nom_fichier):
    with open(nom_fichier,mode='r') as file:
        reader = csv.DictReader(file)
        liste = []
        for row in reader:
            if (row['Occupation']=='oui'):
                if datetime.strptime(row['Horaire de depart prevu'], "%Y-%m-%d %H:%M:%S.%f") < maintenant:
                    liste.append((row["Numero de place"],row["Plaque d'immatriculation"]))
        return liste

def calcul_type(nom_fichier):
    with open(nom_fichier,mode='r') as file:
        reader = csv.DictReader(file)
        liste = []
        for row in reader:
            if (row['Occupation']=='oui'):
                if row['Type de place'] != row['Categorie de vehicule']:
                    liste.append((row["Numero de place"],row["Plaque d'immatriculation"]))
        return liste

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
            writer.writerow({"Categorie":types_places[i], "Places disponibles":donnees[i],"Places totales": nombre_places[i]})


def csv_infra(nom_fichier):
    # Nom des colonnes
    colonnes = [
        "Place",
        "Plaque",
        "Categorie"
    ]

    with open("infraction.csv", mode='w', newline='', encoding='utf-8') as fichier:
        writer = csv.DictWriter(fichier, fieldnames=colonnes)
        writer.writeheader()  # Écrire l'en-tête du CSV
        donneestps= calcul_temps(nom_fichier)
        for i in range(len(donneestps)):
            writer.writerow({"Place":donneestps[i][0],"Plaque":donneestps[i][1],"Categorie":"Temps depasse"})
        donneestyp= calcul_type(nom_fichier)
        for i in range(len(donneestyp)):
            writer.writerow({"Place":donneestyp[i][0],"Plaque":donneestyp[i][1],"Categorie":"Type de places"})


def main(nom_fichier):
    print(calcul_places(nom_fichier))
    csv_infra(nom_fichier)
    csv_places(nom_fichier)
    
if __name__ == "__main__":
    main( "vehicules_gare.csv" )