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
EMAIL = ""              # e.g. "info@mzedigital.com" — leave empty until confirmed; it then appears site-wide
FORM_ENDPOINT = ""      # e.g. "https://formspree.io/f/xxxxxxx" — empty = front-end confirmation only
NEWSLETTER_ENDPOINT = ""  # optional form endpoint for the newsletter box
SUBSTACK_URL = ""       # e.g. "https://<your-publication>.substack.com" — adds a "Read on Substack" link

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
        <p style="max-width:330px">Data science, data analytics and software development for finance and capital markets. Registered with SECP &amp; FBR, Pakistan.</p>
      </div>
      <div>
        <h4>Services</h4>
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

def cta(title="Let’s turn your data into an edge.",
        text="Whether you need a model, a dashboard or a production platform, start with a conversation about the decision you are trying to make."):
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
SERVICES = [
  {"id": "data-science", "icon": "spark", "short": "Data science & ML", "title": "Data Science & Machine Learning",
   "lead": "Predictive models built for financial data: noisy, non-stationary and expensive to get wrong.",
   "body": "We design, validate and document models that forecast returns, volatility and risk, and we test them the way markets will: out of sample, walk-forward, with realistic costs.",
   "items": ["Return, volatility and risk forecasting", "Regression and regularised models (OLS, Ridge)", "Feature engineering from price, volume and macro data", "Walk-forward and out-of-sample validation"],
   "deliverables": ["Validated models", "Research notebooks", "Model documentation"]},
  {"id": "data-analytics", "icon": "bars", "short": "Data analytics & BI", "title": "Data Analytics & Business Intelligence",
   "lead": "Clear, decision-ready views of markets, portfolios and business performance.",
   "body": "From one-off analysis to always-on dashboards, we turn raw market and business data into reporting that leadership, desks and clients can act on.",
   "items": ["Portfolio and performance analytics", "Market breadth, sector rotation and heatmaps", "KPI dashboards and automated reports", "Ad-hoc analysis and research support"],
   "deliverables": ["Interactive dashboards", "Automated reports", "Analysis packs"]},
  {"id": "financial-software", "icon": "code", "short": "Financial software", "title": "Software Development for Finance",
   "lead": "Institutional-grade platforms, APIs and tools for trading, research and risk.",
   "body": "We build and maintain production software for finance, from multi-tenant analytics platforms to focused internal tools, with the same engineering behind KSE Sentinel.",
   "items": ["Trading and analytics platforms", "Multi-tenant SaaS with isolated client workspaces", "APIs and integrations (Python, FastAPI)", "Alert engines, watchlists and position-sizing tools"],
   "deliverables": ["Production software", "APIs", "Maintenance & support"]},
  {"id": "data-engineering", "icon": "db", "short": "Data engineering", "title": "Data Engineering & Market Data",
   "lead": "Reliable pipelines that deliver clean, timely market data without manual work.",
   "body": "Good models start with good data. We automate collection, cleaning and storage so analysts spend their time on analysis, not on copying files.",
   "items": ["Automated end-of-day data ingestion", "Report and PDF extraction into structured data", "Data cleaning, validation and quality checks", "Scheduled jobs and queryable data stores"],
   "deliverables": ["Data pipelines", "Clean datasets", "Runbooks"]},
  {"id": "quant-research", "icon": "flask", "short": "Quant research & backtesting", "title": "Quantitative Research & Backtesting",
   "lead": "Systematic strategy research for capital markets, with every real-world cost counted.",
   "body": "We research, test and stress-test systematic strategies across equities, indices, FX, commodities and crypto, and report results you can trust.",
   "items": ["Signal research (trend, momentum, mean reversion)", "Broker-friction-adjusted backtesting", "ATR-based risk and position sizing", "Robustness and cost stress tests"],
   "deliverables": ["Strategy research reports", "Backtest frameworks", "Signal libraries"]},
  {"id": "advisory", "icon": "compass", "short": "Capital markets advisory", "title": "Capital Markets & Strategy Advisory",
   "lead": "Macro, market and geopolitical analysis for organisations making high-stakes decisions.",
   "body": "We combine quantitative evidence with macro and strategic analysis to give leadership teams a structured view of markets, risks and scenarios.",
   "items": ["Macro and market outlooks", "Geopolitical risk modelling and scenarios", "Data and analytics strategy", "Executive briefings"],
   "deliverables": ["Briefing packs", "Scenario frameworks", "Data strategy roadmaps"]},
]

SECTORS = [("bank", "Brokerages & securities firms", "Market monitoring, client analytics and research tools."),
           ("briefcase", "Asset & fund managers", "Portfolio analytics, risk models and systematic research."),
           ("scale", "Banks & treasury teams", "Market data pipelines, reporting and scenario analysis."),
           ("rocket", "Fintech companies", "Product engineering, data infrastructure and analytics."),
           ("chart", "Traders & investment teams", "Signals, backtesting and position-sizing tools."),
           ("compass", "Corporate & strategy teams", "Macro, market and geopolitical briefings.")]

