# Deploying gnsinspect.ca

The site is static HTML. `python3 build.py` writes everything into `dist/`.
There is no database, no PHP, no WordPress and nothing to patch.

Current hosting (as of October 2026): **Web Hosting Canada (WHC)**, Montréal.
Nameservers `ns1–ns4.mysecurecloudhost.com`, server IP 209.42.24.221.
DNS **and** email (`MX gnsinspect.ca`) are both handled by that WHC account,
so do not move DNS away from WHC unless you also move the mailboxes.

Two options. Option A is the recommended end state; Option B is the fastest
"swap tonight" path and keeps everything at WHC.

---

## Option A — Cloudflare Pages (recommended)

Free, global CDN, automatic HTTPS, redeploys on every push to `main`.

1. **Create the Pages project**
   - cloudflare.com → Workers & Pages → Create → Pages → Connect to Git.
   - Pick `sarzouan-lab/gnsinspect-site`.
   - Build command: `python3 build.py`
   - Build output directory: `dist`
   - Deploy. You get a `*.pages.dev` preview URL. Check it.

2. **Form backend**
   - The quote form posts to Web3Forms (free, 250 submissions/month). The access
     key is in `content.py` → `SITE["form"]["web3forms_key"]`; notifications go to
     `simon.a@gnsinspect.ca`.
   - Submit a test from the preview URL and confirm the email arrives.

3. **Point the domain** (in WHC → cPanel → Zone Editor, *not* by changing nameservers)
   - Delete the existing `A` record for `gnsinspect.ca` (209.42.24.221).
   - Add `CNAME  gnsinspect.ca  →  <project>.pages.dev` (WHC supports CNAME
     flattening at the apex; if it refuses, use the `A`/`AAAA` records
     Cloudflare shows under *Custom domains*).
   - Add `CNAME  www  →  <project>.pages.dev`.
   - Leave `MX`, `TXT`/SPF and mail records untouched.
   - In Cloudflare Pages → Custom domains → add `gnsinspect.ca` and
     `www.gnsinspect.ca`. HTTPS is issued automatically within minutes.

4. **Retire WordPress**
   - In cPanel, rename `public_html` to `public_html_wp_backup_2026-10` so the
     old site, plugins and admin login are no longer reachable.
   - After 30 days with no issues, delete the backup and the WordPress database.

5. **Search Console**
   - search.google.com/search-console → add `gnsinspect.ca` (domain property,
     verify with the TXT record WHC lets you add).
   - Submit `https://gnsinspect.ca/sitemap.xml`.
   - Old WordPress URLs are 301-redirected by `_redirects`, so rankings carry over.

---

## Option B — Stay on WHC, upload the files (fastest)

1. Build locally: `python3 build.py` (any machine with Python 3; no packages needed).
   Or download `site.zip` from the latest GitHub Actions run (Actions → Build →
   artifact `site`).
2. WHC → cPanel → **File Manager** → `public_html`.
3. Rename the existing `public_html` to `public_html_wp_backup_2026-10`
   (one level up, in the home directory), then create a new empty `public_html`.
4. Upload the **contents** of `dist/` (not the folder itself) into `public_html`.
   The `.htaccess` included in `dist/` forces HTTPS and redirects the old
   WordPress URLs. Make sure "Show hidden files" is on so `.htaccess` uploads.
5. Open https://gnsinspect.ca in a private window. Check `/en/`,
   `/inspection-facades-loi-122/` and the form.
6. Every later change = edit `content.py` → `python3 build.py` → re-upload `dist/`.
   (Or switch to Option A whenever you want this to be automatic.)

---

## Preview on GitHub Pages

Every push to `main` rebuilds a preview copy on the `gh-pages` branch, served at
https://sarzouan-lab.github.io/gnsinspect-site/ . It is marked `noindex` and exists
only for review; the form on it is live and sends to the same mailbox.

One-time setting: GitHub → repo → Settings → Pages → Source "Deploy from a branch",
branch `gh-pages`, folder `/ (root)`.

Local equivalent: `PREVIEW_URL=https://sarzouan-lab.github.io/gnsinspect-site python3 build.py`

## Day-to-day editing

- All copy lives in `content.py` (FR and EN side by side).
- Layout, form and schema live in `build.py`; styles in `assets/style.css`.
- Preview locally: `python3 build.py --serve` → http://localhost:8080
- Adding a blog article: add a `{"type": "simple", ...}` entry to `PAGES` with
  the article body as HTML; it gets its own URL, hreflang pair and sitemap entry.

## Checklist before going live

- [ ] Test submission from the live domain received at simon.a@gnsinspect.ca
- [ ] Prices or "à partir de" wording confirmed in `content.py`
- [ ] Google Business Profile claimed and pointing at https://gnsinspect.ca
- [ ] GA4 tag added to `head()` in `build.py` (optional)
- [ ] Old WordPress folder renamed, not deleted, for 30 days
