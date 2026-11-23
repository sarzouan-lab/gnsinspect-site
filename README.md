# gnsinspect.ca

Static, bilingual (FR/EN) website for GNS Inspect — engineering firm specialized in
Loi 122 (Québec Safety Code, Building Chapter) façade and parking-structure verifications.

- `content.py` — all copy, FR and EN
- `build.py` — layout, quote form, schema.org JSON-LD, sitemap, redirects → `dist/`
- `assets/` — CSS and brand images
- `DEPLOY.md` — how to publish (Cloudflare Pages, or upload to Doteasy cPanel)

```
python3 build.py --serve   # http://localhost:8080
```

No dependencies beyond Python 3.