STACK = [("Languages & data", ["Python", "pandas", "NumPy", "SciPy", "SQL"]),
         ("Modelling", ["OLS & Ridge regression", "Walk-forward validation", "Out-of-sample testing", "Scenario analysis"]),
         ("Platforms & APIs", ["FastAPI", "Multi-tenant architecture", "Automated EOD ingestion", "Alert engines"]),
         ("Visualisation", ["Streamlit", "Plotly", "Interactive dashboards", "Automated reporting"])]

def services_cards():
    out = []
    for i, s in enumerate(SERVICES):
        lis = "".join(f"<li>{x}</li>" for x in s["items"][:3])
        out.append(f'<a class="card hover reveal" href="services.html#{s["id"]}"><span class="card-num">0{i+1}</span>'
                   f'<div class="icon-box">{icon(s["icon"])}</div><h3>{s["title"]}</h3><p>{s["lead"]}</p>'
                   f'<ul class="ticks">{lis}</ul><span class="link-arrow">Learn more {ARROW}</span></a>')
    return '<div class="grid grid-3">' + "".join(out) + "</div>"

def stack_table():
    return '<div class="stack-table reveal">' + "".join(
        f'<div><h4>{h}</h4><ul>{"".join(f"<li>{x}</li>" for x in xs)}</ul></div>' for h, xs in STACK) + "</div>"

MODULES = [("eye", "Watchlist manager", "Track tickers, sectors and custom baskets in one view."),
           ("bell", "Alert engine", "Rule-based price, volume and signal alerts."),
           ("grid", "Sector heatmap", "Instant read of breadth and sector rotation."),
           ("globe", "Macro overlay", "Rates, FX and macro context beside price action."),
           ("calendar", "Earnings calendar", "Upcoming results and corporate events."),
           ("scale", "Position sizer", "Risk-based sizing for every trade idea.")]

def modules_html():
    return '<div class="module-grid">' + "".join(
        f'<div class="module">{icon(ic)}<div><b>{t}</b><span>{d}</span></div></div>' for ic, t, d in MODULES) + "</div>"

def terminal():
    random.seed(7)
    shades = ["#5A5D62", "#6B6E72", "#8E9196", "#B7BABE", "#D9DAD8", "#4A4D52", "#3E4145", "#F0EFEB"]
    heat = "".join(f'<i style="background:{random.choice(shades)}"></i>' for _ in range(24))
    return f"""<div class="terminal" role="img" aria-label="Illustrative KSE Sentinel dashboard">
  <div class="terminal-bar"><i></i><i></i><i></i><span>KSE SENTINEL</span></div>
  <div class="terminal-body">
    <div class="t-row">
      <div class="t-kpi"><small>Watchlist</small><b>24</b><em>symbols tracked</em></div>
      <div class="t-kpi"><small>Alerts</small><b>6</b><em>triggered today</em></div>
      <div class="t-kpi"><small>Breadth</small><b>62%</b><em>advancing</em></div>
    </div>
    <div class="t-chart"><span class="t-caption">Index trend · illustrative</span>
      <svg viewBox="0 0 300 120" preserveAspectRatio="none">
        <defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C9A54E" stop-opacity=".28"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>
        <path d="M0 92 L20 86 L40 90 L60 74 L80 78 L100 62 L120 66 L140 52 L160 58 L180 44 L200 48 L220 34 L240 40 L260 26 L280 30 L300 18 L300 120 L0 120Z" fill="url(#g)"/>
        <path d="M0 92 L20 86 L40 90 L60 74 L80 78 L100 62 L120 66 L140 52 L160 58 L180 44 L200 48 L220 34 L240 40 L260 26 L280 30 L300 18" fill="none" stroke="#C9A54E" stroke-width="2"/>
        <path d="M0 100 L50 92 L100 80 L150 70 L200 60 L250 48 L300 38" fill="none" stroke="#8E9196" stroke-width="1.5" stroke-dasharray="4 4"/>
      </svg>
    </div>
    <div><span class="t-caption">Sector heatmap · illustrative</span><div class="t-heat">{heat}</div></div>
  </div>
</div>"""

def lab_panel():
    """Hero visual: an illustrative research notebook (code + equity curve)."""
    return f"""<div class="terminal" role="img" aria-label="Illustrative research notebook: walk-forward model validation">
  <div class="terminal-bar"><i></i><i></i><i></i><span>RESEARCH · WALK-FORWARD</span></div>
  <div class="terminal-body">
<div class="t-code"><span class="c"># illustrative</span>
<span class="k">for</span> train, test <span class="k">in</span> walk_forward(data, window=252):
    model = Ridge(alpha=1.0).fit(X[train], y[train])
    signal = model.predict(X[test])
    pnl += backtest(signal, costs=broker_friction)</div>
    <div class="t-chart"><span class="t-caption">Net equity after costs · illustrative</span>
      <svg viewBox="0 0 300 110" preserveAspectRatio="none">
        <defs><linearGradient id="g2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C9A54E" stop-opacity=".26"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>
        <path d="M0 90 L25 84 L50 86 L75 72 L100 75 L125 60 L150 64 L175 50 L200 54 L225 40 L250 44 L275 28 L300 24 L300 110 L0 110Z" fill="url(#g2)"/>
        <path d="M0 90 L25 84 L50 86 L75 72 L100 75 L125 60 L150 64 L175 50 L200 54 L225 40 L250 44 L275 28 L300 24" fill="none" stroke="#C9A54E" stroke-width="2"/>
        <path d="M0 92 L50 88 L100 82 L150 78 L200 72 L250 68 L300 62" fill="none" stroke="#8E9196" stroke-width="1.5" stroke-dasharray="4 4"/>
      </svg>
    </div>
    <div class="t-row">
      <div class="t-kpi"><small>Validation</small><b>Walk-fwd</b><em>out of sample</em></div>
      <div class="t-kpi"><small>Costs</small><b>Included</b><em>spread · fees · slip</em></div>
      <div class="t-kpi"><small>Data</small><b>EOD</b><em>automated</em></div>
    </div>
  </div>
</div>"""

