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


//News page
const searchFrom = document.querySelector('.search');
const input = document.querySelector('.input');

searchFrom.addEventListener('submit', retrieve)

function retrieve(e) {

    if (input.value == '') {
        alert('Search input is empty!')
        return
    }

    var newsDisplay = document.getElementById('news-section');
    newsDisplay.innerHTML = "";

    e.preventDefault()

    const apiKey = 'f5a53a804dd7f19b1789c83e64c82fe9'
    let topic = input.value;

    let url = `https://gnews.io/api/v3/search?q=${topic}?&token=${apiKey}`

    fetch(url).then((res) => {
        return res.json()
    }).then((data) => {
        console.log(data)
        data.articles.forEach(article => {
            if (article.image == null) {
                console.log('working')
                newsDisplay.innerHTML = newsDisplay.innerHTML + `
                <div class="news-display">
                <a href="${article.url}" target="_blank"><img src="../images/no_image.jpg" alt=""></a>
                <h6><a href="${article.url} target="_blank"">${article.title}</a></h6>
                <p>${article.description}</p>
                <p class="publish-date">${article.publishedAt}</p>
                </div>
                `
            } else {
                newsDisplay.innerHTML = newsDisplay.innerHTML + `
                <div class="news-display">
                <a href="${article.url} target="_blank""><img src="${article.image}" alt=""></a>
                <h6><a href="${article.url} target="_blank"">${article.title}</a></h6>
                <p>${article.description}</p>
                <p class="publish-date">${article.publishedAt}</p>
                </div>
                `
            }
        })
    }).catch((error) => {
        console.log(error)
    })
    console.log(topic)
}

function firstload(e) {
    var newsDisplay = document.getElementById('news-section');
    newsDisplay.innerHTML = "";

    const apiKey = 'f5a53a804dd7f19b1789c83e64c82fe9'

    let url = `https://gnews.io/api/v3/search?q=covid?&token=${apiKey}`

    fetch(url).then((res) => {
        return res.json()
    }).then((data) => {
        console.log(data)
        data.articles.forEach(article => {
            if (article.image == null) {
                console.log('working')
                newsDisplay.innerHTML = newsDisplay.innerHTML + `
                <div class="news-display">
                <a href="${article.url}" target="_blank"><img src="images/no_image.jpg" alt=""></a>
                <h6><a href="${article.url} target="_blank"">${article.title}</a></h6>
                <p>${article.description}</p>
                <p class="publish-date">${article.publishedAt}</p>
                </div>
                `
            } else {
                newsDisplay.innerHTML = newsDisplay.innerHTML + `
                <div class="news-display">
                <a href="${article.url} target="_blank""><img src="${article.image}" alt=""></a>
                <h6><a href="${article.url} target="_blank"">${article.title}</a></h6>
                <p>${article.description}</p>
                <p class="publish-date">${article.publishedAt}</p>
                </div>
                `
            }
        })
    }).catch((error) => {
        console.log(error)
    })
};