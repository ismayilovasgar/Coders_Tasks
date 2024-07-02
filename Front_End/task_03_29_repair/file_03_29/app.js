// Taskiniz:
//* 1. Obyekt yaradin.
//* 2. Array icinde coxlu obyektler yaradin
//* 3. Telebeler obyektinde bir nece telebe elave edin. Hobbileri, xususiyettleri kimi icerisindede deyerleri qeyd edin.
//* 4. Students arrayinin qiymet ortalamasini cixardin. (Butun telebelerin qiymetlerini alib sayini bolun.)
//* 5. Qiymeti 90-dan az olan telebeleri Ad ve Soyadi ile birlikde ekrana cixardib onlara xeberdarliq edin.

let students = [
  {
    id: 1,
    name: "veli",
    surname: "eliyev",
    age: 26,
    skill_id: 3,
    address_id: 70,
    grade: 80,
    hobby: "chess",
  },
  {
    id: 2,
    name: "nicat",
    surname: "hesenli",
    age: 26,
    skill_id: 1,
    address_id: 50,
    grade: 94,
    hobby: "swimming",
  },
  {
    id: 3,
    name: "zaur",
    surname: "memmedov",
    age: 26,
    skill_id: 4,
    address_id: 70,
    grade: 70,
    hobby: "football",
  },
  {
    id: 4,
    name: "cosqun",
    surname: "kazimov",
    age: 26,
    skill_id: 2,
    address_id: 90,
    grade: 93,
    hobby: "basketball",
  },
];

//- 4
function sinif_ortalamasi() {
  let cemi = 0;
  students.map((student) => (cemi += student.grade));
  let ortalama = cemi / students.length;
  console.log(`Telebelerin Ortalamasi: ${ortalama.toFixed(2)}`);
}
sinif_ortalamasi();

//- 5
function asagi_neticeler() {
  let cumle = [];
  students
    .filter((student) => student.grade < 90)
    .map((el) => {
      cumle.push(` ${el.name} ${el.surname}`);
    });
  alert("xeberdarliq:" + cumle);
}

asagi_neticeler();
