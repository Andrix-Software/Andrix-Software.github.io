# Andrix Software website and privacy policies

Public website: https://andrix-software.github.io/ .
All app policies: https://andrix-software.github.io/privacy.html .

| App | Privacy policy URL |
| --- | --- |
| Orbit Flip | https://andrix-software.github.io/orbitflip.html |
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
The data-practice disclosures and their effective dates are unchanged. Contact
information was standardized to andrix.android@gmail.com on 24 October 2026. `policies.json`
records each source and its import hash for migration verification.

Make future policy changes here. Update a policy's date when its disclosures
change. Migration alone is not an audit or a change in data practices. All policies use **andrix.android@gmail.com** for privacy questions. The old personal policy site keeps its existing pages available, so existing
store links still provide policy text during migration. Only update old links
after confirming the organization pages are live.

Before updating Play Console, confirm each new URL loads publicly without
sign-in. Set both the store listing and any in-app policy link to the same URL.
Keep the old URLs available for installed versions that still use them.
Kids Coloring Book uses the external privacy URL configured in its Android
resources. Its policy has not been imported or audited. Do not reuse another
app's policy for this child-facing app.

## Hosting and validation

Plain HTML; no framework or analytics scripts are required. Preserve the existing
GitHub Pages settings. If Pages needs activation, use **Settings → Pages → Deploy
from a branch → main → / (root)**. `.nojekyll` skips Jekyll processing.
`app-ads.txt` remains at the site root for advertising-seller verification.

Run `python3 tools/validate-policies.py` to validate page structure, index links,
and the seller file. Add `--verify-imports` to check the original migration hashes
before the first publication; later policy edits naturally change those hashes. `published_sha256` verifies
the current distributed version, including the standardized contact address. Public Pages deployment must also be checked independently; a
successful Git push does not prove that the website has deployed.

After deployment, run `python3 tools/check-live-policies.py` to confirm all seven
public pages match these policies. This needs network access to the Pages host.

## Google Play links

Each of the eight app cards links to its package-specific Google Play page
and its own privacy policy. The header and app section also link to the developer
page https://play.google.com/store/apps/dev?id=6051062013551575817 .

`apps.json` records package IDs from the app repositories. These are known app
entries, **not a verified complete inventory of the developer's published apps**.
The cloud network currently blocks Google Play; no live listing availability or
developer-account membership has been verified. `play_listing_verified: false`
is intentional. Check the developer page when access is available, add any missing
published apps, and verify each details link before treating the catalogue as
complete. Kids Coloring Book (`com.andrix.kids.coloring`) was added from the user-provided
Play Store URL and its repository package ID. Its existing external privacy URL
comes from `privacy_url` in the Android strings.xml. The external page and its
contact email have not been verified; it is not one of the six locally maintained
policies. Review it against the shipped app before treating it as a migrated
organization policy.

## Orbit Flip policy

`orbitflip.html` was authored on 24 October 2026 from the verified Orbit Flip
0.8.0 source (commit `516f2218774d21783577b077b24b2db8e7a88902`) and the owner's
18-and-over audience decision. It covers local progress, optional rewarded
AdMob ads, UMP consent/privacy controls, SDK data processing, support, retention
and deletion. No separate Firebase Analytics/Crashlytics, billing, player account,
cloud saves or leaderboard service was present in that implementation.

The verified build uses test ads; the supplied live AdMob IDs and release
configuration have not yet been confirmed integrated. The policy does not claim
an age gate or identity verification. Recheck it against the final release
before completing Play Data safety declarations. The policy uses the existing
public privacy contact, andrix.android@gmail.com. It is a new policy, not a
migrated document; its metadata records the implementation source and published
hash without inventing an original import hash.

Orbit Flip's catalogue entry is marked `in_preparation`; its prospective Play
link is not evidence that a listing is published. After deploying, use
https://andrix-software.github.io/orbitflip.html in Play Console. This policy
change does not rebuild or alter the game APK.
