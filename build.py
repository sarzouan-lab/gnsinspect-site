#!/usr/bin/env python3
"""
GNS Inspect static site generator.

Usage:  python3 build.py            -> writes HTML into ./dist
        python3 build.py --serve    -> builds and serves ./dist on :8080

All page content lives in content.py (FR + EN). This file owns the layout,
the quote form, schema.org JSON-LD, sitemap and robots. No dependencies.
"""
import json, os, shutil, sys, datetime
from content import SITE, PAGES, CATEGORIES

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
TODAY = datetime.date.today().isoformat()

# ---------------------------------------------------------------- helpers
SLUGS = {
    ("facades", "fr"): "inspection-facades-loi-122", ("facades", "en"): "facade-inspection-bill-122",
    ("stationnements", "fr"): "inspection-stationnements-loi-122", ("stationnements", "en"): "parking-garage-inspection-bill-122",
    ("services", "fr"): "services", ("services", "en"): "services",
    ("contact", "fr"): "contact", ("contact", "en"): "contact",
}

def url(lang, key):
    """Absolute path for a page. FR is the root language; EN lives under /en/."""
    base = "/" if lang == "fr" else "/en/"
    if key == "index":
        return base
    slug = SLUGS.get((key, lang)) or next(p["slug"] for p in PAGES if p["key"] == key and p["lang"] == lang)
    return f"{base}{slug}/"

def abs_url(lang, slug):
    return SITE["domain"] + url(lang, slug)

def page_by(key, lang):
    return next(p for p in PAGES if p["key"] == key and p["lang"] == lang)

def t(lang, fr, en):
    return fr if lang == "fr" else en

# ---------------------------------------------------------------- layout parts
def head(p):
    lang = p["lang"]
    alt = page_by(p["key"], "en" if lang == "fr" else "fr")
    ld = json.dumps(jsonld(p), ensure_ascii=False, indent=1)
    return f"""<!DOCTYPE html>
<html lang="{'fr-CA' if lang=='fr' else 'en-CA'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p['title']}</title>
<meta name="description" content="{p['meta']}">
<link rel="canonical" href="{abs_url(lang, p['key'])}">
<link rel="alternate" hreflang="fr-CA" href="{abs_url('fr', p['key'])}">
<link rel="alternate" hreflang="en-CA" href="{abs_url('en', p['key'])}">
<link rel="alternate" hreflang="x-default" href="{abs_url('fr', p['key'])}">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['meta']}">
<meta property="og:type" content="website">
<meta property="og:url" content="{abs_url(lang, p['key'])}">
<meta property="og:image" content="{SITE['domain']}/assets/img/icon-512.png">
<meta property="og:locale" content="{'fr_CA' if lang=='fr' else 'en_CA'}">
<link rel="icon" href="/assets/img/favicon-48.png" sizes="48x48">
<link rel="apple-touch-icon" href="/assets/img/icon-192.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>"""

def topbar(p):
    lang = p["lang"]
    alt_lang = "en" if lang == "fr" else "fr"
    return f"""
<div class="topbar"><div class="wrap">
  <div>{t(lang, 'Montréal · Laval · Rive-Sud · Rive-Nord', 'Montréal · Laval · South Shore · North Shore')} &nbsp;|&nbsp; <a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a> &nbsp;|&nbsp; <a href="mailto:{SITE['email']}">{SITE['email']}</a></div>
  <a class="lang" href="{url(alt_lang, p['key'])}" hreflang="{alt_lang}">{'EN' if lang=='fr' else 'FR'}</a>
</div></div>"""

def header(p):
    lang = p["lang"]
    nav = [
        ("facades", t(lang, "Façades", "Façades")),
        ("stationnements", t(lang, "Stationnements", "Parking garages")),
        ("services", t(lang, "Services d’ingénierie", "Engineering services")),
        ("contact", t(lang, "Contact", "Contact")),
    ]
    links = "".join(f'<a href="{url(lang, k)}">{label}</a>' for k, label in nav)
    return f"""
<header class="site"><div class="wrap">
  <a class="brand" href="{url(lang,'index')}"><img src="/assets/img/logo-icon.png" alt="GNS Inspect" width="46" height="46"><span>GNS <b>INSPECT</b></span></a>
  <button class="menu-toggle" aria-label="Menu" onclick="document.querySelector('nav.main').classList.toggle('open')">☰</button>
  <nav class="main">{links}</nav>
  <a class="btn" href="#devis">{t(lang, 'Demander une soumission', 'Request a quote')}</a>
</div></header>"""

