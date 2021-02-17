//Navbar color on scroll
$(window).scroll(function () {
    $('nav').toggleClass('scrolled', $(this).scrollTop() > 50);
})


/*** 
========================================
    Charts
========================================
 ***/

//-------------------------------Bar Chart----------------------------------------------
var ctx = document.getElementById('myChart2').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', "July", "August", "September", "October", "November", "December"],
        datasets: [{
            label: "Sale Amount",
            data: [1500, 800, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            fill: true,
            borderWidth: 3,
            order:0,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 99, 132, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 99, 132, 1)',
            ],
        }]
    },
    options: {
        title: {
          display: true,
          text: 'Total Sale Amount Per Month'
        },
        hover: {
            mode: 'index',
            intersect: true
        },
        scales: {
        yAxes: [{
            ticks: {
                beginAtZero: true
            }
            }]
        }
    }
});