const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});


// chart colors
var colors = ['#007bff', '#28a745', '#333333', '#c3e6cb', '#dc3545', '#6c757d'];

/* large line chart */
var chLine = document.getElementById("chLine");
var line1Checkbox = document.getElementById("line1Checkbox");
var line2Checkbox = document.getElementById("line2Checkbox");

var chartData = {
  labels: ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"],
  datasets: [
    {
      data: [589, 445, 483, 503, 956, 692, 634],
      backgroundColor: 'transparent',
      borderColor: colors[1],
      borderWidth: 3,
      pointBackgroundColor: colors[1],
      hidden: false,
    },
    {
      data: [300, 450, 600, 350, 700, 800, 400],
      backgroundColor: 'transparent',
      borderColor: colors[2],
      borderWidth: 3,
      pointBackgroundColor: colors[2],
      hidden: false,
    },
    {
      data: [400, 550, 650, 550, 500, 400, 800],
      backgroundColor: 'transparent',
      borderColor: colors[0],
      borderWidth: 3,
      pointBackgroundColor: colors[0],
      hidden: false,
    },
  ],
};

if (chLine) {
  var chart = new Chart(chLine, {
    type: 'line',
    data: chartData,
    options: {
      scales: {
        xAxes: [
          {
            ticks: {
              beginAtZero: false,
            },
          },
        ],
      },
      legend: {
        display: false,
      },
      responsive: true,
    },
  });

  // Обработчики для чекбоксов
  line1Checkbox.addEventListener('change', function () {
    chart.data.datasets[0].hidden = !line1Checkbox.checked;
    chart.update();
  });
  line2Checkbox.addEventListener('change', function () {
    chart.data.datasets[1].hidden = !line2Checkbox.checked;
    chart.update();
  });
}

/* bar chart */
  var chBar = document.getElementById("chBar");
  var line3Checkbox = document.getElementById("line3Checkbox");
  var line4Checkbox = document.getElementById("line4Checkbox");
  if (chBar) {
    new Chart(chBar, {
      type: 'bar',
      data: {
        labels: ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "ВС"],
        datasets: [
          {
            data: [589, 445, 483, 503, 689, 692, 634],
            backgroundColor: colors[0]
          },
          {
            data: [639, 465, 493, 478, 589, 632, 674],
            backgroundColor: colors[1]
          }
        ]
      },
      options: {
        legend: {
          display: false
        },
        scales: {
          xAxes: [{
            barPercentage: 0.4,
            categoryPercentage: 0.5
          }]
        }
      }
    });
 // Обработчики для чекбоксов
line1Checkbox.addEventListener('change', function () {
  chBar.data.datasets[0].hidden = !line1Checkbox.checked;
  chBar.update();
});
line2Checkbox.addEventListener('change', function () {
  chBar.data.datasets[1].hidden = !line2Checkbox.checked;
  chBar.update();
});
  }