POSTS = [
  ("pat-1", "Quant Research", "research", "Why broker friction belongs in every backtest", "Spreads, commissions and slippage quietly turn winning strategies into losing ones. Here is how to model them honestly.", "12 min read"),
  ("pat-4", "Data Science", "data-science", "Walk-forward validation for financial models", "Why a single train/test split flatters a model, and how rolling validation gives a more honest picture.", "10 min read"),
  ("pat-3", "Data Engineering", "engineering", "Automating end-of-day market data pipelines", "From daily PDF reports to a clean, queryable database, without manual uploads.", "8 min read"),
  ("pat-2", "Analytics", "analytics", "Reading market breadth with a sector heatmap", "A compact way to see participation and rotation beneath the headline index.", "7 min read"),
  ("pat-6", "Markets", "markets", "Trend and momentum: what still works, and why", "Revisiting the evidence for systematic trend following across asset classes.", "10 min read"),
  ("pat-5", "Macro", "macro", "Modelling geopolitical risk as a portfolio input", "Turning qualitative events into quantitative scenarios that a risk model can actually use.", "11 min read"),
]
def chartline(light=True):
    c = "#ffffff" if light else "#2E3033"
    return (f'<svg class="chartline" viewBox="0 0 300 100" preserveAspectRatio="none"><path d="M0 80 L30 72 L60 76 L90 58 L120 62 '
            f'L150 44 L180 50 L210 30 L240 36 L270 18 L300 22" fill="none" stroke="{c}" stroke-opacity=".55" stroke-width="2"/></svg>')

def post_card(p):
    pat, cat, key, title, ex, rt = p
    light = pat not in ("pat-3", "pat-5")
    return f"""<a class="card post-card reveal" href="article.html" data-cat="{key}">
  <div class="post-thumb"><div class="pattern {pat}"></div>{chartline(light)}<div class="cat"><span class="tag">{cat}</span></div></div>
  <div class="post-body"><div class="post-meta">Ertiza Abbas &nbsp;·&nbsp; {rt}</div><h3>{title}</h3><p>{ex}</p><span class="link-arrow">Read article {ARROW}</span></div>
</a>"""

BOOKS = [("", "STRATEGIC STUDIES", "The Empire", "Strategic studies and the Strategic Dominance Formula."),
         ("v2", "MACROECONOMICS", "The Global Economy", "A structured view of the forces shaping the world economy."),
         ("v3", "LETTERS", "When You Need Me", "Letters to a daughter. ISBN 9789819445387."),
         ("v4", "NON-FICTION", "Witness", "Published 2025.")]
def books_html():
    return '<div class="grid grid-4">' + "".join(
        f'<div class="book reveal"><div class="book-cover {v}"><small>{k}</small><b>{t}</b><small>ERTIZA ABBAS</small></div><div><h4>{t}</h4><p>{d}</p></div></div>'
        for v, k, t, d in BOOKS) + "</div>"

PROJECTS = [
  ("software", "pat-1", True, "Platform", "KSE Sentinel", "Institutional, multi-tenant quantitative trading and analytics engine for the Pakistan Stock Exchange, with six core modules and automated end-of-day data ingestion.", ["FastAPI", "Python", "Multi-tenant"]),
  ("data-science research analytics", "pat-4", True, "Quant Engine", "Multi-Asset Alpha Engine", "Dual EMA/RSI signals, ATR-based risk, OLS and Ridge next-day prediction, walk-forward validation and friction-adjusted backtesting across US30, US100, GER40, Gold, GBPJPY and BTC, with a five-tab Streamlit dashboard.", ["Python", "Plotly", "Streamlit"]),
  ("research", "pat-6", True, "Open Source", "Trend & Momentum Engine", "A systematic trend and momentum research framework, published openly on GitHub.", ["Python", "pandas", "NumPy"]),
  ("research data-science", "pat-2", True, "Research", "Geopolitical Risk Modelling", "Structured models that convert strategic and geopolitical analysis into scenario inputs for portfolio and policy decisions.", ["SciPy", "Scenario analysis"]),
  ("publishing", "pat-5", False, "Publishing", "The Empire & The Global Economy", "Two 2025 books on strategic studies and macroeconomics, including the Strategic Dominance Formula D = (M + A) × C^w.", ["Strategy", "Macroeconomics"]),
  ("publishing", "pat-3", False, "Translation", "Then I Was Guided (Korean edition)", "Korean translation and editorial work on 그때 나는 인도되었노라, published in Seoul.", ["Korean", "Editorial"]),
]
def project_card(p, link=False):
    cat, pat, light, tag, t, d, st = p
    el = "a" if link else "div"
    href = ' href="projects.html"' if link else ""
    return (f'<{el} class="card project reveal" data-cat="{cat}"{href}><div class="post-thumb"><div class="pattern {pat}"></div>{chartline(light)}</div>'
            f'<div class="project-body"><div class="tags"><span class="tag">{tag}</span></div><h3>{t}</h3><p>{d}</p>'
            f'<div class="stack">{"".join(f"<span>{s}</span>" for s in st)}</div></div></{el}>')

