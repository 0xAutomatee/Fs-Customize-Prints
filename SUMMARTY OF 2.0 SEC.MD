+============================================================================+
|                    FS CUSTOM PRINTS - WEBSITE CONTEXT                      |
|                 WordPress / WoodMart / Performance Work                    |
+============================================================================+

SITE
|
+-- Website
|   +-- fscustomprints.com
|
+-- Platform
|   +-- WordPress
|   +-- WooCommerce
|   +-- Elementor
|   +-- Elementor Pro
|   +-- WoodMart Theme
|   +-- WoodMart Core
|   +-- Rank Math SEO / PRO
|
+-- Hosting
|   +-- HosterNow
|   +-- StackCache visible in WordPress
|   +-- Exact web-server type not yet confirmed
|
+-- Cache/Optimization plugins seen
    +-- WP-Optimize
    +-- LiteSpeed Cache was tested
    +-- WoodMart Images Optimizer


+============================================================================+
| 01. ORIGINAL HEADER PROBLEM                                                |
+============================================================================+

Original desktop navigation:

LOGO | Home | Custom Uniform | Custom T-Shirt Printing | Custom Embroidery
     | Corporate Giveaways
     | Custom Branding   <-- wrapped onto second line

Goal:

LOGO | Home | Uniform | T-Shirt | Embroidery | Giveaways | Branding | Search | Cart


+============================================================================+
| 02. HEADER CSS CHANGES                                                     |
+============================================================================+

Problem:
+-- Menu was wrapping to second line.

CSS approach discussed:

@media (min-width: 1025px) {

    .wd-nav-main {
        flex-wrap: nowrap !important;
    }

    .wd-nav-main > li {
        flex-shrink: 0 !important;
    }

    .wd-nav-main > li > a {
        white-space: nowrap !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        padding-left: 7px !important;
        padding-right: 7px !important;
    }
}

Result:
+-- Menu became one line.
+-- But at one stage "Custom Branding" / right side became cut off.
+-- Header width/logo/menu spacing therefore also needed adjustment.

Recommended:
+-- Don't reduce menu below ~14px merely to force it to fit.
+-- Give menu more available width.
+-- Reduce logo width slightly if necessary.
+-- Keep search/cart visible.


+============================================================================+
| 03. DESKTOP CONTENT/DIV CUT-OFF                                            |
+============================================================================+

Observed:
+-- Homepage category/image section could extend beyond desktop viewport.
+-- Right-hand content appeared clipped at some desktop sizes.

Recommended Elementor structure:

Page / viewport
|
+-- Container
    |
    +-- width: 100%
    +-- max-width: ~1400px
    +-- margin-left: auto
    +-- margin-right: auto
    +-- padding-left: ~20px
    +-- padding-right: ~20px

Important:
+-- overflow-x:hidden can hide the symptom.
+-- Better solution is fixing the oversized Elementor container/div itself.
+-- Check fixed widths, negative margins and excessive padding.


+============================================================================+
| 04. FIRST PAGESPEED REPORT                                                 |
+============================================================================+

Approximate report:

Performance ............... 64
Accessibility ............. 89
Best Practices ............ 100
SEO ....................... 100

Important metrics:

FCP ....................... 3.8 sec
LCP ....................... 5.8 sec
TBT ....................... 130 ms
CLS ....................... 0
Speed Index ............... 6.6 sec

Interpretation:

GOOD
+-- CLS
+-- TBT
+-- SEO
+-- Best Practices

NEEDS WORK
+-- LCP
+-- FCP
+-- Speed Index


+============================================================================+
| 05. ORIGINAL PERFORMANCE PRIORITIES                                        |
+============================================================================+

Priority order established:

1. Browser/server caching
2. Render-blocking CSS
3. LCP / above-the-fold image
4. Image optimization
5. Unused CSS/JS
6. Accessibility


+============================================================================+
| 06. CACHE PROBLEM FOUND                                                    |
+============================================================================+

Initial PageSpeed report:

"Use efficient cache lifetimes"

Approximate potential affected resources:
+-- ~1,058 KiB

Many first-party resources showed:

Cache TTL: None

Affected resource types included:

+-- Images
+-- CSS
+-- JavaScript
+-- Other static assets


