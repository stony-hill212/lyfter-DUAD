const pokemon1= fetch("https://pokeapi.co/api/v2/pokemon/25").then(response=>response.json());
const pokemon2= fetch("https://pokeapi.co/api/v2/pokemon/6").then(response=>response.json());
const pokemon3= fetch("https://pokeapi.co/api/v2/pokemon/150").then(response=>response.json());

Promise.all([pokemon1, pokemon2, pokemon3]).then(pokemon=> {
    console.log(pokemon);
})
.catch(error=> {
    console.log("Something went wrong:", error);
});
