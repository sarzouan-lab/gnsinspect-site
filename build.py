#!/usr/bin/env python3
"""
GNS Inspect static site generator.

Usage:  python3 build.py            -> writes HTML into ./dist
        python3 build.py --serve    -> builds and serves ./dist on :8080

All page content lives in content.py (FR + EN). This file owns the layout,
the quote form, schema.org JSON-LD, sitemap and robots. No dependencies.
"""
import json, os, shutil, sys, datetime, urllib.parse
from content import SITE, PAGES, CATEGORIES

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
TODAY = datetime.date.today().isoformat()

# Preview builds (GitHub Pages): set PREVIEW_URL to the address the build is served
# from, e.g. https://sarzouan-lab.github.io/gnsinspect-site . Links and assets then
# carry that sub-path, every page is marked noindex, and canonicals keep pointing at
# the production domain. Unset = production build for gnsinspect.ca.
PREVIEW = os.environ.get("PREVIEW_URL", "").rstrip("/")
PREFIX = urllib.parse.urlparse(PREVIEW).path.rstrip("/") if PREVIEW else ""

# ---------------------------------------------------------------- helpers
SLUGS = {
    ("facades", "fr"): "inspection-facades-loi-122", ("facades", "en"): "facade-inspection-bill-122",
    ("stationnements", "fr"): "inspection-stationnements-loi-122", ("stationnements", "en"): "parking-garage-inspection-bill-122",
    ("services", "fr"): "services", ("services", "en"): "services",
    ("contact", "fr"): "contact", ("contact", "en"): "contact",
    ("merci", "fr"): "merci", ("merci", "en"): "thank-you",
    ("analyse", "fr"): "analyse-energetique-hydro-quebec", ("analyse", "en"): "energy-analysis-hydro-quebec",
    ("fonds", "fr"): "etude-fonds-de-prevoyance-loi-16", ("fonds", "en"): "reserve-fund-study-bill-16",
    ("carnet", "fr"): "carnet-entretien-copropriete-loi-16", ("carnet", "en"): "condominium-maintenance-log-bill-16",
    ("valeur", "fr"): "valeur-de-reconstruction-copropriete-assurance", ("valeur", "en"): "condominium-reconstruction-value-appraisal",
    ("charges", "fr"): "etude-charges-communes-copropriete", ("charges", "en"): "condominium-common-expense-study",
    ("mli", "fr"): "audit-energetique-aph-select-schl", ("mli", "en"): "energy-audit-mli-select-cmhc",
    ("divulgation", "fr"): "divulgation-energie-ges-montreal-reglement-21-042", ("divulgation", "en"): "montreal-energy-ghg-disclosure-bylaw-21-042",
}

def path(lang, key):
    """Site-relative path for a page. FR is the root language; EN lives under /en/."""
    base = "/" if lang == "fr" else "/en/"
    if key == "index":
        return base
    slug = SLUGS.get((key, lang)) or next(p["slug"] for p in PAGES if p["key"] == key and p["lang"] == lang)
    return f"{base}{slug}/"

def url(lang, key):
    """Link target as written in the HTML (carries the preview sub-path, if any)."""
    return PREFIX + path(lang, key)

def abs_url(lang, key):
    """Canonical production URL."""
    return SITE["domain"] + path(lang, key)

