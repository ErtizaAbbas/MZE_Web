"""
MZE Digital — static site generator.

All page content lives in this file. Edit it, then run:

    python build.py

to regenerate every .html page, sitemap.xml and robots.txt in the repository root.
No third-party packages are needed (Python 3.8+).
"""
import json
import os
import random

ROOT = os.path.dirname(os.path.abspath(__file__))

# ============================================================== SITE SETTINGS
SITE_URL = "https://www.mzedigital.com"
EMAIL = "mzedigital1@gmail.com"   # shown on Contact page + footer; contact form sends here
FORM_ENDPOINT = ""      # e.g. "https://formspree.io/f/xxxxxxx" — empty = front-end confirmation only
NEWSLETTER_ENDPOINT = ""  # optional form endpoint for the newsletter box
SUBSTACK_URL = ""       # e.g. "https://<your-publication>.substack.com" — Insights page + newsletter box link here
KSE_URL = ""            # KSE Sentinel public address, e.g. "https://kse-sentinel.com"

ADDRESS_LINES = ["Suite #408, 4th Floor, Silver Trade Tower", "Off JS Bank, Block 13-A",
                 "Gulshan-e-Iqbal, Karachi 75300", "Pakistan"]
ADDRESS_HTML = "<br>".join(ADDRESS_LINES)
PHONES = [("Pakistan", "+92 313 0721042", "+923130721042"), ("Singapore", "+65 9817 6016", "+6598176016")]
LINKS = {"LinkedIn": "https://www.linkedin.com/in/abbas-ertiza/", "GitHub": "https://github.com/ErtizaAbbas",
         "ORCID": "https://orcid.org/0009-0000-5529-1683"}

# ============================================================== ICONS
I = {
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "compass": '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.8-3.6 3.4-5.5 6.5-5.5s5.7 1.9 6.5 5.5"/><path d="M16 4.6a3.5 3.5 0 010 6.8M18 14.8c1.9.7 3.1 2.4 3.5 5.2"/>',
 "book": '<path d="M4 5.5A2.5 2.5 0 016.5 3H20v15H6.5A2.5 2.5 0 004 20.5z"/><path d="M4 20.5A2.5 2.5 0 006.5 23H20v-5"/>',
 "code": '<path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/>',
 "eye": '<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 "bell": '<path d="M6 16V11a6 6 0 1112 0v5l2 2H4z"/><path d="M10 21h4"/>',
 "grid": '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
 "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.8 5.5 3.8 9s-1.3 6.5-3.8 9c-2.5-2.5-3.8-5.5-3.8-9S9.5 5.5 12 3z"/>',
 "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 "scale": '<path d="M12 3v18M5 7h14M5 7l-3 7a3.5 3.5 0 006 0zM19 7l-3 7a3.5 3.5 0 006 0zM8 21h8"/>',
 "chart": '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 6-7"/>',
 "bars": '<path d="M3 21h18"/><rect x="5" y="11" width="3" height="7" rx="1"/><rect x="10.5" y="6" width="3" height="12" rx="1"/><rect x="16" y="9" width="3" height="9" rx="1"/>',
 "brain": '<path d="M9 4a3 3 0 00-3 3 3 3 0 00-2 5 3 3 0 002 5 3 3 0 006 1V5a2 2 0 00-3-1z"/><path d="M15 4a3 3 0 013 3 3 3 0 012 5 3 3 0 01-2 5 3 3 0 01-6 1"/>',
 "db": '<ellipse cx="12" cy="5.5" rx="8" ry="3"/><path d="M4 5.5v13c0 1.7 3.6 3 8 3s8-1.3 8-3v-13"/><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
 "flask": '<path d="M9 3h6M10 3v6l-5.5 9.5A2 2 0 006.2 21h11.6a2 2 0 001.7-2.5L14 9V3"/><path d="M7.5 15h9"/>',
 "bank": '<path d="M3 10l9-6 9 6"/><path d="M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 21h18"/>',
 "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 012-2h2a2 2 0 012 2v2M3 13h18"/>',
 "rocket": '<path d="M5 15c-1.5 1.5-2 5-2 5s3.5-.5 5-2"/><path d="M9 15l-3-3c1-4 4.5-8 12-9-1 7.5-5 11-9 12z"/><circle cx="14.5" cy="9.5" r="1.5"/>',
 "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
 "layers": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
 "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
 "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0119 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 "phone": '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 006 6L16 13l5 2v4a2 2 0 01-2 2A17 17 0 013 5a2 2 0 012-2z"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "link": '<path d="M10 14a4 4 0 005.7 0l3-3a4 4 0 00-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 00-5.7 0l-3 3a4 4 0 005.7 5.7l1-1"/>',
 "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/>',
}
def icon(name, cls=""):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{I[name]}</svg>')
ARROW = icon("arrow")

NAV = [("index.html", "Home"), ("services.html", "Services"), ("products.html", "Products"),
       ("projects.html", "Projects"), ("about.html", "About"), ("team.html", "Team"),
       ("blog.html", "Insights"), ("contact.html", "Contact")]
PAGES = []  # collected for the sitemap

# ============================================================== LAYOUT
def head(title, desc, page, extra_head=""):
    PAGES.append(page)
    url = SITE_URL + "/" + ("" if page == "index.html" else page)
    current = ' aria-current="page"'
    links = "".join(f'<li><a href="{h}"{current if h == page else ""}>{t}</a></li>' for h, t in NAV)
    return f"""<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}/assets/img/og-image.png">
<meta property="og:site_name" content="MZE Digital">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#2E3033">
<link rel="icon" href="assets/img/favicon.ico" sizes="any">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preload" href="assets/fonts/montserrat-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/montserrat-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/style.css">
{extra_head}</head>
<body data-page="{page}">
<a href="#main" class="skip-link">Skip to content</a>
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="index.html" aria-label="MZE Digital home"><img src="assets/img/logo-horizontal-dark.svg" alt="MZE Digital" width="170" height="31"></a>
    <ul class="nav-links">
      {links}
      <li class="mobile-cta"><a class="btn btn--primary" href="contact.html" style="justify-content:center;border:0;color:#fff">Book a consultation</a></li>
    </ul>
    <div class="nav-cta">
      <a class="btn btn--primary" href="contact.html">Book a consultation {ARROW}</a>
      <button class="nav-toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<main id="main">
"""

