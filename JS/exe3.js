const celsius= [0, 10, 20, 30, 40];
const fahrenheit= celsius.map((temperature)=>{
    return (temperature * 9/5)+32;
});
console.log(fahrenheit);