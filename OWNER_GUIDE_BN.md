# Gadget Gallery — ওয়েবসাইট পরিচালনার বাংলা গাইড

**এই গাইডটি সংরক্ষণ করে রাখুন।** Gadget Gallery-এর পণ্য, দাম, ছবি, স্টক, WhatsApp, Facebook ও ওয়েবসাইটের তথ্য পরিবর্তন করার জন্য এটি ব্যবহার করুন। কোনো সফটওয়্যার ইনস্টল বা কমান্ড চালানোর প্রয়োজন নেই।

- **ওয়েবসাইট:** https://jobair-pciu-bd.github.io/gadget-gallery/
- **GitHub রিপোজিটরি:** https://github.com/jobair-pciu-bd/gadget-gallery
- **পণ্য যোগ/পরিবর্তনের ফর্ম:** https://github.com/jobair-pciu-bd/gadget-gallery/actions/workflows/manage-product.yml
- **পণ্যের তথ্য:** https://github.com/jobair-pciu-bd/gadget-gallery/blob/main/data/products.json
- **পণ্যের ছবি:** https://github.com/jobair-pciu-bd/gadget-gallery/tree/main/assets/images/products
- **দোকানের সেটিংস:** https://github.com/jobair-pciu-bd/gadget-gallery/blob/main/data/settings.json
- **ডিপ্লয়মেন্ট অবস্থা:** https://github.com/jobair-pciu-bd/gadget-gallery/actions
- **GitHub Pages সেটিংস:** https://github.com/jobair-pciu-bd/gadget-gallery/settings/pages

> **সতর্কতা:** শুরুতে থাকা ৮টি পণ্য, দাম, স্টক ও ছবি শুধুই নমুনা। সত্যিকারের পণ্য, মূল্য, ছবি, নীতিমালা ও যোগাযোগের তথ্য দিয়ে পরিবর্তন না করা পর্যন্ত ওয়েবসাইটকে বিক্রির জন্য প্রস্তুত ধরে নেবেন না।

## ১. পণ্যের দাম পরিবর্তন — সবচেয়ে সহজ পদ্ধতি

উদাহরণ: Magnetic Clear Phone Case পণ্যের নমুনা মূল্য ৪৯০ টাকা থেকে ৫৫০ টাকা করবেন।

1. উপরের **পণ্য যোগ/পরিবর্তনের ফর্ম** লিংকে যান।
2. GitHub-এ লগইন করা থাকলে **Run workflow** বাটনে ক্লিক করুন।
3. Branch হিসেবে **main** রাখুন।
4. **operation** = **update** নির্বাচন করুন।
5. **product_id** = **magnetic-clear-case** লিখুন।
6. **price** = **550** লিখুন। টাকার চিহ্ন (৳) বা কমা লিখবেন না।
7. **stock_status** = **keep** রাখুন। অন্য কোনো তথ্য বদলাতে না চাইলে অন্য ফিল্ড ফাঁকা রাখুন।
8. সবশেষে সবুজ **Run workflow** বাটনে ক্লিক করুন।
9. চালু হওয়া workflow-তে **edit**, **build**, **deploy** ধাপগুলো সবুজ চেক চিহ্ন হলে ওয়েবসাইট খুলে দাম মিলিয়ে দেখুন।

**মনে রাখবেন:** product_id হলো পণ্যের স্থায়ী পরিচয়। পণ্যের নাম নয়, সঠিক ID ব্যবহার করুন। যেমন magnetic-clear-case, fast-charge-adapter, braided-usbc-cable। সব ID দেখতে পণ্যের তথ্যের লিংক খুলুন।

## ২. নতুন পণ্য যোগ করা

