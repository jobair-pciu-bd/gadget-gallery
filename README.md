# Gadget Gallery — website owner guide

**Gadget Gallery** · *Smart Gadgets. Smart Choice.*  
Mobile accessories • Bangladesh • ৳ BDT

A professional, fully static website with no hosting bill, no database, no terminal setup, and no online payment integration. Manage the store using only **GitHub.com** on your browser.

> **IMPORTANT BEFORE LAUNCH:** The 8 initial products, illustrations, prices, specifications, availability and policies are **DEMONSTRATION DATA**, not verified offers. WhatsApp, Facebook and email are initially blank. Customers cannot use WhatsApp checkout until you enter your real number. Replace and verify everything before advertising the store.

## 1. Website, repository and setup

This project is prepared for the GitHub repository **`jobair-pciu-bd/gadget-gallery`**.

- **Website once GitHub Pages is enabled and deployment succeeds:** `https://jobair-pciu-bd.github.io/gadget-gallery/`
- **Repository:** `https://github.com/jobair-pciu-bd/gadget-gallery`
- **Deployment status:** Repository → **Actions** → **Deploy Gadget Gallery to GitHub Pages**.
- **Editable product file:** `data/products.json`
- **Editable business settings:** `data/settings.json`

**First-time Pages activation (GitHub website):**

1. Open the repository link above and select **Settings**.
2. In the left menu, select **Pages** (under Code and automation).
3. Under **Build and deployment**, choose **Source → GitHub Actions**. Save if required.
4. Open the **Actions** tab, choose **Deploy Gadget Gallery to GitHub Pages**, and click **Run workflow → main → Run workflow**.
5. Wait for a **green checkmark** for both `build` and `deploy` jobs. Then click the website URL in the deployment or the Pages settings screen.

If Pages was already correctly configured, a push to `main` starts deployment automatically. Green GitHub deployment plus opening the live URL are required to confirm publication; committing alone is not proof of a live website.

### First things to update before launch

1. Enter your real WhatsApp number and Facebook Page URL in `data/settings.json`.
2. Update the email, delivery details, actual return/refund terms, privacy notice and address/service area in the same file.
3. Remove or replace all demo products and prices, confirm compatibility and stock, and upload actual images.
4. Replace the announcement text that says the site is a preview. Only launch live sales after making the catalog accurate.

## 2. Add a product without editing JSON (easy method)

1. Open the repository and select the **Actions** tab.
2. On the left choose **Add or update product (no code)**.
3. Click **Run workflow** and choose branch `main`.
4. For `operation`, choose **add**.
5. Enter the product name, category, and price (e.g. `990`, **not** `৳990`). Other fields are optional: ID will be generated from the name. Choose `in-stock` only when you have confirmed available stock; otherwise, newly added products default to out-of-stock.
6. For `image_path`, you can leave it blank and use the generic placeholder for now, or upload an image first (see section 5) and enter its path.
7. For badges, enter `featured`, `new`, `featured,new`, or `none`.
8. Click the green **Run workflow** button. Open the workflow run: `edit`, `build` and `deploy` should all finish with green checkmarks.

**Important:** GitHub Actions-created commits normally do not trigger other workflows; this particular product form contains **its own deployment job**, so the live website still updates.

The form creates default editable specifications of `"Details": "To be confirmed"`. For richer specifications or multiple images, use the JSON edit method below.

## 3. Change a product's price or stock without editing JSON

Use the **same Actions form**, select **update**, and type the existing product ID (for example, `magnetic-clear-case`). Leave other fields blank to keep their existing values.

- Change price: enter just the new number in **price**.
- Out of stock: select **out-of-stock** in **stock_status**.
- Back in stock: select **in-stock** only after verifying inventory.
- Remove original price: enter `none` in **original_price**.
- Change image: first upload an image, then enter its path in **image_path**.
- Do not overwrite existing badges unless you enter a replacement list.