def quote_form(p, compact=False):
    lang = p["lang"]
    f = SITE["form"]
    return f"""
<div class="card" id="devis">
  <h3>{t(lang, 'Soumission en 24 h', 'Quote within 24 h')}</h3>
  <div class="sub">{t(lang, 'Prix fixe confirmé par écrit. Aucune obligation.', 'Fixed price confirmed in writing. No obligation.')}</div>
  <form action="{f['action']}" method="POST">
    <input type="hidden" name="_subject" value="{t(lang,'Nouvelle demande de soumission — gnsinspect.ca','New quote request — gnsinspect.ca')}">
    <input type="hidden" name="_language" value="{lang}">
    <input type="hidden" name="_page" value="{p['key']}">
    <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off">
    <label>{t(lang,'Service','Service')}</label>
    <select name="service" required>
      <option value="facade">{t(lang,'Inspection de façades (Loi 122)','Façade inspection (Bill 122)')}</option>
      <option value="stationnement">{t(lang,'Inspection de stationnement étagé (Loi 122)','Parking garage inspection (Bill 122)')}</option>
      <option value="les-deux">{t(lang,'Les deux','Both')}</option>
      {''.join(f'<option value="{c["key"]}">{c[lang]["title"]}</option>' for c in CATEGORIES)}
      <option value="autre">{t(lang,'Autre / je ne sais pas','Other / not sure')}</option>
    </select>
    <label>{t(lang,'Adresse de l’immeuble','Building address')}</label>
    <input name="adresse" required placeholder="{t(lang,'ex. 2009 rue Sherbrooke Est, Montréal','e.g. 2009 Sherbrooke St E, Montréal')}">
    <div class="row">
      <div><label>{t(lang,'Étages hors sol','Storeys above grade')}</label><input name="etages" type="number" min="1" placeholder="5+"></div>
      <div><label>{t(lang,'Année de construction','Year built')}</label><input name="annee" type="number" min="1850" max="2026" placeholder="1985"></div>
    </div>
    <label>{t(lang,'Vous êtes','You are')}</label>
    <select name="role">
      <option>{t(lang,'Syndicat de copropriété','Condo syndicate')}</option>
      <option>{t(lang,'Gestionnaire immobilier','Property manager')}</option>
      <option>{t(lang,'Propriétaire','Owner')}</option>
      <option>{t(lang,'Autre','Other')}</option>
    </select>
    <div class="row">
      <div><label>{t(lang,'Nom','Name')}</label><input name="nom" required></div>
      <div><label>{t(lang,'Téléphone','Phone')}</label><input name="telephone" type="tel" required></div>
    </div>
    <label>{t(lang,'Courriel','Email')}</label>
    <input name="courriel" type="email" required>
    <button class="btn" type="submit">{t(lang,'Recevoir ma soumission','Get my quote')}</button>
    <div class="fine">{t(lang,'Réponse par un ingénieur, pas un centre d’appels. Vos données ne sont jamais partagées.','Answered by an engineer, not a call centre. Your data is never shared.')}</div>
  </form>
</div>"""

def cred(lang):
    return f"""
<div class="cred">
  <div class="seal">ing.<br>OIQ</div>
  <div>
    <b>{t(lang, 'Une équipe d’ingénieurs membres de l’OIQ', 'A team of OIQ-licensed engineers')}</b><br>
    {t(lang, 'Structure, enveloppe du bâtiment, mécanique et environnement sous un même toit.', 'Structural, building envelope, mechanical and environmental under one roof.')}<br>
    <small>{t(lang, 'Chaque rapport est signé et scellé par un ingénieur qui en assume la responsabilité professionnelle.', 'Every report is signed and sealed by an engineer who takes professional responsibility for it.')}</small>
  </div>
</div>"""

