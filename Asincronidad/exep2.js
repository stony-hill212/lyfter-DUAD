const pokemon1= fetch("https://pokeapi.co/api/v2/pokemon/25").then(response=> {
    if(!response.ok) {
        throw new Error("Pokemon 1 not found");
    }
    return response.json();
});
const pokemon2= fetch("https://pokeapi.co/api/v2/pokemon/6").then(response=> {
    if(!response.ok) {
        throw new Error("Pokemon 2 not found");
    }
    return response.json();
});
const pokemon3= fetch("https://pokeapi.co/api/v2/pokemon/150").then(response=> {
    if(!response.ok) {
        throw new Error("Pokemon 3 not found");
    }
    return response.json();
});

Promise.any([pokemon1, pokemon2, pokemon3]).then(pokemon=> {
    console.log(`The first Pokemon resolved is: ${pokemon.name}`);
}).catch(error=> {
    if (error instanceof AggregateError) {
        console.log("All requests failed.");
    } else {
        console.log("Something went wrong:", error);
    }
});