1. প্রথমে পণ্যের আসল ছবি আপলোড করে রাখুন (৩ নম্বর অধ্যায়)।
2. **পণ্য যোগ/পরিবর্তনের ফর্ম** খুলে **Run workflow** চাপুন।
3. **operation** = **add** দিন।
4. **product_id**-তে ছোট ইংরেজি অক্ষর, সংখ্যা ও হাইফেন দিয়ে ইউনিক ID লিখুন; যেমন premium-usbc-cable। চাইলে ফাঁকা রাখলে নাম থেকে ID বানানো হবে।
5. **name** = পণ্যের পূর্ণ নাম; যেমন Premium USB-C Charging Cable।
6. **category** = যেমন Cables, Chargers, Phone Cases, Earbuds, Power Banks, Screen Protectors, Stands।
7. **price** = যেমন 450 (শুধু সংখ্যা, BDT)।
8. **original_price** = যেমন 600; আগের দাম দেখাতে না চাইলে ফাঁকা রাখুন।
9. **image_path** = যেমন assets/images/products/premium-usbc-cable.webp (ছবিটি আগে GitHub-এ আপলোড থাকতে হবে)।
10. **description**-এ যাচাই করা পণ্যের বিবরণ লিখুন।
11. **stock_status**-এ **in-stock** (নিশ্চিতভাবে মজুত থাকলে) অথবা **out-of-stock** দিন। নতুন পণ্যের ডিফল্ট out-of-stock।
12. **badges**-এ featured / new / featured,new / none লিখুন।
13. সবুজ **Run workflow** চাপুন। তারপর edit → build → deploy সফল হয়েছে কি না দেখুন।

**সীমাবদ্ধতা:** এই সহজ ফর্মে একটি ছবি সেট করা যায়; নতুন পণ্যের বিস্তারিত specifications ডিফল্টভাবে “To be confirmed” থাকে। একাধিক ছবি বা বিস্তারিত স্পেসিফিকেশন যোগ করতে ৫ নম্বর অধ্যায়ের JSON পদ্ধতি ব্যবহার করুন।

## ৩. পণ্যের ছবি আপলোড বা পরিবর্তন

**ধাপ A — ছবি GitHub-এ আপলোড**

1. **পণ্যের ছবি** লিংকে যান।
2. **Add file → Upload files** ক্লিক করুন।
3. আপনার ফোন বা কম্পিউটার থেকে ছবি নির্বাচন করুন।
4. সহজ ইংরেজি ফাইলনাম দিন, যেমন clear-case-blue.webp। ছোট হাতের অক্ষর, কোনো স্পেস নয়।
5. সম্ভব হলে বর্গাকার JPG/WebP ছবি, পরিষ্কার ব্যাকগ্রাউন্ড এবং প্রায় ১০০০×১০০০ পিক্সেল রাখুন; ফাইল ছোট রাখলে সাইট দ্রুত লোড হবে।
6. **Commit changes** দিয়ে main শাখায় সংরক্ষণ করুন।

**ধাপ B — ছবিটি পণ্যের সঙ্গে যুক্ত করুন**

1. **পণ্য যোগ/পরিবর্তনের ফর্ম** খুলুন।
2. **operation** = update এবং **product_id**-তে সংশ্লিষ্ট ID দিন।
3. **image_path**-এ সম্পূর্ণ পথ লিখুন, যেমন **assets/images/products/clear-case-blue.webp**।
4. **stock_status** = keep এবং অন্য অপরিবর্তিত ফিল্ডগুলো ফাঁকা রাখুন।
5. **Run workflow** দিয়ে চালান এবং প্রকাশের পর সাইটে ছবি দেখুন।

**খেয়াল রাখবেন:** ফাইলের নাম এবং পথ হুবহু মিলতে হবে, বড়/ছোট অক্ষরসহ। নতুন ছবির জন্য নতুন ফাইলনাম ব্যবহার করলে পুরোনো browser cache-এর সমস্যা কম হয়। এই ফর্মে ছবি পরিবর্তন করলে আগের images তালিকার জায়গায় নতুন একটি ছবি বসবে।

## ৪. পণ্য স্টকে আছে / নেই — কীভাবে বদলাবেন

1. পণ্য পরিবর্তনের ফর্মে **operation** = update দিন।
2. সংশ্লিষ্ট **product_id** লিখুন।
3. **stock_status** নির্বাচন করুন:
   - **in-stock**: পণ্য বিক্রির জন্য আছে।
   - **out-of-stock**: পণ্য শেষ / আপাতত বিক্রি নয়।
   - **keep**: আগের স্টক অবস্থা অপরিবর্তিত।
4. Run workflow চাপুন এবং ডিপ্লয়মেন্ট দেখুন।

**গুরুত্বপূর্ণ:** WhatsApp-এ অর্ডার এলে ওয়েবসাইট নিজে স্টক কমায় না। বিক্রি হলে আপনাকেই স্টক অবস্থা হালনাগাদ করতে হবে।

## ৫. পণ্যের তথ্য, একাধিক ছবি, স্পেসিফিকেশন বা পণ্য মুছতে চাইলে