ORG_JSONLD = {
  "@context": "https://schema.org", "@type": "Organization", "name": "MZE Digital (Pvt) Limited", "alternateName": "MZE Digital",
  "url": SITE_URL, "logo": SITE_URL + "/assets/img/icon-512.png",
  "description": "Data science, data analytics and software development for finance and capital markets.",
  "address": {"@type": "PostalAddress", "streetAddress": "Suite #408, 4th Floor, Silver Trade Tower, Off JS Bank, Block 13-A, Gulshan-e-Iqbal",
              "addressLocality": "Karachi", "postalCode": "75300", "addressCountry": "PK"},
  "telephone": "+92-313-0721042",
  "founder": {"@type": "Person", "name": "Ertiza Abbas", "jobTitle": "Founder & CEO", "sameAs": list(LINKS.values())},
}
if EMAIL:
    ORG_JSONLD["email"] = EMAIL

# ============================================================== HOME
home = head("MZE Digital — Data Science, Analytics & Software for Finance",
            "MZE Digital builds predictive models, analytics and institutional-grade software for finance and capital markets.",
            "index.html", f'<script type="application/ld+json">{json.dumps(ORG_JSONLD, ensure_ascii=False)}</script>\n') + f"""
<section class="hero">
  <div class="stripes"></div>
  <div class="container hero-grid">
    <div class="reveal">
      <span class="eyebrow">Data science · Analytics · Financial software</span>
      <h1>Data and software for <em>finance and capital markets.</em></h1>
      <p class="lead">MZE Digital designs predictive models, analytics and production-grade platforms for trading, investment and finance teams, built on two decades of market, economic and data experience.</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="services.html">Explore our services {ARROW}</a>
        <a class="btn btn--ghost" href="products.html">See KSE Sentinel</a>
      </div>
      <div class="hero-meta">
        <div><strong>Data science</strong>Models &amp; research</div>
        <div><strong>Analytics</strong>Dashboards &amp; BI</div>
        <div><strong>Software</strong>Platforms &amp; data</div>
      </div>
    </div>
    <div class="hero-visual reveal">
      {lab_panel()}
      <div class="float-card"><div class="ic">{icon("shield")}</div><div><b>Tested before it ships</b><span>Out of sample · costs included</span></div></div>
    </div>
  </div>
</section>

<section class="section--tight" style="padding-top:0">
  <div class="container">
    <div class="facts reveal">
      <div class="fact"><b>20+</b><span>Years across strategy, business development and analytics</span></div>
      <div class="fact"><b>6</b><span>Core modules in our flagship KSE Sentinel platform</span></div>
      <div class="fact"><b>80+</b><span>Students mentored worldwide in trading and investment</span></div>
      <div class="fact"><b>3</b><span>Cities: Singapore, Seoul and Karachi</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split-head">
      <div class="section-head reveal"><span class="eyebrow">Services</span><h2>From raw data to decisions, models and software.</h2></div>
      <a class="link-arrow reveal" href="services.html">All services {ARROW}</a>
    </div>
    {services_cards()}
  </div>
</section>

<section class="section section--dark" style="position:relative;overflow:hidden">
  <div class="container feature">
    <div class="reveal">
      <span class="eyebrow">Flagship product</span>
      <h2>KSE Sentinel</h2>
      <p class="lead">An institutional, multi-tenant quantitative trading and analytics platform for the Pakistan Stock Exchange, built on a modern Python and FastAPI stack.</p>
      {modules_html()}
      <div class="btn-row"><a class="btn btn--light" href="products.html">See the platform {ARROW}</a><a class="btn btn--outline-light" href="contact.html">Request a demo</a></div>
    </div>
    <div class="reveal hide-mobile">{terminal()}</div>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    <div class="section-head center reveal"><span class="eyebrow">Who we build for</span><h2>Made for finance and capital markets</h2><p class="lead">Our work is shaped by the realities of markets: noisy data, real trading costs, tight deadlines and regulated environments.</p></div>
    <div class="grid grid-3">
      {''.join(f'<div class="card reveal"><div class="icon-box">{icon(ic)}</div><h3>{t}</h3><p>{d}</p></div>' for ic, t, d in SECTORS)}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center reveal"><span class="eyebrow">How we work</span><h2>From question to working system</h2><p class="lead">Every engagement follows the same disciplined path, whether the output is a model, a dashboard or production software.</p></div>
    <div class="steps">
      <div class="step reveal"><h4>Discover</h4><p>Define the decision, the data available and what success looks like.</p></div>
      <div class="step reveal"><h4>Model</h4><p>Build and test the analysis out of sample, with real-world costs included.</p></div>
      <div class="step reveal"><h4>Build</h4><p>Turn validated models into reliable pipelines, dashboards and platforms.</p></div>
      <div class="step reveal"><h4>Enable</h4><p>Train your people to use, question and extend what we deliver.</p></div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Technology</span><h2>A proven, open stack</h2><p class="lead">We work in widely used, well-supported tools, so what we build is easy for your team to own.</p></div>
    {stack_table()}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split-head">
      <div class="section-head reveal"><span class="eyebrow">Selected work</span><h2>Research that ships.</h2></div>
      <a class="link-arrow reveal" href="projects.html">All projects {ARROW}</a>
    </div>
    <div class="grid grid-3">{''.join(project_card(p, True) for p in PROJECTS[1:4])}</div>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    <div class="split-head">
      <div class="section-head reveal"><span class="eyebrow">Insights</span><h2>Latest thinking</h2></div>
      <a class="link-arrow reveal" href="blog.html">View all articles {ARROW}</a>
    </div>
    <div class="grid grid-3">{''.join(post_card(p) for p in POSTS[:3])}</div>
  </div>
</section>
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
services = head("Services — MZE Digital", "Data science, data analytics, financial software development, data engineering, quantitative research and capital markets advisory.", "services.html") + page_hero(
  "Services", "What we do", "Data science, analytics and software for finance.",
  "Six connected services that take you from raw market and business data to tested models, clear analytics and production software.",
  '<div class="svc-index">' + "".join(f'<a href="#{s["id"]}">{s["short"]}</a>' for s in SERVICES) + "</div>") + f"""
