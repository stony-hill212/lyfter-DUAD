function removeDuplicates(numbers) {
    const uniqueNumbers= [];
    for (const number of numbers) {
        if (!uniqueNumbers.includes(number)) {
            uniqueNumbers.push(number);
        }
    }
    return uniqueNumbers;
}
const numbers= [4, 2, 7, 4, 2, 9, 7,1];
const result= removeDuplicates(numbers);

console.log(result);
