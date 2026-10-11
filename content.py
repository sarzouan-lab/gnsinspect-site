# -*- coding: utf-8 -*-
"""All site copy, FR and EN. Edit here; run build.py."""

SITE = {
    "domain": "https://gnsinspect.ca",
    "phone": "514-965-2842",
    "phone_tel": "+15149652842",
    "phone_e164": "+1-514-965-2842",
    "email": "info@gnsinspect.ca",
    "street": "970 Montée de Liesse, bureau 209",
    "postal": "H4T 1W7",
    "address": "970 Montée de Liesse, bureau 209, Montréal (Québec) H4T 1W7",
    # Form backend. Create a free Formspree form (formspree.io), set the
    # notification address to simon.a@gnsinspect.ca, and paste its endpoint here.
    "form": {"action": "https://formspree.io/f/REPLACE_ME"},
}

# ------------------------------------------------------------------ FR
FR_HOME = {
    "eyebrow": "Firme d’ingénierie · Loi 122 · Grand Montréal",
    "h1": "Inspection de façades et de stationnements étagés, signée par un ingénieur",
    "lead": "Le chapitre Bâtiment du Code de sécurité du Québec oblige les propriétaires d’immeubles de 5 étages et plus, et de stationnements étagés, à obtenir un rapport de vérification tous les 5 ans. GNS Inspect livre ce rapport, conforme aux exigences de la RBQ, avec un plan d’entretien clair et chiffré.",
    "cta": "Demander une soumission",
    "proof": [("5 ans", "cycle de vérification obligatoire"), ("10 jours", "ouvrables pour livrer le rapport"), ("1 ingénieur", "qui signe et répond de son rapport")],
    "services_eyebrow": "Nos deux spécialités",
    "services_h2": "Les vérifications exigées par la Loi 122",
    "services": [
        {"key": "facades", "tag": "Façades · 5 étages et +", "title": "Inspection de façades",
         "text": "Vérification approfondie des façades, enveloppe et maçonnerie, exigée tous les 5 ans par les articles 371 à 384 du chapitre Bâtiment.",
         "bullets": ["Inspection visuelle et rapprochée (nacelle, cordiste ou drone)", "Classification des conditions dangereuses", "Rapport signé, échéancier et budget de travaux"],
         "cta": "Voir le service façades"},
        {"key": "stationnements", "tag": "Stationnements étagés", "title": "Inspection de stationnements",
         "text": "Vérification annuelle et vérification approfondie quinquennale par un ingénieur des stationnements souterrains et aériens dont une dalle ne repose pas sur le sol.",
         "bullets": ["Sondages, délaminage, corrosion et chlorures", "Plan de localisation des défauts et priorisation", "Fiche de vérification annuelle incluse"],
         "cta": "Voir le service stationnements"},
    ],
    "how_eyebrow": "Comment ça marche",
    "how_h2": "Quatre étapes, un rapport qui tient devant la RBQ",
    "steps": [("Soumission en 24 h", "Vous nous envoyez l’adresse et le nombre d’étages ou de niveaux; nous confirmons un prix fixe par écrit."),
              ("Visite et relevés", "Inspection visuelle complète puis rapprochée des zones à risque, sans fermer votre immeuble ni votre stationnement."),
              ("Rapport signé par un ingénieur", "Constats photographiques, conditions dangereuses, recommandations, échéancier et estimation budgétaire sur 5 ans."),
              ("Suivi", "Avis à la RBQ si requis, appels d’offres et surveillance des travaux de réparation.")],
    "why_eyebrow": "Pourquoi GNS Inspect",
    "why_h2": "Un spécialiste, pas un généraliste",
    "why": ["Ingénieur en structure et en enveloppe du bâtiment : nous comprenons ce que nous inspectons.",
            "Prix fixe confirmé avant la visite, sans frais cachés.",
            "Rapport livré en 10 jours ouvrables, format accepté par la RBQ, les assureurs et les prêteurs.",
            "Un seul interlocuteur, de l’inspection à la surveillance des travaux.",
            "Service en français et en anglais, partout dans le Grand Montréal."],
    "partners": "Rapports acceptés par les principaux prêteurs",
}

FR_FACADES = {
    "crumb": "Inspection de façades",
    "eyebrow": "Loi 122 · Chapitre Bâtiment du Code de sécurité · Art. 371 à 384",
    "h1": "Inspection de façades Loi 122 : rapport d’ingénieur conforme à la RBQ",
    "lead": "Votre immeuble a 5 étages ou plus hors sol? La loi vous oblige à faire vérifier vos façades par un ingénieur ou un architecte tous les 5 ans. GNS Inspect produit le rapport de vérification signé par un ingénieur membre de l’OIQ, avec un plan d’entretien clair et chiffré.",
    "who_h2": "Qui est visé",
    "who": ["Tout bâtiment de 5 étages et plus hors sol : résidentiel, copropriété, commercial, institutionnel.",
            "Première vérification au plus tard 10 ans après la construction, puis tous les 5 ans.",
            "Le propriétaire doit tenir un registre; le rapport doit être disponible pour la RBQ sur demande.",
            "Toute condition dangereuse doit être corrigée sans délai et déclarée à la RBQ."],
    "callout": "<b>Vous ne savez pas quand tombe votre prochaine échéance?</b> Envoyez-nous l’année de construction et la date du dernier rapport : nous vous confirmons la date limite sans frais.",
    "includes_h2": "Ce que comprend notre vérification",
    "includes": [("Revue documentaire.", "Plans, rapports antérieurs, registre d’entretien, travaux réalisés."),
                 ("Inspection visuelle complète.", "Les quatre façades depuis la rue, le toit et les balcons."),
                 ("Inspection rapprochée.", "Nacelle, cordiste ou drone selon l’accès : attaches de maçonnerie, linteaux, joints de dilatation, parapets, balcons, allèges."),
                 ("Sondages exploratoires au besoin.", "Ouvertures, endoscopie, essais d’attaches, relevés d’humidité."),
                 ("Rapport conforme au CBCS.", "Constats photographiques, classification des conditions dangereuses, recommandations, échéancier et estimation budgétaire."),
                 ("Suivi.", "Avis de condition dangereuse à la RBQ si requis, devis de réparation, surveillance de chantier.")],
    "why_h2": "Pourquoi confier vos façades à GNS Inspect",
    "why": ["Rapport signé par un ingénieur en structure et en enveloppe du bâtiment, pas seulement un inspecteur.",
            "Délai de livraison : 10 jours ouvrables après la visite.",
            "Prix fixe par façade, confirmé par écrit avant la visite.",
            "Recommandations priorisées et chiffrées, utilisables directement pour votre fonds de prévoyance."],
}
FR_FACADES_FAQ = [
    ("Mon immeuble a 4 étages plus un sous-sol : suis-je visé?", "Non. Le critère est 5 étages hors sol. Un sous-sol ou un garage souterrain ne compte pas comme étage hors sol."),
    ("Un rapport d’architecte est-il équivalent?", "Oui, la loi admet les deux professions. Un ingénieur est recommandé lorsque la structure, les attaches de maçonnerie ou les balcons sont en cause."),
    ("Que se passe-t-il si une condition dangereuse est détectée?", "Le propriétaire doit immédiatement sécuriser le public et aviser la RBQ. Nous préparons l’avis, le périmètre de protection et le plan de correction."),
    ("Combien de temps dure l’inspection?", "Une demi-journée à deux jours selon la taille de l’immeuble et le mode d’accès (nacelle, cordiste ou drone)."),
    ("Combien coûte une inspection de façade Loi 122?", "Le prix dépend du nombre de façades, de la hauteur et du mode d’accès. Nous confirmons un prix fixe par écrit en 24 h, sans frais cachés."),
]

