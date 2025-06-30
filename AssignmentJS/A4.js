// Helper to flash background green briefly
function flashGreen(el) {
  el.classList.add('flash');
  const original = el.style.backgroundColor;
  el.style.backgroundColor = 'lightgreen';
  setTimeout(() => {
    el.style.backgroundColor = original;
    el.classList.remove('flash');
  }, 200);
}

// 1️⃣ Inline onclick handler in HTML
function inlineClick(el) {
  console.log('Inline onclick: clicked', el.id);
  flashGreen(el);
}

// 2️⃣ Using element.onclick in JS
const w2 = document.getElementById('way2');
w2.onclick = function() {
  console.log('element.onclick: clicked', this.id);
  flashGreen(this);
};

// 3️⃣ Using addEventListener
const w3 = document.getElementById('way3');
w3.addEventListener('click', function() {
  console.log('addEventListener: clicked', this.id);
  flashGreen(this);
});