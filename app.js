
const PRODUCTS = [
  {name:"Ajwa Dates",cat:"Dates",price:699,typ:"date",desc:"Premium Ajwa dates with a naturally rich, soft texture.",details:["Naturally sweet profile","Premium selection","Ideal for gifting and everyday snacking"]},
  {name:"Medjool Dates",cat:"Dates",price:849,typ:"date",desc:"Large, soft Medjool dates selected for premium gifting.",details:["Large fruit size","Soft, caramel-like texture","Premium gifting choice"]},
  {name:"California Almonds",cat:"Nuts",price:599,typ:"nut",desc:"Crunchy, premium almonds for everyday nourishment.",details:["Whole almonds","Naturally crunchy","Everyday pantry staple"]},
  {name:"Pistachio Kernels",cat:"Nuts",price:799,typ:"pistachio",desc:"Delicate pistachio kernels with a rich roasted profile.",details:["Premium kernels","Rich nutty flavour","Great for snacking and desserts"]},
  {name:"Premium Cashews",cat:"Nuts",price:649,typ:"nut",desc:"Creamy whole cashews with a naturally buttery finish.",details:["Whole cashews","Creamy texture","Ideal for gifting"]},
  {name:"Dried Turkish Figs",cat:"Dry Fruits",price:749,typ:"date",desc:"Naturally sweet dried figs with a tender bite.",details:["Naturally dried","Tender texture","Sweet pantry staple"]},
  {name:"Organic Wild Honey",cat:"Organic",price:499,typ:"honey",desc:"Demo product: raw-style honey inspired by natural sourcing.",details:["Demo product","Natural pantry concept","Perfect with breakfast and beverages"]},
  {name:"Signature Gift Box",cat:"Gifting",price:1499,typ:"pistachio",desc:"A curated assortment of dates, nuts and dry fruits.",details:["Curated assortment","Premium presentation","Perfect for celebrations"]}
];

function cart(){return JSON.parse(localStorage.getItem("skTabiiCart")||"[]")}
function saveCart(c){localStorage.setItem("skTabiiCart",JSON.stringify(c));updateCartCount()}
function updateCartCount(){let n=cart().reduce((s,i)=>s+i.qty,0);let el=document.getElementById("cartCount");if(el)el.textContent=n}
function toast(msg){let el=document.getElementById("toast");if(!el)return;el.textContent=msg;el.classList.add("show");setTimeout(()=>el.classList.remove("show"),2200)}
function addToCart(id){let c=cart(),x=c.find(i=>i.id===id);x?x.qty++:c.push({id,qty:1});saveCart(c);toast(PRODUCTS[id].name+" added to your bag.")}
function removeFromCart(id){saveCart(cart().filter(i=>i.id!==id));renderCart()}
function changeQty(id,d){let c=cart(),x=c.find(i=>i.id===id);if(x){x.qty+=d;if(x.qty<1)c=c.filter(i=>i.id!==id)}saveCart(c);renderCart()}
function renderCart(){
 let el=document.getElementById("cartArea"); if(!el)return; let c=cart();
 if(!c.length){el.innerHTML='<div class="panel" style="text-align:center;padding:70px"><div class="eyebrow" style="color:var(--green-700)">Your bag is empty</div><h2>Ready when you are.</h2><p style="color:var(--muted)">Explore the demo collection and add a few favourites.</p><a class="btn btn-gold" href="shop.html">Shop the collection</a></div>';return}
 let total=0; let rows=c.map(i=>{let p=PRODUCTS[i.id],line=p.price*i.qty;total+=line;return `<tr><td><b>${p.name}</b><br><small>${p.cat}</small></td><td>₹${p.price.toLocaleString("en-IN")}</td><td><button class="mini-btn" onclick="changeQty(${i.id},-1)">−</button> ${i.qty} <button class="mini-btn" onclick="changeQty(${i.id},1)">+</button></td><td>₹${line.toLocaleString("en-IN")}</td><td><button class="mini-btn" onclick="removeFromCart(${i.id})">Remove</button></td></tr>`}).join("");
 el.innerHTML=`<div style="overflow:auto"><table class="cart-table"><thead><tr><th>Product</th><th>Price</th><th>Qty</th><th>Total</th><th></th></tr></thead><tbody>${rows}</tbody></table></div><div class="cart-summary"><div class="sum-row"><span>Subtotal</span><b>₹${total.toLocaleString("en-IN")}</b></div><div class="sum-row"><span>Shipping</span><span>Calculated at checkout</span></div><div class="sum-row sum-total"><span>Demo total</span><span>₹${total.toLocaleString("en-IN")}</span></div><button class="btn btn-gold" style="width:100%;margin-top:14px" onclick="toast('Checkout is a demo in this version.')">Proceed to checkout</button></div>`;
}
function renderProduct(){
 let el=document.getElementById("productDetail");if(!el)return;let id=Number(new URLSearchParams(location.search).get("id")||0),p=PRODUCTS[id]||PRODUCTS[0];
 el.innerHTML=`<div class="product-detail"><div class="detail-image"><div class="detail-art ${p.typ}"></div></div><div class="detail-copy"><div class="eyebrow" style="color:var(--green-700)">${p.cat}</div><h1>${p.name}</h1><p class="price">₹${p.price.toLocaleString("en-IN")}</p><p style="color:var(--muted);font-size:17px">${p.desc}</p><div class="qty"><button onclick="this.nextElementSibling.textContent=Math.max(1,Number(this.nextElementSibling.textContent)-1)">−</button><strong>1</strong><button onclick="this.previousElementSibling.textContent=Number(this.previousElementSibling.textContent)+1">+</button></div><button class="btn btn-gold" onclick="addToCart(${id})">Add to bag</button><div style="margin-top:35px"><h3>Product notes</h3><ul>${p.details.map(x=>`<li>${x}</li>`).join("")}</ul></div></div></div>`;
}
function filterProducts(cat,btn){document.querySelectorAll(".filter").forEach(x=>x.classList.remove("active"));btn.classList.add("active");document.querySelectorAll("#productGrid .product").forEach(p=>{p.style.display=cat==="all"||p.dataset.cat===cat?"":"none"})}
function subscribe(e){e.preventDefault();toast("You're on the SK TABII demo list.");e.target.reset()}
function contactSubmit(e){e.preventDefault();toast("Thanks — demo enquiry received.");e.target.reset()}
function toggleMenu(){let x=document.getElementById("mobileNav");x.style.display=x.style.display==="none"?"block":"none"}
function toggleSearch(){let x=document.getElementById("searchBar");x.style.display=x.style.display==="none"?"block":"none";if(x.style.display==="block")document.getElementById("siteSearch").focus()}
function globalSearch(q){q=q.toLowerCase();location.href="shop.html"+(q?"?q="+encodeURIComponent(q):"")}
document.addEventListener("DOMContentLoaded",()=>{updateCartCount();renderCart();renderProduct();let params=new URLSearchParams(location.search),q=params.get("q"),cat=params.get("cat");if(q){let input=document.getElementById("siteSearch");if(input)input.value=q;document.querySelectorAll("#productGrid .product").forEach(p=>p.style.display=p.dataset.name.includes(q.toLowerCase())?"":"none")}if(cat){let b=[...document.querySelectorAll(".filter")].find(x=>x.textContent.toLowerCase().replace(" ","-")===cat);if(b)filterProducts(cat,b)}});