def footer():
    email = f'<br><a href="mailto:{EMAIL}">{EMAIL}</a>' if EMAIL else ""
    return f"""</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <img src="assets/img/logo-horizontal-light.svg" alt="MZE Digital" width="170" height="31">
        <p style="max-width:330px">Consultancy, coaching, training and technology for markets and growth. Registered with SECP &amp; FBR, Pakistan.</p>
      </div>
      <div>
        <h4>What we do</h4>
        <ul>{''.join(f'<li><a href="services.html#{s["id"]}">{s["short"]}</a></li>' for s in SERVICES)}</ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul><li><a href="about.html">About</a></li><li><a href="team.html">Team</a></li><li><a href="products.html">KSE Sentinel</a></li><li><a href="projects.html">Projects</a></li><li><a href="blog.html">Insights</a></li><li><a href="contact.html">Contact</a></li></ul>
      </div>
      <div>
        <h4>Head office</h4>
        <address>{ADDRESS_HTML}</address>
        <p style="margin-top:14px">{'<br>'.join(f'<a href="tel:{t}">{n}</a>' for _, n, t in PHONES)}{email}</p>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> MZE Digital (Pvt) Limited. All rights reserved.</span>
      <span>{' &nbsp;·&nbsp; '.join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in LINKS.items())}</span>
    </div>
  </div>
</footer>
<script src="assets/js/main.js"></script>
</body>
</html>
"""

def page_hero(crumb, eyebrow, h1, lead, extra=""):
    return f"""<section class="page-hero">
  <div class="stripes"></div>
  <div class="container">
    <div class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; {crumb}</div>
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>{extra}
  </div>
</section>"""

def cta(title="Let’s talk about your next step.",
        text="Whether you need strategic advice, a trained team or a working platform, start with a conversation."):
    return f"""<section class="section">
  <div class="container">
    <div class="cta reveal">
      <div class="stripes"></div>
      <div><h2>{title}</h2><p>{text}</p></div>
      <div class="btn-row"><a class="btn btn--light" href="contact.html">Book a consultation {ARROW}</a></div>
    </div>
  </div>
</section>"""

def write(name, html):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(html)

# ============================================================== CONTENT
def ext(url, label, cls="btn btn--light"):
    """Button to an external URL; falls back to the contact page if the URL is not set yet."""
    if url:
        return f'<a class="{cls}" href="{url}" target="_blank" rel="noopener">{label} {ARROW}</a>'
    return f'<a class="{cls}" href="contact.html">{label} {ARROW}</a>'

KSE_BTN_LABEL = "Visit KSE Sentinel"

# Four equal pillars (used on Home, Services, About, footer, contact form)
SERVICES = [
  {"id": "consultancy", "icon": "compass", "short": "Strategy consultancy", "title": "Strategy Consultancy",
   "lead": "Macro, market and strategic advice for organisations making high-stakes decisions.",
   "body": "We combine quantitative evidence with economic and strategic analysis to give leadership teams a clear, structured view of markets, risks and options.",
   "items": ["Macro-economic and market outlooks", "Geopolitical risk assessment and scenarios", "Business development and growth strategy", "Data and analytics strategy"],
   "deliverables": ["Briefing packs", "Scenario frameworks", "Strategy roadmaps"]},
  {"id": "coaching", "icon": "users", "short": "Coaching & mentorship", "title": "Coaching & Mentorship",
   "lead": "One-to-one and small-group mentorship in trading, investment and professional growth.",
   "body": "Built on the experience of mentoring 80+ students worldwide, our coaching develops process, discipline and judgement, not just knowledge.",
   "items": ["Trading and investment mentorship", "Risk management and position sizing", "Personal trading and learning plans", "Ongoing review sessions"],
   "deliverables": ["Personal plans", "Review sessions", "Progress tracking"]},
  {"id": "training", "icon": "book", "short": "Professional training", "title": "Professional Training",
   "lead": "Practical programmes for individuals, teams and institutions, delivered with our training partners.",
   "body": "We design and deliver courses that take people from theory to practice, and we develop training programmes together with partner institutes.",
   "items": ["Data science and Python for finance", "Quantitative methods and backtesting", "Course and curriculum development", "Executive and leadership briefings"],
   "deliverables": ["Courses & curricula", "Workshops", "Learning materials"]},
  {"id": "technology", "icon": "code", "short": "Technology & data", "title": "Technology & Data",
   "lead": "Data science, analytics and software development, including our own platform, KSE Sentinel.",
   "body": "We build models, dashboards, data pipelines and production software for finance and for our partners, with the same engineering behind KSE Sentinel.",
   "items": ["Data science and predictive modelling", "Data analytics, dashboards and reporting", "Data engineering and market-data pipelines", "Web platforms, APIs and financial software"],
   "deliverables": ["Software & platforms", "Dashboards", "Data pipelines"]},
]

SECTORS = [("bank", "Financial institutions", "Brokerages, banks and asset managers that need sharper analysis and better tools."),
           ("briefcase", "Companies & leadership teams", "Organisations planning growth, entering markets or managing risk."),
           ("book", "Training institutes", "Partners that want strong programmes, curricula and technology behind them."),
           ("users", "Professionals & students", "People building skills in trading, investment, data and analysis."),
           ("rocket", "Start-ups & fintechs", "Young companies that need data, product and engineering capability."),
           ("chart", "Traders & investors", "Individuals and teams who want a disciplined, evidence-based process.")]

