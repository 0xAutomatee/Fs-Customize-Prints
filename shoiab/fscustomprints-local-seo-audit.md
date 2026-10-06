# Local SEO Audit & Action Plan: fscustomprints.com

**Business:** FS Custom Prints (Lahore, Pakistan) | **Platform:** WordPress + WooCommerce + Elementor (Xtemos/Woodmart-style theme) + Rank Math SEO
**Audit date:** 2026-10-06
**Method note:** Based on the live homepage, contact page, sitemaps and one product page (Custom Polo Shirts). Alt text and meta data were read through a text conversion, so confirm in the browser (View Source) or Screaming Frog before editing. The product-page findings are assumed to repeat on the other products because they use the same template; spot-check that.

---

## 1. Critical issues (fix first)

| # | Issue | Evidence | Fix |
|---|-------|----------|-----|
| 1 | **Contact page shows demo data** | Address "13 Ridge Square NW, Washington, DC", phone +1 202-853-9050, email xtemos.studio@mail.com, Contact Form 7 placeholder | Replace with real Lahore address, +92 phone/WhatsApp, business email. This breaks NAP, which is the core of local SEO. |
| 2 | **~90 theme demo pages are indexed in the sitemap** | `/home-1/` to `/home-8/`, `/module-*`, `/shop-item-style-*`, `/blog-grid-*`, `/sample-page/`, `/test/`, `/a/`, `/sd/`, `/elementor-21703/`, duplicate cart/checkout/my-account/wishlist | Delete them (or set noindex and remove from the sitemap). They are thin and duplicate content and dilute crawl budget. Keep only Home, About, Contact, Shop, Privacy, FAQ, Refund, Testimonials. |
| 3 | **Homepage meta description is broken** | "...Your Brand. Perfect for fans of the iconic" (cut off, stray gaming text) | Rewrite (see section 3). |
| 4 | **Stray gaming text on the site** | Homepage references unrelated to the business | Remove demo copy. |
| 5 | **No Product / LocalBusiness / Organization schema detected** | Product page has none visible | Configure Rank Math (see section 5). |
| 6 | **Product pages: no meta description, no price, no reviews, ~85-word descriptions** | Custom Polo Shirts page | See sections 4 and 6. |
| 7 | **Empty "Customer Reviews" block** | No reviews or ratings | Collect Google reviews and product reviews. |

---

## 2. Local SEO checklist (Lahore)

### Google Business Profile (GBP)
- [ ] Claim or verify the profile. Name exactly **FS Custom Prints** (no keyword stuffing).
- [ ] Primary category: *Custom t-shirt store* or *Embroidery service*. Secondary: *Uniform store*, *Screen printer*, *Corporate gift supplier*, *Promotional products supplier*.
- [ ] Add the service area (Lahore areas: Gulberg, DHA, Johar Town, Model Town, Bahria Town, Faisal Town, Township, Iqbal Town, Shadman, Wapda Town, etc.).
- [ ] The footer lists **two office locations**. Create a separate GBP for each only if staffed and open to the public. Otherwise use one profile plus service-area listings.
- [ ] Add hours, WhatsApp, website link (UTM-tagged), appointment/quote link.
- [ ] Add each product as a GBP Product/Service with a description and image.
- [ ] Upload 20+ real photos: shop front, machines, finished uniforms, team. Add new photos weekly.
- [ ] Post updates weekly (offers, new work, "Free Design Mockup in 24 hours").
- [ ] Turn on Q&A and seed 10 questions (minimum order, delivery, embroidery pricing).
- [ ] Review goal: 25+ reviews in 60 days. Use a WhatsApp review-link message after each delivered order and reply to every review.

### NAP consistency
- [ ] Use one exact Name, Address, Phone format everywhere: website header, footer, contact page, GBP, Instagram, Facebook and directories.
- [ ] Wrap the footer NAP in a clickable `tel:` link and a Google Maps link.

