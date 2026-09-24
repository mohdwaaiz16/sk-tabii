import os

DIR = "/Users/pmmohammedwaaiz/Desktop/MW-ZAWION-DATA/sk_tabii"

style_css = """
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap');

:root {
  --green-950: #0B2418;
  --green-900: #123D27;
  --green-800: #1D3B28;
  --gold: #C8A45D;
  --gold-dark: #9B783B;
  --cream: #F5EBDD;
  --ivory: #FBF8F1;
  --ink: #171A17;
  --white: #ffffff;
  --line: rgba(200, 164, 93, 0.4);
  --shadow: 0 20px 60px rgba(11, 36, 24, 0.1);
  --shadow-sm: 0 5px 15px rgba(11, 36, 24, 0.05);
  --radius: 4px;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; font-family: 'Inter', sans-serif; color: var(--ink); background: var(--ivory); line-height: 1.6; font-weight: 300; }
a { text-decoration: none; color: inherit; transition: 0.3s ease; }
h1, h2, h3, h4, h5, h6 { font-family: 'Cormorant Garamond', serif; font-weight: 500; margin: 0 0 20px; line-height: 1.1; color: var(--green-950); }
h1 { font-size: clamp(50px, 6vw, 90px); }
h2 { font-size: clamp(36px, 4vw, 54px); }
h3 { font-size: 28px; }

.container { width: min(1280px, 92%); margin: auto; }
.gold { color: var(--gold); }
.green { color: var(--green-900); }

/* Typography */
.eyebrow { font-size: 11px; letter-spacing: 0.25em; text-transform: uppercase; color: var(--gold-dark); margin-bottom: 12px; font-weight: 500; }
.body-large { font-size: 18px; color: rgba(23, 26, 23, 0.8); max-width: 650px; }

/* Backgrounds & Textures */
.bg-green { background-color: var(--green-950); color: var(--cream); position: relative; overflow: hidden; }
.bg-green h1, .bg-green h2, .bg-green h3, .bg-green p, .bg-green .body-large { color: var(--ivory); }
.bg-cream { background-color: var(--cream); }
.texture-paper { background-image: url('data:image/svg+xml;utf8,<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><filter id="noiseFilter"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" stitchTiles="stitch"/></filter><rect width="100%" height="100%" filter="url(%23noiseFilter)" opacity="0.04"/></svg>'); }

/* Buttons */
.btn { display: inline-flex; align-items: center; justify-content: center; gap: 12px; padding: 16px 32px; border-radius: 0; border: 1px solid var(--gold); font-family: 'Inter', sans-serif; font-weight: 500; font-size: 12px; letter-spacing: 0.15em; text-transform: uppercase; cursor: pointer; transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94); position: relative; overflow: hidden; z-index: 1; }
.btn::before { content: ""; position: absolute; inset: 0; background: var(--gold); z-index: -1; transform: scaleX(0); transform-origin: right; transition: transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94); }
.btn:hover::before { transform: scaleX(1); transform-origin: left; }
.btn-gold { background: var(--gold); color: var(--green-950); border-color: var(--gold); }
.btn-gold::before { background: var(--white); }
.btn-gold:hover { color: var(--gold-dark); }
.btn-outline { background: transparent; color: var(--green-950); border-color: var(--green-950); }
.btn-outline::before { background: var(--green-950); }
.btn-outline:hover { color: var(--white); }
.btn-outline-light { background: transparent; color: var(--ivory); border-color: var(--ivory); }
.btn-outline-light::before { background: var(--ivory); }
.btn-outline-light:hover { color: var(--green-950); }
.btn-text { background: none; border: none; padding: 0; border-bottom: 1px solid var(--gold); color: var(--gold-dark); cursor: pointer; text-transform: uppercase; font-size: 12px; letter-spacing: 0.1em; transition: 0.3s; display: inline-block; }
.btn-text:hover { color: var(--green-950); border-color: var(--green-950); }

/* Navigation */
.topbar { background: var(--green-950); color: var(--gold); font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase; text-align: center; padding: 10px; font-weight: 500; }
.nav { position: sticky; top: 0; z-index: 100; background: rgba(251, 248, 241, 0.95); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(11, 36, 24, 0.08); transition: all 0.3s ease; }
.nav-inner { height: 85px; display: flex; align-items: center; justify-content: space-between; }
.logo { display: flex; align-items: center; gap: 12px; color: var(--green-950); text-decoration: none; }
.logo-text { font-family: 'Cormorant Garamond', serif; font-size: 28px; letter-spacing: 0.15em; font-weight: 600; line-height: 1; }
.nav-links { display: flex; gap: 35px; align-items: center; }
.nav-links a { font-size: 12px; letter-spacing: 0.15em; text-transform: uppercase; color: var(--green-950); position: relative; opacity: 0.8; font-weight: 500; }
.nav-links a::after { content: ""; position: absolute; left: 0; bottom: -4px; width: 100%; height: 1px; background: var(--gold); transform: scaleX(0); transform-origin: right; transition: transform 0.3s ease; }
.nav-links a:hover, .nav-links a.active { opacity: 1; color: var(--green-950); }
.nav-links a:hover::after, .nav-links a.active::after { transform: scaleX(1); transform-origin: left; }
.nav-actions { display: flex; align-items: center; gap: 20px; }
.icon-btn { width: 24px; height: 24px; background: transparent; border: none; color: var(--green-950); cursor: pointer; display: flex; align-items: center; justify-content: center; padding: 0; transition: color 0.3s; position: relative; }
.icon-btn:hover { color: var(--gold-dark); }
.cart-count { position: absolute; top: -6px; right: -8px; background: var(--gold); color: var(--white); font-size: 10px; font-weight: 600; min-width: 16px; height: 16px; border-radius: 50%; display: grid; place-items: center; padding: 0 4px; }
.menu { display: none; }
.mobile-nav-panel { display: none; background: var(--green-950); color: var(--ivory); position: absolute; top: 100%; left: 0; width: 100%; padding: 20px 4%; border-bottom: 1px solid var(--gold); }
.mobile-nav-panel a { display: block; padding: 15px 0; font-size: 14px; letter-spacing: 0.15em; text-transform: uppercase; border-bottom: 1px solid rgba(255,255,255,0.05); color: var(--ivory); }

/* Hero */
.hero { height: 90vh; min-height: 700px; display: flex; align-items: center; position: relative; background: var(--green-950); overflow: hidden; padding-top: 0; }
.hero::before { content: ""; position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: url('https://images.unsplash.com/photo-1596647901047-7da354780517?q=80&w=2670&auto=format&fit=crop') center/cover no-repeat; opacity: 0.4; mix-blend-mode: overlay; z-index: 0; }
.hero-content { position: relative; z-index: 2; max-width: 700px; }
.hero h1 { color: var(--ivory); margin-bottom: 24px; text-transform: none; }
.hero p { color: rgba(251, 248, 241, 0.9); margin-bottom: 40px; font-size: 18px; line-height: 1.8; font-weight: 300; }
.hero-badge { display: inline-block; border: 1px solid var(--gold); padding: 8px 16px; color: var(--gold); font-size: 10px; letter-spacing: 0.2em; text-transform: uppercase; margin-bottom: 30px; border-radius: 999px; }
.hero-actions { display: flex; gap: 20px; align-items: center; }
.hero-ornament { position: absolute; right: 5%; top: 50%; transform: translateY(-50%); width: 45%; height: 70%; border: 1px solid rgba(200, 164, 93, 0.3); border-radius: 200px 200px 0 0; z-index: 1; display: flex; align-items: center; justify-content: center; overflow: hidden; }
.hero-ornament img { width: 100%; height: 100%; object-fit: cover; border-radius: 200px 200px 0 0; }

/* Intro / Editorial Section */
.intro { padding: 120px 0; background: var(--ivory); }
.intro-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; }
.intro-img { position: relative; }
.intro-img img { width: 100%; height: auto; object-fit: cover; aspect-ratio: 4/5; }
.intro-img::before { content: ""; position: absolute; top: 30px; left: -30px; width: 100%; height: 100%; border: 1px solid var(--gold); z-index: -1; }

/* Categories */
.category-section { padding: 100px 0; background: var(--cream); }
.section-header { text-align: center; margin-bottom: 60px; }
.section-header p { margin: 0 auto; }
.category-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }
.cat-card { position: relative; overflow: hidden; background: var(--white); display: block; group: hover; transition: all 0.4s; aspect-ratio: 3/4; border: 1px solid rgba(11,36,24,0.05); }
.cat-card-img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; transition: transform 0.7s; }
.cat-card::after { content: ""; position: absolute; inset: 0; background: linear-gradient(to top, rgba(11, 36, 24, 0.8), transparent 50%); }
.cat-card-content { position: absolute; bottom: 0; left: 0; right: 0; padding: 30px; color: var(--white); z-index: 2; }
.cat-card h3 { color: var(--white); margin: 0 0 10px; font-size: 24px; }
.cat-card p { font-size: 13px; opacity: 0.8; margin: 0 0 20px; line-height: 1.4; }
.cat-card:hover .cat-card-img { transform: scale(1.05); }
.cat-card:hover { border-color: var(--gold); }

/* Products */
.products-section { padding: 120px 0; }
.product-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 30px; }
.product-card { position: relative; background: var(--white); border: 1px solid rgba(11,36,24,0.05); padding: 20px; transition: all 0.4s; text-align: center; display: flex; flex-direction: column; }
.product-card:hover { box-shadow: var(--shadow); border-color: var(--gold); transform: translateY(-5px); }
.product-img-wrap { position: relative; width: 100%; aspect-ratio: 1; margin-bottom: 25px; overflow: hidden; display: flex; align-items: center; justify-content: center; background: var(--ivory); }
.product-img-wrap img { max-width: 80%; max-height: 80%; object-fit: contain; transition: transform 0.5s; filter: drop-shadow(0 15px 25px rgba(0,0,0,0.1)); }
.product-card:hover .product-img-wrap img { transform: scale(1.08); }
.product-badge { position: absolute; top: 10px; left: 10px; font-size: 9px; letter-spacing: 0.15em; text-transform: uppercase; background: var(--cream); color: var(--green-950); padding: 4px 10px; z-index: 2; border: 1px solid rgba(11,36,24,0.1); }
.product-info h3 { font-size: 20px; margin: 0 0 5px; }
.product-info .desc { font-size: 13px; color: var(--muted); margin: 0 0 15px; line-height: 1.4; height: 36px; overflow: hidden; }
.product-meta { display: flex; justify-content: space-between; align-items: center; margin-top: auto; padding-top: 15px; border-top: 1px solid rgba(11,36,24,0.05); }
.product-price { font-weight: 500; color: var(--green-950); font-size: 16px; }
.product-actions { display: flex; gap: 8px; }
.icon-btn-small { width: 32px; height: 32px; border: 1px solid rgba(11,36,24,0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; background: transparent; cursor: pointer; color: var(--green-950); transition: all 0.3s; }
.icon-btn-small:hover { background: var(--green-950); color: var(--gold); border-color: var(--green-950); }

/* Story / Heritage */
.heritage { padding: 120px 0; display: grid; grid-template-columns: 1fr 1fr; }
.heritage-img { background: url('https://images.unsplash.com/photo-1598514982205-f36b96d1e8d4?q=80&w=2000&auto=format&fit=crop') center/cover; min-height: 600px; position: relative; }
.heritage-img::after { content: ""; position: absolute; inset: 20px; border: 1px solid rgba(255,255,255,0.3); }
.heritage-content { padding: 80px 10%; display: flex; flex-direction: column; justify-content: center; }

/* Pillars */
.pillars { padding: 100px 0; background: var(--cream); border-top: 1px solid rgba(200,164,93,0.3); border-bottom: 1px solid rgba(200,164,93,0.3); }
.pillar-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 40px; text-align: center; }
.pillar-icon { margin-bottom: 20px; color: var(--gold-dark); height: 40px; }
.pillar h4 { font-family: 'Inter', sans-serif; font-size: 12px; letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 10px; font-weight: 600; }
.pillar p { font-size: 13px; color: var(--muted); }

/* Date Experience */
.date-experience { padding: 120px 0; background: var(--green-950); color: var(--ivory); }
.date-card { border: 1px solid rgba(200,164,93,0.2); padding: 40px 30px; text-align: center; transition: 0.3s; background: rgba(255,255,255,0.02); }
.date-card:hover { border-color: var(--gold); background: rgba(255,255,255,0.05); }
.date-card h3 { color: var(--gold); margin-bottom: 15px; }
.date-card p { font-size: 14px; opacity: 0.8; }

/* Social */
.social-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin-top: 40px; }
.social-img { aspect-ratio: 1; object-fit: cover; width: 100%; filter: grayscale(20%); transition: filter 0.3s; }
.social-img:hover { filter: grayscale(0); }

/* Footer */
.footer { background: var(--green-950); color: rgba(251, 248, 241, 0.7); padding: 100px 0 30px; border-top: 1px solid var(--gold); }
.footer h3 { color: var(--gold); font-family: 'Inter', sans-serif; font-size: 12px; letter-spacing: 0.2em; text-transform: uppercase; font-weight: 500; margin-bottom: 25px; }
.footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1.5fr; gap: 60px; margin-bottom: 60px; }
.footer-logo { display: block; margin-bottom: 20px; }
.footer p { margin-bottom: 20px; font-size: 14px; line-height: 1.8; }
.footer-links { list-style: none; padding: 0; margin: 0; }
.footer-links li { margin-bottom: 15px; }
.footer-links a { color: inherit; font-size: 14px; transition: color 0.3s; }
.footer-links a:hover { color: var(--gold); }
.footer-social { display: flex; gap: 15px; margin-top: 30px; }
.footer-social a { display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border: 1px solid rgba(251, 248, 241, 0.2); border-radius: 50%; color: var(--ivory); transition: all 0.3s; }
.footer-social a:hover { border-color: var(--gold); color: var(--gold); }
.newsletter-form { display: flex; border-bottom: 1px solid rgba(251, 248, 241, 0.3); padding-bottom: 10px; margin-top: 20px; }
.newsletter-form input { background: transparent; border: none; color: var(--ivory); font-family: 'Inter', sans-serif; font-size: 14px; flex: 1; outline: none; }
.newsletter-form input::placeholder { color: rgba(251, 248, 241, 0.4); }
.newsletter-form button { background: transparent; border: none; color: var(--gold); cursor: pointer; font-size: 12px; letter-spacing: 0.1em; text-transform: uppercase; font-weight: 600; }
.footer-bottom { border-top: 1px solid rgba(251, 248, 241, 0.1); padding-top: 30px; display: flex; justify-content: space-between; font-size: 12px; }

/* Product Page */
.page-header { padding: 100px 0 60px; background: var(--cream); text-align: center; border-bottom: 1px solid rgba(11,36,24,0.05); }
.product-detail-layout { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; padding: 80px 0; align-items: start; }
.detail-gallery { background: var(--white); border: 1px solid rgba(11,36,24,0.05); aspect-ratio: 1; display: flex; align-items: center; justify-content: center; position: sticky; top: 120px; }
.detail-gallery img { max-width: 80%; max-height: 80%; object-fit: contain; }
.detail-info h1 { margin-bottom: 10px; font-size: 42px; }
.detail-price { font-size: 24px; color: var(--green-950); margin-bottom: 25px; display: block; font-weight: 500; }
.detail-desc { font-size: 16px; line-height: 1.8; margin-bottom: 40px; color: rgba(23,26,23,0.8); }
.quantity-selector { display: inline-flex; align-items: center; border: 1px solid rgba(11,36,24,0.2); margin-right: 15px; }
.quantity-selector button { background: transparent; border: none; width: 45px; height: 45px; font-size: 18px; cursor: pointer; color: var(--green-950); }
.quantity-selector span { width: 40px; text-align: center; font-weight: 500; font-size: 14px; }
.add-to-cart-wrap { display: flex; margin-bottom: 50px; }
.accordion { border-top: 1px solid rgba(11,36,24,0.1); }
.accordion-item { border-bottom: 1px solid rgba(11,36,24,0.1); }
.accordion-header { padding: 20px 0; font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
.accordion-body { padding-bottom: 20px; font-size: 14px; color: rgba(23,26,23,0.8); display: none; }
.accordion-body ul { padding-left: 20px; margin: 0; }

/* Shop Page */
.shop-layout { display: grid; grid-template-columns: 240px 1fr; gap: 50px; padding: 60px 0 120px; }
.shop-filters { position: sticky; top: 120px; }
.filter-group { margin-bottom: 40px; }
.filter-group h4 { font-family: 'Inter', sans-serif; font-size: 12px; letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 1px solid rgba(11,36,24,0.1); }
.filter-list { list-style: none; padding: 0; margin: 0; }
.filter-list li { margin-bottom: 12px; }
.filter-list button { background: none; border: none; padding: 0; color: rgba(23,26,23,0.7); font-size: 14px; cursor: pointer; text-align: left; width: 100%; transition: 0.3s; }
.filter-list button:hover, .filter-list button.active { color: var(--gold-dark); font-weight: 500; }

/* Cart */
.cart-layout { display: grid; grid-template-columns: 1fr 400px; gap: 60px; padding: 80px 0 120px; }
.cart-table { width: 100%; border-collapse: collapse; }
.cart-table th { text-align: left; font-family: 'Inter', sans-serif; font-size: 11px; letter-spacing: 0.15em; text-transform: uppercase; padding-bottom: 20px; border-bottom: 1px solid rgba(11,36,24,0.1); font-weight: 600; }
.cart-table td { padding: 30px 0; border-bottom: 1px solid rgba(11,36,24,0.05); vertical-align: middle; }
.cart-item-info { display: flex; align-items: center; gap: 20px; }
.cart-item-img { width: 80px; height: 80px; background: var(--cream); border: 1px solid rgba(11,36,24,0.05); display: flex; align-items: center; justify-content: center; padding: 10px; }
.cart-item-img img { max-width: 100%; max-height: 100%; object-fit: contain; }
.cart-summary { background: var(--cream); padding: 40px; border: 1px solid rgba(200,164,93,0.3); }
.cart-summary h3 { font-size: 24px; margin-bottom: 30px; }
.summary-row { display: flex; justify-content: space-between; margin-bottom: 15px; font-size: 14px; }
.summary-total { display: flex; justify-content: space-between; margin-top: 25px; padding-top: 25px; border-top: 1px solid rgba(11,36,24,0.1); font-family: 'Cormorant Garamond', serif; font-size: 24px; font-weight: 600; color: var(--green-950); margin-bottom: 30px; }

/* Contact/About */
.editorial-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; padding: 100px 0; align-items: center; }
.contact-form { display: grid; gap: 20px; }
.contact-form input, .contact-form textarea, .contact-form select { width: 100%; padding: 16px 20px; border: 1px solid rgba(11,36,24,0.2); background: transparent; font-family: 'Inter', sans-serif; font-size: 14px; outline: none; transition: border-color 0.3s; }
.contact-form input:focus, .contact-form textarea:focus { border-color: var(--gold); }
.contact-form textarea { min-height: 150px; resize: vertical; }

.toast { position: fixed; right: 30px; bottom: 30px; background: var(--green-950); color: var(--ivory); padding: 16px 24px; box-shadow: var(--shadow); transform: translateY(150px); opacity: 0; transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94); z-index: 1000; font-size: 14px; border: 1px solid var(--gold); display: flex; align-items: center; gap: 12px; }
.toast.show { transform: translateY(0); opacity: 1; }

/* Search Overlay */
#searchBar { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(251, 248, 241, 0.98); z-index: 200; display: none; align-items: center; justify-content: center; backdrop-filter: blur(10px); }
.search-close { position: absolute; top: 30px; right: 40px; font-size: 30px; cursor: pointer; color: var(--green-950); background: none; border: none; }
#searchBar input { font-size: 48px; font-family: 'Cormorant Garamond', serif; border: none; border-bottom: 2px solid var(--gold); background: transparent; color: var(--green-950); outline: none; width: 80%; max-width: 800px; padding: 10px 0; }
#searchBar input::placeholder { color: rgba(11,36,24,0.3); }

/* Responsive */
@media(max-width: 900px) {
  .nav-links { display: none; }
  .menu { display: flex; }
  .hero-ornament { display: none; }
  .intro-grid, .heritage, .product-detail-layout, .cart-layout, .editorial-grid, .shop-layout { grid-template-columns: 1fr; }
  .shop-filters { position: relative; top: 0; }
  .category-grid, .product-grid, .pillar-grid, .social-grid { grid-template-columns: repeat(2, 1fr); }
  .footer-grid { grid-template-columns: repeat(2, 1fr); }
  .heritage-content { padding: 60px 5%; }
  h1 { font-size: 42px; }
  .cart-table thead { display: none; }
  .cart-table, .cart-table tbody, .cart-table tr, .cart-table td { display: block; width: 100%; }
  .cart-table tr { margin-bottom: 30px; border-bottom: 1px solid rgba(11,36,24,0.1); padding-bottom: 20px; }
  .cart-table td { padding: 10px 0; border: none; text-align: right; }
  .cart-item-info { justify-content: space-between; }
  .cart-item-info::before { content: "Product"; font-weight: 600; font-size: 11px; text-transform: uppercase; }
}

@media(max-width: 560px) {
  .category-grid, .product-grid, .pillar-grid, .footer-grid { grid-template-columns: 1fr; }
  .hero { min-height: 500px; padding: 60px 0; }
  #searchBar input { font-size: 28px; }
}
"""

