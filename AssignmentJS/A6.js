// Task 1: Countdown from 10 to 0, decrementing every second
let count = 10;
const timerEl = document.getElementById('timer');

const countdown = setInterval(() => {
  timerEl.textContent = --count;
  if (count <= 0) {
    clearInterval(countdown);
  }
}, 1000);

// Task 2: Show greeting after a 3‑second delay
const greetingEl = document.getElementById('greeting');

setTimeout(() => {
  greetingEl.textContent = 'Hello! The countdown has started.';
}, 3000);
