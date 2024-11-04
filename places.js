// Fonction pour charger et afficher le tableau des véhicules
async function loadCSV() {
    const response = await fetch('vehicules_gare.csv'); // Assurez-vous que le fichier CSV est dans le même dossier que ce fichier JS
    const data = await response.text();
    const rows = data.split('\n').slice(1); // On ignore la première ligne (les en-têtes)

    const tableBody = document.getElementById('places-table-body'); // Correction ici
    tableBody.innerHTML = ''; // Réinitialiser le contenu

    rows.forEach(row => {
        const columns = row.split(',');

        if (columns.length < 8) return; // Ignorer les lignes incomplètes

        const tr = document.createElement('tr');
        
        // Création des cellules pour chaque colonne
        columns.forEach(column => {
            const td = document.createElement('td');
            td.textContent = column.trim(); // Enlever les espaces autour du texte
            tr.appendChild(td);
        });

        tableBody.appendChild(tr); // Ajouter la ligne au corps du tableau
    });
}

// Appeler la fonction pour charger le CSV quand le DOM est prêt
document.addEventListener('DOMContentLoaded', loadCSV);