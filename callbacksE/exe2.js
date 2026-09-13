const fightersList1= [
    "Jon jones",
    "Alex Pereira",
    "Islam Makhachev",
    "Amanda Nunes",
    "Valentina Shevchenko",
    "Max Holloway"
];
const fightersList2= [
    "Sean Strickland",
    "Amanda Nunes",
    "Alex Pereira",
    "Valentina Shevchenko",
    "Justin Gaethje",
    "Max Holloway"
];
function compareFighters(list1, list2, callback) {
    const repeatedFighters= [];
    for (const name of list1) {
        if (list2.includes(name)) {
            repeatedFighters.push(name);
        }
    }
    callback(repeatedFighters);
}
function showRepeatedFighters(fighters) {
    console.log("Fighters included in both lists:");
    for (const fighter of fighters) {
        console.log(fighter)
    }
}

compareFighters(fightersList1, fightersList2, showRepeatedFighters);
