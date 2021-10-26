const pokemons = ['bellossom', 'bulbasaur', 'butterfree', 'calyrex', 'charizad', 'glastrier', 'mareep', 'marill', 'regidrago', 'regieleki',
    'squirtle', 'sudowoodo', 'xatu', 'zarude'];
const stories = ['you ran into this weird little creature ... it\'s intrigued by you, maybe she likes you, Oh wait she is about to bite you !!!!! Ruuuuun ... oh No you died :)',
    'once upon a time, an adventurer was on his way to a long lost village, but in their way they stumbled upon what will be one of their best friends, and adorable lowkey creepy creature.'];

// declaration d'une fonction qui retourne un nombre aleatoire entre 0 et un maximum.
function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

// choisire un pokemon et une mini histoire aleatoirement.
let pokemonName = pokemons[getRandomInt(pokemons.length)];
let story = stories[getRandomInt(stories.length)];

//retrieve the username
let username = prompt("enter your name adventurer!");

// placer le nom de l'utilisateur dans les span avec l'id username
let usernameSpots = document.querySelectorAll("#username");
usernameSpots.forEach(element => {
    element.innerText = username;
});

// placer le nom du pokemon dans les span avec l'id pokemon-name
let pokemonNamesSpots = document.querySelectorAll("#pokemon-name");
pokemonNamesSpots.forEach(element => {
    element.innerText = pokemonName;
});

// placer l'histoire dans le div avec l'id story
let storySpot = document.querySelector("#story");
storySpot.innerText = story;

//placer l'image dans le div avec l'id image-spot
let imageSpot = document.querySelector("#image-spot");
imageSpot.innerHTML = '<img src = "./assets/' + pokemonName + '.png">';