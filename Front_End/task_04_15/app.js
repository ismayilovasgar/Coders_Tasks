//* api_key = f0f9d8def5-10857e525d-sbzmf0
const from_unit = document.getElementById("from_unit");
const to_unit = document.getElementById("to_unit");
const input_amount = document.getElementById("input_amount");
const result_amount = document.getElementById("result_amount");
const convert_btn = document.getElementById("convert_btn");

const from_select = document.createElement("select");
const to_select = document.createElement("select");
from_select.id = "from_unit";
from_select.id = "to_unit";

let all_money_unit = [];
let all_money_statement = [];

//**************
const get_all_unit = async () => {
  const response = await fetch(
    "https://api.fastforex.io/currencies?api_key=f0f9d8def5-10857e525d-sbzmf0"
  );
  const data = await response.json();
  for (const index in data.currencies) {
    all_money_unit.push(index);
    all_money_statement.push(data.currencies[index]);
  }
  for (let i = 0; i < all_money_statement.length; i++) {
    const from_option = document.createElement("option");
    const to_option = document.createElement("option");
    from_option.value = all_money_unit[i];
    to_option.value = all_money_unit[i];
    from_option.text = `${all_money_unit[i]}  \u00A0\u00A0\u00A0   ${all_money_statement[i]}`;
    to_option.text = `${all_money_unit[i]}    \u00A0\u00A0\u00A0   ${all_money_statement[i]}`;
    from_select.add(from_option);
    to_select.add(to_option);
    from_p.append(from_select);
    to_p.append(to_select);
  }
};
get_all_unit();

//********
const money_convert = async (e) => {
  let amount = input_amount.value.trim();

  if (amount === "" || amount === undefined || amount === null) {
    alert("Pul Vahidi secilmeyib");
    return;
  }
  fetch(
    `https://api.fastforex.io/convert?api_key=f0f9d8def5-10857e525d-sbzmf0&from=${from_select.value}&to=${to_select.value}&amount=${amount}`
  )
    .then((res) => res.json())
    .then((data) => {
      result_amount.value = data.result[`${to_select.value}`].toFixed(3);
    });
};

convert_btn.addEventListener("click", money_convert);
