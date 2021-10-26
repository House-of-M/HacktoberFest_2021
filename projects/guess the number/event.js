let jeu = {
    nombre: NaN,
    afficherSurPage: function (chaine) {
        let space = document.querySelector(".js-manipulation");
        space.innerHTML += "<h1> " + chaine + " </h1>";
        let input = document.getElementById("guess").value = "";
    },
    evalue: function (valeur) {
        if (parseInt(valeur) == jeu.nombre) {
            jeu.afficherSurPage("Bravo tu a gagner!!");
        } else if (parseInt(valeur) > jeu.nombre) {
            jeu.afficherSurPage(valeur + "! t'as visé tros haut :/");
        } else {
            jeu.afficherSurPage(valeur + "! t'as visé tros bas :/");
        }
    },
    init: function () {
        let input = document.getElementById("guess");
        input.addEventListener("keyup", function (e) {
            if (e.key === "Enter") {
                console.log("in");
                jeu.evalue(input.value);
            }
        });
        let _try = document.getElementById("submit").addEventListener("click", function (e) {
            jeu.evalue(input.value);
        });
        jeu.nombre = Math.floor(Math.random() * 100)
    }




}

jeu.init();