## 4. Edit products in GitHub (full control)

1. Repository → **Code** → `data` → `products.json`.
2. Click the **pencil icon** (`Edit this file`).
3. For an existing product, change `"price": 490` to the correct BDT price or `"in_stock": true` to `false`.
4. Click **Commit changes...**, use `main`, and confirm.
5. Open **Actions** to watch validation and deployment.

**Add a full product** by copying a complete `{ ... }` object inside the JSON array, changing at least its `id`, `name`, `price`, `category`, `images`, and details. Each product has:

```json
{
  "id": "blue-charging-cable",
  "name": "Blue Charging Cable",
  "category": "Cables",
  "price": 390,
  "original_price": 490,
  "images": ["assets/images/products/blue-charging-cable.jpg"],
  "description": "Verified description goes here.",
  "specifications": {"Length": "1 metre", "Connector": "USB-C"},
  "in_stock": true,
  "featured": false,
  "new_arrival": true
}
```

The previous entry needs a comma before the new one. The last entry must not have a trailing comma. Prices are **numbers without a currency symbol or commas**. Original price may be `null`. Stock/featured/new-arrival are `true` or `false`, not quoted. An uploaded local image path must exist or validation will stop the deployment to prevent broken catalog data. Invalid edits do not replace the current live site.

To remove a demo product, delete its entire `{ ... }` object from `products.json` (and adjust any commas). You can also use GitHub's **Edit** option with a browser on your phone.

## 5. Upload product images on GitHub.com

1. Repository → **Code** → `assets` → `images` → `products`.
2. Click **Add file → Upload files**.
3. Drag your JPG, PNG, WebP or SVG image onto the page. Prefer a square WebP or JPG, compressed and under about 300 KB, e.g. `blue-cable.webp`.
4. Click **Commit changes** to `main`.
5. Copy the resulting path, e.g. `assets/images/products/blue-cable.webp`, into the product's `images` list or the product management form.

Keep file names lowercase with no spaces. You may list multiple images in JSON; the initial storefront uses the first as its primary product image. If an image cannot load, a neutral fallback is shown. Images are for demonstration only until replaced with actual merchandise photos.

## 6. Change WhatsApp number, Facebook, email or message

1. Open **Code → data → settings.json** and click the pencil icon.
2. Change these lines, keeping the quotation marks:

```json
"whatsapp_number": "8801712345678",
"facebook_page_url": "https://www.facebook.com/your-real-page",
"contact_email": "you@example.com",
"promo_message": "Browse your latest promotional message here."
```

The number above is **illustrative**, not a real store number. Replace it with your business WhatsApp number in international Bangladesh format: `8801XXXXXXXXX` (no leading `+` required).

3. Commit changes to `main`. A deployment runs automatically.

**If WhatsApp is blank or malformed, checkout stays disabled.** The cart will still work, but customers will be told contact information has not been configured. Customer details are never automatically sent to a server; the customer must send the generated WhatsApp draft to request an order. The store must manually confirm order, price, stock, delivery and payment.

## 7. Update your logo and homepage banner

- **Header logo mark:** upload/replace `assets/images/mark.svg`.
- **Browser favicon:** upload/replace `assets/images/favicon.svg`.
- **Homepage hero illustration/banner:** replace `assets/images/hero-banner.svg` with your own **SVG** artwork (same filename). To use JPG or PNG instead, update the path once in `assets/js/app.mjs` where `hero-banner.svg` is referenced; or convert your file to SVG.
- **Facebook share image:** replace `assets/images/share-card.png` with a 1200 × 630 PNG. The build workflow automatically sets its full GitHub Pages URL in Open Graph tags.
- Images are stored in GitHub, so replacement needs no local tools. Click the file and use the browser's upload/replace workflow (you may delete old files via GitHub before uploading a replacement with the same name).

## 8. Delivery, returns, privacy and FAQ