STACK = [("Languages & data", ["Python", "pandas", "NumPy", "SciPy", "SQL"]),
         ("Modelling", ["OLS & Ridge regression", "Walk-forward validation", "Out-of-sample testing", "Scenario analysis"]),
         ("Platforms & APIs", ["FastAPI", "Multi-tenant architecture", "Automated EOD ingestion", "Docker"]),
         ("Visualisation", ["Streamlit", "Plotly", "Interactive dashboards", "Automated reporting"])]

PARTNERS = [("rising-stars.png", "Rising Stars", "Everyone is an achiever"),
            ("fatimaa-skills-institute.png", "Fatimaa Skills Institute", "Skills development and training"),
            ("hadiz-international.png", "Hadiz International", "Business development")]

def services_cards():
    out = []
    for i, s in enumerate(SERVICES):
        lis = "".join(f"<li>{x}</li>" for x in s["items"][:3])
        out.append(f'<a class="card hover reveal" href="services.html#{s["id"]}"><span class="card-num">0{i+1}</span>'
                   f'<div class="icon-box">{icon(s["icon"])}</div><h3>{s["title"]}</h3><p>{s["lead"]}</p>'
                   f'<ul class="ticks">{lis}</ul><span class="link-arrow">Learn more {ARROW}</span></a>')
    return '<div class="grid grid-4">' + "".join(out) + "</div>"

def stack_table():
    return '<div class="stack-table reveal">' + "".join(
        f'<div><h4>{h}</h4><ul>{"".join(f"<li>{x}</li>" for x in xs)}</ul></div>' for h, xs in STACK) + "</div>"

def partners_html():
    return '<div class="partner-grid">' + "".join(
        f'<figure class="partner reveal"><img src="assets/img/partners/{f}" alt="{n} logo" loading="lazy" width="600" height="360">'
        f'<figcaption><b>{n}</b><span>{d}</span></figcaption></figure>' for f, n, d in PARTNERS) + "</div>"

def partners_section(paper=True):
    return f"""<section class="section{' section--paper' if paper else ''}" id="partners">
  <div class="container">
    <div class="section-head center reveal"><span class="eyebrow">Our partners</span><h2>Growing together</h2>
      <p class="lead">We work with partner organisations on business development, coaching and training projects, and serve as their technology and consultancy provider.</p></div>
    {partners_html()}
  </div>
</section>"""

MODULES = [("eye", "Watchlist manager", "Track tickers, sectors and custom baskets in one view."),
           ("bell", "Alert engine", "Rule-based price, volume and signal alerts."),
           ("grid", "Sector heatmap", "Instant read of breadth and sector rotation."),
           ("globe", "Macro overlay", "Rates, FX and macro context beside price action."),
           ("calendar", "Earnings calendar", "Upcoming results and corporate events."),
           ("scale", "Position sizer", "Risk-based sizing for every trade idea.")]

def modules_html():
    return '<div class="module-grid">' + "".join(
        f'<div class="module">{icon(ic)}<div><b>{t}</b><span>{d}</span></div></div>' for ic, t, d in MODULES) + "</div>"

def kse_card():
    """Factual KSE Sentinel product card (no mock data)."""
    rows = [("Market", "Pakistan Stock Exchange (PSX)"), ("Architecture", "Multi-tenant, isolated client workspaces"),
            ("Back end", "Python · FastAPI · Docker"), ("Data", "Automated daily end-of-day ingestion"),
            ("Modules", "6 integrated modules"), ("Built by", "MZE Digital")]
    lis = "".join(f'<div class="spec-row"><small>{a}</small><b>{b}</b></div>' for a, b in rows)
    return f"""<div class="spec-card">
  <div class="spec-head"><span class="spec-dot"></span><span>KSE SENTINEL</span></div>
  <div class="spec-body">{lis}</div>
  <div class="spec-foot">{ext(KSE_URL, KSE_BTN_LABEL, "btn btn--light")}</div>
</div>"""

def pillars_panel():
    """Hero visual: the four pillars, plain and factual."""
    rows = "".join(f'<a class="pillar-row" href="services.html#{s["id"]}"><span class="pillar-ic">{icon(s["icon"])}</span>'
                   f'<span><b>{s["title"]}</b><em>{s["lead"]}</em></span></a>' for s in SERVICES)
    return f'<div class="pillars-panel"><div class="spec-head"><span class="spec-dot"></span><span>WHAT WE DO</span></div>{rows}</div>'

def chartline(light=True):
    c = "#ffffff" if light else "#2E3033"
    return (f'<svg class="chartline" viewBox="0 0 300 100" preserveAspectRatio="none" aria-hidden="true"><path d="M0 80 L30 72 L60 76 L90 58 L120 62 '
            f'L150 44 L180 50 L210 30 L240 36 L270 18 L300 22" fill="none" stroke="{c}" stroke-opacity=".55" stroke-width="2"/></svg>')

BOOKS = [("", "STRATEGIC STUDIES", "The Empire", "Strategic studies and the Strategic Dominance Formula."),
         ("v2", "MACROECONOMICS", "The Global Economy", "A structured view of the forces shaping the world economy."),
         ("v3", "LETTERS", "When You Need Me", "Letters to a daughter. ISBN 9789819445387."),
         ("v4", "NON-FICTION", "Witness", "Published 2025.")]
def books_html():
    return '<div class="grid grid-4">' + "".join(
        f'<div class="book reveal"><div class="book-cover {v}"><small>{k}</small><b>{t}</b><small>ERTIZA ABBAS</small></div><div><h4>{t}</h4><p>{d}</p></div></div>'
        for v, k, t, d in BOOKS) + "</div>"