def cta_band(lang):
    return f"""
<div class="cta-band"><div class="wrap">
  <h2>{t(lang, 'Votre prochaine échéance Loi 122 approche?', 'Is your next Bill 122 deadline coming up?')}</h2>
  <div style="display:flex;gap:16px;align-items:center;flex-wrap:wrap">
    <a class="phone" href="tel:{SITE['phone_tel']}">{SITE['phone']}</a>
    <a class="btn" href="#devis">{t(lang,'Demander une soumission','Request a quote')}</a>
  </div>
</div></div>"""

def footer(p):
    lang = p["lang"]
    return f"""
<footer><div class="wrap">
  <div>
    <a class="brand" href="{url(lang,'index')}" style="color:#fff"><img src="/assets/img/logo-icon.png" alt="" width="46" height="46"><span>GNS <b style="color:var(--yellow)">INSPECT</b></span></a>
    <p style="margin-top:12px">{t(lang, 'Firme d’ingénierie spécialisée dans la vérification des façades et des stationnements étagés exigée par le chapitre Bâtiment du Code de sécurité du Québec (Loi 122).', 'Engineering firm specialized in the façade and parking-structure verifications required by Chapter VIII of Québec’s Safety Code (Bill 122).')}</p>
  </div>
  <div><h4><a href="{url(lang,'services')}">{t(lang,'Services','Services')}</a></h4><ul>
    <li><a href="{url(lang,'facades')}">{t(lang,'Inspection de façades','Façade inspection')}</a></li>
    <li><a href="{url(lang,'stationnements')}">{t(lang,'Inspection de stationnements','Parking garage inspection')}</a></li>
    {''.join(f'<li><a href="{url(lang, c["key"])}">{c[lang]["title"].split(" · ")[0]}</a></li>' for c in CATEGORIES)}
  </ul></div>
  <div><h4>{t(lang,'Entreprise','Company')}</h4><ul>
    <li><a href="{url(lang,'contact')}">{t(lang,'Nous joindre','Contact')}</a></li>
    <li><a href="{url('en' if lang=='fr' else 'fr', p['key'])}">{t(lang,'English','Français')}</a></li>
  </ul></div>
  <div><h4>{t(lang,'Coordonnées','Get in touch')}</h4><ul>
    <li>{SITE['address']}</li>
    <li><a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></li>
    <li><a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
    <li>{t(lang,'Lun–jeu 8 h–18 h · Ven 8 h–13 h','Mon–Thu 8am–6pm · Fri 8am–1pm')}</li>
  </ul></div>
  <div class="legal"><span>© {datetime.date.today().year} GNS Inspect. {t(lang,'Tous droits réservés.','All rights reserved.')}</span><span>{t(lang,'Membre de l’Ordre des ingénieurs du Québec','Member of the Ordre des ingénieurs du Québec')}</span></div>
</div></footer>
</body></html>"""

# ---------------------------------------------------------------- schema.org
def jsonld(p):
    lang = p["lang"]
    org = {
        "@type": "ProfessionalService",
        "@id": SITE["domain"] + "/#org",
        "name": "GNS Inspect",
        "url": SITE["domain"],
        "logo": SITE["domain"] + "/assets/img/icon-512.png",
        "telephone": SITE["phone_e164"],
        "email": SITE["email"],
        "address": {"@type": "PostalAddress", "streetAddress": SITE["street"], "addressLocality": "Montréal",
                    "addressRegion": "QC", "postalCode": SITE["postal"], "addressCountry": "CA"},
        "areaServed": ["Montréal", "Laval", "Longueuil", "Brossard", "Westmount", "Côte Saint-Luc", "Laurentides", "Montérégie"],
        "openingHours": ["Mo-Th 08:00-18:00", "Fr 08:00-13:00"],
        "priceRange": "$$",
    }
    graph = [org]
    if p.get("service_name"):
        graph.append({"@type": "Service", "name": p["service_name"], "serviceType": p["service_name"],
                      "provider": {"@id": SITE["domain"] + "/#org"}, "areaServed": "Greater Montréal",
                      "url": abs_url(lang, p["key"]), "description": p["meta"]})
    if p.get("faq"):
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]})
    return {"@context": "https://schema.org", "@graph": graph}

