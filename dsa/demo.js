const content = [
  [{ name: "jeevan" }, { name: "suresh" }],
  [{ name: "punith" }, { name: "sough" }],
];

const data = content.map((ele) => ele.map((e) => e.name));
console.log(data);
