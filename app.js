
const products = [
    { id: 1, name: "Premium Medjool Dates", desc: "Naturally rich, soft and indulgent.", weight: "250g · 500g · 1kg", price: "₹850", img: "medjool.jpg", category: "dates" },
    { id: 2, name: "Ajwa Dates", desc: "Dark, sweet and traditionally revered.", weight: "250g · 500g · 1kg", price: "₹1200", img: "ajwa.jpg", category: "dates" },
    { id: 3, name: "California Almonds", desc: "Premium crunchy almonds.", weight: "250g · 500g · 1kg", price: "₹450", img: "california_almonds.jpg", category: "nuts" },
    { id: 4, name: "Mamra Almonds", desc: "Rich in oil, supreme quality.", weight: "250g · 500g", price: "₹1800", img: "mamra.jpg", category: "nuts" },
    { id: 5, name: "Premium Cashews W240", desc: "Large, buttery and whole.", weight: "250g · 500g · 1kg", price: "₹650", img: "cashews.jpg", category: "nuts" },
    { id: 6, name: "Roasted Peri-Peri Cashews", desc: "Spicy, crunchy indulgence.", weight: "200g · 400g", price: "₹700", img: "peri_cashews.jpg", category: "roasted" },
    { id: 7, name: "Premium Pistachios", desc: "Salted, roasted and flavourful.", weight: "250g · 500g", price: "₹800", img: "pistachios.jpg", category: "nuts" },
    { id: 8, name: "Walnut Kernels", desc: "Halves, rich in Omega-3.", weight: "250g · 500g", price: "₹750", img: "walnuts.jpg", category: "nuts" },
    { id: 9, name: "Dried Turkish Figs", desc: "Naturally sweet and chewy.", weight: "250g · 500g", price: "₹600", img: "figs.jpg", category: "dry_fruits" },
    { id: 10, name: "Premium Dried Cranberries", desc: "Tart, sweet and perfect for snacking.", weight: "250g · 500g", price: "₹450", img: "cranberries.jpg", category: "dry_fruits" },
    { id: 11, name: "Peri-Peri Makhana", desc: "Roasted fox nuts with a spicy kick.", weight: "100g", price: "₹150", img: "peri_makhana.jpg", category: "makhana" },
    { id: 12, name: "Himalayan Salt Makhana", desc: "Lightly salted everyday crunch.", weight: "100g", price: "₹150", img: "salt_makhana.jpg", category: "makhana" },
    { id: 13, name: "SK TABII Daily Energy Mix", desc: "Curated nuts and fruits for energy.", weight: "250g · 500g", price: "₹550", img: "energy_mix.jpg", category: "mixes" },
    { id: 14, name: "SK TABII Protein Nut Mix", desc: "Almonds, cashews, seeds and more.", weight: "250g · 500g", price: "₹650", img: "protein_mix.jpg", category: "mixes" },
    { id: 15, name: "SK TABII Premium Gift Box", desc: "An elegant assortment of our best.", weight: "Assorted", price: "₹2500", img: "gift_box.jpg", category: "gifting" }
];

function toggleMenu() {
    document.getElementById('mobileNav').classList.toggle('open');
}

function toggleSearch() {
    document.getElementById('searchOverlay').classList.toggle('open');
    if(document.getElementById('searchOverlay').classList.contains('open')) {
        document.getElementById('searchInput').focus();
    }
}

function renderProducts(containerId, limit = null, category = null) {
    const container = document.getElementById(containerId);
    if (!container) return;
    
    let displayProducts = products;
    if (category) {
        displayProducts = products.filter(p => p.category === category);
    }
    if (limit) {
        displayProducts = displayProducts.slice(0, limit);
    }
    
    container.innerHTML = displayProducts.map(p => `
        <div class="product-card">
            <img src="${p.img}" alt="${p.name}" class="product-img" onerror="this.src='https://images.unsplash.com/photo-1596422846543-75c6fc197f0a?auto=format&fit=crop&q=80&w=800';">
            <div class="product-info">
                <h3 class="product-title">${p.name}</h3>
                <p class="product-desc">${p.desc}</p>
                <div class="product-weights">${p.weight}</div>
                <div class="product-bottom">
                    <span class="product-price">${p.price}</span>
                    <button class="btn-add" onclick="addToCart(${p.id})">Add to Cart</button>
                </div>
            </div>
        </div>
    `).join('');
}

let cartCount = 0;
function addToCart(id) {
    cartCount++;
    document.querySelectorAll('.cart-count').forEach(el => el.textContent = cartCount);
    const btn = event.target;
    const originalText = btn.textContent;
    btn.textContent = "Added!";
    btn.style.backgroundColor = "var(--earth-brown)";
    setTimeout(() => {
        btn.textContent = originalText;
        btn.style.backgroundColor = "";
    }, 1500);
}

document.addEventListener('DOMContentLoaded', () => {
    renderProducts('bestsellers-grid', 8);
});

function handleSearch(e) {
    const query = e.target.value.toLowerCase();
    const results = document.getElementById('searchResults');
    if (query.length < 2) {
        results.style.display = 'none';
        return;
    }
    const matches = products.filter(p => p.name.toLowerCase().includes(query) || p.desc.toLowerCase().includes(query));
    if (matches.length === 0) {
        results.innerHTML = '<p>No results found.</p>';
    } else {
        results.innerHTML = matches.map(m => `<div style='display:flex; gap:15px; margin-bottom:15px; align-items:center;'><img src='${m.img}' style='width:50px; height:50px; object-fit:cover; border-radius:4px;' onerror=\"this.src='https://images.unsplash.com/photo-1596422846543-75c6fc197f0a?auto=format&fit=crop&q=80&w=800';\"><a href='product.html?id=${m.id}' style='font-weight:500; color:var(--deep-forest); text-decoration:none;'>${m.name}</a></div>`).join('');
    }
    results.style.display = 'block';
}