FR_STAT = {
    "crumb": "Inspection de stationnements",
    "eyebrow": "Loi 122 · Chapitre Bâtiment du Code de sécurité · Parcs de stationnement",
    "h1": "Inspection de stationnement étagé : vérifications annuelle et quinquennale par un ingénieur",
    "lead": "Si au moins une dalle de roulement de votre stationnement ne repose pas sur le sol, le chapitre Bâtiment du Code de sécurité impose une vérification annuelle et une vérification approfondie par un ingénieur tous les 5 ans. GNS Inspect réalise les deux et livre un rapport signé qui tient devant la RBQ et votre assureur.",
    "who_h2": "Qui est visé",
    "who": ["Stationnements souterrains et aériens, y compris les dalles sur pilotis et les toits-terrasses de stationnement, dont au moins une dalle de roulement est au-dessus d’un vide.",
            "Vérification annuelle par le propriétaire ou son mandataire, consignée au registre.",
            "Vérification approfondie par un ingénieur tous les 5 ans, et dès l’apparition de signes de détérioration.",
            "Le registre et les rapports doivent être conservés et produits à la RBQ sur demande."],
    "callout": "<b>Signes d’alerte :</b> efflorescence, béton fissuré ou écaillé, armatures exposées, infiltrations persistantes, déflexion de dalle. L’un d’eux déclenche une évaluation par un ingénieur, peu importe la date de la dernière vérification.",
    "includes_h2": "Ce que comprend notre vérification approfondie",
    "includes": [("Revue documentaire.", "Plans de structure, rapports antérieurs, registre d’entretien et fiches annuelles."),
                 ("Relevé visuel systématique.", "Dalles, poutres, colonnes, murs de soutènement, joints, membranes et drainage, niveau par niveau."),
                 ("Essais.", "Sondages au marteau et détection de délaminage; épaisseur d’enrobage; potentiel de corrosion et teneur en chlorures au besoin."),
                 ("Classement des défauts.", "Conditions dangereuses et défauts d’entretien selon le CBCS, avec plan de localisation."),
                 ("Rapport signé par un ingénieur.", "Constats photographiques, priorisation des réparations, estimation budgétaire et échéancier sur 5 ans."),
                 ("Fiche de vérification annuelle.", "Prête à l’emploi pour les 4 années suivantes, avec les points à surveiller.")],
    "why_h2": "Pourquoi confier votre stationnement à GNS Inspect",
    "why": ["Ingénieur en structure membre de l’OIQ qui signe et assume le rapport.",
            "Intervention sans fermer le stationnement : relevés par sections, de nuit au besoin.",
            "Rapport livré en 10 jours ouvrables; devis de réparation et surveillance de chantier disponibles.",
            "Prix fixe par niveau, confirmé par écrit."],
}
FR_STAT_FAQ = [
    ("Mon stationnement est entièrement sur terre-plein : suis-je visé?", "Non, sauf si une portion de dalle est au-dessus d’un vide : rampe, entresol, mezzanine ou dalle sur pilotis."),
    ("Qui peut faire la vérification annuelle?", "Le propriétaire ou son gestionnaire, à partir de notre fiche de vérification. Tout signe de détérioration doit déclencher une évaluation par un ingénieur."),
    ("Dois-je envoyer le rapport à la RBQ?", "Le rapport doit être conservé et produit sur demande. Un avis à la RBQ est obligatoire dès qu’une condition dangereuse est constatée."),
    ("L’inspection oblige-t-elle à fermer le stationnement?", "Non. Nous procédons par sections, en dehors des heures de pointe ou de nuit, en coordination avec votre gestionnaire."),
    ("Combien coûte une inspection de stationnement Loi 122?", "Le prix dépend du nombre de niveaux, de la superficie et des essais requis. Prix fixe confirmé par écrit en 24 h."),
]

FR_SERVICES_BODY = """
<h2>Au-delà de la Loi 122</h2>
<p>Notre cœur de métier est la vérification des façades et des stationnements étagés. Les mêmes ingénieurs offrent aussi les services suivants, souvent en complément d’un dossier Loi 122.</p>
<h3>Copropriétés (Loi 16)</h3>
<ul><li>Étude du fonds de prévoyance</li><li>Évaluation de la valeur de remplacement</li><li>Carnet d’entretien</li></ul>
<h3>Ingénierie de structure et d’enveloppe</h3>
<ul><li>Expertise sur infiltration d’eau, vices cachés et litiges</li><li>Conception et dessins de réparation (acier, bois, béton, maçonnerie)</li><li>Surveillance de chantier</li><li>Inspection de toiture</li></ul>
<h3>Inspections pour financement</h3>
<ul><li>Inspection d’immeuble pour prêteurs et assureurs</li><li>Rapport d’état d’immeuble avant acquisition</li></ul>
<h3>Évaluations environnementales</h3>
<ul><li>Phase I (CSA Z768), Phase II et III (CSA Z769)</li><li>Amiante, radon, qualité de l’air</li></ul>
"""
FR_CONTACT_BODY = """
<h2>Parlez directement à un ingénieur</h2>
<p>Téléphone : <a href="tel:+15149652842">514-965-2842</a><br>Courriel : <a href="mailto:info@gnsinspect.ca">info@gnsinspect.ca</a></p>
<p>970 Montée de Liesse, bureau 209<br>Montréal (Québec) H4T 1W7</p>
<p>Lundi à jeudi : 8 h à 18 h<br>Vendredi : 8 h à 13 h<br>Urgences (condition dangereuse) : 7 jours sur 7.</p>
<h2>Territoire desservi</h2>
<p>Île de Montréal, Laval, Longueuil et la Rive-Sud, Rive-Nord, Laurentides et Montérégie.</p>
"""

