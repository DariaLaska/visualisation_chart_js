var ourBar = $("#chartBar");

var barChart = new Chart(ourBar, {
    type: 'bar',
    data: {
        labels: countrties_list,
        datasets: [
            {
                label: 'Популяция 2019 г',
                data: population,
                backgroundColor: 'rgba(54, 162, 235, 0.4)',
                borderWidth: 1,
                borderRadius: 8,
                borderColor: 'rgba(54, 162, 235, 0.9)'
            }
        ]
    },
});