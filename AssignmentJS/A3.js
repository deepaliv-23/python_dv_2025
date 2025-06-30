// Select all buttons once
const buttons = document.querySelectorAll('button');

// Assignment 3: Compare arrow-function vs normal-function `this`
buttons.forEach((btn, idx) => {
  btn.addEventListener('click', () => {
    console.log('Arrow-function listener `this` =', this);
  });

  btn.addEventListener('click', function() {
    console.log('Normal-function listener `this` =', this);
  });
});