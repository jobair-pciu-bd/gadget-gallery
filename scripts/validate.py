#!/usr/bin/env python3
"""Validate owner-editable JSON and protect deployment against broken catalogs."""
import json, re, sys
from pathlib import Path
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parents[1]
ID=re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')

def validate():
    settings=json.loads((ROOT/'data/settings.json').read_text(encoding='utf-8'))
    products=json.loads((ROOT/'data/products.json').read_text(encoding='utf-8'))
    if not isinstance(settings,dict) or not isinstance(products,list):raise ValueError('Both settings object and products array are required')
    for key in ('business_name','tagline','promo_message','announcement','service_area','business_address'):
        if not isinstance(settings.get(key),str):raise ValueError(f'Settings: {key} must be a string')
    if settings.get('currency')!='BDT':raise ValueError('Currency must be BDT')
    if settings.get('whatsapp_number') and not re.fullmatch(r'\+?8801\d{9}',settings['whatsapp_number']):
        raise ValueError('WhatsApp number must be empty or +8801XXXXXXXXX')
    if settings.get('facebook_page_url') and not settings['facebook_page_url'].startswith('https://'):
        raise ValueError('Facebook Page URL must be blank or start with https://')
    if settings.get('contact_email') and not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+',settings['contact_email']):
        raise ValueError('Contact email is invalid')
    if not isinstance(settings.get('faq'),list): raise ValueError('FAQ must be a list')
    for key in ('delivery','returns','privacy'):
        item=settings.get(key)
        if not isinstance(item,dict) or not isinstance(item.get('summary'),str) or not isinstance(item.get('details'),list) or not all(isinstance(x,str) for x in item['details']):raise ValueError(f'Settings: invalid {key}')
    if len(products)>1000:raise ValueError('Too many products (maximum 1000)')
    seen=set()
    for index,p in enumerate(products,1):
        if not isinstance(p,dict):raise ValueError(f'Product #{index} must be an object')
        slug=p.get('id')
        if not isinstance(slug,str) or not ID.fullmatch(slug) or slug in seen:raise ValueError(f'Invalid or duplicate product id #{index}: {slug!r}')
        seen.add(slug)
        for k in ('name','category','description'):
            if not isinstance(p.get(k),str) or (k!='description' and not p[k].strip()):raise ValueError(f'{slug}: invalid {k}')
        if type(p.get('price')) is not int or p['price']<0:raise ValueError(f'{slug}: price must be a nonnegative whole number')
        original=p.get('original_price')
        if original is not None and (type(original) is not int or original < p['price']):raise ValueError(f'{slug}: original_price must be null or >= price')
        for k in ('featured','new_arrival','in_stock'):
            if type(p.get(k)) is not bool:raise ValueError(f'{slug}: {k} must be true or false')
        if not isinstance(p.get('specifications'),dict) or not all(isinstance(k,str) and isinstance(v,str) for k,v in p['specifications'].items()):raise ValueError(f'{slug}: specs must be a string-to-string object')
        imgs=p.get('images')
        if not isinstance(imgs,list) or not imgs:raise ValueError(f'{slug}: missing images list')
        for image in imgs:
            if not isinstance(image,str):raise ValueError(f'{slug}: image path must be a string')
            if image.startswith('https://'):
                parsed=urlsplit(image)
                if not parsed.hostname:raise ValueError(f'{slug}: invalid image HTTPS URL')
            elif not re.fullmatch(r'assets/images/[A-Za-z0-9_./-]+\.(?:png|jpg|jpeg|webp|svg)',image) or '..' in image:
                raise ValueError(f'{slug}: images must be HTTPS URLs or safe assets/images paths: {image!r}')
            elif not (ROOT/image).is_file():
                raise ValueError(f'{slug}: image file missing: {image}. Upload it using GitHub first.')
    print(f'Validation passed: {len(products)} products; settings valid.')
    return settings,products
if __name__=='__main__':
    try:validate()
    except (ValueError,KeyError,TypeError,json.JSONDecodeError) as err:print(f'VALIDATION FAILED: {err}',file=sys.stderr);sys.exit(1)