### Citations (Pakistan and global)
Cybo, Yellow Pages Pakistan, Pakistan Business Directory, OLX Business, Facebook Page, Instagram bio, LinkedIn, Bing Places, Apple Business Connect, Foursquare, Hotfrog, Yelp (if available), Clutch/Sortlist (if B2B), Lahore Chamber of Commerce listing. Keep NAP identical.

### Website local signals
- [ ] "Lahore" in the title, H1 and first 100 words of the homepage and every service/category page.
- [ ] Embed a Google Map on the contact page and footer.
- [ ] Add a "Locations / Areas we serve" section with unique content for each area, or separate landing pages (see section 7).
- [ ] Fix the `locations.kml` sitemap in Rank Math Local SEO with the real coordinates.
- [ ] Add opening hours and the service area in schema.
- [ ] Set up the robots.txt sitemap reference and submit to Google Search Console and Bing Webmaster Tools.

---

## 3. Sitewide title and meta templates

**Homepage**
- Title (≤60 chars): `Custom Uniforms, T-Shirt Printing & Embroidery in Lahore | FS Custom Prints`
- Meta (≤155): `FS Custom Prints in Lahore: custom uniforms, t-shirt printing, embroidery & corporate gifts. Free design mockup in 24 hrs. Order from 1 piece. WhatsApp us.`

**Product title pattern:** `{Product} in Lahore | Bulk & Custom | FS Custom Prints`
**Product meta pattern:** `Order {product} in Lahore with your logo. {Key benefit}. Free mockup in 24 hrs, bulk discounts, delivery across Pakistan. Get a quote on WhatsApp.`

Use the Rank Math title/description variables (`%title%`, `%sep%`, `%sitename%`) as a default template under Rank Math > Titles & Meta > Products, then override per product.

---

## 4. Per-product SEO list

Fix on **every** product (all 38 currently in the sitemap; the product sitemap lists 38 entries):

1. Unique title tag with focus keyword and "Lahore".
2. Meta description (150-155 chars) with a CTA.
3. Clean slug (the current slugs are already good, so keep them).
4. 300-600 word description: materials, sizes, printing method, MOQ, turnaround, pricing guide, delivery.
5. Short description above the fold with the main keyword.
6. Image alt text, descriptive file names, compressed WebP, 3-5 images per product.
7. Product schema (price or "from" price, availability, brand, SKU, reviews).
8. FAQ block (3-5 questions) with FAQPage schema.
9. Internal links to the parent category, 3-4 related products and the contact/quote page.
10. A visible price or "Starting from PKR ___" with a quote button and WhatsApp CTA.
11. Breadcrumbs with schema (Home > Category > Product).

### Product table (suggested focus keyword, title, meta and alt text)

Alt text pattern: `{what it is} with {logo/print method} for {use}, {Lahore}`. Write it as a plain description, no keyword stuffing, and give each image a different alt.

#### A. Uniforms
| Product (URL slug) | Focus keyword | Suggested title | Suggested alt text (main image) |
|---|---|---|---|
| custom-polo-shirts | custom polo shirts Lahore | Custom Polo Shirts in Lahore with Logo \| FS Custom Prints | Navy custom polo shirt with embroidered company logo, Lahore |
| custom-collar-polo-shirts | collar polo shirts with logo Lahore | Custom Collar Polo Shirts Lahore, Bulk Orders | Contrast collar polo shirt with embroidered chest logo |
| corporate-shirts | corporate shirts Lahore | Corporate Shirts & Office Uniforms in Lahore | Folded white corporate shirt with embroidered company logo |
| industrial-staff-uniforms | industrial staff uniforms Lahore | Industrial & Staff Uniforms Manufacturer in Lahore | Factory staff wearing branded industrial uniform shirts and trousers |
| restaurant-cafe-uniforms | restaurant uniforms Lahore | Restaurant & Café Uniforms (Aprons, Shirts) Lahore | Waiter and chef in branded café uniform and apron |
| safety-vests | safety vests with logo Lahore | Custom Printed Safety Vests in Lahore | Hi-vis orange safety vest with reflective strips and printed logo |
| school-university-uniforms | school uniforms Lahore | School & University Uniforms Lahore, Bulk | Students in matching school uniform polo shirts with crest |
| hoodies-sweatshirts | custom hoodies Lahore | Custom Hoodies & Sweatshirts Printing Lahore | Black custom hoodie with front print, folded |
| custom-sports-kits | custom sports kits Lahore | Custom Sports Kits & Jerseys in Lahore | Sublimation football team jersey set with names and numbers |
| corporate-sublimation-sports-kits | sublimation sports kits Lahore | Corporate Sublimation Sports Kits Lahore | Sublimation printed corporate cricket kit with company branding |