# ------------------------------------------------------------------ EN
EN_HOME = {
    "eyebrow": "Engineering firm · Bill 122 · Greater Montréal",
    "h1": "Façade and parking-garage inspections, signed by an engineer",
    "lead": "Chapter VIII of Québec’s Safety Code requires owners of buildings of 5 storeys or more, and of multi-level parking structures, to obtain a verification report every 5 years. GNS Inspect delivers that report, compliant with RBQ requirements, with a clear, costed maintenance plan.",
    "cta": "Request a quote",
    "proof": [("5 years", "mandatory verification cycle"), ("10 days", "business days to deliver the report"), ("1 engineer", "who signs and stands behind it")],
    "services_eyebrow": "Our two specialties",
    "services_h2": "The verifications Bill 122 requires",
    "services": [
        {"key": "facades", "tag": "Façades · 5 storeys +", "title": "Façade inspection",
         "text": "In-depth verification of façades, envelope and masonry, required every 5 years under sections 371–384 of the Building Chapter.",
         "bullets": ["Visual and close-up inspection (lift, rope access or drone)", "Dangerous-condition classification", "Signed report, work schedule and budget"],
         "cta": "See façade service"},
        {"key": "stationnements", "tag": "Multi-level parking", "title": "Parking garage inspection",
         "text": "Annual check and five-year in-depth engineer verification of underground and above-grade garages where a driving slab sits above a void.",
         "bullets": ["Sounding, delamination, corrosion and chloride testing", "Defect map and repair priorities", "Annual verification sheet included"],
         "cta": "See parking service"},
    ],
    "how_eyebrow": "How it works",
    "how_h2": "Four steps to a report that stands up to the RBQ",
    "steps": [("Quote within 24 h", "Send us the address and the number of storeys or levels; we confirm a fixed price in writing."),
              ("Site visit and survey", "Full visual inspection, then close-up survey of at-risk areas, without closing your building or garage."),
              ("Engineer-signed report", "Photo findings, dangerous conditions, recommendations, five-year schedule and budget estimate."),
              ("Follow-through", "RBQ notice if required, repair tenders and construction oversight.")],
    "why_eyebrow": "Why GNS Inspect",
    "why_h2": "A specialist, not a generalist",
    "why": ["Structural and building-envelope engineer: we understand what we inspect.",
            "Fixed price confirmed before the visit, no hidden fees.",
            "Report in 10 business days, in the format accepted by the RBQ, insurers and lenders.",
            "One point of contact from inspection to repair oversight.",
            "Service in English and French across Greater Montréal."],
    "partners": "Reports accepted by major lenders",
}

EN_FACADES = {
    "crumb": "Façade inspection",
    "eyebrow": "Bill 122 · Safety Code, Building Chapter · s. 371–384",
    "h1": "Bill 122 façade inspection: an engineer-signed report that satisfies the RBQ",
    "lead": "If your building has 5 or more storeys above grade, the law requires an engineer or architect to verify its façades every 5 years. GNS Inspect delivers the verification report, signed by an OIQ-licensed engineer, with a prioritized, costed maintenance plan.",
    "who_h2": "Who must comply",
    "who": ["Any building of 5+ storeys above grade: residential, condominium, commercial or institutional.",
            "First verification within 10 years of construction, then every 5 years.",
            "The owner must keep a register; the report must be produced to the RBQ on request.",
            "Any dangerous condition must be corrected without delay and reported to the RBQ."],
    "callout": "<b>Not sure when your next deadline falls?</b> Send us the year of construction and the date of the last report: we will confirm the deadline at no charge.",
    "includes_h2": "What our verification includes",
    "includes": [("Document review.", "Drawings, prior reports, maintenance register, completed work."),
                 ("Full visual inspection.", "All elevations from street level, roof and balconies."),
                 ("Close-up inspection.", "Lift, rope access or drone depending on access: masonry ties, lintels, expansion joints, parapets, balconies, sills."),
                 ("Exploratory openings where warranted.", "Openings, borescope, tie pull tests, moisture surveys."),
                 ("Safety-Code-compliant report.", "Photo findings, dangerous-condition classification, recommendations, schedule and budget estimate."),
                 ("Follow-through.", "RBQ dangerous-condition notice if required, repair specifications, construction oversight.")],
    "why_h2": "Why trust your façades to GNS Inspect",
    "why": ["Report signed by a structural and building-envelope engineer, not just an inspector.",
            "Delivered within 10 business days of the site visit.",
            "Fixed price per elevation, confirmed in writing before the visit.",
            "Prioritized, costed recommendations you can drop straight into your reserve fund plan."],
}
EN_FACADES_FAQ = [
    ("My building has 4 storeys plus a basement. Am I covered?", "No. The threshold is 5 storeys above grade. A basement or underground garage does not count as an above-grade storey."),
    ("Is an architect’s report equivalent?", "Yes, the law accepts both professions. An engineer is recommended where structure, masonry ties or balconies are involved."),
    ("What happens if a dangerous condition is found?", "The owner must immediately protect the public and notify the RBQ. We prepare the notice, the protection perimeter and the correction plan."),
    ("How long does the inspection take?", "Half a day to two days depending on building size and access method (lift, rope access or drone)."),
    ("How much does a Bill 122 façade inspection cost?", "Price depends on the number of elevations, height and access method. We confirm a fixed price in writing within 24 hours, no hidden fees."),
]

