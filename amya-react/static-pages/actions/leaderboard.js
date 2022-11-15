
$(document).ready(function () {

	
	var chart = $("#chart");
	// var ls = chart.getContext('2d'); -- why does this break?


	// labels for each data
	const labels = [
		"my name",
		"user2",
		"user3"
	];

	// the data being displayed
	const data = {
		labels: labels,
		datasets: [{
			label: 'My First Dataset',
			backgroundColor: ['#BB86FC', '#6bafff', '#03DAC6'],
			data: [400, 600, 200],
		}]
	};

	// how the data should be configured/displayed
	const config = {
		type: 'horizontalBar',
		data: data,
		options: {

			legend: {
				display: false,
			},

			scales: {
				yAxes: [{
					ticks: {
						fontColor: "white",
						beginAtZero: true
					}
				}],

				xAxes: [{
					ticks: {
						fontColor: "white",
						beginAtZero: true
					}
				}]
			}

		}
	};

	// display the chart
	const myChart = new Chart (chart, config);
	
});
