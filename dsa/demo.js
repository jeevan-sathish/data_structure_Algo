// const content = [
//   [{ name: "jeevan" }, { name: "suresh" }],
//   [{ name: "punith" }, { name: "sough" }],
// ];

// const data = content.map((ele) => ele.map((e) => e.name));
// console.log(data);

// const tI = setInterval(() => {
//   console.log("hello");
// }, 1000);

// setTimeout(() => {
//   clearInterval(tI);
// }, 4000);

// let str = "Apple, Banana, Kiwi";
// let part = str.slice(7, 6);
// console.log(part);

// const array = [12, 3, 5, 6, 7, 8, 9];

// for (var k of array) {
//   console.log(k);
// }

// const text = "jeevan";
// const result = text.blink();

// console.log(result);

// class A {
//   constructor(name) {
//     this.name = name;
//   }

//   greet() {
//     console.log(this.name);
//   }
// }
// class B extends A {
//   constructor(age) {
//     super();
//     this.age = age;
//   }
// }

// const b = new B("jeevan");
// console.log(b.age);

const data = [
  {
    name: "jeevan",
    age: 20,
  },
  {
    name: "kiran",
    age: 21,
  },
];
const name = "shahsi";
const result = data.map((ele) =>
  ele.age === 21 ? { ...ele, name: name } : ele,
);
console.log(result);