EN_STAT = {
    "crumb": "Parking garage inspection",
    "eyebrow": "Bill 122 · Safety Code, Building Chapter · Parking structures",
    "h1": "Multi-level parking garage inspection: annual and five-year engineer verifications",
    "lead": "If any driving slab of your parking structure sits above a void, Chapter VIII of Québec’s Safety Code requires an annual check and an in-depth engineer verification every 5 years. GNS Inspect performs both and delivers a signed report that stands up to the RBQ and your insurer.",
    "who_h2": "Who must comply",
    "who": ["Underground and above-grade garages, including slabs on columns and roof-deck parking, with at least one driving slab above a void.",
            "Annual verification by the owner or their agent, recorded in the register.",
            "In-depth engineer verification every 5 years, and whenever signs of deterioration appear.",
            "The register and reports must be kept and produced to the RBQ on request."],
    "callout": "<b>Warning signs:</b> efflorescence, cracked or spalling concrete, exposed rebar, persistent leaks, slab deflection. Any one of them triggers an engineer evaluation, regardless of the date of the last verification.",
    "includes_h2": "What our in-depth verification includes",
    "includes": [("Document review.", "Structural drawings, prior reports, maintenance register and annual sheets."),
                 ("Systematic visual survey.", "Slabs, beams, columns, retaining walls, joints, membranes and drainage, level by level."),
                 ("Testing.", "Hammer sounding and delamination survey; cover depth; corrosion potential and chloride content where needed."),
                 ("Defect classification.", "Dangerous conditions and maintenance defects per the Safety Code, with a location plan."),
                 ("Engineer-signed report.", "Photo findings, repair priorities, budget estimate and five-year schedule."),
                 ("Annual verification sheet.", "Ready to use for the following 4 years, with the items to monitor.")],
    "why_h2": "Why trust your garage to GNS Inspect",
    "why": ["OIQ-licensed structural engineer signs and stands behind the report.",
            "No garage closure: sections surveyed off-peak or overnight.",
            "Report in 10 business days; repair specifications and site oversight available.",
            "Fixed price per level, confirmed in writing."],
}
EN_STAT_FAQ = [
    ("My garage is entirely slab-on-grade. Am I covered?", "No, unless part of a slab sits above a void: a ramp, mezzanine, split level or slab on columns."),
    ("Who can do the annual verification?", "The owner or property manager, using our verification sheet. Any sign of deterioration must trigger an engineer evaluation."),
    ("Do I have to send the report to the RBQ?", "The report must be kept and produced on request. A notice to the RBQ is mandatory as soon as a dangerous condition is found."),
    ("Does the inspection require closing the garage?", "No. We work section by section, off-peak or overnight, coordinated with your manager."),
    ("How much does a Bill 122 parking inspection cost?", "Price depends on the number of levels, area and testing required. Fixed price confirmed in writing within 24 hours."),
]

EN_SERVICES_BODY = """
<h2>Beyond Bill 122</h2>
<p>Our core business is façade and parking-structure verification. The same engineers also provide the following services, often alongside a Bill 122 file.</p>
<h3>Condominiums (Bill 16)</h3>
<ul><li>Reserve fund study</li><li>Replacement cost evaluation</li><li>Maintenance log book</li></ul>
<h3>Structural and envelope engineering</h3>
<ul><li>Water infiltration, latent defect and litigation expertise</li><li>Repair design and drawings (steel, wood, concrete, masonry)</li><li>Construction oversight</li><li>Roof inspection</li></ul>
<h3>Financing inspections</h3>
<ul><li>Building inspection for lenders and insurers</li><li>Property condition report before acquisition</li></ul>
<h3>Environmental assessments</h3>
<ul><li>Phase I (CSA Z768), Phase II and III (CSA Z769)</li><li>Asbestos, radon, air quality</li></ul>
"""
EN_CONTACT_BODY = """
<h2>Speak directly with an engineer</h2>
<p>Phone: <a href="tel:+15149652842">514-965-2842</a><br>Email: <a href="mailto:info@gnsinspect.ca">info@gnsinspect.ca</a></p>
<p>970 Montée de Liesse, Suite 209<br>Montréal, Québec H4T 1W7</p>
<p>Monday to Thursday: 8 am to 6 pm<br>Friday: 8 am to 1 pm<br>Emergencies (dangerous condition): 7 days a week.</p>
<h2>Service area</h2>
<p>Island of Montréal, Laval, Longueuil and the South Shore, North Shore, Laurentides and Montérégie.</p>
"""

