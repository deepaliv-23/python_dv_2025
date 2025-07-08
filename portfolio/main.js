// main.js

// Animate donut charts on page load
document.querySelectorAll('.circle').forEach(circle => {
  const percent = circle.style.getPropertyValue('--percent').trim();

  // Apply initial grey background
  circle.style.background = 'conic-gradient(#eee 0%, #eee 100%)';
  circle.style.transition = 'background 0.8s ease';

  // Slight delay to trigger animation
  setTimeout(() => {
    circle.style.background = `conic-gradient(#0563bb ${percent}%, #e0e0e0 ${percent}%)`;
  }, 50);
});

// Handle theme (color) toggle via moon icon
const btn = document.getElementById('theme-toggle');

btn.addEventListener('click', () => {
  const dark = document.body.classList.toggle('dark');
  btn.textContent = dark ? '☀️' : '🌙';

  const fillColor = dark ? 'dark blue' : '#291666';

  document.querySelectorAll('.circle').forEach(circle => {
    const percent = circle.style.getPropertyValue('--percent').trim();
    circle.style.background = `conic-gradient(${fillColor} ${percent}%, #e0e0e0 ${percent}%)`;
  });
});
