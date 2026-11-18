# MZE Digital — website

Company website for **MZE Digital (Pvt) Limited** — data science, data analytics and software development for finance and capital markets.
Live domain: **www.mzedigital.com**

Plain HTML, CSS and JavaScript. No framework and no npm install. A small Python script (`build.py`) generates every page from one file.

---

## Quick start (VS Code)

1. **Clone** the repo: `Ctrl+Shift+P` → *Git: Clone* → `https://github.com/ErtizaAbbas/MZE_Web`
2. Accept the **recommended extensions** prompt (Live Server, Python, Prettier, EditorConfig).
3. **Preview:** right-click `index.html` → *Open with Live Server*. The page reloads as you edit.
4. **Edit content:** open `build.py`, change text, then run `Ctrl+Shift+B` (*Build site*) — or in the terminal:

   ```bash
   python build.py      # Windows: py build.py
   ```

5. **Publish:** Source Control panel → write a message → *Commit* → *Sync/Push*.

> Edit `build.py`, not the `.html` files. The HTML is regenerated on every build, so direct edits to it are overwritten.

---

## Project structure

```
build.py                 ← ALL page content + templates (edit this)
index.html  services.html  products.html  projects.html
about.html  team.html  blog.html  article.html  contact.html  404.html   ← generated
sitemap.xml  robots.txt  site.webmanifest                                  ← generated
assets/
  css/style.css          design tokens (CSS variables) + all components
  js/main.js             sticky header, mobile menu, scroll reveal, filters, forms, year
  fonts/                 Montserrat 300–700 (self-hosted woff2)
  img/                   logos (dark/light), mark, favicon set, og-image.png
.vscode/                 recommended extensions, build + preview tasks
.github/workflows/       optional GitHub Pages deployment
```

## Common edits — all in `build.py`

| What | Where |
|---|---|
| Email address (contact page, footer, structured data) | `EMAIL = ""` at the top |
| Contact form delivery | `FORM_ENDPOINT = ""` — e.g. a free [Formspree](https://formspree.io) endpoint |
| Newsletter box / Substack link | `NEWSLETTER_ENDPOINT`, `SUBSTACK_URL` |
| Services (home cards, Services page, footer, contact dropdown) | `SERVICES` list |
| Sectors, tech stack | `SECTORS`, `STACK` |
| Projects | `PROJECTS` list |
| Blog cards | `POSTS` list (article body is in the `ARTICLE` section) |
| Team | `TEAM` section (placeholder cards are marked `TEMPLATE`) |

Colours and spacing live as CSS variables at the top of `assets/css/style.css`.

## Brand rules

- Use the **original MZE logo shapes** as supplied (files in `assets/img/`). Brand v1.1: only the **Z is gold** (`#C9A54E`), in the mark and in the "MZE" wordmark. Do not redraw or restyle it.
- Palette: Ink `#16171A`, Charcoal `#2E3033`, Graphite `#5A5D62`, Muted `#7D8086`, Line `#E4E4E0`, Paper `#F4F4F2`, **Gold accent `#C9A54E`** (`--gold`).
- Use gold sparingly: eyebrow dashes, the current nav item, ticks and icons on dark sections, chart lines. Never for body text on white (too little contrast).
- Montserrat only. The slanted parallel-line motif (−60°) comes from the logo's double strokes.
- Publishing brand is **MZE Digital**.
- No invented testimonials, client names, email addresses or statistics.

## Deploying

The site is static, so any static host works (GitHub Pages, Netlify, Cloudflare Pages, Vercel).

**GitHub Pages (workflow included):**
1. GitHub repo → *Settings* → *Pages* → *Source*: **GitHub Actions**.
2. Push to `main`. The workflow in `.github/workflows/pages.yml` builds and deploys.
3. Custom domain: add a file named `CNAME` containing `www.mzedigital.com`, then set the DNS at your registrar:
   - `www` → CNAME → `ertizaabbas.github.io`
   - apex `mzedigital.com` → A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
4. In *Settings → Pages*, tick **Enforce HTTPS** once the certificate is issued.

## Still to do

- [ ] Add email address(es) → `EMAIL`
- [ ] Connect the contact form → `FORM_ENDPOINT`
- [ ] Replace the 3 placeholder team cards; add Ertiza's photo
- [ ] Replace sample blog posts with real articles (or link to Search 4 Research)
- [ ] Real book covers, KSE Sentinel screenshots, purchase links
- [ ] Privacy policy and terms pages; analytics if wanted
- [ ] Choose a host and point the domain

© MZE Digital (Pvt) Limited