#### B. T-shirt printing
| Product | Focus keyword | Suggested title | Suggested alt |
|---|---|---|---|
| custom-t-shirts | custom t-shirts Lahore | Custom T-Shirts Printing in Lahore, From 1 Piece | Custom printed round-neck t-shirt with brand logo on chest |
| custom-printed-t-shirts | custom printed t-shirts Lahore | Custom Printed T-Shirts Lahore, Low MOQ | Stack of custom printed t-shirts in assorted colours |
| bulk-t-shirt-printing | bulk t-shirt printing Lahore | Bulk T-Shirt Printing in Lahore, Wholesale Rates | Bulk order of printed team t-shirts packed for delivery |
| specialty-t-shirt-printing | DTF / specialty t-shirt printing Lahore | Specialty T-Shirt Printing (DTF, Puff, Reflective) Lahore | Close-up of DTF printed design on a cotton t-shirt |
| graphic-trending-t-shirts | graphic t-shirts Pakistan | Graphic & Trending T-Shirts Pakistan | Streetwear graphic t-shirt with trending print design |
| oversized-baggy-printed-t-shirts | oversized t-shirts Lahore | Oversized & Baggy Printed T-Shirts Lahore | Model wearing oversized baggy printed t-shirt |
| brand-private-label-t-shirts | private label t-shirts Pakistan | Private Label T-Shirts Manufacturer Pakistan | Custom neck label and tag on private label t-shirt |

#### C. Embroidery
| Product | Focus keyword | Suggested title | Suggested alt |
|---|---|---|---|
| logo-business-embroidery | logo embroidery Lahore | Logo & Business Embroidery Service in Lahore | Embroidery machine stitching a company logo on a polo shirt |
| bulk-embroidery-services | bulk embroidery Lahore | Bulk Embroidery Services in Lahore | Rows of embroidered shirts ready for bulk delivery |
| uniform-embroidery | uniform embroidery Lahore | Uniform Embroidery in Lahore | Embroidered name and logo on staff uniform |
| custom-apparel-embroidery | custom apparel embroidery Lahore | Custom Apparel Embroidery Lahore | Embroidered design on jacket and hoodie |
| cap-patch-badge-embroidery | cap and badge embroidery Lahore | Cap, Patch & Badge Embroidery Lahore | Embroidered patches and badges on a cap |
| personalized-gift-embroidery | personalised embroidery gifts Lahore | Personalised Gift Embroidery Lahore | Towel and handkerchief with embroidered name as a gift |

#### D. Corporate giveaways
| Product | Focus keyword | Suggested title | Suggested alt |
|---|---|---|---|
| corporate-gift-sets | corporate gift sets Lahore | Corporate Gift Sets with Logo in Lahore | Corporate gift set with branded mug, diary and pen |
| custom-gift-boxes-kits | custom gift boxes Lahore | Custom Gift Boxes & Kits Lahore | Branded gift box with welcome kit items |
| custom-drinkware | custom mugs & bottles Lahore | Custom Mugs, Bottles & Drinkware Lahore | Logo printed ceramic mugs and steel bottles |
| custom-pens-stationery | custom pens & stationery Lahore | Custom Pens & Stationery with Logo Lahore | Branded pens and notebooks with company logo |
| custom-keychains | custom keychains Lahore | Custom Keychains Printing Lahore | Metal and acrylic custom logo keychains |
| custom-caps | custom caps Lahore | Custom Caps with Embroidery/Print Lahore | Embroidered baseball caps with company logo |
| promotional-giveaways | promotional giveaways Lahore | Promotional Giveaways & Branded Merchandise Lahore | Assorted promotional items with logo for events |
| employee-client-gifts | employee gifts Lahore | Employee & Client Gift Ideas Lahore | Gift hamper for employees with logo packaging |

