// 04.04.2024 - TASK - ASGAR ISMAYILOV
let i = 1;
let direction = true;
btn.addEventListener("click", () => {
  if (i === 1) {
    direction = true;
  }
  if (i === 10) {
    direction = false;
  }

  if (direction) {
    btn.textContent = `Click me ${i++}`;
  } else {
    btn.textContent = `Click me ${i--}`;
  }
});