PROJECTS = [
  ("software", "pat-1", True, "Platform", "KSE Sentinel", "Institutional, multi-tenant quantitative trading and analytics engine for the Pakistan Stock Exchange, with six core modules and automated end-of-day data ingestion.", ["FastAPI", "Python", "Multi-tenant"], KSE_URL),
  ("data-science research", "pat-4", True, "Quant Engine", "Multi-Asset Alpha Engine", "Dual EMA/RSI signals, ATR-based risk, OLS and Ridge next-day prediction, walk-forward validation and friction-adjusted backtesting across US30, US100, GER40, Gold, GBPJPY and BTC, with a five-tab Streamlit dashboard.", ["Python", "Plotly", "Streamlit"], ""),
  ("research", "pat-6", True, "Open Source", "Trend & Momentum Engine", "A systematic trend and momentum research framework, published openly on GitHub.", ["Python", "pandas", "NumPy"], "https://github.com/ErtizaAbbas"),
  ("research consultancy", "pat-2", True, "Research", "Geopolitical Risk Modelling", "Structured models that convert strategic and geopolitical analysis into scenario inputs for portfolio and policy decisions.", ["SciPy", "Scenario analysis"], ""),
  ("training", "pat-3", False, "Partnership", "Training & skills programmes", "Business development, course development and training delivered with partner institutes, with MZE Digital as technology and consultancy provider.", ["Curriculum", "Delivery", "Technology"], "about.html#partners"),
  ("publishing", "pat-5", False, "Publishing", "The Empire & The Global Economy", "Two 2025 books on strategic studies and macroeconomics, including the Strategic Dominance Formula D = (M + A) × C^w.", ["Strategy", "Macroeconomics"], "about.html#publications"),
]
def project_card(p):
    cat, pat, light, tag, t, d, st, url = p
    if url:
        target = ' target="_blank" rel="noopener"' if url.startswith("http") else ""
        open_, close = f'<a class="card project reveal" data-cat="{cat}" href="{url}"{target}>', "</a>"
    else:
        open_, close = f'<div class="card project reveal" data-cat="{cat}">', "</div>"
    return (f'{open_}<div class="post-thumb"><div class="pattern {pat}"></div>{chartline(light)}</div>'
            f'<div class="project-body"><div class="tags"><span class="tag">{tag}</span></div><h3>{t}</h3><p>{d}</p>'
            f'<div class="stack">{"".join(f"<span>{s}</span>" for s in st)}</div></div>{close}')

# ---- People
TEAM_LEAD = {"name": "Ertiza Abbas", "photo": "assets/img/team/ertiza-abbas.jpg", "role": "Founder & CEO"}
DIRECTORS = [
  {"name": "Syed Naweed Mehdi", "role": "Director & COO", "photo": "", "initials": "NM",
   "bio": "Director and Chief Operating Officer of MZE Digital. He is also CEO of Fatimaa Skills Institute, one of MZE Digital's partners in training and skills development.", "linkedin": ""},
  {"name": "Faiza Zehra", "role": "Director", "photo": "assets/img/team/faiza-zehra.jpg", "initials": "FZ",
   "bio": "Director of MZE Digital. An academic, university lecturer and senior researcher, she brings teaching and research experience to the company's training and research work.", "linkedin": ""},
]
ENGINEERS = [
  {"name": "Syed Taha Ali Naqvi", "role": "Software Engineer (Full-Stack)", "photo": "assets/img/team/syed-taha-ali-naqvi.jpg", "initials": "TN",
   "bio": "Full-stack software engineer and graduate of NED University of Engineering &amp; Technology. Mentored by Ertiza Abbas, he works across front-end and back-end development on MZE Digital's software projects.",
   "linkedin": "https://www.linkedin.com/in/syedtahaalinaqvi/"},
  {"name": "Abdul Moazzim", "role": "Software Engineer (Full-Stack)", "photo": "assets/img/team/abdul-moazzim.jpg", "initials": "AM",
   "bio": "Full-stack software engineer and graduate of NED University of Engineering &amp; Technology. Mentored by Ertiza Abbas, he works across front-end and back-end development on MZE Digital's software projects.",
   "linkedin": "https://www.linkedin.com/in/abdulmoazzim/"},
]
def person_card(p):
    pic = (f'<img src="{p["photo"]}" alt="{p["name"]}" loading="lazy">' if p["photo"] else f'<span>{p["initials"]}</span>')
    li = (f'<a class="link-arrow" href="{p["linkedin"]}" target="_blank" rel="noopener">LinkedIn {ARROW}</a>' if p["linkedin"] else "")
    return (f'<div class="person reveal"><div class="avatar">{pic}</div><h3>{p["name"]}</h3>'
            f'<span class="role">{p["role"]}</span><p>{p["bio"]}</p>{li}</div>')

ORG_JSONLD = {
  "@context": "https://schema.org", "@type": "Organization", "name": "MZE Digital (Pvt) Limited", "alternateName": "MZE Digital",
  "url": SITE_URL, "logo": SITE_URL + "/assets/img/icon-512.png",
  "description": "Strategy consultancy, coaching, professional training and technology for markets and growth.",
  "address": {"@type": "PostalAddress", "streetAddress": "Suite #408, 4th Floor, Silver Trade Tower, Off JS Bank, Block 13-A, Gulshan-e-Iqbal",
              "addressLocality": "Karachi", "postalCode": "75300", "addressCountry": "PK"},
  "telephone": "+92-313-0721042",
  "founder": {"@type": "Person", "name": "Ertiza Abbas", "jobTitle": "Founder & CEO", "sameAs": list(LINKS.values())},
}
if EMAIL:
    ORG_JSONLD["email"] = EMAIL

def newsletter_band():
    sub = ext(SUBSTACK_URL, "Read Search 4 Research", "btn btn--primary")
    return f"""<section class="section section--paper">
  <div class="container feature">
    <div class="reveal"><span class="eyebrow">Insights</span><h2>Search 4 Research</h2>
      <p class="lead">Our publication on markets, economics, strategy and data, read by 2,000+ subscribers.</p></div>
    <div class="reveal"><div class="btn-row" style="justify-content:flex-end">{sub}<a class="btn btn--ghost" href="blog.html">About our insights</a></div></div>
  </div>
</section>"""

