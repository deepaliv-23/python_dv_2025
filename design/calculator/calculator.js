const a = document.getElementById("valueA");
const b = document.querySelector("#valueB");
console.log("A", a);
console.log("B", b);

let valueA, valueB;

a.addEventListener("keyup", (e) => {
  console.log(e.target.value);
  valueA = Number(e.target.value);
});

b.addEventListener("keyup", (e) => {
  console.log(e.target.value);
  valueB = Number(e.target.value);
});

console.log(valueA);
console.log(valueB);

// Operation buttons:
const additionBtn = document.getElementById("addition");
const subtractionBtn = document.getElementById("subtraction");
const multiplicationBtn = document.getElementById("multiplication");
const divisionBtn = document.getElementById("division");
const cancelBtn = document.getElementById("cancel");

function showResult(opSymbol, result) {
  console.log(`${opSymbol}:`, result);
  document.getElementById("result").textContent = `Result: ${result}`;
}

additionBtn.addEventListener("click", () => {
  showResult("+", valueA + valueB);
});

subtractionBtn.addEventListener("click", () => {
  showResult("-", valueA - valueB);
});

multiplicationBtn.addEventListener("click", () => {
  showResult("*", valueA * valueB);
});

divisionBtn.addEventListener("click", () => {
  if (valueB === 0) {
    showResult("/", "Cannot divide by zero");
  } else {
    showResult("/", valueA / valueB);
  }
});

cancelBtn.addEventListener("click", () => {
  a.value = "";
  b.value = "";
  valueA = valueB = undefined;
  document.getElementById("result").textContent = "Result: —";
  console.log("Cleared values");
});