<section class="section">
  <div class="container">{svc_rows}
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Who we build for</span><h2>Built around how finance works</h2></div>
    <div class="grid grid-3">
      {''.join(f'<div class="sector reveal">{icon(ic)}<h4>{t}</h4><p>{d}</p></div>' for ic, t, d in SECTORS)}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Engagement models</span><h2>Work with us the way that suits you</h2></div>
    <div class="grid grid-3">
      <div class="card reveal"><div class="icon-box">{icon("target")}</div><h3>Project</h3><p>A defined scope and outcome: a model, a dashboard, a pipeline or a platform module.</p></div>
      <div class="card reveal"><div class="icon-box">{icon("layers")}</div><h3>Ongoing partnership</h3><p>A standing data, analytics and engineering capability that develops and maintains your systems over time.</p></div>
      <div class="card reveal"><div class="icon-box">{icon("users")}</div><h3>Training &amp; enablement</h3><p>Programmes that help your team use, question and extend what we build. <a class="link-arrow" href="products.html#training">See programmes</a></p></div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Technology</span><h2>Our stack</h2></div>
    {stack_table()}
  </div>
</section>
""" + cta("Tell us what you need to decide, measure or build.", "We will come back with a clear plan, scope and next steps.") + footer()
write("services.html", services)

# ============================================================== ABOUT
about = head("About — MZE Digital", "MZE Digital (Pvt) Limited: data science, analytics and software development for finance, registered with SECP and FBR.", "about.html") + page_hero(
  "About", "Company", "Rigorous analysis, practical delivery.",
  "MZE Digital (Pvt) Limited is a data science, analytics and software company for finance and capital markets, registered with the SECP and FBR in Pakistan and operating across Singapore, Seoul and Karachi.") + f"""