# ============================================================== HOME
home = head("MZE Digital — Strategy, Skills & Technology",
            "MZE Digital provides strategy consultancy, coaching and mentorship, professional training, and data-driven technology for markets and growth.",
            "index.html", f'<script type="application/ld+json">{json.dumps(ORG_JSONLD, ensure_ascii=False)}</script>\n') + f"""
<section class="hero">
  <div class="stripes"></div>
  <div class="container hero-grid">
    <div class="reveal">
      <span class="eyebrow">Consultancy · Coaching · Training · Technology</span>
      <h1>Strategy, skills and technology for <em>markets and growth.</em></h1>
      <p class="lead">MZE Digital helps organisations and professionals grow through strategy consultancy, coaching and mentorship, professional training, and data-driven technology, backed by two decades of experience in markets, economic strategy and analytics.</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="services.html">Explore what we do {ARROW}</a>
        <a class="btn btn--ghost" href="contact.html">Book a consultation</a>
      </div>
      <div class="hero-meta">
        <div><strong>Consultancy</strong>Strategy &amp; markets</div>
        <div><strong>Coaching</strong>Mentorship</div>
        <div><strong>Training</strong>With partners</div>
        <div><strong>Technology</strong>Data &amp; software</div>
      </div>
    </div>
    <div class="hero-visual reveal">
      {pillars_panel()}
      <div class="float-card"><div class="ic">{icon("pin")}</div><div><b>Singapore · Seoul · Karachi</b><span>Registered with SECP &amp; FBR, Pakistan</span></div></div>
    </div>
  </div>
</section>

<section class="section--tight" style="padding-top:0">
  <div class="container">
    <div class="facts reveal">
      <div class="fact"><b>20+</b><span>Years across strategy, business development and analytics</span></div>
      <div class="fact"><b>80+</b><span>Students mentored worldwide in trading and investment</span></div>
      <div class="fact"><b>{len(PARTNERS)}</b><span>Partner organisations in business development and training</span></div>
      <div class="fact"><b>3</b><span>Cities: Singapore, Seoul and Karachi</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split-head">
      <div class="section-head reveal"><span class="eyebrow">What we do</span><h2>Four disciplines. One standard of evidence.</h2></div>
      <a class="link-arrow reveal" href="services.html">All services {ARROW}</a>
    </div>
    {services_cards()}
  </div>
</section>

{partners_section()}

<section class="section section--dark" style="position:relative;overflow:hidden">
  <div class="container feature">
    <div class="reveal">
      <span class="eyebrow">Our platform</span>
      <h2>KSE Sentinel</h2>
      <p class="lead">An institutional, multi-tenant quantitative trading and analytics platform for the Pakistan Stock Exchange, designed and built by MZE Digital.</p>
      {modules_html()}
      <div class="btn-row">{ext(KSE_URL, KSE_BTN_LABEL)}<a class="btn btn--outline-light" href="products.html">Platform details</a></div>
    </div>
    <div class="reveal hide-mobile">{kse_card()}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center reveal"><span class="eyebrow">Who we work with</span><h2>Organisations and people ready to grow</h2></div>
    <div class="grid grid-3">
      {''.join(f'<div class="card reveal"><div class="icon-box">{icon(ic)}</div><h3>{t}</h3><p>{d}</p></div>' for ic, t, d in SECTORS)}
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    <div class="section-head center reveal"><span class="eyebrow">How we work</span><h2>From question to result</h2><p class="lead">Every engagement follows the same disciplined path, whether the outcome is advice, a trained team or a working system.</p></div>
    <div class="steps">
      <div class="step reveal"><h4>Discover</h4><p>Understand the goal, the people involved and what success looks like.</p></div>
      <div class="step reveal"><h4>Design</h4><p>Shape the strategy, programme or solution, tested against real-world conditions.</p></div>
      <div class="step reveal"><h4>Deliver</h4><p>Advise, train or build, with clear milestones and honest reporting.</p></div>
      <div class="step reveal"><h4>Enable</h4><p>Leave people and organisations able to carry the work forward.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split-head">
      <div class="section-head reveal"><span class="eyebrow">Selected work</span><h2>Work that ships.</h2></div>
      <a class="link-arrow reveal" href="projects.html">All projects {ARROW}</a>
    </div>
    <div class="grid grid-3">{''.join(project_card(p) for p in (PROJECTS[0], PROJECTS[4], PROJECTS[1]))}</div>
  </div>
</section>

{newsletter_band()}
""" + cta() + footer()
write("index.html", home)

# ============================================================== SERVICES
svc_rows = "".join(f"""
    <div class="svc-row reveal" id="{s['id']}">
      <div class="num">0{i+1}</div>
      <div><div class="icon-box">{icon(s['icon'])}</div><h3>{s['title']}</h3><p class="lead" style="font-size:1.05rem">{s['lead']}</p><p>{s['body']}</p></div>
      <div><h4>What we do</h4><ul class="ticks">{''.join(f'<li>{x}</li>' for x in s['items'])}</ul>
        <h4>Typical deliverables</h4><div class="chips">{''.join(f'<span>{d}</span>' for d in s['deliverables'])}</div></div>
    </div>""" for i, s in enumerate(SERVICES))
services = head("Services — MZE Digital", "Strategy consultancy, coaching and mentorship, professional training, and technology and data services from MZE Digital.", "services.html") + page_hero(
  "Services", "What we do", "Strategy, skills and technology.",
  "Four connected disciplines that help organisations and professionals decide better, learn faster and build what they need.",
  '<div class="svc-index">' + "".join(f'<a href="#{s["id"]}">{s["short"]}</a>' for s in SERVICES) + "</div>") + f"""
<section class="section">
  <div class="container">{svc_rows}
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Who we work with</span><h2>Organisations and people ready to grow</h2></div>
    <div class="grid grid-3">
      {''.join(f'<div class="sector reveal">{icon(ic)}<h4>{t}</h4><p>{d}</p></div>' for ic, t, d in SECTORS)}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Engagement models</span><h2>Work with us the way that suits you</h2></div>
    <div class="grid grid-3">
      <div class="card reveal"><div class="icon-box">{icon("target")}</div><h3>Project</h3><p>A defined scope and outcome: a strategy paper, a training programme, a model or a platform module.</p></div>
      <div class="card reveal"><div class="icon-box">{icon("layers")}</div><h3>Ongoing partnership</h3><p>A standing advisory, training and technology capability that grows with your organisation.</p></div>
      <div class="card reveal"><div class="icon-box">{icon("users")}</div><h3>One-to-one</h3><p>Personal coaching and mentorship for professionals, traders and investors.</p></div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Technology</span><h2>Our technology stack</h2><p class="lead">Widely used, well-supported tools, so what we build is easy for you to own.</p></div>
    {stack_table()}
  </div>
</section>
""" + cta("Tell us what you want to achieve.", "We will come back with a clear plan, scope and next steps.") + footer()
write("services.html", services)

