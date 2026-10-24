#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.links=[];self.title=False;self.h1=False
    def handle_starttag(self,tag,attrs):
        if tag=='a': self.links.append(dict(attrs).get('href',''))
        if tag=='title': self.title=True
        if tag=='h1': self.h1=True
policies=json.loads((ROOT/'policies.json').read_text())
assert len(policies)==6 and len({p['url'] for p in policies})==6
pages={}
for name in ['index.html','privacy.html']+[p['path'] for p in policies]:
    page=Page();page.feed((ROOT/name).read_text());pages[name]=page
    assert page.title and page.h1,name
    for href in page.links:
        if not href or href.startswith(('https:','http:','mailto:','#')): continue
        target=href.split('#')[0]
        if target and target!='/': assert (ROOT/target.lstrip('/')).exists(),(name,href)
for p in policies:
    assert p['path'] in pages['index.html'].links,p['path']
    assert p['path'] in pages['privacy.html'].links,p['path']
    assert p['url']=='https://andrix-software.github.io/'+p['path']
    if '--verify-imports' in sys.argv:
        assert hashlib.sha256((ROOT/p['path']).read_bytes()).hexdigest()==p['imported_sha256'],p['path']
    print('OK',p['app'],p['url'])
assert (ROOT/'app-ads.txt').read_text().strip()=='google.com, pub-7116396142264702, DIRECT, f08c47fec0942fa0'
print('Six policy imports, homepage/catalog links and app-ads.txt validated.')