# ------------------------------------------------------------------ pages
PAGES = [
    {"key": "index", "lang": "fr", "type": "home",
     "title": "Inspection de façades et de stationnements Loi 122 à Montréal | GNS Inspect",
     "meta": "Firme d’ingénierie spécialisée dans les vérifications de façades (5 étages et +) et de stationnements étagés exigées par la Loi 122. Rapport signé par un ingénieur, soumission en 24 h.",
     "content": FR_HOME},
    {"key": "index", "lang": "en", "type": "home",
     "title": "Bill 122 Façade and Parking Garage Inspections in Montréal | GNS Inspect",
     "meta": "Engineering firm specialized in the façade (5+ storeys) and multi-level parking verifications required by Bill 122. Engineer-signed report, quote within 24 h.",
     "content": EN_HOME},

    {"key": "facades", "lang": "fr", "type": "service",
     "title": "Inspection de façades Loi 122 à Montréal | Ingénieur GNS Inspect",
     "meta": "Vérification quinquennale des façades de 5 étages et plus, rapport signé par un ingénieur conforme au chapitre Bâtiment du Code de sécurité. Soumission en 24 h.",
     "service_name": "Inspection de façades Loi 122", "faq": FR_FACADES_FAQ, "content": FR_FACADES},
    {"key": "facades", "lang": "en", "type": "service",
     "title": "Bill 122 Façade Inspection Montréal | GNS Inspect Engineers",
     "meta": "Five-year verification of façades on buildings of 5+ storeys, engineer-signed report compliant with Québec’s Safety Code. Quote within 24 h.",
     "service_name": "Bill 122 Façade Inspection", "faq": EN_FACADES_FAQ, "content": EN_FACADES},

    {"key": "stationnements", "lang": "fr", "type": "service",
     "title": "Inspection de stationnement étagé Loi 122 à Montréal | GNS Inspect",
     "meta": "Vérification annuelle et vérification approfondie quinquennale de votre stationnement souterrain ou aérien par un ingénieur. Rapport conforme à la RBQ.",
     "service_name": "Inspection de stationnement étagé Loi 122", "faq": FR_STAT_FAQ, "content": FR_STAT},
    {"key": "stationnements", "lang": "en", "type": "service",
     "title": "Bill 122 Parking Garage Inspection Montréal | GNS Inspect Engineers",
     "meta": "Annual check and five-year in-depth engineer verification of your underground or above-grade parking structure. RBQ-compliant report.",
     "service_name": "Bill 122 Parking Garage Inspection", "faq": EN_STAT_FAQ, "content": EN_STAT},

    {"key": "services", "lang": "fr", "type": "hub",
     "title": "Services d’ingénierie du bâtiment à Montréal | GNS Inspect",
     "meta": "Inspections pré-achat et pour financement, expertise structurale, plans de structure et de CVAC, évaluations environnementales Phase I-II-III, fonds de prévoyance. Équipe d’ingénieurs OIQ, Montréal.",
     "content": {"crumb": "Services d’ingénierie", "h1": "Une suite complète de services d’ingénierie du bâtiment", "lead": "Inspections, expertise, structure, mécanique du bâtiment, environnement et copropriété : une seule équipe d’ingénieurs, de l’inspection jusqu’à la surveillance des travaux."}},
    {"key": "services", "lang": "en", "type": "hub",
     "title": "Building Engineering Services in Montréal | GNS Inspect",
     "meta": "Pre-purchase and financing inspections, structural expertise, structural and HVAC design, Phase I-II-III environmental assessments, reserve fund studies. OIQ engineering team, Montréal.",
     "content": {"crumb": "Engineering services", "h1": "A full suite of building engineering services", "lead": "Inspections, expertise, structural, building mechanical, environmental and condominium services: one engineering team, from inspection through construction oversight."}},

    {"key": "contact", "lang": "fr", "type": "simple",
     "title": "Nous joindre | GNS Inspect",
     "meta": "Joignez un ingénieur de GNS Inspect : 514-965-2842, info@gnsinspect.ca. Montréal, Laval, Rive-Sud, Rive-Nord.",
     "content": {"crumb": "Contact", "h1": "Nous joindre", "lead": "Une question sur votre obligation Loi 122? Un ingénieur vous répond.", "body": FR_CONTACT_BODY}},
    {"key": "contact", "lang": "en", "type": "simple",
     "title": "Contact | GNS Inspect",
     "meta": "Reach a GNS Inspect engineer: 514-965-2842, info@gnsinspect.ca. Montréal, Laval, South Shore, North Shore.",
     "content": {"crumb": "Contact", "h1": "Contact us", "lead": "A question about your Bill 122 obligation? An engineer answers.", "body": EN_CONTACT_BODY}},
]


