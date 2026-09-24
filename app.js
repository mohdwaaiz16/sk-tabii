
const PRODUCTS = [
  {id: 0, name: "Ajwa Dates", cat: "dates", price: 699, typ: "date", desc: "Premium Ajwa dates with a naturally rich, soft texture.", details: ["Naturally sweet profile", "Premium selection", "Ideal for gifting and everyday snacking"], img: "images/prod_0.jpg"},
  {id: 1, name: "Medjool Dates", cat: "dates", price: 849, typ: "date", desc: "Large, soft Medjool dates selected for premium gifting.", details: ["Large fruit size", "Soft, caramel-like texture", "Premium gifting choice"], img: "images/prod_1.jpg"},
  {id: 2, name: "California Almonds", cat: "nuts", price: 599, typ: "nut", desc: "Crunchy, premium almonds for everyday nourishment.", details: ["Whole almonds", "Naturally crunchy", "Everyday pantry staple"], img: "images/prod_2.jpg"},
  {id: 3, name: "Pistachio Kernels", cat: "nuts", price: 799, typ: "pistachio", desc: "Delicate pistachio kernels with a rich roasted profile.", details: ["Premium kernels", "Rich nutty flavour", "Great for snacking and desserts"], img: "images/prod_3.jpg"},
  {id: 4, name: "Premium Cashews", cat: "nuts", price: 649, typ: "nut", desc: "Creamy whole cashews with a naturally buttery finish.", details: ["Whole cashews", "Creamy texture", "Ideal for gifting"], img: "images/prod_4.jpg"},
  {id: 5, name: "Dried Turkish Figs", cat: "dry-fruits", price: 749, typ: "date", desc: "Naturally sweet dried figs with a tender bite.", details: ["Naturally dried", "Tender texture", "Sweet pantry staple"], img: "images/prod_5.jpg"},
  {id: 6, name: "Organic Wild Honey", cat: "organic", price: 499, typ: "honey", desc: "Demo product: raw-style honey inspired by natural sourcing.", details: ["Demo product", "Natural pantry concept", "Perfect with breakfast and beverages"], img: "images/prod_6.jpg"},
  {id: 7, name: "Signature Gift Box", cat: "gifting", price: 1499, typ: "pistachio", desc: "A curated assortment of dates, nuts and dry fruits.", details: ["Curated assortment", "Premium presentation", "Perfect for celebrations"], img: "images/prod_7.jpg"}
];

function cart(){return JSON.parse(localStorage.getItem("skTabiiCart")||"[]")}
function saveCart(c){localStorage.setItem("skTabiiCart",JSON.stringify(c));updateCartCount()}
function updateCartCount(){let n=cart().reduce((s,i)=>s+i.qty,0);document.querySelectorAll(".cart-count").forEach(el=>el.textContent=n)}
function toast(msg){let el=document.getElementById("toast");if(!el)return;el.innerHTML=`<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> ${msg}`;el.classList.add("show");setTimeout(()=>el.classList.remove("show"),3000)}
function addToCart(id){
    let c=cart(),x=c.find(i=>i.id===id);
    if(x) {
        x.qty++;
    } else {
        c.push({id: parseInt(id),qty:1});
    }
    saveCart(c);
    let p = PRODUCTS.find(prod => prod.id == id);
    toast((p ? p.name : 'Item') + " added to your bag.");
}
function removeFromCart(id){saveCart(cart().filter(i=>i.id!==id));renderCart()}
function changeQty(id,d){let c=cart(),x=c.find(i=>i.id===id);if(x){x.qty+=d;if(x.qty<1)c=c.filter(i=>i.id!==id)}saveCart(c);renderCart()}

