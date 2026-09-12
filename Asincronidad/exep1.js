const pokemon1= fetch("https://pokeapi.co/api/v2/pokemon/25");
const pokemon2= fetch("https://pokeapi.co/api/v2/pokemon/6");
const pokemon3= fetch("https://pokeapi.co/api/v2/pokemon/150");

Promise.all([pokemon1, pokemon2, pokemon3]).then(responses=> {
    return Promise.all(
        responses.map(response=> response.json())
    );
}).then(pokemon=> {
    console.log(pokemon);
}).catch(error=> {
    console.log("Something went wrong:", error);
});