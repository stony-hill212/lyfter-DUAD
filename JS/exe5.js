const student= {
    name: "Jimmy Conway",
    grades: [
        {name: "math", grade: 80},
        {name: "chemistry", grade: 100},
        {name: "history", grade: 60},
        {name: "PE", grade: 90},
        {name: "music", grade: 98}
    ]
};
let total= 0;
for (const subject of student.grades) {total+=subject.grade;}
const gradeAvg= total/student.grades.length;
let highest= student.grades[0];
let lowest= student.grades[0];
for (const subject of student.grades) {
    if (subject.grade > highest.grade) {highest= subject;}
    if (subject.grade < lowest.grade) {lowest=subject;}
}
const result= {
    name: student.name,
    gradeAvg: gradeAvg,
    highestGrade: highest.name,
    lowestGrade: lowest.name
};
console.log(result)