# ============================================================== ABOUT
about = head("About — MZE Digital", "MZE Digital (Pvt) Limited: strategy consultancy, coaching, training and technology, registered with SECP and FBR.", "about.html") + page_hero(
  "About", "Company", "Rigorous analysis, practical delivery.",
  "MZE Digital (Pvt) Limited is a consultancy, coaching, training and technology company registered with the SECP and FBR in Pakistan, operating across Singapore, Seoul and Karachi.") + f"""
<section class="section">
  <div class="container feature">
    <div class="reveal">
      <span class="eyebrow">Who we are</span>
      <h2>Built on two decades of market and strategy experience.</h2>
      <p>MZE Digital was founded by Ertiza Abbas, a quantitative data and macro strategic analyst with 20 years of experience across business development, economic strategy and analytics.</p>
      <p>We exist to close the gap between analysis and action: to turn rigorous research into better decisions, skilled people and working systems. Our work spans strategy consultancy, coaching and mentorship, professional training, technology and publishing, and we are the parent company behind KSE Sentinel.</p>
      <div class="btn-row" style="margin-top:28px"><a class="btn btn--primary" href="team.html">Meet the team {ARROW}</a><a class="btn btn--ghost" href="services.html">Our services</a></div>
    </div>
    <div class="reveal">
      <div class="grid grid-2">
        <div class="card"><div class="icon-box">{icon("target")}</div><h4>Mission</h4><p>Give organisations and professionals clarity, skills and tools to grow.</p></div>
        <div class="card"><div class="icon-box">{icon("spark")}</div><h4>Vision</h4><p>Institutions and people that decide with evidence and act with confidence.</p></div>
        <div class="card"><div class="icon-box">{icon("layers")}</div><h4>Approach</h4><p>Evidence first: tested assumptions, real-world costs and honest reporting.</p></div>
        <div class="card"><div class="icon-box">{icon("shield")}</div><h4>Integrity</h4><p>Neutral, consistent analysis, with the same standard applied to every market and state.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    <span class="eyebrow reveal">Our principle</span>
    <p class="quote reveal">Good analysis is not the most complicated model. It is the <b>honest</b> one: tested against reality, with every real-world cost counted.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">What we offer</span><h2>Our services</h2></div>
    {services_cards()}
  </div>
</section>

{partners_section()}

<section class="section section--dark">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Where we work</span><h2>Three cities, one team.</h2></div>
    <div class="grid grid-3">
      <div class="office reveal"><small>Head office</small><h3>Karachi</h3><p>Suite #408, 4th Floor, Silver Trade Tower, Off JS Bank, Block 13-A, Gulshan-e-Iqbal, Karachi 75300</p></div>
      <div class="office reveal"><small>Regional</small><h3>Singapore</h3><p>Research, strategy and client advisory for Southeast Asia.</p></div>
      <div class="office reveal"><small>Regional</small><h3>Seoul</h3><p>Publishing, translation and advisory work in Korea.</p></div>
    </div>
  </div>
</section>

<section class="section" id="publications">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Publishing</span><h2>Publications</h2><p class="lead">Books, research papers and analytical content published under MZE Digital, including Korean translation and editorial work on <em>그때 나는 인도되었노라</em> (Then I Was Guided), published in Seoul.</p></div>
    {books_html()}
  </div>
</section>
""" + cta() + footer()
write("about.html", about)

# ============================================================== TEAM
creds = [("NUS Business School", "Executive credentials"), ("Corporate Finance Institute (USA)", "Professional certification"),
         ("Korean Civil & Administrative Law", "Specialist credentials"), ("Certified Trader", "Singapore banks association"),
         ("80+ students", "Mentored in trading and investment"), ("Search 4 Research", "Publisher, 2,000+ subscribers")]
team = head("Team — MZE Digital", "Meet the people behind MZE Digital.", "team.html") + page_hero(
  "Team", "Our people", "Experience you can build on.",
  "Directors, researchers and engineers, led by two decades of experience in markets, strategy and data.") + f"""
<section class="section">
  <div class="container leader">
    <div class="avatar reveal"><img src="{TEAM_LEAD['photo']}" alt="Ertiza Abbas, Founder &amp; CEO of MZE Digital"></div>
    <div class="reveal">
      <span class="eyebrow">Founder &amp; CEO</span>
      <h2>Ertiza Abbas</h2>
      <p class="lead">Quantitative Data &amp; Macro Strategic Analyst, published author and macro strategist.</p>
      <p>Ertiza brings 20 years of experience spanning business development, economic strategy and analytics. His work combines data science and data engineering with macro and geopolitical analysis, from systematic alpha engines and friction-adjusted backtesting to geopolitical risk modelling. He is the principal architect of KSE Sentinel, has mentored 80+ students worldwide, and works in English and Urdu across Singapore, Seoul and Karachi.</p>
      <div class="cred-list">{''.join(f'<div><b>{a}</b>{b}</div>' for a, b in creds)}</div>
      <div class="btn-row">
        <a class="btn btn--primary" href="{LINKS['LinkedIn']}" target="_blank" rel="noopener">LinkedIn {ARROW}</a>
        <a class="btn btn--ghost" href="{LINKS['GitHub']}" target="_blank" rel="noopener">GitHub</a>
        <a class="btn btn--ghost" href="{LINKS['ORCID']}" target="_blank" rel="noopener">ORCID</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Leadership</span><h2>Directors</h2></div>
    <div class="grid grid-3 team-grid">{''.join(person_card(p) for p in DIRECTORS)}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Engineering</span><h2>Software engineers</h2></div>
    <div class="grid grid-3 team-grid">{''.join(person_card(p) for p in ENGINEERS)}</div>
  </div>
</section>

<section class="section section--paper">
  <div class="container feature">
    <div class="reveal"><span class="eyebrow">Careers</span><h2>Work with us</h2><p class="lead">We are always interested in people who combine curiosity with rigour: analysts, trainers, engineers and researchers.</p></div>
    <div class="reveal"><div class="btn-row" style="justify-content:flex-end"><a class="btn btn--primary" href="contact.html">Send your profile {ARROW}</a></div></div>
  </div>
</section>
""" + footer()
write("team.html", team)