#### E. Branding and packaging
| Product | Focus keyword | Suggested title | Suggested alt |
|---|---|---|---|
| business-printing-marketing-materials | business printing Lahore | Business Cards, Flyers & Marketing Print Lahore | Printed business cards, brochures and flyers |
| signboards-outdoor-branding | signboards Lahore | Outdoor Signboards & Branding in Lahore | Illuminated outdoor shop signboard with logo |
| neon-indoor-branding | neon signs Lahore | Neon Signs & Indoor Branding Lahore | Custom LED neon sign on a café wall |
| signboard-maintenance-branding-support | signboard repair Lahore | Signboard Maintenance & Branding Support Lahore | Technician repairing an illuminated signboard |
| restaurant-food-packaging | restaurant food packaging Lahore | Custom Food Packaging for Restaurants Lahore | Branded takeaway boxes and paper bags for a restaurant |
| apparel-fashion-packaging | apparel packaging Lahore | Fashion & Apparel Packaging Lahore | Branded poly mailers and boxes for clothing brands |
| custom-business-packaging | custom packaging Lahore | Custom Business Packaging Lahore | Custom printed packaging boxes with logo |

*Tip: swap the generic description for what the photo actually shows. The alt text above is a template, so edit it to match each real image.*

---

## 5. Images and technical on-page

- [ ] **Alt text:** The audit found multiple images on the product page without alt text. Fill the alt attribute on every product, category, banner and logo image. Decorative images get empty `alt=""`.
- [ ] **File names:** Already descriptive on some (`custom-polo-shirts.webp`). Rename any `IMG_1234`/`image1` files to `custom-polo-shirts-lahore.webp` before upload.
- [ ] **Placeholder images:** Related products show placeholder images. Replace them with real photos of your own work, since stock and placeholder images hurt rankings and conversions.
- [ ] **Compression/size:** WebP, under 150 KB each, 800-1200 px wide. Use lazy loading for below-fold images and set explicit width/height (CLS).
- [ ] **Image titles/captions:** Optional. Keep the title short.
- [ ] **Image sitemap:** Enable in Rank Math so product images are included.
- [ ] **Open Graph / Twitter cards:** Set default OG image (1200x630) in Rank Math.
- [ ] **Favicon and logo:** Real brand logo with alt `FS Custom Prints logo`.
- [ ] **Core Web Vitals:** Run PageSpeed Insights. The theme with Elementor is heavy, so use a caching plugin (LiteSpeed/WP Rocket), minify, remove unused demo CSS.
- [ ] **Headings:** One H1 per page. Add keyword-relevant H2s such as "Why choose FS Custom Prints in Lahore", "Printing methods", "Sizes and colours", "Bulk pricing", "FAQs". Replace the generic "Customer Reviews" and "You may also like" H2s, or keep them but add the others.
- [ ] **Canonical tags:** Confirm each page self-canonicalises. Set canonical for filtered/sorted shop URLs and noindex cart, checkout, my-account, wishlist and compare pages.
- [ ] **robots.txt:** Block `/cart/`, `/checkout/`, `/my-account/`, `?add-to-cart=`, `?orderby=`.
- [ ] **HTTPS, www/non-www redirect, no 404s:** Verify in Search Console.
- [ ] **Breadcrumbs:** Enable Rank Math breadcrumbs with schema.
- [ ] **Mobile:** Test the WhatsApp button, click-to-call, and quote form on phones.

---

## 6. Schema markup (Rank Math)

