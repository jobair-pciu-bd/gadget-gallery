import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {validateProducts,filterProducts,normalizeCart,cartSubtotal,money,normalizePhone,whatsappNumber,makeOrderMessage,whatsappLink} from '../assets/js/core.mjs';
const products=validateProducts(JSON.parse(fs.readFileSync(new URL('../data/products.json',import.meta.url),'utf8')));

test('catalog has eight valid unique sample products',()=>{assert.equal(products.length,8);assert.equal(new Set(products.map(p=>p.id)).size,products.length)});
test('invalid product data rejected',()=>{assert.throws(()=>validateProducts([...products,products[0]]));assert.throws(()=>validateProducts([{...products[0],price:'bad'}]));assert.deepEqual(validateProducts([]),[])});
test('search and category filtering',()=>{assert.ok(filterProducts(products,{query:'cable'}).some(p=>p.id==='braided-usbc-cable'));assert.ok(filterProducts(products,{category:'Chargers'}).every(p=>p.category==='Chargers'));assert.equal(filterProducts([],{}).length,0);assert.equal(filterProducts(products,{query:'does-not-match'}).length,0)});
test('sorting by price',()=>{const items=filterProducts(products,{sort:'price-low'});assert.equal(items[0].price,290);assert.equal(filterProducts(products,{sort:'price-high'})[0].price,1690)});
test('cart normalizes unexpected, duplicate and oversized quantities',()=>{assert.deepEqual(normalizeCart([{id:products[0].id,qty:2},{id:products[0].id,qty:3},{id:'bad',qty:1},{id:products[0].id,qty:-5}],products),[{id:products[0].id,qty:5}]);assert.deepEqual(normalizeCart({},products),[]);assert.deepEqual(normalizeCart([],products),[])});
test('cart totals and quantity changes',()=>{let cart=normalizeCart([{id:products[0].id,qty:3},{id:products[1].id,qty:2}],products);assert.equal(cartSubtotal(cart,products),3*490+2*890);cart[0].qty=1;assert.equal(cartSubtotal(cart,products),490+2*890);assert.equal(cartSubtotal([],products),0)});
test('BDT formatting',()=>{assert.ok(money(1690).startsWith('৳'))});
test('WhatsApp store number requires complete international Bangladesh number',()=>{assert.equal(whatsappNumber('+8801712345678'),'8801712345678');assert.equal(whatsappNumber('01712345678'),'');assert.equal(whatsappNumber(''), '');assert.equal(normalizePhone('01712345678'),'8801712345678')});
test('order draft includes customer details, item quantities and subtotal',()=>{const cart=[{id:products[0].id,qty:2},{id:products[1].id,qty:1}];const msg=makeOrderMessage({name:'Amina',phone:'01712345678',address:'Chattogram, Bangladesh',notes:'Blue colour'},cart,products);assert.match(msg,/Amina/);assert.match(msg,/Chattogram/);assert.match(msg,/Blue colour/);assert.match(msg,/2 ×/);assert.match(msg,/Product subtotal:/);assert.match(msg,/Delivery fee: To be confirmed/);assert.match(msg,/not confirmed|before accepting this order/);const url=whatsappLink('8801712345678',msg);assert.equal(new URL(url).hostname,'wa.me');assert.equal(new URL(url).searchParams.get('text'),msg)});
