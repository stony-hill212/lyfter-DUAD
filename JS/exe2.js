const numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const evenNumbers= [];
for (const number of numbers) {
    if (number%2===0) {
        evenNumbers.push(number);
    }
}
console.log(evenNumbers);


const numbers2= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const evenNumbers2= numbers2.filter((number2)=>{return number2%2===0;});

console.log(evenNumbers2);