1. **Local SEO setup** (Rank Math > Titles & Meta > Local SEO): business type *LocalBusiness / ClothingStore* (or ProfessionalService), name, logo, real address, phone, geo coordinates, opening hours, price range, social profiles (Instagram @fscustomprint, Facebook).
2. **Organization / WebSite** schema in the Rank Math global setup.
3. **Product schema** on every product: name, image, description, SKU (e.g. FS-U001), brand, `offers` with `priceCurrency: PKR`. If a price cannot be published, use `priceSpecification` from price or add reviews. Add `aggregateRating` only when genuine reviews exist.
4. **FAQPage schema** on products, categories and the homepage.
5. **BreadcrumbList** schema.
6. Validate with Google's Rich Results Test and Schema Markup Validator.

---

## 7. Content to add

**Location landing pages** (unique content for each, not copy-paste):
- Custom Uniforms in Lahore
- T-Shirt Printing in Lahore
- Embroidery in Lahore
- Corporate Gifts in Lahore
- Optional area pages: Gulberg, DHA, Johar Town, Model Town, Bahria Town, Faisal Town

**Blog topics (target local and informational keywords):**
1. How much does custom t-shirt printing cost in Lahore? (price guide)
2. DTF vs screen printing vs sublimation: which to choose
3. Embroidery vs print for company uniforms
4. How to order corporate uniforms for your company (checklist)
5. Best corporate gift ideas in Lahore for Eid, Ramadan and New Year
6. School uniform ordering guide for Lahore schools
7. How to design a logo for embroidery (file formats, size)
8. Restaurant uniform ideas for cafés in Lahore
9. Case studies with real photos of finished orders

**Other pages:** About Us with a real story and team photos, Testimonials with real names, FAQ (MOQ, turnaround, payment, delivery, mockup), a "Get a Quote" page, Delivery & Returns, Portfolio/Gallery with alt-tagged photos.

---

## 8. Internal linking and site structure

- Home > 5 categories (Uniforms, T-Shirt Printing, Embroidery, Corporate Giveaways, Branding & Packaging) > products.
- Each category page needs 200-400 words of intro text, an H1, a meta title/description and an FAQ.
- Link products to each other (polo shirts <-> embroidery <-> corporate shirts <-> uniform embroidery).
- Use descriptive anchors ("custom polo shirts in Lahore"), not "click here".
- Link blog posts to the matching product and category.
- Remove duplicate "shop-2", "shop-list", "product-categories", "most-viewed-products", etc. unless they're real, used pages.

---

## 9. Reviews and off-page

- Ask each customer for a Google review via WhatsApp (short link).
- Add a testimonials section with real customer logos and photos (with permission).
- Backlinks: local business directories, Lahore chambers/associations, supplier and partner sites, local bloggers, event sponsorships, guest posts on Pakistani business blogs.
- Social: post work photos on Instagram and Facebook and link back. Add geotags and Lahore hashtags.
- Add Instagram feed and link in the footer, with the same NAP.

---

## 10. Tracking

- Google Search Console and Bing Webmaster Tools (submit `sitemap_index.xml`).
- Google Analytics 4 with events for WhatsApp click, phone click, form submit, quote request.
- GBP Insights for calls, directions and website clicks.
- Rank tracking for 15-20 target keywords (e.g. "custom uniforms Lahore", "t-shirt printing Lahore", "embroidery Lahore", "corporate gifts Lahore") using Local Falcon, BrightLocal or a free tracker.

---

## 11. Priority roadmap

**Week 1:** Fix contact page NAP, delete/noindex demo pages, fix homepage title/meta, set up GBP, set up Rank Math Local SEO, submit sitemap.
**Week 2:** Write meta titles/descriptions and alt text for all products (tables above), add Product schema, fix placeholder images.
**Week 3:** Rewrite the top 10 product descriptions (300+ words, FAQs), add the 4 location/service landing pages, embed the map.
**Week 4:** Citations, review campaign, first 2 blog posts, set up tracking.
**Ongoing:** Weekly GBP posts and photos, 2 blog posts a month, review replies, monthly rank and traffic report.

---

# Appendix: Page Inventory (Remove / Improve / Missing)

Based on `page-sitemap.xml` (92 pages) and `product-sitemap.xml` (38 products). Verify each page in WP Admin > Pages before deleting. Set up 301 redirects for any page that has backlinks or traffic.