Edit `data/settings.json` only. Sections `delivery`, `returns`, and `privacy` each have a `summary` and a `details` array. The `faq` array holds question/answer pairs. Replace each sample statement with actual business policies **before accepting live customer orders**. Avoid offering unverified warranties, guaranteed delivery dates, or unconditional refunds.

## 9. Check automatic publishing / fix a failed deployment

All commits to `main` trigger **Deploy Gadget Gallery to GitHub Pages** automatically:

**Validate JSON → run JavaScript tests → generate pages and sitemap → upload site → deploy.**

Manual product form runs the same validations and deploys within that workflow.

1. Repository → **Actions** → click the latest run (red X for a failure).
2. Click the failed job, then expand the red step to read the exact error.
3. If **Validate product catalog and settings** fails, revisit your recent JSON edit: check syntax, price types, image paths, missing fields and unique IDs.
4. If **Configure GitHub Pages** or **Publish GitHub Pages** fails, open **Settings → Pages** and select **GitHub Actions** as the Source. Ensure repository is public and Actions workflows are enabled.
5. After fixing the problem, commit the corrected file. Alternatively use **Actions → Deploy Gadget Gallery to GitHub Pages → Run workflow**.
6. On success, open the site and hard-refresh the browser if you are still seeing an old cached page.

If GitHub displays an `Error: Resource not accessible by integration`, review **Settings → Actions → General** and repo permissions; the included workflows already request read contents plus `pages: write` and `id-token: write` on deployment jobs.

## 10. Website sections and shopping behavior

- Home page, category tiles, featured/new items, banner and WhatsApp contact.
- Shop with text search, category filters and price sorting.
- Shareable product pages built as static HTML with unique titles/descriptions and social tags.
- Cart saved in this browser's `localStorage`; quantity changes and subtotals in BDT; no cross-device synchronization.
- Required name, Bangladesh mobile number and delivery address before WhatsApp checkout; optional note.
- Delivery is deliberately **excluded from subtotal** until seller confirmation; no fake order number is generated.
- About, contact, FAQ, delivery, returns, privacy and sitemap.
- No accounts, cookies for analytics, database, payments, stock syncing, order management or automatic fulfillment.

**Important practical limitation:** A static WhatsApp-only shop cannot prove a message was actually sent, automatically reserve stock, confirm delivery, or process payments. You must review and confirm each enquiry manually on WhatsApp.

## 11. Project files

```text
index.html, shop.html, product.html, cart.html
about.html, contact.html, faq.html, delivery.html, returns.html, privacy.html
data/settings.json               ← all business settings and policy text
/data/products.json              ← all products
assets/css/styles.css            ← design
assets/js/app.mjs                ← website interactions
assets/js/core.mjs               ← cart, search, WhatsApp functions
assets/images/                  ← logo, banner, product images
scripts/validate.py              ← checks owner edits
scripts/build.py                 ← creates GitHub Pages-ready _site, SEO product pages
scripts/manage_product.py        ← GitHub Actions add/update form
.github/workflows/deploy.yml     ← auto/manual site publishing
.github/workflows/manage-product.yml ← browser-based product manager + publish
tests/store.test.mjs             ← nine automated checks
archive/previous-index.html     ← archived example test page
```

Source files do not need a JavaScript framework, Node build packages or paid tools. Python and Node are already supplied by GitHub Actions runners; you never need to install them.

## 12. Quick owner checklist

- [ ] Real WhatsApp number configured and verified on a phone.
- [ ] Real Facebook page, email and address/service coverage.
- [ ] All demo product details replaced and supplier stock confirmed.
- [ ] Actual product photos uploaded and linked.
- [ ] Delivery and return/refund policies finalized.
- [ ] Test a full checkout and actually press Send in WhatsApp.
- [ ] Confirm both GitHub Actions jobs are green and open the public website.

Built for **Gadget Gallery — Smart Gadgets. Smart Choice.**
