// Task - 26.03.2024
// 1. Daxil olunan ədədin sadə yoxsa mürəkkəb olduğunu tapın.
let eded_1 = +prompt("1-) Bir eded daxil edin:");
let bolen_sayi_1 = 0;
if (eded_1 === 1) {
  console.log(` ${eded_1} ededi ne sade nede murekkeb ededdir`);
} else if (eded_1 > 1) {
  for (let bolen = 1; bolen <= eded_1; bolen++) {
    if (eded_1 % bolen === 0) {
      bolen_sayi_1++;
    }
  }
  if (bolen_sayi_1 == 2) {
    console.log(`${eded_1} ededi sade ededir`);
  } else {
    console.log(`${eded_1} ededi murekkeb ededir`);
  }
} else {
  console.log(`${eded_1}, 0-dan boyuk eded daxil edin `);
}

// 2. Daxil olunan ədədin mükəmməl olub olmadığını tapın.
let eded_2 = +prompt("2-) Bir eded daxil edin :");
let cem_2 = 0;
for (let bolen = 1; bolen < eded_2; bolen++) {
  if (eded_2 % bolen === 0) {
    cem_2 += bolen;
  }
}
if (eded_2 === cem_2) {
  console.log(`${eded_2} mukemmel ededdir`);
} else {
  console.log(`${eded_2} mukemmel eded deyil`);
}

// 3. Daxil olunan 2 ədəd arasındakı mükəmməl ədədləri göstərin.
let min_number = +prompt("3-) 1-ci ededi daxil edin :");
let max_number = +prompt("3-) 2-ci ededi daxil edin :");
let sum = 0;
console.log(`${min_number} ve ${max_number} arasi mukemmel ededler: `);
for (let i = min_number + 1; i < max_number; i++) {
  sum = 0;
  for (let bolen = 1; bolen < i; bolen++) {
    if (i % bolen === 0) {
      sum += bolen;
    }
  }
  if (i === sum) {
    console.log(`${i} - mukemmel`);
  }
}

// 4. Daxil olunan 2 ədəd arasındakı sadə ədədləri göstərin.
let min_num = +prompt("4-) 1-ci ededi daxil edin :");
let max_num = +prompt("4-) 2-ci ededi daxil edin :");
let bolen_sayi_4 = 0;
console.log(`${min_num} ve ${max_num} arasi sade ededler: `);
for (let i = min_num + 1; i < max_num; i++) {
  bolen_sayi_4 = 0;
  for (let bolen = 1; bolen <= i; bolen++) {
    if (i % bolen === 0) {
      bolen_sayi_4++;
    }
  }
  if (bolen_sayi_4 == 2) {
    console.log(`${i} -eded sadedi`);
  }
}

//  5. Daxil olunan 2 ədəd arasındakı sonu 7 ilə bitən ədədləri göstərin.
let min_numb = +prompt("5-) 1-ci ededi daxil edin :");
let max_numb = +prompt("5-) 2-ci ededi daxil edin :");

console.log(`${min_numb} ve ${max_numb} arasi 7-le biten ededler: `);
for (let i = min_numb; i < max_numb; i++) {
  if (i % 10 === 7) {
    console.log(` ${i} `);
  }
}