def served_url(lang, key):
    """URL on the host this build is actually served from (form redirect)."""
    return (PREVIEW or SITE["domain"]) + path(lang, key)

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
{'<meta name="robots" content="noindex">' if (p.get("noindex") or PREVIEW) else ""}
<link rel="alternate" hreflang="fr-CA" href="{abs_url('fr', p['key'])}">
<link rel="alternate" hreflang="en-CA" href="{abs_url('en', p['key'])}">
<link rel="alternate" hreflang="x-default" href="{abs_url('fr', p['key'])}">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['meta']}">
<meta property="og:type" content="website">
<meta property="og:url" content="{abs_url(lang, p['key'])}">
<meta property="og:image" content="{SITE['domain']}/assets/img/icon-512.png">
<meta property="og:locale" content="{'fr_CA' if lang=='fr' else 'en_CA'}">
<link rel="icon" href="{PREFIX}/assets/img/favicon-48.png" sizes="48x48">
<link rel="apple-touch-icon" href="{PREFIX}/assets/img/icon-192.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{PREFIX}/assets/style.css">
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
        ("copropriete", t(lang, "Copropriété", "Condos")),
        ("energie", t(lang, "Énergie", "Energy")),
        ("tests", t(lang, "Tests", "Testing")),
        ("services", t(lang, "Services", "Services")),
        ("contact", t(lang, "Contact", "Contact")),
    ]
    links = "".join(f'<a href="{url(lang, k)}">{label}</a>' for k, label in nav)
    return f"""
<header class="site"><div class="wrap">
  <a class="brand" href="{url(lang,'index')}"><img src="{PREFIX}/assets/img/logo-icon.png" alt="GNS Inspect" width="46" height="46"><span>GNS <b>INSPECT</b></span></a>
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
  <form action="https://api.web3forms.com/submit" method="POST">
    <input type="hidden" name="access_key" value="{f['web3forms_key']}">
    <input type="hidden" name="subject" value="{t(lang,'Nouvelle demande de soumission — gnsinspect.ca','New quote request — gnsinspect.ca')}">
    <input type="hidden" name="from_name" value="gnsinspect.ca">
    <input type="hidden" name="redirect" value="{served_url(lang,'merci')}">
    <input type="hidden" name="langue" value="{lang}">
    <input type="hidden" name="page" value="{p['key']}">
    <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off">
    <label>{t(lang,'Service','Service')}</label>
    <select name="service" required>
      <option value="facade">{t(lang,'Inspection de façades (Loi 122)','Façade inspection (Bill 122)')}</option>
      <option value="stationnement">{t(lang,'Inspection de stationnement étagé (Loi 122)','Parking garage inspection (Bill 122)')}</option>
      <option value="les-deux">{t(lang,'Les deux','Both')}</option>
      {''.join(f'<option value="{c["key"]}"{" selected" if c["key"] == p["key"] else ""}>{c[lang]["title"]}</option>' for c in CATEGORIES)}
      <option value="analyse-energetique"{' selected' if p['key'] == 'analyse' else ''}>{t(lang,'Analyse énergétique (Hydro-Québec)','Energy analysis (Hydro-Québec)')}</option>
      <option value="fonds-prevoyance"{' selected' if p['key'] == 'fonds' else ''}>{t(lang,'Étude du fonds de prévoyance (Loi 16)','Reserve fund study (Bill 16)')}</option>
      <option value="carnet-entretien"{' selected' if p['key'] == 'carnet' else ''}>{t(lang,'Carnet d’entretien (Loi 16)','Maintenance log (Bill 16)')}</option>
      <option value="valeur-reconstruction"{' selected' if p['key'] == 'valeur' else ''}>{t(lang,'Valeur de reconstruction (copropriété)','Reconstruction value (condominium)')}</option>
      <option value="charges-communes"{' selected' if p['key'] == 'charges' else ''}>{t(lang,'Étude des charges communes','Common-expense study')}</option>
      <option value="aph-select"{' selected' if p['key'] == 'mli' else ''}>{t(lang,'Audit énergétique APH Select (SCHL)','MLI Select energy audit (CMHC)')}</option>
      <option value="divulgation-21-042"{' selected' if p['key'] == 'divulgation' else ''}>{t(lang,'Divulgation énergie et GES (Montréal)','Energy and GHG disclosure (Montréal)')}</option>
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
    <small>{t(lang, 'Chaque rapport est signé et scellé par un ingénieur et couvert par une assurance responsabilité professionnelle (erreurs et omissions).', 'Every report is signed and sealed by an engineer and covered by professional liability (errors and omissions) insurance.')}</small>
  </div>
</div>"""

