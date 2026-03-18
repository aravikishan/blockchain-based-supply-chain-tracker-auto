// JavaScript for Navigation Interactions
const navLinks = document.querySelectorAll('nav a');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navLinks.forEach(link => link.classList.remove('active'));
        link.classList.add('active');
    });
});

// Smooth Scrolling
const smoothScroll = (target) => {
    document.querySelector(target).scrollIntoView({
        behavior: 'smooth'
    });
};

navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        smoothScroll(e.target.getAttribute('href'));
    });
});

// Form Validation
const forms = document.querySelectorAll('form');
forms.forEach(form => {
    form.addEventListener('submit', (e) => {
        const inputs = form.querySelectorAll('.form-control');
        inputs.forEach(input => {
            if (!input.value) {
                e.preventDefault();
                input.classList.add('is-invalid');
            } else {
                input.classList.remove('is-invalid');
            }
        });
    });
});

// Dynamic Content Loading
async function loadProducts() {
    const response = await fetch('/api/products');
    const products = await response.json();
    const productsContainer = document.querySelector('#products-container');
    productsContainer.innerHTML = products.map(product => `
        <div class="card">
            <h2>${product.name}</h2>
            <p>Status: ${product.status}</p>
        </div>
    `).join('');
}

document.addEventListener('DOMContentLoaded', loadProducts);