# ============================================================== PROJECTS
projects = head("Projects — MZE Digital", "Selected software, research, training and publishing work by MZE Digital.", "projects.html") + page_hero(
  "Projects", "Our work", "Selected projects",
  "Platforms, research, training partnerships and publishing, each delivered to the same standard of evidence.") + f"""
<section class="section">
  <div class="container">
    <div class="split-head reveal">
      <p class="muted" style="margin:0">Filter by discipline</p>
      <div class="filters">
        <button class="filter active" data-filter="all">All</button>
        <button class="filter" data-filter="software">Software</button>
        <button class="filter" data-filter="data-science">Data science</button>
        <button class="filter" data-filter="research">Research</button>
        <button class="filter" data-filter="training">Training</button>
        <button class="filter" data-filter="publishing">Publishing</button>
      </div>
    </div>
    <div class="grid grid-3">{''.join(project_card(p) for p in PROJECTS)}</div>
  </div>
</section>
""" + cta("Have a project in mind?", "Tell us what you are trying to decide, learn or build. We will come back with a clear plan.") + footer()
write("projects.html", projects)

# ============================================================== PRODUCTS
products = head("Products — MZE Digital", "KSE Sentinel, training programmes and publications from MZE Digital.", "products.html") + page_hero(
  "Products", "Products & programmes", "Tools and programmes for better decisions.",
  "Institutional software for the Pakistan equity market, structured training for professionals, and research you can read.") + f"""
<section class="section">
  <div class="container">
    <div class="product-hero-card reveal">
      <div class="stripes"></div>
      <div class="feature">
        <div>
          <span class="eyebrow">Our platform</span>
          <h2>KSE Sentinel</h2>
          <p class="lead">An institutional, multi-tenant quantitative trading and analytics engine for the Pakistan Stock Exchange. One secure platform for monitoring, alerts, research and risk, for multiple desks or client organisations.</p>
          <ul class="ticks">
            <li>Multi-tenant architecture with isolated client workspaces</li>
            <li>Modern Python and FastAPI back end built for speed and integration</li>
            <li>Automated daily end-of-day data ingestion</li>
          </ul>
          <div class="btn-row" style="margin-top:28px">{ext(KSE_URL, KSE_BTN_LABEL)}<a class="btn btn--outline-light" href="contact.html">Request a demo</a></div>
        </div>
        <div>{kse_card()}</div>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Inside KSE Sentinel</span><h2>Six modules, one workflow.</h2></div>
    <div class="grid grid-3">
      {''.join(f'<div class="card reveal"><div class="icon-box">{icon(ic)}</div><h3>{t}</h3><p>{d}</p></div>' for ic, t, d in MODULES)}
    </div>
  </div>
</section>

<section class="section" id="training">
  <div class="container">
    <div class="section-head center reveal"><span class="eyebrow">Training &amp; mentorship</span><h2>Programmes</h2><p class="lead">Practical, evidence-based programmes for individuals, teams and institutions. Formats and fees are tailored to each engagement.</p></div>
    <div class="grid grid-3">
      <div class="card price-card reveal"><span class="tag">Individuals</span><h3>Trading &amp; Investment Mentorship</h3><p>One-to-one guidance on process, discipline and risk, drawing on 80+ students mentored worldwide.</p><ul class="ticks"><li>Personal trading plan</li><li>Risk &amp; position sizing</li><li>Ongoing review sessions</li></ul><a class="btn btn--ghost" href="contact.html">Enquire</a></div>
      <div class="card price-card featured reveal"><span class="tag">Teams &amp; institutes</span><h3>Data Science for Finance with Python</h3><p>From spreadsheets to systematic analysis: data, modelling and honest backtesting.</p><ul class="ticks"><li>pandas, NumPy &amp; SciPy</li><li>Regression, signals &amp; out-of-sample tests</li><li>Friction-adjusted backtesting</li></ul><a class="btn btn--light" href="contact.html">Enquire</a></div>
      <div class="card price-card reveal"><span class="tag">Organisations</span><h3>Executive Strategy Briefings</h3><p>Focused sessions on macro outlook, geopolitical risk and data strategy for leadership teams.</p><ul class="ticks"><li>Tailored to your sector</li><li>Scenario frameworks</li><li>Written briefing pack</li></ul><a class="btn btn--ghost" href="contact.html">Enquire</a></div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Books</span><h2>Publications</h2></div>
    {books_html()}
  </div>
</section>
""" + cta("See KSE Sentinel in action.", "Book a walkthrough of the platform with our team.") + footer()
write("products.html", products)

