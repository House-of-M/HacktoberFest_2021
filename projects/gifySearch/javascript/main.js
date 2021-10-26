/* 1. Grab the input value */

var button = document.querySelector("button");

button.addEventListener('click', function () {
    var Query = document.querySelector("input").value;
    pushToDOMGify(Query);
});

document.querySelector("input").addEventListener('keyup', function (e) {
    var Query = document.querySelector("input").value;
    if (e.key === 'Enter') {
        pushToDOMGify(Query);

    }
});


/* 2. do the data stuff with the API */
function pushToDOMGify(Query) {
    var container = document.getElementsByClassName('js-container')[0]
    _Query = Query.replace(" ", "+");
    var url = "http://api.giphy.com/v1/gifs/search?q=" + _Query + "&api_key=dc6zaTOxFJmzC";
    var GiphyAJAXCall = new XMLHttpRequest();
    GiphyAJAXCall.open('GET', url);
    GiphyAJAXCall.send();
    GiphyAJAXCall.addEventListener('load', function (e) {
        var data = e.target.response;
        var response = JSON.parse(data);

        response.data.forEach(element => {
            var imageURL = element.images.fixed_height.url;
            gif = "<img src=\"" + imageURL + "\" class=\"container-image\">";
            pushToDOM(gif);

        });

    });
}



/* 3. Show me the GIFs */
function pushToDOM(object) {
    var container = document.getElementsByClassName('js-container')[0]
    container.innerHTML += object;
}

