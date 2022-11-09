
var ctx = document.getElementById('myChart').getContext('2d');
// And for a doughnut chart
var myDoughnutChart = new Chart(ctx, {
  type: 'horizontalBar',
  data: {
    datasets: [
      {
        data: [400, 600, 200],
        backgroundColor: ['#BB86FC', '#6bafff', '#03DAC6',],
      },
    ],
    labels: ['user1', 'user2', 'user3'],
  },
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
});