<section class="section">
  <div class="container feature">
    <div class="reveal">
      <span class="eyebrow">Who we are</span>
      <h2>Built on two decades of market and data experience.</h2>
      <p>MZE Digital was founded by Ertiza Abbas, a quantitative data and macro strategic analyst with 20 years of experience across business development, economic strategy and analytics.</p>
      <p>We exist to close the gap between analysis and action: to turn market and business data into tested models, clear analytics and dependable software. Alongside our core data and software work, we offer coaching, professional training and publishing.</p>
      <div class="btn-row" style="margin-top:28px"><a class="btn btn--primary" href="services.html">Our services {ARROW}</a><a class="btn btn--ghost" href="team.html">Meet the team</a></div>
    </div>
    <div class="reveal">
      <div class="grid grid-2">
        <div class="card"><div class="icon-box">{icon("target")}</div><h4>Mission</h4><p>Give finance teams quantitative clarity through data science, analytics and software.</p></div>
        <div class="card"><div class="icon-box">{icon("spark")}</div><h4>Vision</h4><p>Institutions that decide with clean data, tested models and well-trained teams.</p></div>
        <div class="card"><div class="icon-box">{icon("layers")}</div><h4>Approach</h4><p>Evidence first: out-of-sample testing, real-world costs and transparent assumptions.</p></div>
        <div class="card"><div class="icon-box">{icon("shield")}</div><h4>Integrity</h4><p>Neutral, consistent analysis, with the same standard applied to every market and state.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    <span class="eyebrow reveal">Our principle</span>
    <p class="quote reveal">Good analysis is not the most complicated model. It is the <b>honest</b> one: tested out of sample, with every real-world cost counted.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">What we offer</span><h2>Our services</h2></div>
    {services_cards()}
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Where we work</span><h2>Three cities, one team.</h2></div>
    <div class="grid grid-3">
      <div class="office reveal"><small>Head office</small><h3>Karachi</h3><p>Suite #408, 4th Floor, Silver Trade Tower, Off JS Bank, Block 13-A, Gulshan-e-Iqbal, Karachi 75300</p></div>
      <div class="office reveal"><small>Regional</small><h3>Singapore</h3><p>Research, analytics and client advisory for Southeast Asia.</p></div>
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
  "A focused team of data scientists, engineers and analysts, led by two decades of experience in markets, strategy and data.") + f"""
<section class="section">
  <div class="container leader">
    <!-- To add a photo: place it in assets/img/ and add <img src="assets/img/ertiza.jpg" alt="Ertiza Abbas"> inside .avatar -->
    <div class="avatar dark reveal"><span>EA</span></div>
    <div class="reveal">
      <span class="eyebrow">Founder &amp; CEO</span>
      <h2>Ertiza Abbas</h2>
      <p class="lead">Quantitative Data &amp; Macro Strategic Analyst, published author and macro strategist.</p>
      <p>Ertiza brings 20 years of experience spanning business development, economic strategy and analytics. His work combines data science and data engineering with macro and geopolitical analysis, from systematic alpha engines and friction-adjusted backtesting to geopolitical risk modelling. He is the principal architect of KSE Sentinel and works in English and Urdu across Singapore, Seoul and Karachi.</p>
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
    <div class="section-head reveal"><span class="eyebrow">The team</span><h2>Data scientists, engineers and analysts</h2></div>
    <!-- TEMPLATE: replace each card below with a real team member (photo: put an <img> inside .avatar) -->
    <div class="grid grid-3">
      <div class="person reveal"><div class="avatar"><span>DS</span></div><h3>Team member name</h3><span class="role">Data Scientist</span><p>Short bio: background, focus areas and what they bring to clients.</p></div>
      <div class="person reveal"><div class="avatar"><span>SE</span></div><h3>Team member name</h3><span class="role">Software Engineer</span><p>Short bio: background, focus areas and what they bring to clients.</p></div>
      <div class="person reveal"><div class="avatar"><span>DA</span></div><h3>Team member name</h3><span class="role">Data Analyst</span><p>Short bio: background, focus areas and what they bring to clients.</p></div>
    </div>
    <p class="placeholder-note">Template note: these three cards are placeholders. Replace them with your team members' names, roles, bios and photos, or remove the section.</p>
  </div>
</section>

<section class="section">
  <div class="container feature">
    <div class="reveal"><span class="eyebrow">Careers</span><h2>Work with us</h2><p class="lead">We are always interested in people who combine curiosity with rigour: data scientists, data engineers, quantitative developers and analysts.</p></div>
    <div class="reveal"><div class="btn-row" style="justify-content:flex-end"><a class="btn btn--primary" href="contact.html">Send your profile {ARROW}</a></div></div>
  </div>
</section>
""" + footer()
write("team.html", team)

# ============================================================== PROJECTS
projects = head("Projects — MZE Digital", "Selected software, data science and research projects by MZE Digital.", "projects.html") + page_hero(
  "Projects", "Our work", "Selected projects",
  "Financial software, data science and quantitative research, plus our publishing work, each built to the same standard of evidence.") + f"""
<section class="section">
  <div class="container">
    <div class="split-head reveal">
      <p class="muted" style="margin:0">Filter by discipline</p>
      <div class="filters">
        <button class="filter active" data-filter="all">All</button>
        <button class="filter" data-filter="software">Software</button>
        <button class="filter" data-filter="data-science">Data science</button>
        <button class="filter" data-filter="analytics">Analytics</button>
        <button class="filter" data-filter="research">Research</button>
        <button class="filter" data-filter="publishing">Publishing</button>
      </div>
    </div>
    <div class="grid grid-3">{''.join(project_card(p) for p in PROJECTS)}</div>
  </div>
</section>
""" + cta("Have a project in mind?", "Tell us what you are trying to decide, measure or build. We will come back with a clear plan.") + footer()
write("projects.html", projects)

