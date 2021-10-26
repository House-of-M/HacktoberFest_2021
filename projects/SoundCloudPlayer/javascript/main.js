

var search = {
    init: function () {
        query = document.querySelector('.js-search');
        submit = document.querySelector('.js-submit');
        reset = document.querySelector('.reset');
        reset.addEventListener('click', function () {
            localStorage.clear();
        });
        submit.addEventListener('click', function () {
            search.submit(query);
        });
        query.addEventListener('keyup', function (e) {
            if (e.key === 'Enter') {
                search.enter(query);
            }
        })
    },
    submit: function (query) {
        SoundCloudAPI.getTrack(query.value);
    },
    enter: function (query) {
        SoundCloudAPI.getTrack(query.value);
    }
}

var SoundCloudAPI = {
    init: function () {
        SC.initialize({
            client_id: 'cd9be64eeb32d1741c17cb39e41d254d'
        });
    },
    getTrack: function (query) {
        SC.get('/tracks', {
            q: query
        }).then(function (tracks) {
            tracks.forEach(track => {
                SoundCloudAPI.renderTrack(track);
            });
        });
    },
    renderTrack: function (track) {
        card = document.createElement("div");
        card.classList.add("card");

        image = document.createElement("div");
        image.classList.add("image");

        img = document.createElement("img");
        img.classList.add("image_img");
        img.src = track.artwork_url

        image.appendChild(img);

        card.appendChild(image);

        content = document.createElement("div");
        content.classList.add("content");

        header = document.createElement("div");
        header.classList.add("header");

        link = document.createElement("a");
        link.href = track.permalink_url;
        link.target = "_blank";
        link.innerHTML = track.title;

        header.appendChild(link);

        content.appendChild(header);

        card.appendChild(content);

        bottom = document.createElement("div");
        bottom.classList.add("ui", "bottom", "attached", "button", "js-button");

        i = document.createElement("i");
        i.classList.add("add", "icon");

        span = document.createElement("span");
        span.innerHTML = "Add to playlist";

        bottom.appendChild(i);
        bottom.appendChild(span);

        bottom.addEventListener('click', function () {
            SoundCloudAPI.embedTrack(track.permalink_url);
        });

        card.appendChild(bottom);


        document.querySelector(".js-search-results").appendChild(card);
    },
    embedTrack: function (trackLink) {
        SC.oEmbed(trackLink, {
            auto_play: true
        }).then(function (embed) {
            box = document.createElement("div");
            box.innerHTML = embed.html;
            sideBar = document.querySelector(".js-playlist")
            sideBar.insertAfter(box, sideBar.firstChild);
            localStorage.setItem("key", sideBar.innerHTML);
            localStorage.clear();
        });
    }

}



//restore context
sideBar = document.querySelector(".js-playlist")
if (!localStorage.getItem("key") === '') {
    sideBar.innerHTML = localStorage.getItem("key");
}
//init
SoundCloudAPI.init();
search.init();