+============================================================================+
| 07. EXISTING WORDPRESS PLUGINS                                             |
+============================================================================+

Screenshot showed approximately:

WordPress Plugins
|
+-- Elementor
+-- Elementor Pro
+-- Rank Math SEO
+-- Rank Math SEO PRO
+-- WooCommerce
+-- WoodMart Core
+-- WoodMart Images Optimizer
+-- WP-Optimize - Clean, Compress, Cache
|
+-- StackCache also visible in WP admin menu


+============================================================================+
| 08. WP-OPTIMIZE VS LITESPEED                                               |
+============================================================================+

Discussion:

WP-Optimize
|
+-- Good basic page caching
+-- Good database optimization
+-- Works independently of LiteSpeed server
+-- Easier configuration

LiteSpeed Cache
|
+-- Excellent when server is LiteSpeed/OpenLiteSpeed
+-- Advanced cache controls
+-- Advanced CSS/JS optimization
+-- Image optimization
+-- QUIC.cloud integration
+-- WooCommerce-aware features

IMPORTANT:
+-- Do NOT have WP-Optimize and LiteSpeed both independently
|   doing page caching/minification.
|
+-- One system should own each optimization responsibility.


+============================================================================+
| 09. LITESPEED SERVER WARNING                                               |
+============================================================================+

LiteSpeed Cache -> Browser screenshot showed:

WARNING:

"LSCache caching functions on this page are currently unavailable!"

and approximately:

"To use the caching functions you must have a LiteSpeed web server
 or be using QUIC.cloud CDN."

Meaning:

HosterNow server
      |
      +--> LiteSpeed server cache NOT currently available to plugin
              |
              +--> unless hosting configuration changes
              OR
              +--> QUIC.cloud is used

Therefore:

+-- LiteSpeed cannot currently provide its normal server-level LSCache
|   page caching.
|
+-- Need to confirm HosterNow's actual server technology.
|
+-- StackCache may be part of HosterNow's caching system.


+============================================================================+
| 10. LITESPEED CACHE SETTINGS REVIEWED                                      |
+============================================================================+

Cache Control recommended:

Enable Cache ..................... ON
Cache Logged-in Users ............ OFF
Cache Commenters ................. OFF
Cache REST API ................... ON
Cache Login Page ................. ON
Cache Mobile ..................... OFF
Mobile User Agents ............... DEFAULT
Private Cached URLs .............. EMPTY

Reason for Cache Mobile OFF:
+-- WoodMart/Elementor is responsive.
+-- Separate mobile HTML cache normally isn't required unless site
    actually outputs different mobile HTML.


+============================================================================+
| 11. LITESPEED BROWSER CACHE                                                |
+============================================================================+

Screen showed:

Browser Cache ................. OFF initially
Browser Cache TTL ............. 31557600

Recommended:

Browser Cache ................. ON
Browser Cache TTL ............. 31557600 seconds

31557600 seconds
       |
       +--> approximately 1 year

Purpose:
+-- Browser stores static resources locally.
+-- Helps address PageSpeed "efficient cache lifetimes" warning.


+============================================================================+
| 12. SECOND / LATER PAGESPEED FINDINGS                                      |
+============================================================================+

Major issue:

RENDER-BLOCKING REQUESTS

At one stage estimated savings:
+-- ~11.5 seconds

Report contained many individual:

WoodMart CSS
Elementor CSS
WooCommerce CSS
WordPress CSS
jQuery
jQuery Migrate
Google Fonts

The site is not necessarily suffering from one giant CSS file.

Instead:

Browser
|
+-- CSS #1
+-- CSS #2
+-- CSS #3
+-- CSS #4
+-- CSS #5
+-- ...
+-- many WoodMart component CSS files
|
+--> rendering waits on many resources


+============================================================================+
| 13. GOOGLE FONT ISSUE                                                      |
+============================================================================+

Fonts observed included:

+-- Roboto
+-- Roboto Slab
+-- Lexend Deca

At one audit stage these contributed significant loading delay.

Future optimization:
+-- Reduce unnecessary font families/weights.
+-- Consider local font hosting.
+-- Ensure font-display behavior is optimized.

NOT YET COMPLETED.


+============================================================================+
| 14. WOODMART PERFORMANCE -> CSS                                            |
+============================================================================+

