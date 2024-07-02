// Task - 25.03.2024
let txt=prompt("1-) bir soz daxil edin:");
let txt_simvol = prompt("bir simvol daxil edin");

// 1.İstifadəçinin daxil etdiyi adın neçə simvoldan ibarət olduğunu tapın.
console.log("length:",txt.length);

// 2.İstifadəçinin daxil etdiyi 1 ci sözdə daxil etdiyi 2 ci simvol varmı ?.
console.log(txt.includes(txt_simvol));

// 3.İstifadəçinin daxil etdiyi 1 ci söz daxil etdiyi 2 ci simvolla başlayırmı ?.
console.log(txt.startsWith(txt_simvol));

// 4.İstifadəçinin daxil etdiyi 1 ci söz daxil etdiyi 2 ci simvolla bitirmi ?.
console.log(txt.endsWith(txt_simvol));

// 5.İstifadəçinin daxil etdiyi 1 ci sözdə daxil etdiyi 2 ci simvolun index`ini tapın.
console.log(txt.indexOf(txt_simvol));

// 6.İstifadəçinin daxil etdiyi sözün böyük hərf olub olmadığını tapın.
console.log(txt.includes(txt.toUpperCase()));