## A. REMOVE (delete, or noindex + remove from sitemap)

All of these are leftover theme demo pages. They are thin, duplicate and irrelevant, and they waste crawl budget.

| Group | URLs | Action |
|---|---|---|
| Demo homepages | /home-1/ to /home-8/ (home-1, 2, 3, 4, 5, 6, 7, 8) | Delete. Keep only the one real homepage `/`. 301 to `/`. |
| Theme module demos | /module-mini-cart/, /module-tab/, /module-slider/, /module-search/, /module-pricing-table/, /module-menu/, /module-mailchimp/, /module-list-link/, /module-instagram/, /module-info-box/, /module-button/, /module-breadcrumb/, /module-banner-info/, /module-accordion/ | Delete. |
| Shop layout demos | /shop-item-style-1/ to /shop-item-style-12/, /shop-hover-translate/, /shop-hover-zoom-out/, /shop-hover-rotate/, /shop-grid-4-column/, /shop-grid-5-column/, /shop-sidebar-left/, /shop-sidebar-right/, /shop-list/ | Delete. |
| Blog layout demos | /blog-item-style-1/ to /blog-item-style-4/, /blog-grid-2-column/, /blog-grid-4-column/, /blog-gird/, /blog-gird-style-2/, /blog-list/, /blog-list-style-2/, /blog-list-style-3/, /blog-filter-top/ | Delete. Create one real `/blog/` instead. |
| Duplicate WooCommerce pages | /cart-2/, /cart-2-2/, /checkout-2/, /checkout-3/, /my-account-2/, /my-account-3/, /wishlist/, /wishlist-2/, /wishlist-3/ | Delete the duplicates. Keep only one cart, checkout and my-account (the ones assigned in WooCommerce > Settings > Advanced). |
| Duplicate/demo contact, about, FAQ | /contact-page/, /contact-page-v2/, /about-page/, /faqs-v1/, /faqs-v2/ | Merge into one real /contact-us/, /about-us/ and /faq/. 301 the rest. |
| Junk/test pages | /sample-page/, /sample-page-2/, /test/, /a/, /sd/, /elementor-21703/ | Delete. |
| Product list widgets pages | /most-viewed-products/, /best-seller-products/, /recent-products/, /featured-products/, /sale-products/, /top-rated-products/ | Delete or noindex. They duplicate shop content. |
| Duplicate privacy/refund slugs | /privacy-policy-2/, /refund_returns-2/ | Keep one of each with a clean slug (/privacy-policy/, /refund-returns/). 301 the old ones. |
| Comparison/utility | /yith-compare/ | noindex. |

Also noindex (not delete): /cart/, /checkout/, /my-account/, /wishlist/ (the real ones). In Rank Math use *Titles & Meta > Misc / WooCommerce* and remove them from the sitemap.

Also check: tag, author, attachment and date archives, and the empty `post-sitemap.xml`/`category-sitemap.xml` if there are no real posts (remove "Hello world" posts).

**Result:** about 92 pages should drop to roughly 10-12 real ones.

## B. IMPROVE (keep, but content is weak)