with open(os.path.join(DIR, "style.css"), "w") as f:
    f.write(style_css)

app_js = """
const PRODUCTS = [
  {id: 0, name: "Ajwa Dates", cat: "dates", price: 699, typ: "date", desc: "Premium Ajwa dates with a naturally rich, soft texture.", details: ["Naturally sweet profile", "Premium selection", "Ideal for gifting and everyday snacking"], img: "https://images.unsplash.com/photo-1596431934301-4470bc5e8354?w=500&auto=format&fit=crop"},
  {id: 1, name: "Medjool Dates", cat: "dates", price: 849, typ: "date", desc: "Large, soft Medjool dates selected for premium gifting.", details: ["Large fruit size", "Soft, caramel-like texture", "Premium gifting choice"], img: "https://images.unsplash.com/photo-1550828552-824c0d0a7931?w=500&auto=format&fit=crop"},
  {id: 2, name: "California Almonds", cat: "nuts", price: 599, typ: "nut", desc: "Crunchy, premium almonds for everyday nourishment.", details: ["Whole almonds", "Naturally crunchy", "Everyday pantry staple"], img: "https://images.unsplash.com/photo-1508061253366-f7da158b6d46?w=500&auto=format&fit=crop"},
  {id: 3, name: "Pistachio Kernels", cat: "nuts", price: 799, typ: "pistachio", desc: "Delicate pistachio kernels with a rich roasted profile.", details: ["Premium kernels", "Rich nutty flavour", "Great for snacking and desserts"], img: "https://images.unsplash.com/photo-1524316972046-63e27599ea79?w=500&auto=format&fit=crop"},
  {id: 4, name: "Premium Cashews", cat: "nuts", price: 649, typ: "nut", desc: "Creamy whole cashews with a naturally buttery finish.", details: ["Whole cashews", "Creamy texture", "Ideal for gifting"], img: "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?w=500&auto=format&fit=crop"},
  {id: 5, name: "Dried Turkish Figs", cat: "dry-fruits", price: 749, typ: "date", desc: "Naturally sweet dried figs with a tender bite.", details: ["Naturally dried", "Tender texture", "Sweet pantry staple"], img: "https://images.unsplash.com/photo-1600858591873-1081cb9f2a03?w=500&auto=format&fit=crop"},
  {id: 6, name: "Organic Wild Honey", cat: "organic", price: 499, typ: "honey", desc: "Demo product: raw-style honey inspired by natural sourcing.", details: ["Demo product", "Natural pantry concept", "Perfect with breakfast and beverages"], img: "https://images.unsplash.com/photo-1587049352847-4d4b124032d2?w=500&auto=format&fit=crop"},
  {id: 7, name: "Signature Gift Box", cat: "gifting", price: 1499, typ: "pistachio", desc: "A curated assortment of dates, nuts and dry fruits.", details: ["Curated assortment", "Premium presentation", "Perfect for celebrations"], img: "https://images.unsplash.com/photo-1549465220-1a8b9238cd48?w=500&auto=format&fit=crop"}
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
"""

