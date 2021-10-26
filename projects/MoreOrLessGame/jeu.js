// génération d'un nombre random
function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}
let max = 100;
let nbAdeviner = getRandomInt(max);
let compteur = 3;

// Première instruction : lorsque l'utilisateur clique sur le bouton, on récupère la supposition 
// Pour se faire, on va utiliser l'attribut value des input field 
// on récupère le bouton et on le stock dans une variable (let button <= querySelector)
let button = document.querySelector("button");
// on lui ajoute un EventListener (button.addEventListener('click','fonction'));
button.addEventListener('click', function (){
// la fonction va consister à récupérer la valeur de input field 
// on va déclarer une variable input (let input = querySelector())
let input = document.querySelector("input");
// on va ensuite lui assigner la valeur à l'intérieur de l'input (input = input.value)
let temp = input.value;
input.value = "";
compteur=compteur-1;
let reponse = plusOuMoins(temp, nbAdeviner, compteur);
pushToDom(reponse);
});

// Deuxième instruction, il faut voir si la valeur récupérer est supérieur ou inférieur au nombre généré aléatoirement 
// pour cela, il faut créer une fonction plusOuMoins 
function plusOuMoins(x, random, compteur){
    // elle prend en entrée la valeur (input)
    // et retourne en sortie un string "plus" si la valeur input est inférieure au nombre généré
    if (compteur==0){
        return "tu as perdu";
    }
    else if (x<random){
        return "plus";
    }
    else if(x==random){
        return "tu as trouvé !";
    }
    else {
        return "moins";
    }
    // et retourne en string "moins" si la valeur input est supérieure au nombre généré 
}


// Troisième instruction, il faut écrire une fonction pushToDom qui prend en entrée un string 
function pushToDom(chaine){
    let p = document.querySelector("#reponse-js");
    console.log(p);
    p.innerText=chaine;
}
// (plus ou moins, que nous renvoie la fonction plusOuMoins)
// elle va récupérer le champ texte vide et le stocker dans une variable (let texte = querySelector())
// elle va mettre plus ou moins dans son text en utilisant l'attribut (innerText)

// les fonctions plusOuMoins et pushToDom sont appelées dans la fonction de l'EventListener.
// donc dans la fonction eventListener 
// à la suite de input = input.value 
// on va faire let plusMoins = plusOuMoins(input) // appeler la fonction plusOuMoins qui va retourner si la valeur est plus grande ou plus petite 
// puis on va faire pushToDom(plusOuMoins) qui va écrire dans le champ de texte plus ou moins.

addEventListener