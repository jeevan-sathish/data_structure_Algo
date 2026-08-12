// const array: number[] = [10, 2, 3, 4, 5];

// for (let i: number = 0; i < array.length; i++) {
//   console.log(array[i]);
// }

// type User = {
//   name: string;
//   age: number;
// };
// const user: User = {
//   name: "jeevan",
//   age: 20,
// };
// user.name = "sathish";

// console.log(Object.values(user));

// const User1: User = {
//   name: "prajwal",
//   age: 20,
// };

// console.log(User1.name);
type Adress = {
  city: string;
};

type User = {
  name: string;
  age: number;
  adress: Adress;
};

const info: User = {
  name: "jeevan",
  age: 20,
  adress: {
    city: "mysore",
  },
};
info.adress.city = "mandya";
console.log(info);
export {};