with open(os.path.join(DIR, "app.js"), "w") as f:
    f.write(app_js)

def get_nav():
    return """
    <div class="topbar">Free delivery on premium selections • Pure Natural Goodness</div>
    <nav class="nav">
        <div class="container nav-inner">
            <a href="index.html" class="logo">
                <span class="logo-text">SK TABII</span>
            </a>
            <div class="nav-links">
                <a href="index.html">Home</a>
                <a href="shop.html">Shop</a>
                <a href="shop.html?cat=dates">Dates</a>
                <a href="shop.html?cat=nuts">Nuts</a>
                <a href="shop.html?cat=gifting">Gifting</a>
                <a href="about.html">Our Story</a>
            </div>
            <div class="nav-actions">
                <button class="icon-btn" onclick="toggleSearch()" aria-label="Search">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                </button>
                <a class="icon-btn" href="cart.html" aria-label="Cart">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 8h12l1 13H5L6 8Zm3 0V6a3 3 0 0 1 6 0v2"></path></svg>
                    <span class="cart-count">0</span>
                </a>
                <button class="icon-btn menu" onclick="toggleMenu()" aria-label="Menu">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
                </button>
            </div>
        </div>
    </nav>
    <div id="mobileNav" class="mobile-nav-panel">
        <a href="index.html">Home</a>
        <a href="shop.html">Shop All</a>
        <a href="shop.html?cat=dates">Dates</a>
        <a href="shop.html?cat=nuts">Nuts</a>
        <a href="about.html">Our Story</a>
        <a href="contact.html">Contact</a>
    </div>
    <div id="searchBar">
        <button class="search-close" onclick="toggleSearch()">×</button>
        <input type="text" id="siteSearch" placeholder="Search premium dates, nuts..." onkeydown="globalSearch(event)">
    </div>
    """

