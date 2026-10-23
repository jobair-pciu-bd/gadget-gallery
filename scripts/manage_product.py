#!/usr/bin/env python3
"""GitHub Actions form -> guarded catalog add/update. Inputs only through env."""
import json, os, re, sys
from pathlib import Path
from validate import validate, ROOT
PATH=ROOT/'data/products.json'

def field(k):return os.environ.get('FIELD_'+k,'').strip()
def main():
    rows=json.loads(PATH.read_text(encoding='utf-8'))
    operation=field('OPERATION').lower()
    if operation not in ('add','update'):raise ValueError('Choose add or update')
    slug=field('ID').lower()
    if operation=='add' and not slug:
        slug=re.sub(r'[^a-z0-9]+','-',field('NAME').lower()).strip('-')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',slug):raise ValueError('ID must contain lowercase letters, numbers and hyphens')
    existing=next((p for p in rows if p['id']==slug),None)
    if operation=='add' and existing:raise ValueError('ID already exists; select update instead')
    if operation=='add' and not field('PRICE'):raise ValueError('A selling price is required when adding a product')
    if operation=='update' and not existing:raise ValueError('Product ID not found; select add instead')
    p=existing if existing else {'id':slug,'name':'','category':'','price':0,'original_price':None,'images':['assets/images/placeholder.svg'],'description':'Specifications pending verification.','specifications':{'Details':'To be confirmed'},'in_stock':False,'featured':False,'new_arrival':False}
    for key,field_name in [('name','NAME'),('category','CATEGORY'),('description','DESCRIPTION')]:
        value=field(field_name)
        if value:p[key]=value[:1500]
    for key,field_name in [('price','PRICE'),('original_price','ORIGINAL_PRICE')]:
        value=field(field_name)
        if value.lower()=='none' and key=='original_price':p[key]=None
        elif value:
            if not re.fullmatch(r'\d+',value):raise ValueError(f'{key} must be a whole-number BDT amount')
            p[key]=int(value)
    image=field('IMAGE_PATH')
    if image:p['images']=[image]
    stock=field('STOCK_STATUS')
    if stock=='in-stock':p['in_stock']=True
    elif stock=='out-of-stock':p['in_stock']=False
    elif stock not in ('','keep'):raise ValueError('Unknown stock choice')
    tags=field('BADGES').lower()
    if tags:
        if tags=='none':p['featured']=p['new_arrival']=False
        else:
            labels={s.strip() for s in tags.split(',')}
            if not labels.issubset({'featured','new'}):raise ValueError('Badges: use featured, new, featured,new, or none')
            p['featured']='featured' in labels
            p['new_arrival']='new' in labels
    if not existing:rows.append(p)
    PATH.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    validate()
    print(f'{operation.capitalize()} product: {slug}')
if __name__=='__main__':
    try:main()
    except (ValueError,KeyError,json.JSONDecodeError) as exc:print(f'Product edit failed: {exc}',file=sys.stderr);sys.exit(1)
