// js/dataProcessor.js

function loadCSVData(file) {
    Papa.parse(file, {
        download: true,
        header: true,
        complete: function(results) {
            displayData(results.data);
        },
        error: function(error) {
            console.error('Erreur lors du chargement du CSV :', error);
        }
    });
}

function displayData(data) {
    const tableBody = document.querySelector('#vehicules-garés tbody');
    
    data.forEach(row => {
        const newRow = document.createElement('tr');
        
        newRow.innerHTML = `
            <td>${row["Numero de place"]}</td>
            <td>${row["Type de place"]}</td>
            <td>${row["Occupation"]}</td>
            <td>${row["Plaque d'immatriculation"]}</td>
            <td>${row["Categorie de véhicule"]}</td>
            <td>${row["Temps paye"]}</td>
            <td>${row["Prix paye"]}</td>
            <td>${row["Horaire d'arrive"]}</td>
            <td>${row["Horaire de depart prevu"]}</td>
        `;
        
        tableBody.appendChild(newRow);
    });
}
