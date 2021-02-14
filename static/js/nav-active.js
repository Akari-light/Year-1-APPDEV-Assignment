$(window).on("load", setTimeout(function () {
    var url = window.location.pathname;
    var filename = url.substring(url.lastIndexOf('/') + 1);
    var nav2 = document.getElementsByClassName("nav-link");
    var arr2 = toArray(nav2);
    arr2.forEach((item) => {
        if (item.getAttribute("href").includes(filename)) {
            item.parentElement.classList.add("active");
        }
        else {
            item.parentElement.classList.remove("active");
        }
    });
    $("#footer-date").html(new Date().getFullYear())
}
    , 1000));

function toArray(x) {
    for (var i = 0, a = []; i < x.length; i++)
        a.push(x[i]);

    return a
}