def get_footer():
    return """
    <footer class="footer texture-paper">
        <div class="container">
            <div class="footer-grid">
                <div>
                    <a href="index.html" class="logo footer-logo" style="color:var(--gold);">
                        <span class="logo-text">SK TABII</span>
                    </a>
                    <p>Natural • Pure • Wholesome</p>
                    <p style="margin-top:20px; font-size:13px; opacity:0.8;">Premium natural foods, dates, nuts, dry fruits, and gifting curated with a passion for nature.</p>
                </div>
                <div>
                    <h3>Explore</h3>
                    <ul class="footer-links">
                        <li><a href="shop.html">Shop All</a></li>
                        <li><a href="shop.html?cat=dates">Premium Dates</a></li>
                        <li><a href="shop.html?cat=nuts">Nuts</a></li>
                        <li><a href="shop.html?cat=dry-fruits">Dry Fruits</a></li>
                        <li><a href="shop.html?cat=organic">Organic</a></li>
                        <li><a href="shop.html?cat=gifting">Gifting</a></li>
                    </ul>
                </div>
                <div>
                    <h3>Customer Care</h3>
                    <ul class="footer-links">
                        <li><a href="contact.html">Contact Us</a></li>
                        <li><a href="#">Shipping Information</a></li>
                        <li><a href="#">Returns & Exchanges</a></li>
                        <li><a href="#">Privacy Policy</a></li>
                        <li><a href="#">Terms of Service</a></li>
                        <li><a href="#">FAQs</a></li>
                    </ul>
                </div>
                <div>
                    <h3>Join the TABII Journal</h3>
                    <p style="font-size:13px;">Subscribe for fresh drops, seasonal gifting, and exclusive natural goodness.</p>
                    <form class="newsletter-form" onsubmit="subscribe(event)">
                        <input type="email" required placeholder="Enter your email">
                        <button type="submit">Subscribe</button>
                    </form>
                    <div class="footer-social">
                        <a href="#" aria-label="Instagram"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
                        <a href="#" aria-label="Facebook"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <span>© 2026 SK TABII. Premium Natural Foods.</span>
                <span>EST. WITH A PASSION FOR NATURE</span>
            </div>
        </div>
    </footer>
    <div id="toast" class="toast"></div>
    <script src="app.js"></script>
    """