# ============================================================== PRODUCTS
products = head("Products — MZE Digital", "KSE Sentinel, training programmes and publications from MZE Digital.", "products.html") + page_hero(
  "Products", "Products & programmes", "Tools and programmes for better decisions.",
  "Institutional software for the Pakistan equity market, structured training for finance professionals, and research you can read.") + f"""
<section class="section">
  <div class="container">
    <div class="product-hero-card reveal">
      <div class="stripes"></div>
      <div class="feature">
        <div>
          <span class="eyebrow">Flagship platform</span>
          <h2>KSE Sentinel</h2>
          <p class="lead">An institutional, multi-tenant quantitative trading and analytics engine for the Pakistan Stock Exchange. One secure platform for monitoring, alerts, research and risk, for multiple desks or client organisations.</p>
          <ul class="ticks">
            <li>Multi-tenant architecture with isolated client workspaces</li>
            <li>Modern FastAPI back end built for speed and integration</li>
            <li>Automated daily end-of-day data ingestion</li>
          </ul>
          <div class="btn-row" style="margin-top:28px"><a class="btn btn--light" href="contact.html">Request a demo {ARROW}</a></div>
        </div>
        <div>{terminal()}</div>
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
    <div class="section-head center reveal"><span class="eyebrow">Training &amp; mentorship</span><h2>Programmes</h2><p class="lead">Practical, evidence-based programmes for individuals and teams. Formats and fees are tailored to each engagement.</p></div>
    <div class="grid grid-3">
      <div class="card price-card reveal"><span class="tag">Individuals</span><h3>Trading &amp; Investment Mentorship</h3><p>One-to-one guidance on process, discipline and risk, drawing on 80+ students mentored worldwide.</p><ul class="ticks"><li>Personal trading plan</li><li>Risk &amp; position sizing</li><li>Ongoing review sessions</li></ul><a class="btn btn--ghost" href="contact.html">Enquire</a></div>
      <div class="card price-card featured reveal"><span class="tag">Teams</span><h3>Data Science for Finance with Python</h3><p>From spreadsheets to systematic analysis: data, modelling and honest backtesting.</p><ul class="ticks"><li>pandas, NumPy &amp; SciPy</li><li>Regression, signals &amp; out-of-sample tests</li><li>Friction-adjusted backtesting</li></ul><a class="btn btn--light" href="contact.html">Enquire</a></div>
      <div class="card price-card reveal"><span class="tag">Organisations</span><h3>Executive Data &amp; Strategy Briefings</h3><p>Focused sessions on data strategy, macro outlook and geopolitical risk for leadership teams.</p><ul class="ticks"><li>Tailored to your sector</li><li>Scenario frameworks</li><li>Written briefing pack</li></ul><a class="btn btn--ghost" href="contact.html">Enquire</a></div>
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

# ============================================================== BLOG
fp = POSTS[0]
nl_action = f' action="{NEWSLETTER_ENDPOINT}" method="POST"' if NEWSLETTER_ENDPOINT else ""
substack = f'<p style="margin-top:14px"><a class="link-arrow" href="{SUBSTACK_URL}" target="_blank" rel="noopener">Read on Substack {ARROW}</a></p>' if SUBSTACK_URL else ""
blog = head("Insights — MZE Digital", "Articles on data science, analytics, financial software, markets and macroeconomics.", "blog.html") + page_hero(
  "Insights", "Insights", "Research and commentary",
  "Data science, analytics, engineering and markets, written to be useful, not noisy.") + f"""
<section class="section">
  <div class="container">
    <a class="card featured-post reveal" href="article.html">
      <div class="post-thumb"><div class="pattern {fp[0]}"></div>{chartline()}<div class="cat"><span class="tag">Featured · {fp[1]}</span></div></div>
      <div class="post-body"><div class="post-meta">Ertiza Abbas &nbsp;·&nbsp; {fp[5]}</div><h3>{fp[3]}</h3><p>{fp[4]}</p><span class="link-arrow">Read article {ARROW}</span></div>
    </a>
    <div class="split-head reveal" style="margin-top:72px">
      <h2 style="margin:0">All articles</h2>
      <div class="filters"><button class="filter active" data-filter="all">All</button><button class="filter" data-filter="data-science">Data science</button><button class="filter" data-filter="analytics">Analytics</button><button class="filter" data-filter="engineering">Engineering</button><button class="filter" data-filter="markets">Markets</button><button class="filter" data-filter="macro">Macro</button></div>
    </div>
    <div class="grid grid-3">{''.join(post_card(p) for p in POSTS[1:])}</div>
    <p class="placeholder-note">Template note: these articles are sample content showing the layout. Replace them with your own posts, or link the cards to your Search 4 Research articles.</p>
  </div>
</section>

<section class="section section--paper">
  <div class="container feature">
    <div class="reveal"><span class="eyebrow">Newsletter</span><h2>Search 4 Research</h2><p class="lead">Join 2,000+ readers receiving research on markets, economics and data.</p>{substack}</div>
    <div class="reveal">
      <form class="newsletter" data-form{nl_action}>
        <input type="email" name="email" placeholder="Your email address" aria-label="Email address" required>
        <span class="hp" aria-hidden="true"><input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></span>
        <button class="btn btn--primary" type="submit">Subscribe</button>
        <div class="form-success">Thank you, you are on the list.</div>
        <div class="form-error">Something went wrong. Please try again.</div>
      </form>
    </div>
  </div>
