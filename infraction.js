// Fonction pour charger le CSV et remplir le tableau
async function loadCSV() {
    try {
        // Charge le fichier CSV
        const response = await fetch('infraction.csv');
        if (!response.ok) throw new Error(`Erreur HTTP : ${response.status}`);
        
        const data = await response.text();
        
        // Transformation des lignes CSV en tableaux de données
        const rows = data.split('\n').map(row => row.split(','));
        
        // Sélection du corps de la table pour y insérer les lignes
        const tableBody = document.getElementById('infraction-table-body');
        
        // Nettoie le contenu existant du tableau
        tableBody.innerHTML = '';
        
        // Remplit le tableau avec les données CSV
        rows.forEach((row, index) => {
            if (index === 0) return; // Ignorer l'en-tête CSV
            
            // Création d'une ligne HTML pour chaque ligne de données
            const rowElement = document.createElement('tr');
            
            row.forEach(cellText => {
                const cellElement = document.createElement('td');
                cellElement.textContent = cellText.trim();
                rowElement.appendChild(cellElement);
            });
            
            tableBody.appendChild(rowElement);
        });
    } catch (error) {
        console.error('Erreur lors du chargement du fichier CSV:', error);
    }
}

// Appel de la fonction au chargement de la page
document.addEventListener('DOMContentLoaded', loadCSV);