def cta_band(lang, heading=None):
    return f"""
<div class="cta-band"><div class="wrap">
  <h2>{heading or t(lang, 'Votre prochaine échéance Loi 122 approche?', 'Is your next Bill 122 deadline coming up?')}</h2>
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
    <a class="brand" href="{url(lang,'index')}" style="color:#fff"><img src="{PREFIX}/assets/img/logo-icon.png" alt="" width="46" height="46"><span>GNS <b style="color:var(--yellow)">INSPECT</b></span></a>
    <p style="margin-top:12px">{t(lang, 'Firme d’ingénierie spécialisée dans la vérification des façades et des stationnements étagés exigée par le chapitre Bâtiment du Code de sécurité du Québec (Loi 122).', 'Engineering firm specialized in the façade and parking-structure verifications required by Chapter VIII of Québec’s Safety Code (Bill 122).')}</p>
  </div>
  <div><h4><a href="{url(lang,'services')}">{t(lang,'Services','Services')}</a></h4><ul>
    <li><a href="{url(lang,'facades')}">{t(lang,'Inspection de façades','Façade inspection')}</a></li>
    <li><a href="{url(lang,'stationnements')}">{t(lang,'Inspection de stationnements','Parking garage inspection')}</a></li>
    {''.join(f'<li><a href="{url(lang, k)}">{t(lang, fr, en)}</a></li>' for k, fr, en, _a, _b in ENERGY)}
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
def testimonials(lang):
    items = [x for x in (SITE.get("testimonials") or []) if x.get("approved")]
    if not items:
        return ""
    cards = "".join(f"""<div class="service"><p>« {x['quote_fr'] if lang == 'fr' else x['quote_en']} »</p><p style="margin-top:auto"><b>{x['name']}</b><br><span style="color:var(--grey)">{x['role_fr'] if lang == 'fr' else x['role_en']}</span></p></div>""" for x in items)
    return f"""<section><div class="wrap"><span class="eyebrow">{t(lang,'Témoignages','Testimonials')}</span><h2>{t(lang,'Ce que nos clients en disent','What our clients say')}</h2><div class="grid-3" style="margin-top:24px">{cards}</div></div></section>"""

# Homepage hero slides after the Loi 122 one: (page key, eyebrow, heading, text, button) in FR and EN.
HERO_SLIDES = [
    ("analyse", ("Partenaire du programme Solutions efficaces d’Hydro-Québec", "Partner in Hydro-Québec’s Solutions efficaces program"),
     ("Analyse énergétique de votre bâtiment, remboursée jusqu’à 60 000 $", "An energy analysis of your building, reimbursed up to $60,000"),
     ("Votre bâtiment consomme 1 GWh ou plus par année? Hydro-Québec rembourse l’analyse réalisée par nos ingénieurs. Nous préparons la demande, faisons l’analyse et vous accompagnons jusqu’aux mesures.", "Does your building use 1 GWh or more a year? Hydro-Québec reimburses the analysis carried out by our engineers. We prepare the application, do the analysis and stay with you through the measures."),
     ("Voir si vous êtes admissible", "Check your eligibility")),
    ("facades", ("Loi 122 · Bâtiments de 5 étages et plus", "Bill 122 · Buildings of 5+ storeys"),
     ("Inspection de façades : votre rapport quinquennal, signé par un ingénieur", "Façade inspection: your five-year report, signed by an engineer"),
     ("Inspection visuelle et rapprochée par nacelle, cordiste ou drone, classification des conditions dangereuses, échéancier et budget de travaux. Rapport livré en 10 jours ouvrables.", "Visual and close-up inspection by lift, rope access or drone, dangerous-condition classification, work schedule and budget. Report delivered in 10 business days."),
     ("Voir l’inspection de façades", "See façade inspection")),
    ("tests", ("Tests et analyses en laboratoire", "Testing and laboratory analysis"),
     ("Moisissures, radon, amiante : des tests indépendants, un rapport d’ingénieur", "Mould, radon, asbestos: independent testing, an engineer’s report"),
     ("Nous prélevons, faisons analyser en laboratoire et expliquons les résultats, leur cause et les correctifs. Nous ne vendons aucun travail de décontamination.", "We sample, have it analysed in a laboratory and explain the results, their cause and the fix. We sell no decontamination work."),
     ("Voir les tests offerts", "See our testing services")),
    ("stationnements", ("Loi 122 · Stationnements étagés", "Bill 122 · Multi-level parking"),
     ("Inspection de stationnement : vérifications annuelle et quinquennale", "Parking garage inspection: annual and five-year verifications"),
     ("Sondages, délaminage, corrosion et chlorures, plan de localisation des défauts et priorités de réparation, sans fermer votre stationnement.", "Sounding, delamination, corrosion and chloride testing, a defect map and repair priorities, without closing your garage."),
     ("Voir l’inspection de stationnements", "See parking inspection")),
    ("copropriete", ("Copropriété · Loi 16 · Échéance août 2028", "Condominiums · Bill 16 · August 2028 deadline"),
     ("Carnet d’entretien et étude du fonds de prévoyance pour votre syndicat", "Maintenance log and reserve fund study for your syndicate"),
     ("Tous les syndicats doivent maintenant les obtenir d’un professionnel. Nos ingénieurs produisent les deux à partir d’une même inspection, avec vos obligations Loi 122 intégrées.", "Every syndicate must now obtain them from a professional. Our engineers produce both from a single inspection, with your Bill 122 obligations built in."),
     ("Voir les services aux copropriétés", "See condominium services")),
    ("mli", ("SCHL · APH Select · Immeubles multilogements", "CMHC · MLI Select · Multi-unit buildings"),
     ("Audit énergétique APH Select pour votre financement SCHL", "MLI Select energy audit for your CMHC financing"),
     ("Inspection, modélisation et rapport d’audit signé par un ingénieur : les points d’efficacité énergétique qui donnent accès aux primes réduites et à l’amortissement prolongé.", "Inspection, modelling and an engineer-signed audit report: the energy-efficiency points that unlock reduced premiums and longer amortization."),
     ("Voir l’audit APH Select", "See the MLI Select audit")),
    ("services", ("Une suite complète de services d’ingénierie", "A full suite of engineering services"),
     ("Structure, mécanique, environnement, expertise : une seule équipe d’ingénieurs", "Structural, mechanical, environmental, expertise: one engineering team"),
     ("Inspections pré-achat et pour financement, plans de structure et de CVAC, évaluations environnementales, vices cachés, fonds de prévoyance : de l’inspection jusqu’à la surveillance des travaux.", "Pre-purchase and financing inspections, structural and HVAC design, environmental assessments, latent defects, reserve fund studies: from inspection through construction oversight."),
     ("Voir tous les services", "See all services")),
]

def hero_slides(lang):
    k = 0 if lang == "fr" else 1
    return "".join(f"""
      <div class="slide">
        <span class="eyebrow">{eb[k]}</span>
        <p class="h1">{h[k]}</p>
        <p class="lead">{tx[k]}</p>
        <div class="cta"><a class="btn" href="{url(lang, key)}">{cta[k]}</a><a class="phone" href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></div>
      </div>""" for key, eb, h, tx, cta in HERO_SLIDES)

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
  <div class="hero-rotator" data-interval="7000">
    <div class="hero-slides">
      <div class="slide on">
        <span class="eyebrow">{c['eyebrow']}</span>
        <h1>{c['h1']}</h1>
        <p class="lead">{c['lead']}</p>
        <div class="cta"><a class="btn" href="#devis">{c['cta']}</a><a class="phone" href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></div>
        <div class="proof">{''.join(f'<div><b>{b}</b>{s}</div>' for b, s in c['proof'])}</div>
      </div>
      {hero_slides(lang)}
    </div>
    <div class="hero-dots" role="tablist" aria-label="{t(lang,'Services à la une','Featured services')}">{''.join(f'<button type="button" class="{"on" if i == 0 else ""}" aria-label="{i+1}"></button>' for i in range(len(HERO_SLIDES) + 1))}</div>
  </div>
  {quote_form(p)}
</div></section>
<script>
(function () {{
  var r = document.querySelector('.hero-rotator'); if (!r) return;
  var slides = r.querySelectorAll('.slide'), dots = r.querySelectorAll('.hero-dots button'), i = 0, timer = null;
  function show(n) {{
    i = (n + slides.length) % slides.length;
    slides.forEach(function (s, k) {{ s.classList.toggle('on', k === i); }});
    dots.forEach(function (d, k) {{ d.classList.toggle('on', k === i); }});
  }}
  function start() {{ if (!timer) timer = setInterval(function () {{ show(i + 1); }}, +r.dataset.interval); }}
  function stop() {{ clearInterval(timer); timer = null; }}
  dots.forEach(function (d, k) {{ d.addEventListener('click', function () {{ stop(); r.dataset.stopped = '1'; show(k); }}); }});
  r.addEventListener('mouseenter', stop);
  r.addEventListener('mouseleave', function () {{ if (!r.dataset.stopped) start(); }});
  r.addEventListener('focusin', stop);
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) start();
}})();
</script>
<a class="strip" href="{url(lang,'analyse')}"><div class="wrap"><b>{t(lang,'Bâtiment de 1 GWh et plus par année?','Building using 1 GWh or more a year?')}</b> {t(lang,'Analyse énergétique remboursée jusqu’à 60 000 $ par Hydro-Québec.','Energy analysis reimbursed up to $60,000 by Hydro-Québec.')} <span>{t(lang,'Voir si vous êtes admissible →','Check your eligibility →')}</span></div></a>

<section><div class="wrap">
  <span class="eyebrow">{c['services_eyebrow']}</span>
  <h2>{c['services_h2']}</h2>
  <div class="grid-3 lead-cards" style="margin-top:28px">{svc_cards}</div>
</div></section>

<section class="soft"><div class="wrap grid-2">
  <div><span class="eyebrow">{c['how_eyebrow']}</span><h2>{c['how_h2']}</h2><ol class="steps">{steps}</ol></div>
  <div><span class="eyebrow">{c['why_eyebrow']}</span><h2>{c['why_h2']}</h2><ul class="checks">{why}</ul>{cred(lang)}</div>
</div></section>

{suite_section(lang)}
{testimonials(lang)}

<section class="soft"><div class="wrap">
  <div class="cred" style="background:#0b3d5c">
    <div class="seal" style="background:#fff;color:#0b3d5c;font-size:.7rem">Hydro-<br>Québec</div>
    <div><b>{t(lang,'Partenaire du programme Solutions efficaces d’Hydro-Québec','Partner in Hydro-Québec’s Solutions efficaces program')}</b><br>
    {t(lang,'Bâtiment de 1 GWh et plus par année? Votre analyse énergétique peut être remboursée jusqu’à 60 000 $, et les mesures qui suivent financées en partie.','Building using 1 GWh or more a year? Your energy analysis can be reimbursed up to $60,000, and the measures that follow partly funded.')}
    &nbsp;<a href="{url(lang,'analyse')}" style="color:var(--yellow);font-weight:700">{t(lang,'Voir l’analyse énergétique →','See the energy analysis →')}</a></div>
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
    {group_pointer(lang, GROUP_OF[p['key']], p['key'], 'grid-2' if GROUP_OF[p['key']] == 'energie' else None) if p['key'] in GROUP_OF else ''}
    <h2>{t(lang,'Questions fréquentes','Frequently asked questions')}</h2>
    <div class="faq">{faq}</div>
  </div>
  <aside class="sticky">{quote_form(p)}</aside>
</div></section>
{cta_band(lang, {'analyse': t(lang,'Votre bâtiment consomme 1 GWh ou plus par année?','Does your building use 1 GWh or more a year?'), 'mli': t(lang,'Un dossier APH Select à monter?','An MLI Select file to assemble?'), 'divulgation': t(lang,'Votre divulgation est due le 30 juin.','Your disclosure is due June 30.'), 'fonds': t(lang,'Votre étude du fonds de prévoyance est due d’ici août 2028.','Your reserve fund study is due by August 2028.'), 'carnet': t(lang,'Votre carnet d’entretien est dû d’ici août 2028.','Your maintenance log is due by August 2028.'), 'valeur': t(lang,'Votre évaluation a plus de 5 ans?','Is your appraisal more than 5 years old?'), 'charges': t(lang,'Des charges communes qui grimpent?','Common expenses climbing?')}.get(p['key']))}"""

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
  <span class="eyebrow">{t(lang,'Nos services phares','Our lead services')}</span>
  <h2>{t(lang,'Loi 122 et analyse énergétique','Bill 122 and energy analysis')}</h2>
  <div class="grid-3 lead-cards" style="margin-top:24px">
    <div class="service"><h3>{t(lang,'Inspection de façades','Façade inspection')}</h3><p>{t(lang,'Bâtiments de 5 étages et plus, tous les 5 ans.','Buildings of 5+ storeys, every 5 years.')}</p><a class="btn ghost" href="{url(lang,'facades')}">{t(lang,'Voir le service','See service')}</a></div>
    <div class="service"><h3>{t(lang,'Inspection de stationnements étagés','Parking garage inspection')}</h3><p>{t(lang,'Vérification annuelle et approfondie quinquennale.','Annual check and five-year in-depth verification.')}</p><a class="btn ghost" href="{url(lang,'stationnements')}">{t(lang,'Voir le service','See service')}</a></div>
    <div class="service"><h3>{t(lang,'Analyse énergétique','Energy analysis')}</h3><p>{t(lang,'Bâtiments de 1 GWh et plus : remboursée jusqu’à 60 000 $ par Hydro-Québec.','Buildings using 1 GWh or more: reimbursed up to $60,000 by Hydro-Québec.')}</p><a class="btn ghost" href="{url(lang,'analyse')}">{t(lang,'Voir le service','See service')}</a></div>
  </div>
