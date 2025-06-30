// Elements
const counterBtn = document.getElementById('counterBtn');
const display = document.getElementById('countDisplay');
let count = 0;

// Handler #1: update visible counter
counterBtn.addEventListener('click', function() {
  count++;
  display.textContent = count;
});

// Handler #2: log event details
counterBtn.addEventListener('click', function(event) {
  console.log(`Event type: ${event.type}`);
  console.log(`Timestamp: ${event.timeStamp}`);
  console.log(`this.tagName: ${this.tagName}`);
});