# ============================================================== INSIGHTS (blog.html)
sub_btn = ext(SUBSTACK_URL, "Read Search 4 Research", "btn btn--primary")
blog = head("Insights — MZE Digital", "Search 4 Research: research and commentary on markets, economics, strategy and data from MZE Digital.", "blog.html") + page_hero(
  "Insights", "Insights", "Search 4 Research",
  "Our research publication on markets, macroeconomics, strategy and quantitative methods, read by 2,000+ subscribers.",
  f'<div class="btn-row" style="margin-top:32px">{sub_btn}</div>') + f"""
<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">What we write about</span><h2>Topics</h2></div>
    <div class="grid grid-4">
      <div class="card reveal"><div class="icon-box">{icon("chart")}</div><h3>Markets</h3><p>Equities, indices, FX and commodities, and the evidence behind systematic strategies.</p></div>
      <div class="card reveal"><div class="icon-box">{icon("globe")}</div><h3>Macro &amp; geopolitics</h3><p>The economic and strategic forces shaping markets, analysed with consistent, neutral terms.</p></div>
      <div class="card reveal"><div class="icon-box">{icon("flask")}</div><h3>Quantitative methods</h3><p>Modelling, validation and honest backtesting with real-world costs.</p></div>
      <div class="card reveal"><div class="icon-box">{icon("book")}</div><h3>Skills &amp; learning</h3><p>Practical guidance for professionals building skills in data and investing.</p></div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Books</span><h2>Publications</h2></div>
    {books_html()}
  </div>
</section>
""" + cta("Want a briefing on a topic?", "We prepare tailored briefings for leadership teams and investors.") + footer()
write("blog.html", blog)

# ============================================================== CONTACT
interests = [s["title"] for s in SERVICES] + ["KSE Sentinel", "Partnership", "Publishing", "Other"]
email_item = (f'<div class="contact-item"><div class="icon-box">{icon("mail")}</div><div><small>Email</small><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>'
              if EMAIL else "")
form_attrs = f' action="{FORM_ENDPOINT}" method="POST"' if FORM_ENDPOINT else f' data-mailto="{EMAIL}"'
contact = head("Contact — MZE Digital", "Contact MZE Digital in Karachi or Singapore.", "contact.html") + page_hero(
  "Contact", "Get in touch", "Let’s talk about what you need.",
  "Consultancy, coaching, training, technology or a KSE Sentinel demo: send a message, email or call us directly.") + f"""
<section class="section">
  <div class="container contact-grid">
    <div class="reveal">
      <div class="contact-item"><div class="icon-box">{icon("pin")}</div><div><small>Head office</small><b>{ADDRESS_HTML}</b></div></div>
      {''.join(f'<div class="contact-item"><div class="icon-box">{icon("phone")}</div><div><small>{c} · call or WhatsApp</small><a href="tel:{t}">{n}</a> &nbsp;·&nbsp; <a href="https://wa.me/{t.lstrip("+")}" target="_blank" rel="noopener">WhatsApp</a></div></div>' for c, n, t in PHONES)}
      {email_item}
      <div class="contact-item"><div class="icon-box">{icon("link")}</div><div><small>Online</small><a href="{LINKS['LinkedIn']}" target="_blank" rel="noopener">LinkedIn</a> &nbsp;·&nbsp; <a href="{LINKS['GitHub']}" target="_blank" rel="noopener">GitHub</a></div></div>
    </div>
    <form class="form reveal" data-form{form_attrs}>
      <h3 style="margin-bottom:6px">Send us a message</h3>
      <p class="muted" style="font-size:.9rem">Tell us a little about your enquiry and we will get back to you.</p>
      <div class="form-row">
        <div class="field"><label for="n">Full name</label><input id="n" name="name" required placeholder="Your name"></div>
        <div class="field"><label for="c">Company</label><input id="c" name="company" placeholder="Organisation (optional)"></div>
      </div>
      <div class="form-row">
        <div class="field"><label for="e">Email</label><input id="e" name="email" type="email" required placeholder="you@company.com"></div>
        <div class="field"><label for="p">Phone</label><input id="p" name="phone" type="tel" placeholder="+92 / +65 …"></div>
      </div>
      <div class="field"><label for="s">I’m interested in</label>
        <select id="s" name="interest">{''.join(f'<option>{x.replace("&", "&amp;")}</option>' for x in interests)}</select></div>
      <div class="field"><label for="m">Message</label><textarea id="m" name="message" required placeholder="Tell us about your project or question"></textarea></div>
      <span class="hp" aria-hidden="true"><input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></span>
      <button class="btn btn--primary" type="submit">Send message {ARROW}</button>
      <p class="form-note">Sending opens your email app with your message ready to send to {EMAIL}.</p>
      <div class="form-success">Thank you. Your email app should now be open with your message. If it did not open, please email {EMAIL} directly.</div>
      <div class="form-error">Sorry, the message could not be sent. Please email or call us instead.</div>
    </form>
  </div>
</section>
""" + footer()
write("contact.html", contact)

# ============================================================== 404
notfound = head("Page not found — MZE Digital", "The page you are looking for could not be found.", "404.html") + f"""
<section class="section notfound">
  <div class="container">
    <b>404</b>
    <h2>This page could not be found.</h2>
    <p class="lead" style="margin:0 auto 28px">It may have moved, or the link may be out of date.</p>
    <div class="btn-row" style="justify-content:center"><a class="btn btn--primary" href="index.html">Back to home {ARROW}</a><a class="btn btn--ghost" href="services.html">Our services</a></div>
  </div>
</section>
""" + footer()
write("404.html", notfound)
PAGES.remove("404.html")

# remove retired sample article if present
if os.path.exists(os.path.join(ROOT, "article.html")):
    os.remove(os.path.join(ROOT, "article.html"))

# ============================================================== SEO FILES
sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for p in PAGES:
    sitemap.append(f"  <url><loc>{SITE_URL}/{'' if p == 'index.html' else p}</loc></url>")
sitemap.append("</urlset>")
write("sitemap.xml", "\n".join(sitemap) + "\n")
write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
write("site.webmanifest", json.dumps({
    "name": "MZE Digital", "short_name": "MZE Digital", "start_url": "/", "display": "standalone",
    "background_color": "#FFFFFF", "theme_color": "#2E3033",
    "icons": [{"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
              {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2) + "\n")
print(f"Built {len(PAGES) + 1} pages, sitemap.xml, robots.txt and site.webmanifest.")