Screen:

WoodMart
  -> Theme Settings
     -> Performance
        -> CSS

Options shown:

[ ] Disable default Gutenberg blocks styles
[ ] Convert large CSS files to inline styles

Advanced:
+-- Styles always load
+-- Styles never load

Recommended:

Disable default Gutenberg blocks styles
    -> YES

Convert large CSS files to inline styles
    -> NO

Styles always load
    -> EMPTY

Styles never load
    -> EMPTY


+============================================================================+
| 15. WHY GUTENBERG CSS WAS TARGETED                                         |
+============================================================================+

PageSpeed identified:

/wp-includes/css/dist/block-library/style.min.css

Approx:
+-- 24.7 KiB
+-- significant render delay in the audit

Since the site primarily uses:

Elementor + WoodMart

we attempted:

Disable default Gutenberg blocks styles -> YES

However, later PageSpeed still showed:

block-library/style.min.css

Therefore:

+-- Setting may not have removed it.
+-- Cache/generated assets may need refreshing.
+-- Another component may require/load it.
+-- Do NOT manually delete WordPress CSS files.


+============================================================================+
| 16. MOST RECENT PAGESPEED STATE                                            |
+============================================================================+

Latest report reviewed showed approximately:

Render-blocking potential savings:
+-- 2,980 ms

Cache warning:
+-- ~52 KiB

Image opportunity:
+-- ~270 KiB

Conclusion:

BEFORE:
Cache was a major issue (~1,058 KiB)

NOW:
Cache warning much smaller (~52 KiB)

Therefore current focus shifted:

CACHE
   |
   +--> mostly improved / lower priority

RENDER BLOCKING
   |
   +--> CURRENT #1 PRIORITY

IMAGES
   |
   +--> CURRENT #2 PRIORITY


+============================================================================+
| 17. IMAGE OPTIMIZATION FINDINGS                                            |
+============================================================================+

Homepage image findings included approximately:

Custom Uniform
|
+-- File size: ~167.7 KiB
+-- Possible saving: ~154.6 KiB
+-- HIGH PRIORITY

Embroidery
|
+-- Served around 768x768
+-- Displayed around 634x634
+-- ~30 KiB possible saving

T-Shirt Printing
|
+-- Served around 768x768
+-- Displayed around 634x634
+-- ~27 KiB possible saving

Logo
|
+-- Source around 738x306
+-- Displayed around 211x87
+-- ~20 KiB possible saving

Future:
+-- Resize images closer to actual display dimensions.
+-- Compress aggressively while retaining visual quality.
+-- Continue WebP/modern formats.


+============================================================================+
| 18. POSSIBLE OLD/UNRELATED ASSETS                                          |
+============================================================================+

Earlier report contained files with names similar to:

gms-cubes-bg-opt.jpg
gms-franchise-logo-bttf-opt.jpg
gms-franchise-logo-fallout-opt.jpg
gms-franchise-logo-tlou-opt.jpg
gms-cubes-logo-opt.png
gms-slide-1-logo-opt.png

These don't appear related to FS Custom Prints.

Possible causes:
+-- Old demo content
+-- Hidden Elementor sections
+-- Theme demo imports
+-- Slider/template content

TODO:
+-- Identify what loads these.
+-- Remove unused content instead of merely compressing it.


+============================================================================+
| 19. WOODMART PERFORMANCE -> JS                                             |
+============================================================================+

Most recent screen:

WoodMart
  -> Theme Settings
     -> Performance
        -> JS

General options:

Disable Swiper slider script on mobile devices
    -> NO

Remove jQuery Migrate
    -> NO initially

Recommended:

Disable Swiper slider script on mobile devices
    -> KEEP NO

Remove jQuery Migrate
    -> YES
    -> Then test site carefully.


+============================================================================+
| 20. WHY REMOVE JQUERY MIGRATE                                              |
+============================================================================+

PageSpeed showed approximately:

jquery.min.js
+-- ~35 KiB
+-- ~1.4 sec in audit

jquery-migrate.min.js
+-- ~5.6 KiB
+-- ~310 ms in audit

WoodMart provides:

"Remove jQuery Migrate"

Recommended:
+-- Turn YES.
+-- Purge cache.
+-- Test everything.

