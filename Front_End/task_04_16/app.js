const centerBtn = document.createElement("button");
centerBtn.id = "centerBtn";
centerBtn.textContent = "Add Button";
document.body.append(centerBtn);

const section_message = document.createElement("div");
section_message.className = "section_message";
document.body.append(section_message);

//* Array
const message_content = [
  "message - 1",
  "message - 2",
  "message - 3",
  "message - 4",
];
const message_type = ["warning", "info", "error"];

const addButton = (e) => {
  const item = document.createElement("div");
  item.classList.add("message_items");
  item.classList.add(message_type[Math.floor(Math.random() * 3)]);
  item.textContent = message_content[Math.floor(Math.random() * 4)];

  console.log(item.className);
  section_message.append(item);

  setTimeout(() => {
    item.remove();
  }, 1500);
};

centerBtn.addEventListener("click", addButton);
