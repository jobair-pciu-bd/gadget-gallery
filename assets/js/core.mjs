/** Pure, dependency-free storefront utilities. Tested with Node's built-in test runner. */
export const BDT = new Intl.NumberFormat('en-BD', { maximumFractionDigits: 0 });
export const money = value => `৳${BDT.format(Number(value) || 0)}`;
export const validId = id => typeof id === 'string' && /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(id);
export function validateProducts(rows) {
  if (!Array.isArray(rows)) throw new Error('Products file must contain a JSON array.');
  const ids = new Set();
  return rows.map((p, i) => {
    if (!p || !validId(p.id) || ids.has(p.id)) throw new Error(`Product ${i + 1}: invalid or duplicate ID.`);
    ids.add(p.id);
    if (typeof p.name !== 'string' || !p.name.trim() || typeof p.category !== 'string' || !p.category.trim()) throw new Error(`Product ${p.id}: name/category missing.`);
    if (!Number.isSafeInteger(p.price) || p.price < 0) throw new Error(`Product ${p.id}: price must be a nonnegative whole-number BDT amount.`);
    if (p.original_price != null && (!Number.isSafeInteger(p.original_price) || p.original_price < p.price)) throw new Error(`Product ${p.id}: original_price must be at least price.`);
    if (!Array.isArray(p.images) || !p.images.length || !p.images.every(s => typeof s === 'string' && s.length)) throw new Error(`Product ${p.id}: images must contain at least one path.`);
    if (typeof p.description !== 'string' || !p.specifications || typeof p.specifications !== 'object' || Array.isArray(p.specifications)) throw new Error(`Product ${p.id}: description/specifications invalid.`);
    for (const key of ['in_stock','featured','new_arrival']) if (typeof p[key] !== 'boolean') throw new Error(`Product ${p.id}: ${key} must be true or false.`);
    return p;
  });
}
export function filterProducts(products, { query = '', category = '', sort = 'featured' } = {}) {
  const q = query.trim().toLowerCase();
  const filtered = products.filter(p => (!category || p.category === category) && (!q || `${p.name} ${p.description} ${p.category}`.toLowerCase().includes(q)));
  if (sort === 'price-low') filtered.sort((a,b) => a.price - b.price || a.name.localeCompare(b.name));
  else if (sort === 'price-high') filtered.sort((a,b) => b.price - a.price || a.name.localeCompare(b.name));
  else if (sort === 'new') filtered.sort((a,b) => Number(b.new_arrival) - Number(a.new_arrival));
  else filtered.sort((a,b) => Number(b.featured) - Number(a.featured) || Number(b.new_arrival) - Number(a.new_arrival));
  return filtered;
}
export function normalizeCart(rows, products) {
  const catalog = new Map(products.map(p => [p.id,p]));
  if (!Array.isArray(rows)) return [];
  const combined = new Map();
  for (const item of rows) {
    if (!item || !catalog.has(item.id) || !Number.isSafeInteger(item.qty) || item.qty < 1) continue;
    combined.set(item.id, Math.min(99, (combined.get(item.id) || 0) + item.qty));
  }
  return [...combined].map(([id,qty]) => ({id,qty}));
}
export function cartSubtotal(cart, products) {
  const catalog = new Map(products.map(p => [p.id,p]));
  return cart.reduce((sum, item) => sum + (catalog.get(item.id)?.price || 0) * item.qty, 0);
}
export function normalizePhone(value) {
  const s = String(value || '').replace(/[\s()+-]/g, '');
  if (s.startsWith('8801') && /^8801\d{9}$/.test(s)) return s;
  if (/^01\d{9}$/.test(s)) return '88' + s;
  if (/^[1-9]\d{7,14}$/.test(s)) return s;
  return '';
}
export function whatsappNumber(value) {
  // Configured number MUST be a real Bangladesh international-format 8801... number.
  const s = String(value || '').replace(/[\s()+-]/g, '');
  return /^8801\d{9}$/.test(s) ? s : '';
}
export function makeOrderMessage({name,phone,address,notes = ''}, cart, products) {
  const productsById = new Map(products.map(p => [p.id,p]));
  const lines = ['Hello Gadget Gallery! I would like to request an order.', '', 'CUSTOMER DETAILS', `Name: ${name.trim()}`, `Phone: ${phone.trim()}`, `Delivery address: ${address.trim()}`];
  if (notes.trim()) lines.push(`Notes: ${notes.trim()}`);
  lines.push('', 'ORDER ITEMS');
  cart.forEach((item, i) => {
    const p = productsById.get(item.id);
    if (!p) return;
    lines.push(`${i + 1}. ${p.name}`, `   ${item.qty} × ${money(p.price)} = ${money(p.price * item.qty)}`);
  });
  lines.push('', `Product subtotal: ${money(cartSubtotal(cart,products))}`, 'Delivery fee: To be confirmed', 'Total payable: To be confirmed', '', 'Please confirm availability, final price, delivery charge, and payment method before accepting this order.');
  return lines.join('\n');
}
export function makeProductMessage(product) {
  return `Hello Gadget Gallery! I am interested in:\n${product.name}\nDisplayed price: ${money(product.price)} (please confirm)\n\nPlease confirm current availability, specifications and delivery charges.`;
}
export const whatsappLink = (digits, message) => `https://wa.me/${digits}?text=${encodeURIComponent(message)}`;