def wrap_html(title, content):
    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="description" content="SK TABII — Premium natural foods, dates, nuts, dry fruits, and organic products.">
    <title>{title} — SK TABII</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    {get_nav()}
    <main>
    {content}
    </main>
    {get_footer()}
</body>
</html>"""

# INDEX HTML
index_content = """
<section class="hero texture-paper">
    <div class="container hero-content">
        <div class="hero-badge">EST. WITH A PASSION FOR NATURE</div>
        <h1>Pure. Natural.<br><span class="gold">Wholesome.</span></h1>
        <p>Premium dates, nuts, dry fruits and natural goodness, carefully selected for everyday indulgence.</p>
        <div class="hero-actions">
            <a href="shop.html" class="btn btn-gold">Explore Collection</a>
            <a href="about.html" class="btn btn-outline-light">Our Story</a>
        </div>
    </div>
    <div class="hero-ornament">
        <img src="https://images.unsplash.com/photo-1596647901047-7da354780517?q=80&w=1000&auto=format&fit=crop" alt="Premium Assortment">
    </div>
</section>

<section class="intro texture-paper">
    <div class="container intro-grid">
        <div class="intro-img">
            <img src="https://images.unsplash.com/photo-1550828552-824c0d0a7931?q=80&w=1000&auto=format&fit=crop" alt="Premium Medjool Dates">
        </div>
        <div>
            <div class="eyebrow">Premium Brand</div>
            <h2>Nature, <br><span class="green">carefully chosen.</span></h2>
            <p class="body-large" style="margin-top:30px;">SK TABII brings together premium dates, nuts, dry fruits and natural products selected with care. We believe that true luxury lies in the purity of ingredients, harvested respectfully from nature.</p>
            <a href="about.html" class="btn-text" style="margin-top:30px;">Discover the Philosophy</a>
        </div>
    </div>