# ---------------------------------------------------------------- page bodies
def render_home(p):
    lang, c = p["lang"], p["content"]
    svc_cards = "".join(f"""
    <div class="service"><span class="tag">{s['tag']}</span><h3>{s['title']}</h3><p>{s['text']}</p>
      <ul>{''.join(f'<li>{b}</li>' for b in s['bullets'])}</ul>
      <a class="btn ghost" href="{url(lang, s['key'])}">{s['cta']}</a></div>""" for s in c["services"])
    steps = "".join(f"<li><b>{a}</b>{b}</li>" for a, b in c["steps"])
    why = "".join(f"<li>{x}</li>" for x in c["why"])
    return f"""
<section class="hero"><div class="wrap">
  <div>
    <span class="eyebrow">{c['eyebrow']}</span>
    <h1>{c['h1']}</h1>
    <p class="lead">{c['lead']}</p>
    <div class="cta"><a class="btn" href="#devis">{c['cta']}</a><a class="phone" href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></div>
    <div class="proof">{''.join(f'<div><b>{b}</b>{s}</div>' for b, s in c['proof'])}</div>
  </div>
  {quote_form(p)}
</div></section>

<section><div class="wrap">
  <span class="eyebrow">{c['services_eyebrow']}</span>
  <h2>{c['services_h2']}</h2>
  <div class="grid-2" style="margin-top:28px">{svc_cards}</div>
</div></section>

<section class="soft"><div class="wrap grid-2">
  <div><span class="eyebrow">{c['how_eyebrow']}</span><h2>{c['how_h2']}</h2><ol class="steps">{steps}</ol></div>
  <div><span class="eyebrow">{c['why_eyebrow']}</span><h2>{c['why_h2']}</h2><ul class="checks">{why}</ul>{cred(lang)}</div>
</div></section>

{suite_section(lang)}

<section class="soft"><div class="wrap">
  <div class="cred" style="background:#0b3d5c">
    <div class="seal" style="background:#fff;color:#0b3d5c;font-size:.7rem">Hydro-<br>Québec</div>
    <div><b>{t(lang,'Partenaire du programme Solutions efficaces d’Hydro-Québec','Partner in Hydro-Québec’s Solutions efficaces program')}</b><br>
    {t(lang,'Nous déposons vos demandes d’appui financier : étude d’ingénierie subventionnée jusqu’à 60 000 $ et mesures financées en partie, pour les bâtiments commerciaux et multilogements.','We file your financial-assistance applications: engineering study subsidized up to $60,000 and measures partly funded, for commercial and multi-unit buildings.')}
    &nbsp;<a href="{url(lang,'energie')}" style="color:var(--yellow);font-weight:700">{t(lang,'En savoir plus →','Learn more →')}</a></div>
  </div>
</div></section>

<section><div class="wrap">
  <p style="text-align:center;color:var(--grey);font-weight:700;margin-bottom:18px">{c['partners']}</p>
  <div class="logos"><span>Banque Scotia</span><span>Banque Nationale</span><span>Banque Laurentienne</span><span>First National</span><span>CIBC</span></div>
</div></section>
{cta_band(lang)}"""

def render_service(p):
    lang, c = p["lang"], p["content"]
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in p["faq"])
    who = "".join(f"<li>{x}</li>" for x in c["who"])
    incl = "".join(f"<li><b>{a}</b> {b}</li>" for a, b in c["includes"])
    why = "".join(f"<li>{x}</li>" for x in c["why"])
    return f"""
<section class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{url(lang,'index')}">{t(lang,'Accueil','Home')}</a> › {c['crumb']}</div>
  <span class="eyebrow" style="color:var(--yellow)">{c['eyebrow']}</span>
  <h1>{c['h1']}</h1>
  <p class="lead">{c['lead']}</p>
  <div class="cta"><a class="btn" href="#devis">{t(lang,'Demander une soumission','Request a quote')}</a><a class="phone" href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></div>
</div></section>

<section><div class="wrap two-col">
  <div class="prose">
    <h2>{c['who_h2']}</h2><ul class="checks">{who}</ul>
    <div class="callout">{c['callout']}</div>
    <h2>{c['includes_h2']}</h2><ol class="steps">{incl}</ol>
    <h2>{c['why_h2']}</h2><ul class="checks">{why}</ul>
    {cred(lang)}
    <h2>{t(lang,'Questions fréquentes','Frequently asked questions')}</h2>
    <div class="faq">{faq}</div>
  </div>
  <aside class="sticky">{quote_form(p)}</aside>
</div></section>
{cta_band(lang)}"""