function renderCart(){
    let el=document.getElementById("cartArea"); 
    if(!el) return; 
    let c=cart();
    
    if(!c.length){
        el.innerHTML=`
        <div style="text-align:center; padding:100px 20px; max-width:500px; margin:0 auto;">
            <h2 class="green">Your basket is empty.</h2>
            <p class="body-large" style="margin:20px auto 40px;">Explore our collection of premium dates, nuts, and natural goodness.</p>
            <a class="btn btn-gold" href="shop.html">Explore Collection</a>
        </div>`;
        return;
    }
    
    let total=0; 
    let rows=c.map(i=>{
        let p=PRODUCTS.find(prod => prod.id === i.id);
        if(!p) return '';
        let line=p.price*i.qty;
        total+=line;
        return `
        <tr>
            <td>
                <div class="cart-item-info">
                    <a href="product.html?id=${p.id}" class="cart-item-img"><img src="${p.img}" alt="${p.name}"></a>
                    <div>
                        <h4 style="margin:0 0 5px; font-family:'Inter',sans-serif; font-size:16px;">${p.name}</h4>
                        <span style="font-size:12px; color:var(--gold-dark); text-transform:uppercase; letter-spacing:0.1em;">${p.cat}</span>
                    </div>
                </div>
            </td>
            <td style="font-size:16px;">₹${p.price.toLocaleString("en-IN")}</td>
            <td>
                <div class="quantity-selector" style="margin:0;">
                    <button onclick="changeQty(${p.id},-1)">−</button>
                    <span>${i.qty}</span>
                    <button onclick="changeQty(${p.id},1)">+</button>
                </div>
            </td>
            <td style="font-weight:600; font-size:16px;">₹${line.toLocaleString("en-IN")}</td>
            <td style="text-align:right;">
                <button class="btn-text" onclick="removeFromCart(${p.id})">Remove</button>
            </td>
        </tr>`;
    }).join("");
    
    el.innerHTML=`
    <div class="cart-layout">
        <div>
            <table class="cart-table">
                <thead><tr><th>Product</th><th>Price</th><th>Quantity</th><th>Total</th><th></th></tr></thead>
                <tbody>${rows}</tbody>
            </table>
        </div>
        <div>
            <div class="cart-summary">
                <h3>Order Summary</h3>
                <div class="summary-row"><span>Subtotal</span><span>₹${total.toLocaleString("en-IN")}</span></div>
                <div class="summary-row"><span>Shipping</span><span>Calculated at checkout</span></div>
                <div class="summary-total"><span>Total</span><span>₹${total.toLocaleString("en-IN")}</span></div>
                <button class="btn btn-gold" style="width:100%" onclick="toast('Checkout is a demo in this version.')">Proceed to Checkout</button>
                <p style="text-align:center; font-size:12px; color:var(--muted); margin-top:20px;">Your basket is filled with goodness.</p>
            </div>
        </div>
    </div>`;
}

function renderProduct(){
    let el=document.getElementById("productDetail");
    if(!el)return;
    let id=Number(new URLSearchParams(location.search).get("id")||0);
    let p=PRODUCTS.find(prod => prod.id === id) || PRODUCTS[0];
    
    el.innerHTML=`
    <div class="product-detail-layout container">
        <div class="detail-gallery">
            <img src="${p.img}" alt="${p.name}">
        </div>
        <div class="detail-info">
            <div class="eyebrow">${p.cat}</div>
            <h1>${p.name}</h1>
            <div style="margin-bottom:20px; display:flex; gap:5px; color:var(--gold);">
                ★ ★ ★ ★ ★ <span style="color:var(--muted); font-size:14px; margin-left:10px;">(Demo Reviews)</span>
            </div>
            <span class="detail-price">₹${p.price.toLocaleString("en-IN")}</span>
            <p class="detail-desc">${p.desc}</p>
            
            <div class="add-to-cart-wrap">
                <div class="quantity-selector">
                    <button onclick="let span=this.nextElementSibling; span.textContent=Math.max(1,Number(span.textContent)-1)">−</button>
                    <span id="pQty">1</span>
                    <button onclick="let span=this.previousElementSibling; span.textContent=Number(span.textContent)+1">+</button>
                </div>
                <button class="btn btn-gold" style="flex:1;" onclick="addMultipleToCart(${p.id})">Add to Cart</button>
            </div>
            
            <button class="btn-text" onclick="toast('Added to Wishlist')" style="margin-bottom:40px;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right:8px; vertical-align:middle;"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg> Add to Wishlist
            </button>
            
            <div class="accordion">
                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        Product Information <span>+</span>
                    </div>
                    <div class="accordion-body" style="display:block;">
                        <ul>${p.details.map(x=>`<li style="margin-bottom:8px">${x}</li>`).join("")}</ul>
                    </div>
                </div>
                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        Storage & Shipping <span>+</span>
                    </div>
                    <div class="accordion-body">
                        Store in a cool, dry place. Premium packaging ensures freshness. Shipping calculated at checkout.
                    </div>
                </div>
                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        TABII Quality <span>+</span>
                    </div>
                    <div class="accordion-body">
                        Carefully sourced for maximum natural goodness. No artificial preservatives. Pure luxury from nature.
                    </div>
                </div>
            </div>
        </div>
    </div>`;
}

