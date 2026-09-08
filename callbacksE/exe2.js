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
    for (let i=0; i< list1.length; i++) {
        if (list2.includes(list1[i])) {
            repeatedFighters.push(list1[i]);
        }
    }
    callback(repeatedFighters);
}
function showRepeatedFighters(fighters) {
    console.log("Fighters included in both lists:");
    for (let i=0; i<fighters.length; i++) {
        console.log(fighters[i]);
    }
}

compareFighters(fightersList1, fightersList2, showRepeatedFighters);