</div></section>
<section><div class="wrap">
  <span class="eyebrow">{t(lang,'Énergie et financement','Energy and financing')}</span>
  {energy_pointer(lang, cls='grid-3')}
</div></section>
<section><div class="wrap" style="margin-top:-40px">
  <span class="eyebrow">{t(lang,'Syndicats de copropriété · Loi 16','Condominium syndicates · Bill 16')}</span>
  {group_pointer(lang, 'copropriete', cls='grid-2', only=('fonds','carnet','valeur','charges'))}
</div></section>
<section class="soft"><div class="wrap">
  <span class="eyebrow">{t(lang,'Services d’ingénierie','Engineering services')}</span>
  <h2>{t(lang, f'{len(CATEGORIES)} domaines, une équipe', f'{len(CATEGORIES)} practice areas, one team')}</h2>
  <div class="grid-3" style="margin-top:24px">{category_cards(lang)}</div>
  <div style="margin-top:36px">{cred(lang)}</div>
</div></section>
<section class="soft"><div class="wrap two-col"><div class="prose"><h2>{t(lang,'Une question? Un ingénieur vous répond.','A question? An engineer answers.')}</h2><p>{t(lang,'Décrivez votre situation; nous vous dirons en 24 h quel service s’applique et à quel prix.','Describe your situation; within 24 h we will tell you which service applies and at what price.')}</p></div><aside>{quote_form(p)}</aside></div></section>
{cta_band(lang)}"""

ENERGY = [
    ("analyse", "Analyse énergétique remboursée", "Reimbursed energy analysis", "Bâtiments de 1 GWh et plus : jusqu’à 60 000 $ d’Hydro-Québec.", "Buildings using 1 GWh or more: up to $60,000 from Hydro-Québec."),
    ("mli", "Audit énergétique APH Select", "MLI Select energy audit", "Les points d’efficacité énergétique de votre financement SCHL.", "The energy-efficiency points behind your CMHC financing."),
    ("divulgation", "Divulgation annuelle énergie et GES", "Annual energy and GHG disclosure", "Règlement 21-042 de Montréal : dépôt avant le 30 juin.", "Montréal By-law 21-042: filing before June 30."),
]

CONDO = [
    ("fonds", "Étude du fonds de prévoyance", "Reserve fund study", "Projection sur 25 ans et scénarios de cotisation. Échéance août 2028.", "25-year projection and contribution scenarios. August 2028 deadline."),
    ("carnet", "Carnet d’entretien", "Maintenance log", "Inventaire, état des composantes et calendrier de 25 ans.", "Inventory, component condition and 25-year schedule."),
    ("valeur", "Valeur de reconstruction", "Reconstruction value", "Évaluation pour l’assurance du syndicat, obligatoire tous les 5 ans.", "Appraisal for the syndicate’s insurance, mandatory every 5 years."),
    ("charges", "Étude des charges communes", "Common-expense study", "Où va l’argent, et un budget d’exploitation réaliste.", "Where the money goes, and a realistic operating budget."),
    ("facades", "Inspection de façades (Loi 122)", "Façade inspection (Bill 122)", "Immeubles de 5 étages et plus, tous les 5 ans.", "Buildings of 5+ storeys, every 5 years."),
    ("stationnements", "Inspection de stationnement (Loi 122)", "Parking garage inspection (Bill 122)", "Vérification annuelle et approfondie quinquennale.", "Annual check and five-year in-depth verification."),
]
GROUPS = {"energie": (ENERGY, "Nos services en énergie", "Our energy services"),
          "copropriete": (CONDO, "Nos services aux copropriétés", "Our condominium services")}
GROUP_OF = {k: g for g, (items, _f, _e) in GROUPS.items() for k, *_ in items if k not in ("facades", "stationnements")}

def group_pointer(lang, group, skip=None, cls=None, only=None):
    items, hfr, hen = GROUPS[group]
    cards = "".join(f"""<div class="service"><h3>{t(lang, fr, en)}</h3><p>{t(lang, dfr, den)}</p><a class="btn ghost" href="{url(lang, k)}">{t(lang,'Voir le service','See service')}</a></div>"""
                    for k, fr, en, dfr, den in items if k != skip and (only is None or k in only))
    return f"""<h2>{t(lang, hfr, hen)}</h2><div class="{cls or 'rows'} lead-cards" style="margin:18px 0 28px">{cards}</div>"""

def energy_pointer(lang, skip=None, cls=None):
    return group_pointer(lang, "energie", skip, cls or ('rows' if skip is None else 'grid-2'))

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
    {group_pointer(lang, p["key"]) if p["key"] in GROUPS else ""}
    <h2>{t(lang,'Pour qui','Who it is for')}</h2><ul class="checks">{who}</ul>
    <h2>{t(lang,'Nos services','Our services')}</h2><ol class="steps">{items}</ol>
    {cred(lang)}
    <h2>{t(lang,'Autres domaines','Other practice areas')}</h2><ul>{others}</ul>
  </div>
  <aside class="sticky">{quote_form(p)}</aside>
</div></section>
{cta_band(lang, {'energie': t(lang,'Un projet en efficacité énergétique?','An energy-efficiency project?'), 'copropriete': t(lang,'Carnet d’entretien et fonds de prévoyance : échéance août 2028.','Maintenance log and reserve fund study: August 2028 deadline.')}.get(p['key']))}"""