</section>

<section class="category-section">
    <div class="container">
        <div class="section-header">
            <div class="eyebrow">Curated Selection</div>
            <h2>Explore Categories</h2>
        </div>
        <div class="category-grid">
            <a href="shop.html?cat=dates" class="cat-card">
                <img src="https://images.unsplash.com/photo-1596431934301-4470bc5e8354?q=80&w=600&auto=format&fit=crop" class="cat-card-img" alt="Dates">
                <div class="cat-card-content">
                    <h3>Dates</h3>
                    <p>Ajwa, Medjool and more.</p>
                    <span class="btn-text" style="color:#fff; border-color:rgba(255,255,255,0.3)">Explore</span>
                </div>
            </a>
            <a href="shop.html?cat=nuts" class="cat-card">
                <img src="https://images.unsplash.com/photo-1508061253366-f7da158b6d46?q=80&w=600&auto=format&fit=crop" class="cat-card-img" alt="Nuts">
                <div class="cat-card-content">
                    <h3>Nuts</h3>
                    <p>Premium everyday crunch.</p>
                    <span class="btn-text" style="color:#fff; border-color:rgba(255,255,255,0.3)">Explore</span>
                </div>
            </a>
            <a href="shop.html?cat=dry-fruits" class="cat-card">
                <img src="https://images.unsplash.com/photo-1600858591873-1081cb9f2a03?q=80&w=600&auto=format&fit=crop" class="cat-card-img" alt="Dry Fruits">
                <div class="cat-card-content">
                    <h3>Dry Fruits</h3>
                    <p>Wholesome sweetness.</p>
                    <span class="btn-text" style="color:#fff; border-color:rgba(255,255,255,0.3)">Explore</span>
                </div>
            </a>
            <a href="shop.html?cat=organic" class="cat-card">
                <img src="https://images.unsplash.com/photo-1587049352847-4d4b124032d2?q=80&w=600&auto=format&fit=crop" class="cat-card-img" alt="Organic">
                <div class="cat-card-content">
                    <h3>Organic</h3>
                    <p>Purely organic goodness.</p>
                    <span class="btn-text" style="color:#fff; border-color:rgba(255,255,255,0.3)">Explore</span>
                </div>
            </a>
        </div>
    </div>
</section>

<section class="products-section bg-cream">
    <div class="container">
        <div class="section-header" style="display:flex; justify-content:space-between; align-items:flex-end; text-align:left;">
            <div>
                <div class="eyebrow">Featured</div>
                <h2 style="margin:0">The TABII Collection</h2>
            </div>
            <a href="shop.html" class="btn btn-outline">View All</a>
        </div>
        
        <div class="product-grid" id="productGridFeatured">
            <!-- Rendered by JS or statically here since it's just the homepage -->
            <div class="product-card" data-cat="dates">
                <div class="product-badge">Dates</div>
                <a href="product.html?id=1" class="product-img-wrap"><img src="https://images.unsplash.com/photo-1550828552-824c0d0a7931?w=500&auto=format&fit=crop" alt="Medjool Dates"></a>
                <div class="product-info">
                    <h3><a href="product.html?id=1">Medjool Dates</a></h3>
                    <p class="desc">Large, soft Medjool dates selected for premium gifting.</p>
                    <div class="product-meta">
                        <span class="product-price">₹849</span>
                        <div class="product-actions">
                            <button class="icon-btn-small" onclick="addToCart(1)" aria-label="Add to Cart"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 8h12l1 13H5L6 8Zm3 0V6a3 3 0 0 1 6 0v2"></path></svg></button>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="product-card" data-cat="nuts">
                <div class="product-badge">Nuts</div>
                <a href="product.html?id=2" class="product-img-wrap"><img src="https://images.unsplash.com/photo-1508061253366-f7da158b6d46?w=500&auto=format&fit=crop" alt="California Almonds"></a>
                <div class="product-info">
                    <h3><a href="product.html?id=2">California Almonds</a></h3>
                    <p class="desc">Crunchy, premium almonds for everyday nourishment.</p>
                    <div class="product-meta">
                        <span class="product-price">₹599</span>
                        <div class="product-actions">
                            <button class="icon-btn-small" onclick="addToCart(2)" aria-label="Add to Cart"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 8h12l1 13H5L6 8Zm3 0V6a3 3 0 0 1 6 0v2"></path></svg></button>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="product-card" data-cat="nuts">
                <div class="product-badge">Nuts</div>
                <a href="product.html?id=3" class="product-img-wrap"><img src="https://images.unsplash.com/photo-1524316972046-63e27599ea79?w=500&auto=format&fit=crop" alt="Pistachio Kernels"></a>
                <div class="product-info">
                    <h3><a href="product.html?id=3">Pistachio Kernels</a></h3>
                    <p class="desc">Delicate pistachio kernels with a rich roasted profile.</p>
                    <div class="product-meta">
                        <span class="product-price">₹799</span>
                        <div class="product-actions">
                            <button class="icon-btn-small" onclick="addToCart(3)" aria-label="Add to Cart"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 8h12l1 13H5L6 8Zm3 0V6a3 3 0 0 1 6 0v2"></path></svg></button>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="product-card" data-cat="gifting">
                <div class="product-badge">Gifting</div>
                <a href="product.html?id=7" class="product-img-wrap"><img src="https://images.unsplash.com/photo-1549465220-1a8b9238cd48?w=500&auto=format&fit=crop" alt="Signature Gift Box"></a>
                <div class="product-info">
                    <h3><a href="product.html?id=7">Signature Gift Box</a></h3>
                    <p class="desc">A curated assortment of dates, nuts and dry fruits.</p>
                    <div class="product-meta">
                        <span class="product-price">₹1,499</span>
                        <div class="product-actions">
                            <button class="icon-btn-small" onclick="addToCart(7)" aria-label="Add to Cart"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 8h12l1 13H5L6 8Zm3 0V6a3 3 0 0 1 6 0v2"></path></svg></button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="heritage bg-green">
    <div class="heritage-img"></div>
    <div class="heritage-content texture-paper">
        <div class="eyebrow" style="color:var(--gold);">From Nature. With Purpose.</div>
        <h2 style="color:var(--ivory);">The Art of <br><span class="gold">Sourcing.</span></h2>
        <p class="body-large" style="color:rgba(251,248,241,0.8); margin-top:20px; margin-bottom:40px;">Our story begins with a profound respect for nature. We travel the world to source the finest dates, crunchiest nuts, and purest organic ingredients, ensuring every product carries the hallmark of TABII quality.</p>
        <a href="about.html" class="btn btn-outline-light" style="align-self:flex-start;">Read Our Story</a>
    </div>
