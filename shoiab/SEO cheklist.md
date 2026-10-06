# FS Custom Prints: WordPress + WoodMart + Rank Math Checklist

## Reference repos
- Front-End Checklist: https://github.com/thedaviddias/Front-End-Checklist
- Front-End Performance Checklist: https://github.com/thedaviddias/Front-End-Performance-Checklist
- SEO Checklist: https://github.com/marcobiedermann/search-engine-optimization

## Tools
- Rich Results Test: https://search.google.com/test/rich-results
- Google Search Console: https://search.google.com/search-console
- PageSpeed Insights: https://pagespeed.web.dev
- Google Business Profile: https://business.google.com

---

## 1. Rank Math setup
- [ ] Run **Rank Math → Setup Wizard** (site type: Business / Local Business)
- [ ] **Titles & Meta → Local SEO**: Company, business type = Local Business/Store, name, logo (square, 112px+), address, phone, hours (Mon-Sat 09:00-22:00, remove Sunday), price range, geo coordinates, contact page
- [ ] Enable **Use Multiple Locations**; add Gulberg and Mustafa Town as Locations
- [ ] **Titles & Meta → Pages**: default Schema Type = None or WebPage (not Article)
- [ ] **Titles & Meta → Posts**: Schema = Article
- [ ] **Titles & Meta → Products**: Schema = Product
- [ ] **Titles & Meta → Global Meta**: set default social image
- [ ] **General Settings → Links**: strip category base off; open external links in new tab (rel nofollow only where needed)
- [ ] **General Settings → Breadcrumbs**: enable, add the breadcrumb shortcode/widget to the WoodMart page title area
- [ ] **General Settings → Webmaster Tools**: verify Google Search Console
- [ ] **Sitemap Settings**: enable; include Pages, Products, Categories, Posts; exclude noindex pages
- [ ] **Analytics**: connect Search Console (and GA4 if used)
- [ ] **Instant Indexing**: optional, enable for fast Google/Bing pings
- [ ] Remove demo text ("Perfect for fans of the iconic platformer") from home page content and meta description

## 2. Every page / product
- [ ] Unique title, 50-60 chars, main keyword + "Lahore" where relevant
- [ ] Unique meta description, 140-160 chars, with a call to action
- [ ] Focus keyword set; Rank Math score green (aim 80+, but write for people)
- [ ] One H1 only, matching the page topic; logical H2/H3 below it
- [ ] Canonical URL correct
- [ ] Images: descriptive file names, alt text, compressed WebP
- [ ] 2-5 internal links to related pages/products
- [ ] Schema type correct (Rank Math → Schema tab)
- [ ] Page is indexable (not noindex by mistake)

## 3. WoodMart theme settings
- [ ] **Theme Settings → Performance**: enable lazy loading, minify CSS/JS, disable unused theme modules, Google font preload
- [ ] **Typography**: limit to 1-2 font families, `font-display: swap`
- [ ] **General → Site width/Responsive**: check mobile layout on real phone
- [ ] **Page title**: use a real H1; don't use a separate heading plus the title bar H1
- [ ] **Shop / Product archive**: set sensible products-per-page; enable pagination or load-more with crawlable links
- [ ] **Single product**: show price, stock status, reviews; short description filled in
- [ ] **Social profiles**: add Facebook (and other) links
- [ ] **Header/Footer**: add business name, phone, address, both locations, links to Contact/About/Privacy
- [ ] **Custom JS**: remove the old LocalBusiness JS once Rank Math Local SEO is saved
- [ ] Use a **child theme** for any code edits
- [ ] Keep WoodMart and bundled plugins (WPBakery/Elementor, Slider Revolution) updated

## 4. Speed and Core Web Vitals
- [ ] Caching plugin on (WP Rocket, LiteSpeed Cache, or host cache)
- [ ] Image optimisation plugin (ShortPixel, Imagify, or Smush); serve WebP
- [ ] No images wider than needed; hero image under about 200 KB
- [ ] Remove unused plugins and sliders; deactivate rather than just hide
- [ ] CDN (Cloudflare) enabled
- [ ] PHP 8.1+ and HTTPS on the host
- [ ] PageSpeed Insights mobile: aim for LCP under 2.5s, CLS under 0.1, INP under 200ms
- [ ] Purge cache after every setting change

## 5. Technical SEO
- [ ] HTTPS everywhere; www/non-www redirect to one version
- [ ] Settings → Reading: "Discourage search engines" is **unchecked**
- [ ] Permalinks = Post name (`/%postname%/`)
- [ ] `robots.txt` lets Google crawl; points to sitemap (`/sitemap_index.xml`)
- [ ] Sitemap submitted in Search Console
- [ ] Fix 404s; add 301 redirects for removed pages (Rank Math → Redirections)
- [ ] No duplicate content (tag/archive pages set to noindex if thin)
- [ ] Mobile-friendly; no horizontal scroll
- [ ] Custom 404 page
- [ ] Cookie/privacy page present

## 6. Local SEO
- [ ] Google Business Profile claimed and verified for **each** office
- [ ] Name, address, phone (NAP) identical on site, GBP, Facebook and directories
- [ ] Categories, services, photos, hours, and products added to GBP
- [ ] Ask customers for Google reviews; reply to every review
- [ ] Add embedded Google Map and contact details on the Contact page
- [ ] Location/service landing pages (e.g. "Custom uniforms Lahore") with unique text
- [ ] Local directory listings (Pakistan business directories)

## 7. Structured data check
- [ ] Rich Results Test on home page: one LocalBusiness item, no warnings (address, priceRange, image)
- [ ] Product page: Product + Offer, price and availability
- [ ] Only one LocalBusiness item per page (no duplicate from JS)
- [ ] Search Console → Enhancements: no errors

## 8. Accessibility and quality
- [ ] Colour contrast passes (WCAG AA)
- [ ] Alt text on all meaningful images
- [ ] Forms have labels; buttons have text
- [ ] Links have descriptive text (not "click here")
- [ ] Lighthouse: Accessibility and Best Practices 90+

## 9. Security and maintenance
- [ ] Security plugin (Wordfence or Sucuri); limit login attempts
- [ ] Strong admin password; no user named "admin"
- [ ] Automatic backups (UpdraftPlus or host backups)
- [ ] WordPress core, theme and plugins updated monthly
- [ ] SSL certificate auto-renews

## 10. Monthly routine
- [ ] Search Console: check Coverage, Performance, Core Web Vitals, Enhancements
- [ ] Re-run PageSpeed on home and a product page
- [ ] Publish or update content (blog posts, product pages)
- [ ] Check for broken links
- [ ] Review GBP insights and answer reviews
