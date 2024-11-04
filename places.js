// Fonction pour charger et afficher le tableau des véhicules
async function loadCSV() {
    const response = await fetch('vehicules_gare.csv');
    const data = await response.text();
    const rows = data.split('\n').slice(1); // Ignorer les en-têtes

    const tableBody = document.getElementById('places-table-body');
    tableBody.innerHTML = ''; // Réinitialiser le contenu

    rows.forEach(row => {
        let columns = row.split(',').map(col => col.trim());

        if (columns.length < 8) return; // Ignorer les lignes incomplètes

        // Concaténer les colonnes 6 et 7 si la ligne a 10 colonnes
        if (columns.length === 10) {
            columns[5] = `${columns[5].replace(/"/g, '')} ${columns[6].replace(/"/g, '')}`;
            columns.splice(6, 1);
        }

        const tr = document.createElement('tr');
        const occupation = columns[2];
        if (occupation.toLowerCase() === 'non') {
            tr.classList.add('non-occupee');
        }

        columns.forEach(column => {
            const td = document.createElement('td');
            td.textContent = column;
            tr.appendChild(td);
        });

        tableBody.appendChild(tr);
    });
}

// Appeler la fonction pour charger le CSV quand le DOM est prêt
document.addEventListener('DOMContentLoaded', loadCSV);