def render_simple(p):
    lang, c = p["lang"], p["content"]
    return f"""
<section class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{url(lang,'index')}">{t(lang,'Accueil','Home')}</a> › {c['crumb']}</div>
  <h1>{c['h1']}</h1><p class="lead">{c['lead']}</p>
</div></section>
<section><div class="wrap two-col">
  <div class="prose">{c['body']}</div>
  <aside class="sticky">{quote_form(p)}</aside>
</div></section>
{cta_band(lang)}"""

def category_cards(lang):
    return "".join(f"""
    <div class="service"><h3>{c[lang]['title']}</h3><p>{c[lang]['card']}</p>
      <a class="btn ghost" href="{url(lang, c['key'])}">{t(lang,'En savoir plus','Learn more')}</a></div>""" for c in CATEGORIES)

def suite_section(lang):
    return f"""
<section><div class="wrap">
  <span class="eyebrow">{t(lang,'Suite complète','Full suite')}</span>
  <h2>{t(lang,'Tous les services d’ingénierie du bâtiment, une seule équipe','Every building engineering service, one team')}</h2>
  <p style="max-width:70ch;color:var(--grey)">{t(lang,'Inspections, expertise, structure, mécanique du bâtiment, environnement et copropriété : nos ingénieurs vous suivent de l’inspection jusqu’à la surveillance des travaux.','Inspections, expertise, structural, building mechanical, environmental and condominium services: our engineers stay with you from inspection through construction oversight.')}</p>
  <div class="grid-3" style="margin-top:28px">{category_cards(lang)}</div>
</div></section>"""

def render_hub(p):
    lang, c = p["lang"], p["content"]
    return f"""
<section class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{url(lang,'index')}">{t(lang,'Accueil','Home')}</a> › {c['crumb']}</div>
  <h1>{c['h1']}</h1><p class="lead">{c['lead']}</p>
  <div class="cta"><a class="btn" href="#devis">{t(lang,'Demander une soumission','Request a quote')}</a><a class="phone" href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></div>
</div></section>
<section class="soft"><div class="wrap">
  <span class="eyebrow">{t(lang,'Obligations Loi 122','Bill 122 obligations')}</span>
  <h2>{t(lang,'Vérifications réglementaires','Regulatory verifications')}</h2>
  <div class="grid-2" style="margin-top:24px">
    <div class="service"><h3>{t(lang,'Inspection de façades','Façade inspection')}</h3><p>{t(lang,'Bâtiments de 5 étages et plus, tous les 5 ans.','Buildings of 5+ storeys, every 5 years.')}</p><a class="btn ghost" href="{url(lang,'facades')}">{t(lang,'Voir le service','See service')}</a></div>
    <div class="service"><h3>{t(lang,'Inspection de stationnements étagés','Parking garage inspection')}</h3><p>{t(lang,'Vérification annuelle et approfondie quinquennale.','Annual check and five-year in-depth verification.')}</p><a class="btn ghost" href="{url(lang,'stationnements')}">{t(lang,'Voir le service','See service')}</a></div>
  </div>
</div></section>
<section><div class="wrap">
  <span class="eyebrow">{t(lang,'Services d’ingénierie','Engineering services')}</span>
  <h2>{t(lang,'Sept domaines, une équipe','Seven practice areas, one team')}</h2>
  <div class="grid-3" style="margin-top:24px">{category_cards(lang)}</div>
  <div style="margin-top:36px">{cred(lang)}</div>
</div></section>
<section class="soft"><div class="wrap two-col"><div class="prose"><h2>{t(lang,'Une question? Un ingénieur vous répond.','A question? An engineer answers.')}</h2><p>{t(lang,'Décrivez votre situation; nous vous dirons en 24 h quel service s’applique et à quel prix.','Describe your situation; within 24 h we will tell you which service applies and at what price.')}</p></div><aside>{quote_form(p)}</aside></div></section>
{cta_band(lang)}"""