</section>
""" + footer()
write("blog.html", blog)

# ============================================================== ARTICLE (template)
article = head("Why broker friction belongs in every backtest — MZE Digital", "Spreads, commissions and slippage quietly turn winning strategies into losing ones.", "article.html") + f"""
<section class="section" style="padding-bottom:0">
  <div class="container">
    <div class="article-header reveal">
      <div class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; <a href="blog.html">Insights</a> &nbsp;/&nbsp; Quant Research</div>
      <span class="tag">Quant Research</span>
      <h1 style="margin-top:18px">Why broker friction belongs in every backtest</h1>
      <div class="byline"><span class="mini">EA</span><span><b>Ertiza Abbas</b>12 min read</span></div>
    </div>
    <div class="article-cover reveal"><div class="pattern pat-1" style="position:absolute;inset:0"></div>{chartline()}</div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="container">
    <article class="article prose reveal">
      <p>Most strategies look brilliant in a backtest. Far fewer survive contact with a real brokerage account. The gap is rarely the signal itself; it is everything that happens between the signal and the fill.</p>
      <h2>The three hidden costs</h2>
      <p>Every trade pays some combination of three frictions. Leave any of them out and the equity curve is fiction.</p>
      <ul>
        <li><b>Spread</b>: the difference between the bid and the ask, paid on entry and exit.</li>
        <li><b>Commission</b>: explicit broker and exchange fees, fixed or proportional.</li>
        <li><b>Slippage</b>: the difference between the price you expected and the price you got.</li>
      </ul>
      <blockquote>A strategy that trades often and earns a little per trade is the one most exposed to friction.</blockquote>
      <h2>Modelling it honestly</h2>
      <p>The simplest robust approach is to charge a cost per round trip that reflects the instrument and the market conditions you actually trade in, then check that the result still holds out of sample.</p>
      <div class="formula">Net return = Gross return − (spread + commission + slippage)</div>
      <p>From there, stress-test: double the costs and see whether the edge survives. If it disappears, it was never an edge.</p>
      <div class="callout"><b>Template note:</b> this is sample article content showing the article layout (headings, lists, quotes, formula blocks and callouts). Replace it with your own writing.</div>
      <h3>Key takeaways</h3>
      <ul><li>Always include spread, commission and slippage.</li><li>Validate out of sample, and stress-test costs.</li><li>Prefer fewer, higher-quality trades when frictions are high.</li></ul>
      <div class="author-box"><span class="mini">EA</span><div><b>Ertiza Abbas</b><p>Founder &amp; CEO of MZE Digital. Quantitative data and macro strategic analyst, author and publisher of Search 4 Research.</p></div></div>
      <div class="article-footer"><a class="link-arrow" href="blog.html">← Back to all articles</a><a class="btn btn--primary" href="contact.html">Discuss your project {ARROW}</a></div>
    </article>
  </div>
</section>
<section class="section section--paper">
  <div class="container">
    <div class="section-head reveal"><h2>Related articles</h2></div>
    <div class="grid grid-3">{''.join(post_card(p) for p in POSTS[1:4])}</div>
  </div>
</section>
""" + footer()
write("article.html", article)

# ============================================================== CONTACT
form_action = f' action="{FORM_ENDPOINT}" method="POST"' if FORM_ENDPOINT else ""
email_item = (f'<div class="contact-item"><div class="icon-box">{icon("mail")}</div><div><small>Email</small><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>'
              if EMAIL else "<!-- Email: set EMAIL in build.py and rebuild -->")
interests = ["Data science & machine learning", "Data analytics & BI", "Financial software development", "Data engineering & market data",
             "Quantitative research & backtesting", "Capital markets & strategy advisory", "KSE Sentinel demo", "Training & mentorship", "Publishing", "Other"]
contact = head("Contact — MZE Digital", "Contact MZE Digital in Karachi or Singapore.", "contact.html") + page_hero(
  "Contact", "Get in touch", "Let’s talk about your data.",
  "A model, a dashboard, a platform or a KSE Sentinel demo: send a message or call us directly.") + f"""
<section class="section">
  <div class="container contact-grid">
    <div class="reveal">
      <div class="contact-item"><div class="icon-box">{icon("pin")}</div><div><small>Head office</small><b>{ADDRESS_HTML}</b></div></div>
      {''.join(f'<div class="contact-item"><div class="icon-box">{icon("phone")}</div><div><small>{c}</small><a href="tel:{t}">{n}</a></div></div>' for c, n, t in PHONES)}
      {email_item}
      <div class="contact-item"><div class="icon-box">{icon("link")}</div><div><small>Online</small><a href="{LINKS['LinkedIn']}" target="_blank" rel="noopener">LinkedIn</a> &nbsp;·&nbsp; <a href="{LINKS['GitHub']}" target="_blank" rel="noopener">GitHub</a></div></div>
    </div>
    <form class="form reveal" data-form{form_action}>
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
      <p class="form-note">By sending this form you agree to be contacted about your enquiry.</p>
      <div class="form-success">Thank you, your message has been received. We will be in touch.</div>
      <div class="form-error">Sorry, the message could not be sent. Please call us instead.</div>
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