def render_thanks(p):
    lang, c = p["lang"], p["content"]
    return f"""
<section class="page-hero"><div class="wrap"><h1>{c['h1']}</h1><p class="lead">{c['lead']}</p>
<div class="cta"><a class="btn" href="{url(lang,'index')}">{t(lang,'Retour à l’accueil','Back to home')}</a><a class="phone" href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></div></div></section>
<section><div class="wrap prose" style="max-width:720px">{c['body']}</div></section>"""

RENDER = {"thanks": render_thanks, "home": render_home, "service": render_service, "simple": render_simple, "hub": render_hub, "category": render_category}

# ---------------------------------------------------------------- build
# Hero photos: drop <name>.jpg (or .webp) into assets/img/photos/ and rebuild.
# A page uses its own photo if there is one, otherwise its group's photo.
PHOTO_FALLBACK = {"index": "home", "fonds": "copropriete", "carnet": "copropriete", "valeur": "copropriete", "charges": "copropriete",
                  "analyse": "energie", "mli": "energie", "divulgation": "energie", "services": "home", "contact": "home"}

def photo_for(key):
    for name in (key, PHOTO_FALLBACK.get(key)):
        for ext in ("jpg", "webp"):
            if name and os.path.exists(os.path.join(ROOT, "assets", "img", "photos", f"{name}.{ext}")):
                return f"{PREFIX}/assets/img/photos/{name}.{ext}"
    return None