</section>

<section class="pillars">
    <div class="container">
        <div class="section-header">
            <div class="eyebrow">Why SK TABII</div>
            <h2>Quality in Every Detail</h2>
        </div>
        <div class="pillar-grid">
            <div class="pillar">
                <svg class="pillar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg>
                <h4>Premium Selection</h4>
                <p>Only the finest grades chosen.</p>
            </div>
            <div class="pillar">
                <svg class="pillar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path><path d="M2 12h20"></path></svg>
                <h4>Carefully Sourced</h4>
                <p>Ethical global partnerships.</p>
            </div>
            <div class="pillar">
                <svg class="pillar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path><line x1="7" y1="7" x2="7.01" y2="7"></line></svg>
                <h4>Natural Goodness</h4>
                <p>Pure ingredients, no compromises.</p>
            </div>
            <div class="pillar">
                <svg class="pillar-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                <h4>Made for Gifting</h4>
                <p>Elegant boxes for every occasion.</p>
            </div>
        </div>
    </div>
</section>

<section class="date-experience texture-paper">
    <div class="container">
        <div class="section-header">
            <div class="eyebrow" style="color:var(--gold);">Heritage</div>
            <h2 style="color:var(--ivory);">The Art of the Date</h2>
            <p style="color:rgba(251,248,241,0.8); max-width:600px;">Discover the rich, caramel notes of our Middle-Eastern inspired date collection, ranging from the revered Ajwa to the succulent Medjool.</p>
        </div>
        <div class="category-grid">
            <div class="date-card">
                <h3>Ajwa</h3>
                <p>Revered, dark, with notes of prune and natural sweetness.</p>
            </div>
            <div class="date-card">
                <h3>Medjool</h3>
                <p>The 'King of Dates' — large, soft, and caramel-like.</p>
            </div>
            <div class="date-card">
                <h3>Mabroom</h3>
                <p>Firm, chewy, and naturally rich with a slender body.</p>
            </div>
            <div class="date-card">
                <h3>Sukkari</h3>
                <p>Melt-in-the-mouth texture with a golden sugary bite.</p>
            </div>
        </div>
        <div style="text-align:center; margin-top:50px;">
            <a href="shop.html?cat=dates" class="btn btn-gold">Explore Dates</a>
        </div>
    </div>
</section>

<section style="padding:100px 0; background:var(--white);">
    <div class="container" style="text-align:center;">
        <div class="eyebrow">Follow the TABII Journey</div>
        <h2>@SKTABII</h2>
        <div class="social-grid">
            <img src="https://images.unsplash.com/photo-1596431934301-4470bc5e8354?w=500&auto=format&fit=crop" class="social-img">
            <img src="https://images.unsplash.com/photo-1508061253366-f7da158b6d46?w=500&auto=format&fit=crop" class="social-img">
            <img src="https://images.unsplash.com/photo-1600858591873-1081cb9f2a03?w=500&auto=format&fit=crop" class="social-img">
            <img src="https://images.unsplash.com/photo-1550828552-824c0d0a7931?w=500&auto=format&fit=crop" class="social-img">
        </div>
    </div>
</section>
"""

with open(os.path.join(DIR, "index.html"), "w") as f:
    f.write(wrap_html("Home", index_content))

# ABOUT HTML
about_content = """
<header class="page-header texture-paper">
    <div class="container">
        <div class="eyebrow">Our Heritage</div>
        <h1>From Nature. <span class="gold">With Purpose.</span></h1>
    </div>
</header>
<section class="editorial-grid container">
    <div>
        <img src="https://images.unsplash.com/photo-1596647901047-7da354780517?q=80&w=1000&auto=format&fit=crop" style="width:100%; border:1px solid rgba(11,36,24,0.1);">
    </div>
    <div style="padding:0 5%;">
        <h2>The <span class="green">Philosophy.</span></h2>
        <p class="body-large" style="margin-bottom:20px;">SK TABII was born out of a desire to bring the world's most premium natural ingredients back to the modern table. We believe that true luxury lies in simplicity.</p>
        <p class="body-large">By partnering directly with trusted growers across the globe, we ensure that every date, every almond, and every dried fruit that carries the TABII name meets an uncompromising standard of quality.</p>
    </div>
</section>
<section class="bg-green texture-paper" style="padding:100px 0; text-align:center;">
    <div class="container">
        <h2 style="color:var(--gold);">"The best things in life are often the simplest — naturally grown, carefully chosen, beautifully shared."</h2>
        <p style="color:var(--ivory); letter-spacing:0.15em; text-transform:uppercase; font-size:12px; margin-top:30px;">— The TABII Vision</p>
    </div>
</section>
"""

with open(os.path.join(DIR, "about.html"), "w") as f:
    f.write(wrap_html("Our Story", about_content))

# SHOP HTML
shop_content = """
<header class="page-header texture-paper">
    <div class="container">
        <div class="eyebrow">The Collection</div>
        <h1>Purely <span class="gold">Premium.</span></h1>
    </div>
</header>
<section class="container shop-layout">
    <aside class="shop-filters">
        <div class="filter-group">
            <h4>Categories</h4>
            <ul class="filter-list">
                <li><button class="active" data-filter="all" onclick="filterProducts('all', this)">All Products</button></li>
                <li><button data-filter="dates" onclick="filterProducts('dates', this)">Premium Dates</button></li>
                <li><button data-filter="nuts" onclick="filterProducts('nuts', this)">Nuts & Kernels</button></li>
                <li><button data-filter="dry-fruits" onclick="filterProducts('dry-fruits', this)">Dry Fruits</button></li>
                <li><button data-filter="organic" onclick="filterProducts('organic', this)">Organic Pantry</button></li>
                <li><button data-filter="gifting" onclick="filterProducts('gifting', this)">Gifting Hampers</button></li>
            </ul>
        </div>
    </aside>
    <div>
        <div class="product-grid" id="productGrid">
            <!-- Products injected here by app.js -->
        </div>
    </div>