1. **পণ্যের তথ্য** লিংক খুলুন। এটি data/products.json ফাইল।
2. ডান পাশে **পেন্সিল (Edit this file)** চিহ্নে ক্লিক করুন।
3. পণ্য খুঁজে সঠিক ঘরের মান বদলান:
   - **price**: বিক্রয়মূল্য, যেমন 550
   - **original_price**: আগের মূল্য, যেমন 650; না থাকলে null
   - **images**: ছবির পথের তালিকা
   - **in_stock**: true অথবা false
   - **featured**: true অথবা false
   - **new_arrival**: true অথবা false
   - **description**: পণ্যের বিবরণ
   - **specifications**: পণ্যের সত্যিকারের তথ্য
4. পণ্য মুছতে তার সম্পূর্ণ তথ্যের অংশ সরান; মাঝখানের কমা সঠিক আছে কি না দেখুন।
5. **Commit changes** দিয়ে main-এ সংরক্ষণ করুন।
6. Actions-এ **Deploy Gadget Gallery to GitHub Pages** সফল হয়েছে কি না দেখুন।

**JSON সতর্কতা:** price-এর পাশে ৳ বা কমা লিখবেন না; true/false এবং null-এর চারপাশে উদ্ধৃতি চিহ্ন দেবেন না। লেখার ভেতরের ডাবল কোটেশন ও কমার নিয়ম ঠিক রাখতে হবে। ভুল হলে GitHub-এর validation ডিপ্লয়মেন্ট আটকে দেবে, যাতে ভুল তথ্য লাইভ না হয়।

## ৬. WhatsApp, Facebook, ইমেইল, ঠিকানা বা অফার পরিবর্তন

1. **দোকানের সেটিংস** লিংক খুলুন (data/settings.json)।
2. **Edit this file** ক্লিক করুন।
3. প্রয়োজনমতো এই ফিল্ডগুলোর মান বদলান:
   - **whatsapp_number** = 8801XXXXXXXXX (বাংলাদেশের আন্তর্জাতিক ফরম্যাট; উদাহরণ নম্বর নয়, আপনার আসল নম্বর দিন)
   - **facebook_page_url** = আপনার Facebook পেজের সম্পূর্ণ https:// লিংক
   - **contact_email** = আপনার ব্যবসার ইমেইল
   - **service_area** = কোন এলাকায় সেবা দেন
   - **business_address** = ব্যবসার বাস্তব ঠিকানা/অনলাইন স্টোরের বিবরণ
   - **promo_message** = হোমপেজের প্রচারণার লেখা
   - **announcement** = উপরের ঘোষণা
4. একই ফাইলে **delivery**, **returns**, **privacy** এবং **faq**-এর প্রকৃত নীতিমালা লিখুন।
5. শুধু সংশ্লিষ্ট লাইনগুলো পরিবর্তন করে **Commit changes** দিন। পুরো ফাইল মুছে নতুন কয়েকটি লাইন বসাবেন না।
6. Actions-এ সফল ডিপ্লয়মেন্ট দেখুন।

**বিশেষভাবে জরুরি:** WhatsApp নম্বর এখন ফাঁকা থাকলে WhatsApp checkout চালু হবে না। বিক্রির আগে বাস্তব নম্বর এবং ডেলিভারি/রিটার্ন নীতিমালা সেট করুন।

## ৭. লোগো, ব্যানার ও Facebook share ছবির পরিবর্তন

ছবিগুলো assets/images ফোল্ডারে আছে।

- **mark.svg** = হেডারের লোগো চিহ্ন
- **favicon.svg** = ব্রাউজারের ছোট আইকন
- **hero-banner.svg** = হোমপেজের প্রধান ছবি
- **share-card.png** = Facebook-এ ওয়েবসাইটের লিংক শেয়ার করার প্রিভিউ

বর্তমান mark, favicon এবং hero banner হলো SVG ফাইল। একই নাম ও সঠিক SVG ফরম্যাটে প্রতিস্থাপন করলে কোড বদলাতে হবে না। শুধু JPG/PNG ছবির নাম পাল্টে .svg করা যাবে না। ব্যানারের জন্য JPG/PNG ব্যবহার করতে চাইলে assets/js/app.mjs-এ hero-banner.svg রেফারেন্সও একবার বদলাতে হবে।

## ৮. একজন ক্রেতা কীভাবে অর্ডার করবেন

