import unittest
from io import StringIO
import csv
from unittest.mock import patch, mock_open
from Traitement import calcul_places, csv_places, csv_infra
import pandas as pd






class Tests(unittest.TestCase):

    
    def get_categories_indexes(self, df):
        categories = ["handicape", "voiture", "camion", "moto"]
        indexes = {}

        for categorie in categories:
            if categorie in df["Type de place"].values:
                category_rows = df[df["Type de place"] == categorie]
                first_index = category_rows.index[0]
                indexes[categorie] = first_index

        return indexes
        
        
    # Test de la position des catégories dans le fichier CSV
    def test_creation_csv_indexes(self):
        
        df = pd.read_csv("vehicules_gare.csv")
        resultat = self.get_categories_indexes(df)

        resultat_attendu = {
            "handicape": 0,
            "voiture": 20,
            "camion": 120,
            "moto": 160
        }
        
        self.assertEqual(resultat, resultat_attendu)

        
        
    # Test de la fonction calcul_places
    @patch("builtins.open", new_callable=mock_open)
    def test_calcul_places(self, mock_file):
        # Liste des cas de test avec des configurations différentes
        test_cases = [
            ("Numero de place,Occupation\n1,oui\n21,oui\n121,non\n161,oui", (1, 1, 0, 1, 3)),
            ("Numero de place,Occupation\n5,oui\n30,oui\n130,oui\n170,oui", (1, 1, 1, 1, 4)),
            ("Numero de place,Occupation\n2,oui\n25,non\n122,oui\n165,non", (1, 0, 1, 0, 2)),
        ]
        
        # Boucle sur chaque cas de test
        for read_data, expected_result in test_cases:
            with self.subTest(read_data=read_data, expected_result=expected_result):
                mock_file.return_value.read_data = read_data  # Redéfinir le contenu de mock_open
                result = calcul_places("vehicule_gare.csv")
                self.assertEqual(result, expected_result)
    
    
    # Test de la fonction calcul_places avec un numéro de place trop élevé
    @patch("builtins.open", new_callable=mock_open, read_data="Numero de place,Occupation\n201,oui")
    def test_calcul_places_high_number_error(self, mock_file):

        with self.assertRaises(ValueError) as context:
            calcul_places("fichier.csv")
        
        self.assertIn("Numéro de place trop élevé", str(context.exception))
        
        
    # Test de csv_places  
    @patch("builtins.open", new_callable=mock_open)
    @patch("Traitement.calcul_places", return_value=(10, 50, 20, 20, 100))
    def test_csv_places(self, mock_calcul_places, mock_file):
        csv_places("vehicules_gare.csv")

        mock_file().write.assert_any_call("Categorie,Places disponibles,Places totales\n")
        mock_file().write.assert_any_call("camion,10,20\n")
        mock_file().write.assert_any_call("voiture,50,100\n")
        mock_file().write.assert_any_call("moto,20,40\n")
        mock_file().write.assert_any_call("handicape,20,40\n")
        mock_file().write.assert_any_call("total,100,200\n")
    
     # Test de csv_infra
    @patch("builtins.open", new_callable=mock_open)
    def test_csv_infra(self, mock_file):
        nombre_vehicules = 5
        csv_infra(nombre_vehicules)
        # Vérification que le fichier contient le bon nombre de lignes
        mock_file().write.assert_any_call("Plaque,Categorie\n")
        self.assertEqual(mock_file().write.call_count, nombre_vehicules + 1)  # +1 pour l'en-tête

    
    

if __name__ == "__main__":
    unittest.main()