</section>
"""

with open(os.path.join(DIR, "shop.html"), "w") as f:
    f.write(wrap_html("Shop", shop_content))

# PRODUCT HTML
product_content = """
<div id="productDetail">
    <!-- Product detail injected here by app.js -->
</div>
<section style="padding:80px 0; background:var(--cream);">
    <div class="container">
        <h3 style="text-align:center; margin-bottom:50px;">You May Also Like</h3>
        <div class="product-grid">
             <div class="product-card" data-cat="dates">
                <div class="product-badge">Dates</div>
                <a href="product.html?id=0" class="product-img-wrap"><img src="https://images.unsplash.com/photo-1596431934301-4470bc5e8354?w=500&auto=format&fit=crop" alt="Ajwa Dates"></a>
                <div class="product-info">
                    <h3><a href="product.html?id=0">Ajwa Dates</a></h3>
                    <div class="product-meta">
                        <span class="product-price">₹699</span>
                        <div class="product-actions"><button class="icon-btn-small" onclick="addToCart(0)"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 8h12l1 13H5L6 8Zm3 0V6a3 3 0 0 1 6 0v2"></path></svg></button></div>
                    </div>
                </div>
            </div>
            <div class="product-card" data-cat="nuts">
                <div class="product-badge">Nuts</div>
                <a href="product.html?id=2" class="product-img-wrap"><img src="https://images.unsplash.com/photo-1508061253366-f7da158b6d46?w=500&auto=format&fit=crop" alt="California Almonds"></a>
                <div class="product-info">
                    <h3><a href="product.html?id=2">California Almonds</a></h3>
                    <div class="product-meta">
                        <span class="product-price">₹599</span>
                        <div class="product-actions"><button class="icon-btn-small" onclick="addToCart(2)"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 8h12l1 13H5L6 8Zm3 0V6a3 3 0 0 1 6 0v2"></path></svg></button></div>
                    </div>
                </div>
            </div>
            <div class="product-card" data-cat="dry-fruits">
                <div class="product-badge">Dry Fruits</div>
                <a href="product.html?id=5" class="product-img-wrap"><img src="https://images.unsplash.com/photo-1600858591873-1081cb9f2a03?w=500&auto=format&fit=crop" alt="Turkish Figs"></a>
                <div class="product-info">
                    <h3><a href="product.html?id=5">Dried Turkish Figs</a></h3>
                    <div class="product-meta">
                        <span class="product-price">₹749</span>
                        <div class="product-actions"><button class="icon-btn-small" onclick="addToCart(5)"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 8h12l1 13H5L6 8Zm3 0V6a3 3 0 0 1 6 0v2"></path></svg></button></div>
                    </div>
                </div>
            </div>
            <div class="product-card" data-cat="gifting">
                <div class="product-badge">Gifting</div>
                <a href="product.html?id=7" class="product-img-wrap"><img src="https://images.unsplash.com/photo-1549465220-1a8b9238cd48?w=500&auto=format&fit=crop" alt="Signature Gift Box"></a>
                <div class="product-info">
                    <h3><a href="product.html?id=7">Signature Gift Box</a></h3>
                    <div class="product-meta">
                        <span class="product-price">₹1,499</span>
                        <div class="product-actions"><button class="icon-btn-small" onclick="addToCart(7)"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 8h12l1 13H5L6 8Zm3 0V6a3 3 0 0 1 6 0v2"></path></svg></button></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
"""

with open(os.path.join(DIR, "product.html"), "w") as f:
    f.write(wrap_html("Product", product_content))

# CART HTML
cart_content = """
<header class="page-header texture-paper">
    <div class="container">
        <div class="eyebrow">Your Selection</div>
        <h1>The <span class="gold">Basket.</span></h1>
    </div>
</header>
<section class="container">
    <div id="cartArea">
        <!-- Cart injected here by app.js -->
    </div>
</section>
"""

with open(os.path.join(DIR, "cart.html"), "w") as f:
    f.write(wrap_html("Cart", cart_content))

# CONTACT HTML
contact_content = """
<header class="page-header texture-paper">
    <div class="container">
        <div class="eyebrow">Get in touch</div>
        <h1>Talk to <span class="gold">Us.</span></h1>
    </div>
</header>
<section class="editorial-grid container">
    <div style="padding-right:5%;">
        <h2>We're here to help.</h2>
        <p class="body-large" style="margin-bottom:30px;">Whether you have a question about our products, corporate gifting, or wholesale orders, we would love to hear from you.</p>
        
        <div style="margin-bottom:30px;">
            <div class="eyebrow">Store Location</div>
            <p>SK TABII Premium Boutique<br>Chennai, Tamil Nadu, India</p>
        </div>
        
        <div style="margin-bottom:30px;">
            <div class="eyebrow">Contact Details</div>
            <p>Phone: +91 72008 95492<br>Email: hello@sktabii.com</p>
        </div>
        
        <div>
            <div class="eyebrow">Business Hours</div>
            <p>Mon-Sat: 10:00 AM - 8:00 PM<br>Sunday: Closed</p>
        </div>
    </div>
    <div>
        <form class="contact-form" onsubmit="contactSubmit(event)" style="background:var(--white); padding:40px; border:1px solid rgba(11,36,24,0.1);">
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:20px;">
                <input type="text" placeholder="First Name" required>
                <input type="text" placeholder="Last Name" required>
            </div>
            <input type="email" placeholder="Email Address" required>
            <input type="text" placeholder="Subject (Optional)">
            <textarea placeholder="Your Message" required></textarea>
            <button type="submit" class="btn btn-gold" style="width:100%">Send Message</button>
        </form>
    </div>
</section>
"""

with open(os.path.join(DIR, "contact.html"), "w") as f:
    f.write(wrap_html("Contact", contact_content))

print("Files written.")