1. ক্রেতা ওয়েবসাইটে পণ্য দেখবেন ও **Add to Cart** চাপবেন।
2. Cart-এ পরিমাণ বদলাতে পারবেন।
3. নাম, মোবাইল নম্বর এবং ডেলিভারি ঠিকানা লিখবেন।
4. **Place Order via WhatsApp** চাপলে অর্ডারের খসড়া মেসেজ WhatsApp-এ খুলবে।
5. ক্রেতাকে নিজে WhatsApp-এ **Send** করতে হবে।
6. আপনি মেসেজ পেয়ে দাম, স্টক, ডেলিভারি ফি, পেমেন্ট পদ্ধতি ও ডেলিভারি সময় নিশ্চিত করবেন।

**মনে রাখবেন:** WhatsApp খুললেই অর্ডার নিশ্চিত হয় না। ওয়েবসাইটের cart-এ শুধু পণ্যের subtotal থাকে; ডেলিভারি চার্জ যোগ হয় না। এটি ডাটাবেস ছাড়া static দোকান; অর্ডার ট্র্যাকিং, পেমেন্ট, স্টক কমানো বা কুরিয়ার বুকিং স্বয়ংক্রিয় নয়।

## ৯. পরিবর্তন ওয়েবসাইটে পৌঁছেছে কি না যাচাই

1. **ডিপ্লয়মেন্ট অবস্থা** লিংক খুলুন।
2. সংশ্লিষ্ট সর্বশেষ workflow রান খুলুন।
3. edit (পণ্য ফর্মের ক্ষেত্রে), build ও deploy ধাপে সবুজ টিক আছে কি না দেখুন।
4. সফল হলে আসল ওয়েবসাইট খুলে পণ্য/দাম/ছবি মিলিয়ে দেখুন।
5. লাল X দেখালে ব্যর্থ ধাপ খুলে এরর পড়ুন। প্রাথমিক কারণ হতে পারে ভুল JSON, ভুল ছবির পথ, অবৈধ দাম, বা GitHub Pages সেটিংস।
6. GitHub Pages সেটিংসে গিয়ে **Build and deployment → Source → GitHub Actions** নির্বাচন করুন।
7. সমস্যা ঠিক করার পর আবার main-এ Commit করুন; অথবা **Deploy Gadget Gallery to GitHub Pages → Run workflow** দিন।

**শুধু Commit হয়েছে মানেই ওয়েবসাইট আপডেট হয়েছে—এমন নয়।** সফল deployment এবং লাইভ সাইট খুলে মিলিয়ে দেখা জরুরি।

## ১০. প্রতিদিন ও প্রতি সপ্তাহে করণীয়

**প্রতিদিন:** WhatsApp মেসেজ দেখুন, স্টক যাচাই করুন, বিক্রি শেষ হলে out-of-stock দিন, অর্ডার নিশ্চিত করুন, প্রয়োজন হলে দাম বদলান।

**নতুন পণ্য এলে:** সঠিক ছবি → GitHub-এ আপলোড → Add product ফর্ম → মূল্য/স্টক যাচাই → ডিপ্লয়মেন্ট পরীক্ষা করুন।

**প্রতি সপ্তাহে:** সব মূল্য, স্টক, বিবরণ, ফোনের compatibility, delivery/return নীতিমালা ও লিংক ঠিক আছে কি না পরীক্ষা করুন।

## ১১. দ্রুত মনে রাখার তালিকা

| কী পরিবর্তন করবেন | কোথায় যাবেন |
| --- | --- |
| দাম | Actions → Add or update product (no code) → update |
| নতুন পণ্য | Actions → Add or update product (no code) → add |
| পণ্যের ছবি | assets/images/products → Upload files; তারপর Product form → image_path |
| স্টক | Product form → stock_status |
| WhatsApp ও Facebook | data/settings.json |
| ডেলিভারি ও রিটার্ন পলিসি | data/settings.json |
| একাধিক ছবি বা স্পেসিফিকেশন | data/products.json |
| পণ্য মুছে ফেলা | data/products.json |
| লোগো/ব্যানার | assets/images |
| প্রকাশ/সমস্যা পরীক্ষা | Actions |
| সাইট প্রকাশের প্রাথমিক সেটিং | Settings → Pages → GitHub Actions |

**Gadget Gallery · Smart Gadgets. Smart Choice.**
