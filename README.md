# Andrix Software website and privacy policies

Public website: https://andrix-software.github.io/ .
All app policies: https://andrix-software.github.io/privacy.html .

| App | Privacy policy URL |
| --- | --- |
| NetPulse | https://andrix-software.github.io/netpulse.html |
| TapSync | https://andrix-software.github.io/tapsync.html |
| Dot Dodge | https://andrix-software.github.io/dotdodge.html |
| jQuery Learn | https://andrix-software.github.io/jquery.html |
| English Grammar Learn | https://andrix-software.github.io/english-grammar.html |
| Movies Now | https://andrix-software.github.io/movies-now.html |

## Migration and maintenance

NetPulse, TapSync and Dot Dodge were copied from
[ASHWIN-S-ASHOK/andrix-softwares](https://github.com/ASHWIN-S-ASHOK/andrix-softwares).
The latest policies there take precedence over older app-repository snapshots.
jQuery and English Grammar were imported from their app repositories. Movies Now
was imported from the existing `andrix-softwares/projects` policy site.
The imported policy wording and effective dates are unchanged. `policies.json`
records each source and its import hash for migration verification.

Make future policy changes here. Update a policy's date when its disclosures
change. Migration alone is not an audit or a change in data practices. Individual
policies retain their existing privacy contacts. The old personal policy site keeps its existing pages available, so existing
store links still provide policy text during migration. Only update old links
after confirming the organization pages are live.

Before updating Play Console, confirm each new URL loads publicly without
sign-in. Set both the store listing and any in-app policy link to the same URL.
Keep the old URLs available for installed versions that still use them.
Kids-Coloring-Painting and puzzle-battler have no supplied policy page; do not
reuse another app's policy for those apps.

## Hosting and validation

Plain HTML; no framework or analytics scripts are required. Preserve the existing
GitHub Pages settings. If Pages needs activation, use **Settings → Pages → Deploy
from a branch → main → / (root)**. `.nojekyll` skips Jekyll processing.
`app-ads.txt` remains at the site root for advertising-seller verification.

Run `python3 tools/validate-policies.py` to validate page structure, index links,
and the seller file. Add `--verify-imports` to check the original migration hashes
before the first publication; later policy edits naturally change those hashes. Public Pages deployment must also be checked independently; a
successful Git push does not prove that the website has deployed.

After deployment, run `python3 tools/check-live-policies.py` to confirm all six
public pages match these policies. This needs network access to the Pages host.
