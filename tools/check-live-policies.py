#!/usr/bin/env python3
"""Run after GitHub Pages deployment; does not modify either repository."""
import json,urllib.request
from pathlib import Path
root=Path(__file__).resolve().parents[1]
for policy in json.loads((root/'policies.json').read_text()):
    with urllib.request.urlopen(policy['url'],timeout=20) as response:
        body=response.read().decode('utf-8')
        assert response.status==200,policy['url']
        assert 'privacy' in body.lower(),policy['url']
        assert body==(root/policy['path']).read_text(),('Deployed content differs',policy['url'])
        print('LIVE',policy['url'])
print('All six public pages match the migrated policies.')
