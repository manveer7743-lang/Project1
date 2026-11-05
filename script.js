"use strict";

const targets = { 3: 495, 4: 6174 };

const form = document.querySelector("#calculator-form");
const numberInput = document.querySelector("#number-input");
const calculateButton = document.querySelector("#calculate-button");
const clearButton = document.querySelector("#clear-button");
const errorMessage = document.querySelector("#error-message");
const results = document.querySelector("#results");
const stepsList = document.querySelector("#steps-list");
const iterationCount = document.querySelector("#iteration-count");

function validate(value) {
  const x = value.trim();
  if (!/^\d+$/.test(x)) {
    return "Please enter numbers only.";
  }
  if (!(x.length in targets)) {
    return "Please enter a 3 or 4 digit number.";
  }
  if (new Set(x).size === 1) {
    return "All digits can't be the same. Please enter a valid number.";
  }
  return null;
}

function kaprekar(value) {
  const x = value.trim();
  const size = x.length;
  const target = targets[size];
  const steps = [];
  let current = x;
  let diff = 0;

  while (diff !== target) {
    const digits = [...current].sort();
    const number1 = Number(digits.join(""));
    const number2 = Number([...digits].reverse().join(""));
    diff = number2 - number1;
    steps.push(`${number2} - ${number1} = ${diff}`);
    current = String(diff).padStart(size, "0");
  }

  return { steps, iterations: steps.length };
}

function clearResults() {
  stepsList.replaceChildren();
  iterationCount.textContent = "";
  results.hidden = true;
}

function updateCalculateButton() {
  calculateButton.disabled = numberInput.value.trim() === "";
}

numberInput.addEventListener("input", updateCalculateButton);

clearButton.addEventListener("click", () => {
  numberInput.value = "";
  errorMessage.textContent = "";
  clearResults();
  updateCalculateButton();
  numberInput.focus();
});

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const error = validate(numberInput.value);
  if (error !== null) {
    errorMessage.textContent = error;
    clearResults();
    return;
  }

  const { steps, iterations } = kaprekar(numberInput.value);
  errorMessage.textContent = "";
  stepsList.replaceChildren(
    ...steps.map((step, index) => {
      const item = document.createElement("li");
      item.textContent = step;
      item.style.setProperty("--step-index", index);
      if (index === steps.length - 1) {
        item.classList.add("final-step");
      }
      return item;
    }),
  );
  iterationCount.textContent = `Iterations: ${iterations}`;
  results.hidden = false;
});

updateCalculateButton();