function addMultipleToCart(id) {
    let qty = parseInt(document.getElementById('pQty').innerText);
    let c = cart();
    let x = c.find(i => i.id === id);
    if(x) {
        x.qty += qty;
    } else {
        c.push({id: id, qty: qty});
    }
    saveCart(c);
    let p = PRODUCTS.find(prod => prod.id == id);
    toast(`${qty} x ${p ? p.name : 'Item'} added to your bag.`);
}

function toggleAccordion(el) {
    let body = el.nextElementSibling;
    let icon = el.querySelector('span');
    if (body.style.display === 'block') {
        body.style.display = 'none';
        icon.textContent = '+';
    } else {
        body.style.display = 'block';
        icon.textContent = '−';
    }
}

function renderShopProducts(filter = 'all') {
    let grid = document.getElementById("productGrid");
    if (!grid) return;
    
    let filtered = filter === 'all' ? PRODUCTS : PRODUCTS.filter(p => p.cat === filter);
    
    if (filtered.length === 0) {
        grid.innerHTML = '<p style="grid-column: 1/-1; text-align:center; padding: 40px;">No products found in this category.</p>';
        return;
    }
    
    grid.innerHTML = filtered.map(p => `
    <div class="product-card" data-cat="${p.cat}" data-name="${p.name.toLowerCase()}">
        <div class="product-badge">${p.cat.replace('-', ' ')}</div>
        <a href="product.html?id=${p.id}" class="product-img-wrap">
            <img src="${p.img}" alt="${p.name}">
        </a>
        <div class="product-info">
            <h3><a href="product.html?id=${p.id}">${p.name}</a></h3>
            <p class="desc">${p.desc}</p>
            <div class="product-meta">
                <span class="product-price">₹${p.price.toLocaleString("en-IN")}</span>
                <div class="product-actions">
                    <button class="icon-btn-small" onclick="toast('Added to Wishlist')" aria-label="Wishlist">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                    </button>
                    <button class="icon-btn-small" onclick="addToCart(${p.id})" aria-label="Add to Cart">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 8h12l1 13H5L6 8Zm3 0V6a3 3 0 0 1 6 0v2"></path></svg>
                    </button>
                </div>
            </div>
        </div>
    </div>`).join("");
}

function filterProducts(cat, btn) {
    document.querySelectorAll(".filter-list button").forEach(x => x.classList.remove("active"));
    if (btn) btn.classList.add("active");
    renderShopProducts(cat);
}

function subscribe(e){e.preventDefault();toast("Welcome to the TABII Journal.");e.target.reset()}
function contactSubmit(e){e.preventDefault();toast("Thank you. We will be in touch shortly.");e.target.reset()}

function toggleMenu(){
    let x=document.getElementById("mobileNav");
    if(x.style.display==="block") {
        x.style.display="none";
    } else {
        x.style.display="block";
    }
}

function toggleSearch(){
    let x=document.getElementById("searchBar");
    if(x.style.display==="flex") {
        x.style.display="none";
    } else {
        x.style.display="flex";
        document.getElementById("siteSearch").focus();
    }
}

function globalSearch(e) {
    if (e.key === 'Enter') {
        let q = e.target.value.toLowerCase();
        location.href = "shop.html" + (q ? "?q=" + encodeURIComponent(q) : "");
    }
}

document.addEventListener("DOMContentLoaded", () => {
    updateCartCount();
    renderCart();
    renderProduct();
    
    if(document.getElementById("productGrid")) {
        renderShopProducts();
    }
    
    let params=new URLSearchParams(location.search),q=params.get("q"),cat=params.get("cat");
    
    if(q && document.getElementById("productGrid")){
        document.getElementById("productGrid").innerHTML = PRODUCTS.filter(p => p.name.toLowerCase().includes(q) || p.desc.toLowerCase().includes(q)).map(p => `
        <div class="product-card" data-cat="${p.cat}">
            <a href="product.html?id=${p.id}" class="product-img-wrap"><img src="${p.img}" alt="${p.name}"></a>
            <div class="product-info">
                <h3><a href="product.html?id=${p.id}">${p.name}</a></h3>
                <div class="product-meta">
                    <span class="product-price">₹${p.price.toLocaleString("en-IN")}</span>
                    <button class="icon-btn-small" onclick="addToCart(${p.id})"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 8h12l1 13H5L6 8Zm3 0V6a3 3 0 0 1 6 0v2"></path></svg></button>
                </div>
            </div>
        </div>`).join("");
    } else if(cat && document.getElementById("productGrid")){
        let btn = [...document.querySelectorAll(".filter-list button")].find(x => x.dataset.filter === cat);
        filterProducts(cat, btn);
    }
});