def build():
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(DIST, "assets"))
    urls = []
    for p in PAGES:
        html = head(p) + topbar(p) + header(p) + RENDER[p["type"]](p) + footer(p)
        ph = photo_for(p["key"])
        if ph:
            # share image and early fetch of the hero photo (largest element on the page)
            html = html.replace(f"{SITE['domain']}/assets/img/icon-512.png", SITE['domain'] + ph[len(PREFIX):], 1)
            html = html.replace('<link rel="stylesheet"', f'<link rel="preload" as="image" href="{ph}" fetchpriority="high">\n<link rel="stylesheet"', 1)
            for cls in ("hero", "page-hero"):
                html = html.replace(f'<section class="{cls}">', f'<section class="{cls} has-photo" style="--photo:url({ph})">', 1)
        html = html.replace(" 000 $", "\u00a0000\u00a0$")  # keep dollar amounts on one line
        rel = path(p["lang"], p["key"]).lstrip("/")
        out_dir = os.path.join(DIST, rel)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        urls.append((abs_url(p["lang"], p["key"]), p["key"]))
    # sitemap with hreflang pairs
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for loc, key in urls:
        if key == "merci":
            continue
        sm.append(f"<url><loc>{loc}</loc><lastmod>{TODAY}</lastmod>"
                  f'<xhtml:link rel="alternate" hreflang="fr-CA" href="{abs_url("fr", key)}"/>'
                  f'<xhtml:link rel="alternate" hreflang="en-CA" href="{abs_url("en", key)}"/></url>')
    sm.append("</urlset>")
    open(os.path.join(DIST, "sitemap.xml"), "w").write("\n".join(sm))
    open(os.path.join(DIST, "robots.txt"), "w").write(
        "User-agent: *\nDisallow: /\n" if PREVIEW else f"User-agent: *\nAllow: /\nSitemap: {SITE['domain']}/sitemap.xml\n")
    open(os.path.join(DIST, ".nojekyll"), "w").write("")
    # legacy WordPress URLs -> new pages (Netlify/Cloudflare _redirects format)
    open(os.path.join(DIST, "_redirects"), "w").write(
        "/our-services/* /services/ 301\n/our-services /services/ 301\n/contact-us/ /contact/ 301\n"
        "/about-us/ / 301\n/blog/* / 301\n/wp-content/* / 301\n/wp-admin/* / 301\n")
    # same for Apache (Doteasy cPanel)
    open(os.path.join(DIST, ".htaccess"), "w").write(
        "DirectoryIndex index.html\n"
        "RedirectMatch 301 ^/(wp-[^/]*\\.php|xmlrpc\\.php|index\\.php)$ /\n"
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
