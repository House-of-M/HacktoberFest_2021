// RECUPERER RESULTAT

let result = document.querySelector('#result');

// ------------- DECLARATION FONCTIONS UTILISEES
function display(valeur){
    result.value+=valeur
}

// AJOUTER EVENT LISTENER SUR LES NUMEROS ET LISTENERS

let tab=[];
let list_op = ['mul', 'div', 'sus', 'add'];
for(let i=0; i<10; i++){
    tab.push(document.querySelector('#num'+i));
}
for(let i=0; i<list_op.length; i++){
    tab.push(document.querySelector('#'+list_op[i]));  
}

tab.forEach(element => {
    element.addEventListener('click', function(){
        display(element.value);
    })
})

// AJOUTER SUR CLEAR

let clear = document.querySelector("#clear");
clear.addEventListener('click', function(){
    result.value="";
})

// CALCULER
let cal = document.querySelector("#cal");
cal.addEventListener('click', function(){
    result.value=eval(result.value);

})



