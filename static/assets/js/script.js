'use strict';



/**
 * add event on multiple elements
 */

const addEventOnElements = function (elem, type, callback) {
  for (let i = 0, len = elem.length; i < len; i++) {
    elem[i].addEventListener(type, callback);
  }
}



/**
 * LOADING
 */

const loadingElement = document.querySelector("[data-loading-container]");

window.addEventListener("load", function () {
  loadingElement.classList.add("loaded");
  document.body.classList.add("loaded");
});



/**
 * MOBILE NAVBAR TOGGLE
 */

const navbar = document.querySelector("[data-navbar]");
const navTogglers = document.querySelectorAll("[data-nav-toggler]");
const navbarLinks = document.querySelectorAll("[data-nav-link]");
const overlay = document.querySelector("[data-overlay]");

const toggleNavbar = function () {
  navbar.classList.toggle("active");
  overlay.classList.toggle("active");
  document.body.classList.toggle("active");
}

addEventOnElements(navTogglers, "click", toggleNavbar);

const closeNavbar = function () {
  navbar.classList.remove("active");
  overlay.classList.remove("active");
  document.body.classList.remove("active");
}

addEventOnElements(navbarLinks, "click", closeNavbar);



/**
 * HEADER
 */

// header will be active after scroll 200px of window

const header = document.querySelector("[data-header]");

const headerActive = function () {
  window.scrollY > 200 ? header.classList.add("active")
    : header.classList.remove("active");
}

window.addEventListener("scroll", headerActive);



/**
 * SCROLL REVEAL
 */

const revealElements = document.querySelectorAll("[data-reveal]");

const scrollReveal = function () {
  for (let i = 0, len = revealElements.length; i < len; i++) {
    if (revealElements[i].getBoundingClientRect().top < window.innerHeight / 1.2) {
      revealElements[i].classList.add("revealed");
    }
  }
}

window.addEventListener("scroll", scrollReveal);
window.addEventListener("load", scrollReveal);



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