#!/usr/bin/env python3
"""No-dependency GitHub Pages build: static pages, social previews, sitemap."""
import html, json, os, re, shutil
from pathlib import Path
from urllib.parse import quote
from validate import validate
ROOT=Path(__file__).resolve().parents[1]
PAGES=['index','shop','product','cart','about','contact','faq','delivery','returns','privacy']

def build():
    settings, products = validate()
    owner,repo = os.environ.get('GITHUB_REPOSITORY','example/gadget-gallery').split('/',1)
    hostname=f'https://{owner.lower()}.github.io'
    prefix='/' if repo.lower()==f'{owner.lower()}.github.io' else f'/{quote(repo)}/'
    base_url=hostname+prefix
    out=ROOT/'_site'
    if out.exists():shutil.rmtree(out)
    out.mkdir()
    shutil.copytree(ROOT/'assets',out/'assets')
    shutil.copytree(ROOT/'data',out/'data')
    (out/'.nojekyll').write_text('')
    def patch(text,relative_page,seo_title=None,seo_description=None,product_id=None):
        page_url=base_url+relative_page
        social_url=base_url+'assets/images/share-card.png'
        text=text.replace('content="assets/images/share-card.png"',f'content="{html.escape(social_url,quote=True)}"')
        if seo_title:
            text=re.sub(r'<title>.*?</title>',f'<title>{html.escape(seo_title)}</title>',text)
            text=re.sub(r'(<meta property="og:title" content=")[^"]*',lambda m:m.group(1)+html.escape(seo_title,quote=True),text)
        if seo_description:
            for meta in ['name="description"','property="og:description"']:
                text=re.sub(r'(<meta '+meta+r' content=")[^"]*',lambda m:m.group(1)+html.escape(seo_description[:155],quote=True),text)
        text=text.replace('</head>',f'  <link rel="canonical" href="{html.escape(page_url,quote=True)}">\n  <meta property="og:url" content="{html.escape(page_url,quote=True)}">\n</head>')
        if product_id:
            text=text.replace('data-page="product" data-base="./"',f'data-page="product" data-base="../" data-product-id="{product_id}"')
            text=text.replace('href="assets/', 'href="../assets/').replace('src="assets/','src="../assets/')
        return text
    for page in PAGES:
        if page=='product':continue  # Every product receives a shareable pre-generated static URL.
        s=(ROOT/f'{page}.html').read_text(encoding='utf-8')
        (out/f'{page}.html').write_text(patch(s,('' if page=='index' else page+'.html')),encoding='utf-8')
    # Generic compatibility page also supported: /product.html?id=product-id
    generic=(ROOT/'product.html').read_text(encoding='utf-8')
    (out/'product.html').write_text(patch(generic,'product.html'),encoding='utf-8')
    (out/'p').mkdir()
    for p in products:
        path=f'p/{p["id"]}.html'
        t=patch(generic,path, f'{p["name"]} | {settings["business_name"]}',p['description'],p['id'])
        (out/path).write_text(t,encoding='utf-8')
    urls=[base_url]+[base_url+f'{x}.html' for x in PAGES if x not in ('index','product','cart')]+[base_url+f'p/{p["id"]}.html' for p in products]
    # Search crawlers can see full product meta descriptions, without needing JS execution.
    sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{html.escape(u)}</loc></url>\n' for u in urls)+'</urlset>\n'
    (out/'sitemap.xml').write_text(sitemap,encoding='utf-8')
    (out/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {base_url}sitemap.xml\n',encoding='utf-8')
    print(f'Build complete: {len(products)} shareable product pages, {len(urls)} sitemap URLs. Pages base: {base_url}')
if __name__=='__main__':build()