def render_category(p):
    lang, c = p["lang"], p["content"]
    items = "".join(f"<li><b>{a}</b>{b}</li>" for a, b in c["items"])
    who = "".join(f"<li>{x}</li>" for x in c["for"])
    others = "".join(f'<li><a href="{url(lang, k["key"])}">{k[lang]["title"]}</a></li>' for k in CATEGORIES if k["key"] != p["key"])
    return f"""
<section class="page-hero"><div class="wrap">
  <div class="breadcrumb"><a href="{url(lang,'index')}">{t(lang,'Accueil','Home')}</a> › <a href="{url(lang,'services')}">{t(lang,'Services d’ingénierie','Engineering services')}</a> › {c['title']}</div>
  <h1>{c['h1']}</h1><p class="lead">{c['lead']}</p>
  <div class="cta"><a class="btn" href="#devis">{t(lang,'Demander une soumission','Request a quote')}</a><a class="phone" href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></div>
</div></section>
<section><div class="wrap two-col">
  <div class="prose">
    <h2>{t(lang,'Pour qui','Who it is for')}</h2><ul class="checks">{who}</ul>
    <h2>{t(lang,'Nos services','Our services')}</h2><ol class="steps">{items}</ol>
    {cred(lang)}
    <h2>{t(lang,'Autres domaines','Other practice areas')}</h2><ul>{others}</ul>
  </div>
  <aside class="sticky">{quote_form(p)}</aside>
</div></section>
{cta_band(lang)}"""

RENDER = {"home": render_home, "service": render_service, "simple": render_simple, "hub": render_hub, "category": render_category}

# ---------------------------------------------------------------- build
def build():
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(DIST, "assets"))
    urls = []
    for p in PAGES:
        html = head(p) + topbar(p) + header(p) + RENDER[p["type"]](p) + footer(p)
        rel = url(p["lang"], p["key"]).lstrip("/")
        out_dir = os.path.join(DIST, rel)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        urls.append((abs_url(p["lang"], p["key"]), p["key"]))
    # sitemap with hreflang pairs
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for loc, key in urls:
        sm.append(f"<url><loc>{loc}</loc><lastmod>{TODAY}</lastmod>"
                  f'<xhtml:link rel="alternate" hreflang="fr-CA" href="{abs_url("fr", key)}"/>'
                  f'<xhtml:link rel="alternate" hreflang="en-CA" href="{abs_url("en", key)}"/></url>')
    sm.append("</urlset>")
    open(os.path.join(DIST, "sitemap.xml"), "w").write("\n".join(sm))
    open(os.path.join(DIST, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE['domain']}/sitemap.xml\n")
    # legacy WordPress URLs -> new pages (Netlify/Cloudflare _redirects format)
    open(os.path.join(DIST, "_redirects"), "w").write(
        "/our-services/* /services/ 301\n/our-services /services/ 301\n/contact-us/ /contact/ 301\n"
        "/about-us/ / 301\n/blog/* / 301\n/wp-content/* / 301\n/wp-admin/* / 301\n")
    # same for Apache (WHC cPanel)
    open(os.path.join(DIST, ".htaccess"), "w").write(
        "RewriteEngine On\nRewriteCond %{HTTPS} off\nRewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]\n"
        "Redirect 301 /our-services/ /services/\nRedirect 301 /contact-us/ /contact/\nRedirect 301 /about-us/ /\n"
        "RedirectMatch 301 ^/blog/.*$ /\nRedirectMatch 301 ^/wp-(content|admin|includes)/.*$ /\n"
        "ErrorDocument 404 /index.html\n"
        "<IfModule mod_expires.c>\nExpiresActive On\nExpiresByType image/png \"access plus 1 year\"\nExpiresByType text/css \"access plus 1 month\"\n</IfModule>\n")
    print(f"Built {len(PAGES)} pages into {DIST}")

if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        import http.server, functools
        h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIST)
        print("Serving on http://localhost:8080")
        http.server.ThreadingHTTPServer(("", 8080), h).serve_forever()
