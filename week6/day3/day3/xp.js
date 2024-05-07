
//ex1
//1lat will represent 49.2827, and lng -123.1207

//ex2
function displayStudentInfo({first,last}){
return `Your full name is ${first} ${last}`
}
console.log(displayStudentInfo({first:'Elie',last:'Schoppik'}))
// function displayStudentInfo({ first, last }) {
//     console.log(first, last);
//     return `Your full name is ${first} ${last}`;
// }

// console.log(displayStudentInfo({ first: 'Elie', last: 'Schoppik' }));


//ex3
const users = { user1: 18273, user2: 92833, user3: 90315 }
const userArr =Object.entries(users)
console.log(userArr);
let multiply = userArr.map((cv)=> cv[1]*2)
console.log(multiply)
    

//ex4
//object

//ex5
//the second 

//ex6
/**
 * obj2 = 4
 * obj3 = 4
 * obj4 = 5
 *  */ 

class Animal {
 constructor(name,type,color){
    this.name = name
    this.type = type
    this.color = color
 }
}

class Mammal extends Animal {
    constructor(name,type,color){
        super(name,type,color,)
        
    }
      sound(sound){
        return `I'm a ${this.type}, named ${this.name} and T'm ${this.color}.${sound}`
}
}
const farmerCow = new Mammal('Lily','cow','brown and white')
console.log((farmerCow.sound('Moooo')));
