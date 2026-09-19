import os
import subprocess
from pathlib import Path
from openai import OpenAI

ROOT = Path(".")
PARENTS = ["Uniforms","Custom Apparel","Embroidery","Printing","Corporate Merchandise"]

client = OpenAI()

def generate(product, category):
    prompt = f"""
Create COMPLETE READY-TO-PASTE WooCommerce content for FS Custom Prints.

Product/Service: {product}
Parent Category: {category}
Business: FS Custom Prints
Market: Lahore, Pakistan
Website: fscustomprints.com

This is FINAL WEBSITE COPY, not instructions or a template.

Follow current Google SEO principles. Write naturally for customers. Do not keyword-stuff.

Never invent materials, fabric composition, GSM, sizes, colors, MOQ, prices, delivery times, printing methods, embroidery specifications, production capacity, certifications, guarantees, machine specifications or turnaround times.

Return EXACTLY these sections:

# {product}

## PRODUCT NAME / H1
Create a natural SEO-friendly commercial product title. Use "Premium" only when appropriate.

## PRODUCT DESCRIPTION
Write approximately 450-550 words of unique finished website content specifically about {product}.

Naturally cover:
- what the product/service is
- business use
- custom branding use
- suitable customers
- relevant industries
- common applications
- corporate/commercial use
- custom and bulk order context
- Lahore relevance
- Pakistan relevance
- practical customer benefits
- inquiry/quotation CTA

Use useful headings and readable paragraphs.

## PRODUCT SHORT DESCRIPTION
Write 40-70 words of finished WooCommerce copy.

## FOCUS KEYWORD
Give ONE primary commercial search keyword.

## SEO TITLE
Create a Rank Math SEO title. Preferred structure when accurate:
Premium [Focus Keyword] in Lahore | FS Custom Prints

## META DESCRIPTION
Write approximately 150-160 characters with commercial search intent.

## URL SLUG
Give a clean lowercase hyphenated slug.

## IMAGE ALT TEXT
Write natural alt text for a representative main product image. Describe the product and purpose without keyword stuffing.

## IMAGE TITLE
Write: [Product Name] – FS Custom Prints

## IMAGE CAPTION
Write a short customer-facing image caption.

## IMAGE DESCRIPTION
Write a natural image description explaining the product, intended business/custom use, branding context, and Lahore/Pakistan where appropriate.

## IMAGE FILENAME
Create a lowercase filename in this format:
[focus-keyword]-fs-custom-prints.jpg

## WOODMART IMAGE OPTIMIZER
Optimize: Yes
Exclude attachment from sitemap: No / Leave unchecked

## PARENT CATEGORY
{category}

## PRODUCT / SUBCATEGORY
{product}

Do not add explanations before or after the content.
"""
    r = client.responses.create(
        model="gpt-5.6",
        input=prompt
    )
    return r.output_text.strip()

count = 0

for category in PARENTS:
    parent = ROOT / category
    if not parent.exists():
        print(f"⚠ Missing parent: {category}")
        continue

    products = sorted(
        x for x in parent.iterdir()
        if x.is_dir() and not x.name.startswith(".")
    )

    # Parent README
    names = "\n".join(f"- {x.name}" for x in products)
    (parent/"README.md").write_text(
f"""# {category} — FS Custom Prints

## Category
{category}

## Market
Lahore, Pakistan

## Products / Services
{names}

## Website
fscustomprints.com
""", encoding="utf-8")

    for folder in products:
        print(f"\nGenerating: {category} > {folder.name}")

        try:
            content = generate(folder.name, category)
            (folder/"README.md").write_text(content + "\n", encoding="utf-8")
            count += 1
            print("✓ DONE")
        except Exception as e:
            print(f"✗ FAILED: {e}")

# Main repository README
(ROOT/"README.md").write_text(
"""# FS Custom Prints — WooCommerce Content Repository

Ready-to-paste WooCommerce product content for FS Custom Prints.

## Main Categories
- Uniforms
- Custom Apparel
- Embroidery
- Printing
- Corporate Merchandise

Each product folder contains:
- Product Name / H1
- ~500-word Product Description
- Short Description
- Focus Keyword
- Rank Math SEO Title
- Meta Description
- URL Slug
- Image Alt Text
- Image Title
- Image Caption
- Image Description
- Image Filename
- WoodMart Image Optimizer settings
- Category information

Website: fscustomprints.com
Market: Lahore, Pakistan
""", encoding="utf-8")

print(f"\n✓ Generated {count} product READMEs.")

subprocess.run(["git","add","-A"], check=True)

status = subprocess.run(
    ["git","status","--porcelain"],
    capture_output=True,text=True
)

if status.stdout.strip():
    subprocess.run([
        "git","commit","-m",
        "Generate complete WooCommerce product content"
    ], check=True)
    subprocess.run(["git","push","origin","main"], check=True)
    print("\n✓ PUSHED TO GITHUB")
else:
    print("\nNothing new to commit.")