Test specifically:

[ ] Homepage
[ ] Desktop navigation
[ ] Mobile navigation
[ ] Search
[ ] Product page
[ ] Product variations
[ ] Add to cart
[ ] Mini cart
[ ] Cart
[ ] Checkout
[ ] Elementor sections/sliders
[ ] Popups


+============================================================================+
| 21. SWIPER                                                                 |
+============================================================================+

Latest report also showed Swiper-related work/forced reflow.

swiperInit.min.js
+-- approximately 139 ms reflow in report

However:

Disable Swiper slider script on mobile devices
    -> KEEP NO for now

Reason:
+-- Site may depend on sliders/carousels.
+-- Don't risk breaking mobile UX merely for a small optimization.

Optimize later after more important items.


+============================================================================+
| 22. CURRENT WOODMART JS SCREEN                                             |
+============================================================================+

Current state being worked on:

Performance
|
+-- CSS                    DONE / TESTING
|
+-- JS
|   |
|   +-- Disable Swiper mobile ........ NO
|   +-- Remove jQuery Migrate ......... change to YES
|   |
|   +-- Advanced scripts controls
|       |
|       +--> NOT REVIEWED YET
|
+-- Fonts & Icons          TODO
+-- Lazy loading           TODO
+-- Images optimizer       TODO
+-- Plugins                TODO
+-- Preloader              TODO
+-- LCP                    TODO
+-- Other                  TODO


+============================================================================+
| 23. CURRENT ACTION POINT                                                   |
+============================================================================+

WE ARE HERE:

WoodMart
  |
  +-- Theme Settings
      |
      +-- Performance
          |
          +-- JS
              |
              +-- Remove jQuery Migrate = YES
              |
              +-- Save Options
              |
              +-- Purge Cache
              |
              +-- Test site
              |
              +-- NEXT:
                  Advanced Scripts Controls


+============================================================================+
| 24. DO NOT DO YET                                                         |
+============================================================================+

DO NOT randomly enable all of these together:

[X] Combine every CSS file
[X] Combine every JS file
[X] Delay all JavaScript
[X] Remove all unused CSS automatically
[X] Aggressive async CSS
[X] Disable random WoodMart styles
[X] Disable random WooCommerce scripts
[X] Run two page-cache systems simultaneously

Reason:

WoodMart + Elementor + WooCommerce
          |
          +--> Header can break
          +--> Mobile menu can break
          +--> Cart can break
          +--> Variations can break
          +--> Elementor layout can break
          +--> Checkout can break


+============================================================================+
| 25. OPTIMIZATION ROADMAP                                                   |
+============================================================================+

                         START
                           |
                           v
                 +-------------------+
                 | 1. CACHE          |
                 +-------------------+
                           |
                         MOSTLY
                         IMPROVED
                           |
                           v
                 +-------------------+
                 | 2. WOODMART CSS   |
                 +-------------------+
                           |
                           v
                 +-------------------+
                 | 3. WOODMART JS    |  <-- CURRENT
                 +-------------------+
                           |
                           v
                 +-------------------+
                 | 4. FONTS          |
                 +-------------------+
                           |
                           v
                 +-------------------+
                 | 5. IMAGES / LCP   |
                 +-------------------+
                           |
                           v
                 +-------------------+
                 | 6. LAZY LOADING   |
                 +-------------------+
                           |
                           v
                 +-------------------+
                 | 7. RETEST         |
                 +-------------------+
                           |
                           v
                  PageSpeed Mobile


+============================================================================+
| TARGET                                                                     |
+============================================================================+

Preserve:

SEO ......................... 100
Best Practices .............. 100
CLS ......................... ~0
TBT ......................... Good

Improve:

Performance ................. 64 -> ideally 80-90+
FCP ......................... 3.8s -> < 1.8s
LCP ......................... 5.8s -> < 2.5s
Speed Index ................. 6.6s -> substantially lower

MAIN CURRENT TARGET:

              +-----------------------------+
              | REDUCE RENDER-BLOCKING TIME |
              +-----------------------------+
                           |
              +------------+------------+
              |                         |
              v                         v
        WoodMart / CSS              JS / jQuery
              |                         |
              +------------+------------+
                           |
                           v
                    Images + LCP
