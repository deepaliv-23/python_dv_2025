let products = [];
let cart = [];

const productContainer = document.getElementById('product-container');
const searchInput = document.getElementById('search');
const categoryFilter = document.getElementById('category-filter');
const cartCount = document.getElementById('cart-count');
const totalPrice = document.getElementById('total-price');

fetch('https://dummyjson.com/products')
  .then(res => res.json())
  .then(data => {
    products = data.products;
    displayProducts(products);
  })
  .catch(err => console.error('Fetch error:', err));

function displayProducts(items) {
  productContainer.innerHTML = '';
  items.forEach(product => {
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = `
      <img src="${product.thumbnail}" alt="${product.title}" />
      <h3>${product.title}</h3>
      <p>$${product.price}</p>
      <button>Add to Cart</button>
    `;
    card.querySelector('button').addEventListener('click', () => addToCart(product));
    productContainer.appendChild(card);
  });
}

function addToCart(product) {
  cart = [...cart, product]; // using map-like immutability
  cartCount.textContent = cart.length;
  const total = cart.reduce((sum, p) => sum + p.price, 0);
  totalPrice.textContent = total.toFixed(2);
}

searchInput.addEventListener('input', () => {
  const term = searchInput.value.toLowerCase().trim();
  const filtered = products.filter(p => p.title.toLowerCase().includes(term));
  const byCategory = categoryFilter.value !== 'all'
    ? filtered.filter(p => p.category === categoryFilter.value)
    : filtered;
  displayProducts(byCategory);
});

categoryFilter.addEventListener('change', () => {
  const cat = categoryFilter.value;
  const filtered = cat === 'all'
    ? products
    : products.filter(p => p.category === cat);
  const term = searchInput.value.toLowerCase().trim();
  const final = term
    ? filtered.filter(p => p.title.toLowerCase().includes(term))
    : filtered;
  displayProducts(final);
});
