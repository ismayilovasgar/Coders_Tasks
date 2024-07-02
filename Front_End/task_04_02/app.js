// 1. mehsullarin ucuzdan bahaya siralanmasi

let products = [
  {
    id: 1,
    name: "Iphone 14 Pro",
    price: 900,
  },
  {
    id: 2,
    name: "BMW",
    price: 20000,
  },
  {
    id: 3,
    name: "Samsung A70",
    price: 600,
  },
  {
    id: 4,
    name: "Iphone 15 Pro Max", // iphone 15 pro max
    price: 1500,
  },
];

let arr1 = [];
products
  .sort((a, b) => a.price - b.price)
  .map((el) => arr1.push(`${el.name} ${el.price} AZN`));
console.log(arr1.join(", ") + ".");

// 2. Beş random eded yaradib arraya yigin, sonda ise onlarin cemini gosterin
let arr2 = [];
let sum = 0;
for (let i = 0; i < 5; i++) {
  arr2.push(Math.floor(Math.random() * 100));
}
arr2.map((el) => (sum += el));
console.log(arr2);
console.log(`${arr2.join(" + ")} => CEMi: ${sum}`);
