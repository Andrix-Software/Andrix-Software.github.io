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
assert len(policies)==7 and len({p['url'] for p in policies})==7
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
    if '--verify-imports' in sys.argv and 'imported_sha256' in p:
        assert hashlib.sha256((ROOT/p['path']).read_bytes()).hexdigest()==p['imported_sha256'],p['path']
    assert 'mailto:andrix.android@gmail.com' in pages[p['path']].links,p['path']
    assert all(href == 'mailto:andrix.android@gmail.com' for href in pages[p['path']].links if href.startswith('mailto:')),p['path']
    if 'published_sha256' in p:
        assert hashlib.sha256((ROOT/p['path']).read_bytes()).hexdigest()==p['published_sha256'],p['path']
    print('OK',p['app'],p['url'])
assert (ROOT/'app-ads.txt').read_text().strip()=='google.com, pub-7116396142264702, DIRECT, f08c47fec0942fa0'
print('Seven policies, homepage/catalog links and app-ads.txt validated.')

catalogue=json.loads((ROOT/'apps.json').read_text())
assert catalogue['developer_page'] in pages['index.html'].links
assert len(catalogue['apps'])==8
assert len({app['package'] for app in catalogue['apps']})==8
for app in catalogue['apps']:
    assert app['play_store_url']=='https://play.google.com/store/apps/details?id='+app['package']
    assert app['play_store_url'] in pages['index.html'].links,app['name']
    assert app['privacy_policy'] in pages['index.html'].links,app['name']
    assert app['privacy_policy'] in pages['privacy.html'].links,app['name']
    if app['privacy_policy'].startswith('https://'):
        assert app.get('privacy_policy_source'),app['name']
    else:
        assert (ROOT/app['privacy_policy']).is_file(),app['name']
print('Eight app-specific Play links, policy links and developer-page link validated locally.')