| Page | Problem | What to do |
|---|---|---|
| **Homepage `/`** | Truncated meta, generic copy, gaming text, no Lahore-focused H1 | H1 "Custom Uniforms, T-Shirt Printing & Embroidery in Lahore". 600-900 words: services, why choose us, process (mockup > approve > print > deliver), areas served, reviews, FAQ, CTA. Add map and NAP. |
| **/contact-us/** | Demo address, phone and email, placeholder form | Real NAP, Google Map, hours, WhatsApp button, working quote form (file upload for logos), LocalBusiness schema. |
| **/about-us/** | Likely template text | Real story, team and workshop photos, years of experience, machines, clients served, Lahore references. |
| **/testimonials/** | May be empty or demo | Real customer reviews with names, company, photos and Google review links. Add Review schema carefully (genuine reviews only). |
| **/shop-2/ (main shop)** | Probably no intro text | Set one canonical shop page at `/shop/` with 200+ words of intro and links to the 5 categories. |
| **/product-categories/** and the 5 category pages | Likely no descriptions | Each category: H1, 250-400 words, meta, FAQ, internal links to its products. Categories: Custom Uniforms, T-Shirt Printing, Embroidery Services, Corporate Giveaways, Custom Branding & Packaging. |
| **Product pages (all 38)** | ~85 words, no price/reviews/schema/meta | Follow section 4 of this report. Do the top sellers first: polo shirts, custom t-shirts, bulk t-shirt printing, logo embroidery, corporate gift sets, industrial uniforms, hoodies, custom caps. |
| **Thin/overlapping products** | Several near-duplicates cause keyword cannibalisation: *custom-t-shirts / custom-printed-t-shirts / bulk-t-shirt-printing*; *custom-sports-kits / corporate-sublimation-sports-kits*; *logo-business-embroidery / uniform-embroidery / custom-apparel-embroidery*; *custom-polo-shirts / custom-collar-polo-shirts* | Give each a clearly different focus keyword and unique copy, or merge the weakest into the strongest with a 301. |
| **/privacy-policy/, /refund-returns/** | Possibly template text | Rewrite with the real business name, address and policy. These are trust signals. |
| **Footer** | Lists two office locations | Make sure the addresses and phones match GBP and the contact page exactly. |

## C. MISSING (create)

**Core pages**
1. **/blog/** with real posts (none are in use; the layouts are demos).
2. **/faq/** (single, real FAQ with FAQPage schema).
3. **/get-a-quote/** (dedicated landing page with form and WhatsApp).
4. **/portfolio/** or **/gallery/** with real work photos (alt-tagged).
5. **/delivery-shipping/** (areas, timelines, charges).
6. **/terms-and-conditions/**.
7. **/bulk-order-pricing/** (MOQ and price tiers, a strong converting page).
8. **/how-it-works/** or **/design-mockup/** (the free 24-hour mockup is a selling point).
9. **/size-guide/** (reduces returns, adds content).
10. **/clients/** or case studies (corporate and school logos, with permission).

**Local landing pages (unique content for each, not duplicated)**
- /custom-uniforms-lahore/
- /t-shirt-printing-lahore/
- /embroidery-services-lahore/
- /corporate-gifts-lahore/
- /custom-packaging-lahore/
- Optional area pages: /t-shirt-printing-gulberg-lahore/, DHA, Johar Town, Model Town, Bahria Town, etc. Add only if you can give each real local content and don't spin them.

**Category pages with real content** (see B), plus a **Locations page** listing both offices with maps and hours.

**Blog posts to write first:** printing cost guide for Lahore, DTF vs screen vs sublimation, embroidery vs print for uniforms, corporate uniform ordering checklist, Eid/Ramadan corporate gift ideas, school uniform guide, restaurant uniform ideas.

## D. Target site structure (after cleanup)

```
Home
├── About Us
├── Contact Us (map, NAP, form)
├── Get a Quote
├── Shop
│   ├── Custom Uniforms (10 products)
│   ├── T-Shirt Printing (7)
│   ├── Embroidery Services (6)
│   ├── Corporate Giveaways (8)
│   └── Custom Branding & Packaging (7)
├── Lahore service pages (5)
├── Portfolio / Gallery
├── Testimonials
├── Bulk Order Pricing
├── FAQ
├── Blog
├── Delivery, Refund & Returns, Privacy, Terms
└── Cart / Checkout / My Account (noindex)
```

## E. Cleanup steps in order

1. Back up the site (full backup + database).
2. Export the page list from WP Admin and mark each as keep, delete or redirect.
3. Check Google Search Console > Pages and Performance for any demo URL that has impressions, then 301 those.
4. Delete demo pages (Trash first, then empty the trash after checking).
5. Remove unused Elementor templates, demo posts, demo products, demo menus and unused plugins.
6. Rank Math > Sitemap: re-save, confirm only real pages remain, then resubmit in Search Console.
7. Use the URL Removal tool in Search Console for any demo URL still indexed after deletion.