# ------------------------------------------------------------------ full service suite
# Each category becomes a page in both languages (slug per language) and a card on the
# services hub and homepage.
CATEGORIES = [
    {"key": "inspections-immeubles",
     "slug": {"fr": "inspection-immeuble-prealable-achat-financement", "en": "building-inspection-pre-purchase-financing"},
     "fr": {"title": "Inspections d’immeubles", "card": "Pré-achat, pré-vente, financement et rapport d’état d’immeuble, par un ingénieur.",
            "h1": "Inspection d’immeuble pré-achat, pré-vente et pour financement",
            "lead": "Avant d’acheter, de vendre ou de refinancer un immeuble, un rapport d’ingénieur vous donne l’état réel de la structure, de l’enveloppe et des systèmes, ainsi que le budget des travaux à prévoir.",
            "for": ["Acheteurs et vendeurs d’immeubles résidentiels, multilogements et commerciaux", "Prêteurs et assureurs exigeant un rapport d’ingénieur", "Syndicats et gestionnaires préparant un plan de travaux"],
            "items": [("Inspection pré-achat", "Structure, enveloppe, toiture, fondations, plomberie, électricité, CVAC; estimation des travaux à court et moyen terme."),
                      ("Inspection pré-vente", "Identifier et documenter les défauts avant la mise en marché pour éviter les renégociations."),
                      ("Inspection pour financement", "Rapport d’état d’immeuble au format exigé par les prêteurs (Banque Scotia, Banque Nationale, Banque Laurentienne, First National, CIBC)."),
                      ("Inspection de toiture", "État des membranes, solins, drains et parapets; durée de vie résiduelle."),
                      ("Thermographie et drone", "Relevés infrarouges de l’enveloppe et inspection par drone des toitures et façades."),
                      ("Caméra de drain et de conduits", "Inspection vidéo des drains de fondation et des conduits de ventilation.")],
            "meta": "Inspection d’immeuble par un ingénieur à Montréal : pré-achat, pré-vente, financement, toiture, thermographie, drone. Rapport accepté par les prêteurs."},
     "en": {"title": "Building inspections", "card": "Pre-purchase, pre-sale, financing and property condition reports, by an engineer.",
            "h1": "Pre-purchase, pre-sale and financing building inspections",
            "lead": "Before buying, selling or refinancing a building, an engineer’s report gives you the true condition of the structure, envelope and systems, and the budget for the work ahead.",
            "for": ["Buyers and sellers of residential, multi-unit and commercial buildings", "Lenders and insurers requiring an engineer’s report", "Syndicates and managers preparing a capital plan"],
            "items": [("Pre-purchase inspection", "Structure, envelope, roof, foundations, plumbing, electrical, HVAC; short- and medium-term work estimate."),
                      ("Pre-sale inspection", "Identify and document defects before listing to avoid renegotiation."),
                      ("Financing inspection", "Property condition report in the format lenders require (Scotiabank, National Bank, Laurentian Bank, First National, CIBC)."),
                      ("Roof inspection", "Membranes, flashings, drains and parapets; remaining service life."),
                      ("Thermography and drone", "Infrared envelope surveys and drone inspection of roofs and façades."),
                      ("Drain and duct camera", "Video inspection of foundation drains and ventilation ducts.")],
            "meta": "Engineer building inspection in Montréal: pre-purchase, pre-sale, financing, roof, thermography, drone. Reports accepted by lenders."}},

    {"key": "expertise",
     "slug": {"fr": "expertise-ingenierie-vices-caches-infiltration", "en": "engineering-expertise-latent-defects-water-infiltration"},
     "fr": {"title": "Expertise et litiges", "card": "Vices cachés, infiltrations d’eau, ocre ferreuse, pyrite : rapports d’expert recevables en cour.",
            "h1": "Expertise d’ingénierie : vices cachés, infiltrations et litiges",
            "lead": "Quand un défaut apparaît après l’achat ou qu’un entrepreneur conteste sa responsabilité, un rapport d’expertise signé par un ingénieur établit la cause, la gravité et le coût de correction.",
            "for": ["Propriétaires et acheteurs confrontés à un vice caché", "Avocats et assureurs ayant besoin d’un témoin expert", "Syndicats en litige avec un constructeur ou un entrepreneur"],
            "items": [("Vices cachés", "Diagnostic, chronologie, lien avec la vente, estimation des correctifs."),
                      ("Infiltration d’eau", "Origine de l’eau (toiture, enveloppe, fondations, plomberie), essais d’arrosage, recommandations."),
                      ("Ocre ferreuse et pyrite", "Échantillonnage, analyse en laboratoire, solutions de drainage ou de remplacement de dalle."),
                      ("Qualité de l’eau et de l’air", "Moisissures, amiante, radon, eau potable : prélèvements et interprétation."),
                      ("Expertise légale", "Rapport conforme aux exigences des tribunaux, témoignage d’expert, contre-expertise."),
                      ("Surveillance de correctifs", "Vérification que les travaux de réparation règlent la cause et non le symptôme.")],
            "meta": "Expertise d’ingénieur à Montréal : vices cachés, infiltration d’eau, ocre ferreuse, pyrite, moisissures. Rapports d’expert pour litiges et assurances."},
     "en": {"title": "Expertise and litigation", "card": "Latent defects, water infiltration, iron ochre, pyrite: expert reports that stand up in court.",
            "h1": "Engineering expertise: latent defects, water infiltration and litigation",
            "lead": "When a defect appears after purchase or a contractor disputes liability, an engineer-signed expert report establishes cause, severity and the cost to correct.",
            "for": ["Owners and buyers facing a latent defect", "Lawyers and insurers needing an expert witness", "Syndicates in dispute with a builder or contractor"],
            "items": [("Latent defects", "Diagnosis, timeline, link to the sale, correction estimate."),
                      ("Water infiltration", "Source of water (roof, envelope, foundations, plumbing), water testing, recommendations."),
                      ("Iron ochre and pyrite", "Sampling, laboratory analysis, drainage or slab replacement solutions."),
                      ("Water and air quality", "Mould, asbestos, radon, potable water: sampling and interpretation."),
                      ("Legal expertise", "Court-compliant reports, expert testimony, counter-expertise."),
                      ("Repair oversight", "Verifying that repairs fix the cause, not the symptom.")],
            "meta": "Engineering expertise in Montréal: latent defects, water infiltration, iron ochre, pyrite, mould. Expert reports for litigation and insurance."}},

    {"key": "structure",
     "slug": {"fr": "ingenierie-structure-plans-calculs", "en": "structural-engineering-design-drawings"},
     "fr": {"title": "Ingénierie de structure", "card": "Plans, calculs et dessins d’atelier en acier, bois, béton et maçonnerie; surveillance de chantier.",
            "h1": "Ingénierie de structure : conception, calculs et surveillance",
            "lead": "Renforcement, retrait de colonne ou de mur porteur, ajout d’étage, réparation de balcons ou de dalle de stationnement : nos ingénieurs conçoivent, calculent et signent les plans, puis surveillent les travaux.",
            "for": ["Entrepreneurs et promoteurs ayant besoin d’un ingénieur en structure", "Propriétaires planifiant une rénovation structurale", "Fabricants exigeant des dessins d’atelier signés"],
            "items": [("Plans et calculs de structure", "Acier, bois, béton, maçonnerie; conformité au Code de construction du Québec."),
                      ("Modifications structurales", "Retrait de murs porteurs et de colonnes, transferts de charge, ouvertures, mezzanines."),
                      ("Réparation de béton et de maçonnerie", "Balcons, dalles de stationnement, parapets, attaches de maçonnerie : devis et plans de réparation."),
                      ("Dessins d’atelier", "Fabrication et installation : acier, aluminium, panneaux, enveloppe."),
                      ("Équipements en toiture", "Renforcement de structure pour unités CVAC, panneaux solaires et équipements lourds."),
                      ("Surveillance de chantier", "Visites, rapports de surveillance et attestation de conformité pour la municipalité et l’assureur.")],
            "meta": "Ingénieur en structure à Montréal : plans et calculs acier, bois, béton, maçonnerie; retrait de mur porteur; dessins d’atelier; surveillance de chantier."},
     "en": {"title": "Structural engineering", "card": "Design, calculations and shop drawings in steel, wood, concrete and masonry; site oversight.",
            "h1": "Structural engineering: design, calculations and oversight",
            "lead": "Reinforcement, column or bearing-wall removal, added storeys, balcony or parking-slab repairs: our engineers design, calculate and sign the drawings, then oversee the work.",
            "for": ["Contractors and developers who need a structural engineer", "Owners planning a structural renovation", "Fabricators requiring sealed shop drawings"],
            "items": [("Structural design and calculations", "Steel, wood, concrete, masonry; Québec Construction Code compliance."),
                      ("Structural modifications", "Bearing-wall and column removal, load transfers, openings, mezzanines."),
                      ("Concrete and masonry repair", "Balconies, parking slabs, parapets, masonry ties: repair specifications and drawings."),
                      ("Shop drawings", "Fabrication and installation: steel, aluminum, panels, envelope."),
                      ("Rooftop equipment", "Structural reinforcement for HVAC units, solar arrays and heavy equipment."),
                      ("Construction oversight", "Site visits, oversight reports and compliance letters for the municipality and insurer.")],
            "meta": "Structural engineer in Montréal: steel, wood, concrete and masonry design; bearing-wall removal; shop drawings; construction oversight."}},

    {"key": "mecanique",
     "slug": {"fr": "ingenierie-mecanique-batiment-cvac", "en": "building-mechanical-engineering-hvac"},
     "fr": {"title": "Mécanique du bâtiment et CVAC", "card": "Plans d’installation CVAC, inspection et nettoyage de conduits, qualité de l’air, efficacité énergétique.",
            "h1": "Mécanique du bâtiment : plans CVAC, ventilation et qualité de l’air",
            "lead": "De la conception du système de chauffage-ventilation-climatisation à l’inspection des conduits existants, nos ingénieurs livrent des plans signés et des rapports conformes aux codes et aux exigences des assureurs.",
            "for": ["Propriétaires remplaçant ou ajoutant un système CVAC", "Entrepreneurs ayant besoin de plans signés pour le permis", "Gestionnaires avec des plaintes de qualité d’air ou de confort"],
            "items": [("Plans d’installation CVAC", "Conception, calculs de charges, sélection d’équipements, plans pour permis et soumission."),
                      ("Structure et support d’équipements", "Coordination avec notre équipe de structure pour les unités en toiture."),
                      ("Inspection et nettoyage de conduits", "Caméra, évaluation de l’état et du nettoyage requis."),
                      ("Qualité de l’air intérieur", "Moisissures, CO2, humidité, radon : mesures, interprétation et correctifs."),
                      ("Efficacité énergétique", "Audit énergétique, recommandations et accompagnement pour les programmes de subventions."),
                      ("Surveillance d’installation", "Vérification de conformité aux plans et mise en service.")],
            "meta": "Ingénieur en mécanique du bâtiment à Montréal : plans d’installation CVAC, inspection de conduits, qualité de l’air, efficacité énergétique."},
     "en": {"title": "Building mechanical and HVAC", "card": "HVAC installation design, duct inspection and cleaning, air quality, energy efficiency.",
            "h1": "Building mechanical: HVAC design, ventilation and air quality",
            "lead": "From designing a heating-ventilation-air-conditioning system to inspecting existing ductwork, our engineers deliver sealed drawings and reports that satisfy codes and insurers.",
            "for": ["Owners replacing or adding an HVAC system", "Contractors needing sealed drawings for a permit", "Managers handling air-quality or comfort complaints"],
            "items": [("HVAC installation drawings", "Design, load calculations, equipment selection, permit and tender drawings."),
                      ("Equipment structure and support", "Coordinated with our structural team for rooftop units."),
                      ("Duct inspection and cleaning", "Camera survey, condition assessment and cleaning scope."),
                      ("Indoor air quality", "Mould, CO2, humidity, radon: measurement, interpretation and corrective measures."),
                      ("Energy efficiency", "Energy audits, recommendations and support for incentive programs."),
                      ("Installation oversight", "Verification against drawings and commissioning.")],
            "meta": "Building mechanical engineer in Montréal: HVAC installation drawings, duct inspection, indoor air quality, energy efficiency."}},

    {"key": "environnement",
     "slug": {"fr": "evaluation-environnementale-phase-1-2-3", "en": "environmental-site-assessment-phase-1-2-3"},
     "fr": {"title": "Évaluations environnementales", "card": "Phase I, II et III selon CSA Z768 et Z769; amiante, radon, pyrite et essais en laboratoire.",
            "h1": "Évaluation environnementale de site : Phase I, II et III",
            "lead": "Exigée par les prêteurs et les acheteurs avant toute transaction commerciale ou industrielle, l’évaluation environnementale identifie les contaminations potentielles et chiffre les mesures de réhabilitation.",
            "for": ["Acheteurs et prêteurs de propriétés commerciales et industrielles", "Propriétaires préparant une vente ou un changement d’usage", "Entrepreneurs devant gérer l’amiante ou les sols contaminés"],
            "items": [("Phase I (CSA Z768)", "Revue historique, visite de site, entrevues; identification des zones préoccupantes."),
                      ("Phase II (CSA Z769)", "Échantillonnage des sols et de l’eau souterraine, analyses en laboratoire, comparaison aux critères du MELCCFP."),
                      ("Phase III", "Plan de réhabilitation, estimation des coûts, surveillance des travaux de décontamination."),
                      ("Amiante et matériaux dangereux", "Relevé avant travaux, échantillonnage et plan de gestion conformes à la CNESST."),
                      ("Radon, pyrite et ocre ferreuse", "Mesures et essais, interprétation et solutions."),
                      ("Réservoirs souterrains", "Localisation, évaluation et accompagnement pour le retrait.")],
            "meta": "Évaluation environnementale de site à Montréal : Phase I CSA Z768, Phase II et III CSA Z769, amiante, radon, pyrite. Rapports acceptés par les prêteurs."},
     "en": {"title": "Environmental assessments", "card": "Phase I, II and III per CSA Z768 and Z769; asbestos, radon, pyrite and laboratory testing.",
            "h1": "Environmental site assessment: Phase I, II and III",
            "lead": "Required by lenders and buyers before any commercial or industrial transaction, an environmental assessment identifies potential contamination and costs the remediation.",
            "for": ["Buyers and lenders of commercial and industrial property", "Owners preparing a sale or change of use", "Contractors managing asbestos or contaminated soil"],
            "items": [("Phase I (CSA Z768)", "Historical review, site visit, interviews; identification of areas of concern."),
                      ("Phase II (CSA Z769)", "Soil and groundwater sampling, laboratory analysis, comparison with MELCCFP criteria."),
                      ("Phase III", "Remediation plan, cost estimate, oversight of decontamination work."),
                      ("Asbestos and hazardous materials", "Pre-work survey, sampling and CNESST-compliant management plan."),
                      ("Radon, pyrite and iron ochre", "Measurement and testing, interpretation and solutions."),
                      ("Underground tanks", "Location, assessment and removal support.")],
            "meta": "Environmental site assessment in Montréal: Phase I CSA Z768, Phase II and III CSA Z769, asbestos, radon, pyrite. Lender-accepted reports."}},

    {"key": "copropriete",
     "slug": {"fr": "copropriete-fonds-prevoyance-loi-16", "en": "condominium-reserve-fund-study-bill-16"},
     "fr": {"title": "Copropriétés (Loi 16)", "card": "Étude du fonds de prévoyance, carnet d’entretien et valeur de remplacement exigés par la Loi 16.",
            "h1": "Services aux syndicats de copropriété : fonds de prévoyance et carnet d’entretien",
            "lead": "La Loi 16 oblige les syndicats à faire établir leur fonds de prévoyance et leur carnet d’entretien par un professionnel. Nos ingénieurs les produisent et les arriment aux obligations Loi 122 de votre immeuble.",
            "for": ["Syndicats de copropriété et conseils d’administration", "Gestionnaires de copropriétés", "Copropriétaires avant un achat"],
            "items": [("Étude du fonds de prévoyance", "Inventaire des composantes, durées de vie, coûts de remplacement et scénarios de cotisation sur 25 ans."),
                      ("Carnet d’entretien", "Création et mise à jour; intégration des vérifications Loi 122."),
                      ("Évaluation de la valeur de remplacement", "Pour l’assurance du syndicat, conforme aux exigences des assureurs."),
                      ("Étude des charges communes", "Analyse et recommandations sur la répartition des frais."),
                      ("Inspection des parties communes", "Enveloppe, toiture, stationnement, mécanique : état et priorités."),
                      ("Accompagnement en assemblée", "Présentation des conclusions aux copropriétaires.")],
            "meta": "Fonds de prévoyance, carnet d’entretien et valeur de remplacement (Loi 16) par des ingénieurs à Montréal. Arrimés aux obligations Loi 122."},
     "en": {"title": "Condominiums (Bill 16)", "card": "Reserve fund study, maintenance log book and replacement value required by Bill 16.",
            "h1": "Condominium syndicate services: reserve fund study and maintenance log",
            "lead": "Bill 16 requires syndicates to have their reserve fund and maintenance log prepared by a professional. Our engineers produce both and align them with your building’s Bill 122 obligations.",
            "for": ["Condominium syndicates and boards", "Condominium managers", "Co-owners before a purchase"],
            "items": [("Reserve fund study", "Component inventory, service lives, replacement costs and 25-year contribution scenarios."),
                      ("Maintenance log book", "Creation and updates; integration of Bill 122 verifications."),
                      ("Replacement value appraisal", "For the syndicate’s insurance, per insurer requirements."),
                      ("Common expense study", "Analysis and recommendations on cost allocation."),
                      ("Common area inspection", "Envelope, roof, parking, mechanical: condition and priorities."),
                      ("Assembly support", "Presenting findings to co-owners.")],
            "meta": "Reserve fund study, maintenance log book and replacement value (Bill 16) by engineers in Montréal. Aligned with Bill 122 obligations."}},

    {"key": "energie",
     "slug": {"fr": "efficacite-energetique-partenaire-hydro-quebec", "en": "energy-efficiency-hydro-quebec-partner"},
     "fr": {"title": "Efficacité énergétique · Solutions efficaces", "card": "Partenaire du programme Solutions efficaces d’Hydro-Québec : études et projets d’efficacité énergétique subventionnés pour bâtiments commerciaux et multilogements.",
            "h1": "Efficacité énergétique : partenaire du programme Solutions efficaces d’Hydro-Québec",
            "lead": "GNS Inspect est partenaire reconnu du programme Solutions efficaces d’Hydro-Québec. Nous préparons et déposons vos demandes d’appui financier pour les bâtiments commerciaux, institutionnels et multilogements : l’étude d’ingénierie peut être subventionnée jusqu’à 60 000 $, et les mesures retenues financées en partie par Hydro-Québec.",
            "for": ["Propriétaires et gestionnaires d’immeubles commerciaux, industriels et institutionnels", "Syndicats et propriétaires de multilogements avec factures énergétiques élevées", "Investisseurs visant les points énergie du programme MLI Select de la SCHL"],
            "items": [("Étude de faisabilité subventionnée", "Audit énergétique et analyse d’ingénierie admissibles au programme Solutions efficaces; GNS Inspect prépare et dépose la demande à titre de partenaire."),
                      ("Conception des mesures", "Enveloppe, CVAC, éclairage, récupération de chaleur, thermopompes, contrôles : plans signés par nos ingénieurs."),
                      ("Montage financier", "Cumul des aides d’Hydro-Québec, des programmes fédéraux et provinciaux, et du financement MLI Select."),
                      ("Suivi et mesurage", "Plan de mesurage et vérification, rapports de performance exigés par les programmes."),
                      ("Solaire et BIPV", "Analyse de production, autoproduction et mesurage net avec Hydro-Québec, structure de support."),
                      ("Surveillance des travaux", "Conformité aux plans et aux conditions des subventions.")],
            "meta": "Partenaire du programme Solutions efficaces d’Hydro-Québec à Montréal : études d’efficacité énergétique subventionnées, conception CVAC et enveloppe, aide financière pour bâtiments commerciaux et multilogements."},
     "en": {"title": "Energy efficiency · Solutions efficaces", "card": "Partner in Hydro-Québec’s Solutions efficaces program: subsidized energy-efficiency studies and projects for commercial and multi-unit buildings.",
            "h1": "Energy efficiency: partner in Hydro-Québec’s Solutions efficaces program",
            "lead": "GNS Inspect is a recognized partner in Hydro-Québec’s Solutions efficaces program. We prepare and file your financial-assistance applications for commercial, institutional and multi-unit buildings: the engineering study can be subsidized up to $60,000, and the selected measures partly funded by Hydro-Québec.",
            "for": ["Owners and managers of commercial, industrial and institutional buildings", "Syndicates and multi-unit owners with high energy bills", "Investors targeting the energy points of CMHC’s MLI Select program"],
            "items": [("Subsidized feasibility study", "Energy audit and engineering analysis eligible under the Solutions efficaces program; GNS Inspect prepares and files the application as a partner."),
                      ("Measure design", "Envelope, HVAC, lighting, heat recovery, heat pumps, controls: drawings sealed by our engineers."),
                      ("Financial structuring", "Stacking Hydro-Québec assistance, federal and provincial programs, and MLI Select financing."),
                      ("Measurement and follow-up", "Measurement and verification plan, performance reports required by the programs."),
                      ("Solar and BIPV", "Production analysis, self-generation and net metering with Hydro-Québec, support structure."),
                      ("Construction oversight", "Compliance with drawings and subsidy conditions.")],
            "meta": "Partner in Hydro-Québec’s Solutions efficaces program, Montréal: subsidized energy-efficiency studies, HVAC and envelope design, financial assistance for commercial and multi-unit buildings."}},
]

# Register one page per category and language
for _c in CATEGORIES:
    for _l in ("fr", "en"):
        PAGES.append({"key": _c["key"], "lang": _l, "type": "category",
                      "title": _c[_l]["h1"][:60].rsplit(" ", 1)[0] + " | GNS Inspect",
                      "meta": _c[_l]["meta"], "service_name": _c[_l]["title"], "content": _c[_l], "slug": _c["slug"][_l]})
