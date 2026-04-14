# SEO Audit — elyanlabs.ai

**Date**: 2026-04-14  
**Auditor**: 小米粒 🌾 (zhaog100)  
**Bounty**: #2957 (10 RTC)

---

## Executive Summary

elyanlabs.ai is a well-designed single-page site with good meta tags but **critical SEO gaps**: no sitemap.xml, no robots.txt, no canonical URLs, no structured data (JSON-LD), no blog/docs section, and missing internal linking between related projects. The site has excellent branding but near-zero discoverability for search engines.

**Overall SEO Score: ~35/100**

| Category | Score | Status |
|----------|-------|--------|
| Meta Tags | 8/10 | ✅ Good |
| Structured Data | 0/10 | ❌ Missing |
| Technical SEO | 3/10 | ❌ Critical gaps |
| Content | 4/10 | ⚠️ Thin |
| Internal Linking | 2/10 | ❌ Weak |
| Performance | 7/10 | ✅ Decent |
| Mobile | 8/10 | ✅ Good |

---

## 1. Meta Tags — Score: 8/10 ✅

**What's Good**:
- `<title>` descriptive and keyword-rich
- `<meta name="description">` present with relevant content
- Open Graph tags complete (og:title, og:description, og:image, og:type, og:url)
- Twitter Card tags present (summary_large_image)
- `<meta name="viewport">` for mobile
- `<meta name="theme-color">` set

**Issues**:
- ❌ **No canonical URL** — `<link rel="canonical">` missing. Search engines may index http/https and www/non-www as separate pages.
- ⚠️ Title is 68 chars — good, but could be more keyword-targeted for discovery.

**Fix — Add canonical**:
```html
<link rel="canonical" href="https://elyanlabs.ai">
```

---

## 2. Structured Data (JSON-LD) — Score: 0/10 ❌

**No structured data exists.** This is the single highest-impact fix.

**Fix — Add Organization schema**:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Elyan Labs",
  "url": "https://elyanlabs.ai",
  "logo": "https://elyanlabs.ai/assets/elyan_tile_1_logo.jpg",
  "description": "Private research lab for exotic-architecture LLM inference, persistent AI persona systems, and non-bijunctive attention.",
  "foundingLocation": "Lake Charles, Louisiana",
  "sameAs": [
    "https://github.com/Scottcjn",
    "https://x.com/elyanlabs"
  ],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Projects",
    "itemListElement": [
      {
        "@type": "SoftwareApplication",
        "name": "RustChain",
        "description": "Hardware-fingerprinted blockchain with Proof of Antiquity consensus",
        "url": "https://github.com/Scottcjn/Rustchain"
      },
      {
        "@type": "SoftwareApplication",
        "name": "BoTTube",
        "description": "AI-native video platform",
        "url": "https://bottube.ai"
      }
    ]
  }
}
</script>
```

**Fix — Add WebSite schema for sitelinks**:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Elyan Labs",
  "url": "https://elyanlabs.ai"
}
</script>
```

---

## 3. Technical SEO — Score: 3/10 ❌

### 3.1 Missing sitemap.xml ❌

`https://elyanlabs.ai/sitemap.xml` returns 404.

**Fix — Create sitemap.xml**:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://elyanlabs.ai/</loc>
    <lastmod>2026-04-12</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://elyanlabs.ai/contact.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://elyanlabs.ai/vintage-voice.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
</urlset>
```

### 3.2 Missing robots.txt ❌

`https://elyanlabs.ai/robots.txt` returns 404.

**Fix — Create robots.txt**:
```
User-agent: *
Allow: /
Sitemap: https://elyanlabs.ai/sitemap.xml
```

### 3.3 No canonical URLs ❌

Every page should declare its canonical URL to prevent duplicate content issues.

### 3.4 Security Headers ⚠️

Present and good:
- ✅ `X-Frame-Options: SAMEORIGIN`
- ✅ `X-Content-Type-Options: nosniff`
- ✅ `Referrer-Policy: no-referrer-when-downgrade`

Missing:
- ⚠️ `Content-Security-Policy` — no CSP header
- ⚠️ `Strict-Transport-Security` — no HSTS (HTTPS is used but not enforced)

---

## 4. Content Gaps — Score: 4/10 ⚠️

### 4.1 Missing Pages

| Page | Priority | Why Needed |
|------|----------|------------|
| `/about` | HIGH | Trust signal for visitors and search engines |
| `/team` | HIGH | Currently inline — should be separate page with more detail |
| `/blog` | CRITICAL | No indexable content beyond the landing page |
| `/docs` | HIGH | Technical documentation for RustChain, Beacon, etc. |
| `/roadmap` | MEDIUM | Shows project maturity and future plans |
| `/projects` | HIGH | Dedicated page for RustChain, BoTTube, Beacon, TrashClaw |
| `/contributions` | HIGH | Showcase 44+ upstream PRs (OpenSSL, Ghidra, vLLM, etc.) |

### 4.2 Missing Credibility Signals

The site does NOT mention:
- ❌ **44+ upstream PRs** to OpenSSL, Ghidra, vLLM, LLVM, PyTorch, CPython, wolfSSL
- ❌ **CVPR 2026 paper** (only mentioned in meta description, not visible in body)
- ❌ **GitHub stars/impact metrics** for projects
- ❌ **Specific hardware** supported (PowerPC G4/G5, POWER8, N64, etc.)

These are massive trust signals that should be prominently displayed.

### 4.3 Keyword Opportunities

| Target Keyword | Monthly Volume (est.) | Current Ranking |
|----------------|-----------------------|-----------------|
| Proof of Antiquity | Low | Not ranking |
| vintage computing blockchain | Low | Not ranking |
| AI agent economy | Medium | Not ranking |
| hardware attestation | Medium | Not ranking |
| DePIN blockchain | High | Not ranking |
| exotic architecture LLM | Low | Not ranking |
| PowerPC AI inference | Low | Not ranking |
| RustChain | Brand | Not ranking |

**Strategy**: Start with low-competition niche terms (Proof of Antiquity, vintage computing blockchain) and build authority before targeting broader terms (DePIN, AI agents).

---

## 5. Internal Linking — Score: 2/10 ❌

**Current state**: The site has only internal anchor links (#research, #accomplishments) and external links to GitHub/Bottube.

**Critical gaps**:
- ❌ No links between RustChain ↔ BoTTube ↔ Beacon ↔ TrashClaw projects
- ❌ No "Related Projects" section
- ❌ No cross-linking from accomplishments to project pages
- ❌ Only 3 actual pages: `/`, `/contact.html`, `/vintage-voice.html`

**Fix**: Each project section should link to:
1. Its own detail page (`/projects/rustchain`)
2. Related projects ("Built on RustChain → see also BoTTube")
3. Relevant accomplishments ("OpenSSL contributions → see our security research")

---

## 6. Performance — Score: 7/10 ✅

**What's Good**:
- ✅ Static HTML (58KB) — fast loading
- ✅ `loading="lazy"` on images
- ✅ `font-display: swap` via Google Fonts
- ✅ Nginx serving with ETag support
- ✅ `Accept-Ranges: bytes` for partial content

**Issues**:
- ⚠️ Google Fonts loaded from external CDN (2 DNS lookups + CSS download) — consider self-hosting
- ⚠️ No cache-control headers visible — add `Cache-Control: max-age=86400` for static assets
- ⚠️ No `preconnect` for bottube.ai external links

---

## 7. Backlink Strategy

### High-Priority Backlinks (Free)

| Source | Type | Action |
|--------|------|--------|
| GitHub Profile (Scottcjn) | Homepage link | Add elyanlabs.ai as organization website |
| awesome-depin | Awesome list | Submit PR adding RustChain |
| awesome-blockchain | Awesome list | Submit PR |
| awesome-ai-agents | Awesome list | Submit PR |
| Dev.to | Blog post | Write "Building LLM inference on vintage PowerPC hardware" |
| Hacker News | Show HN | "Show HN: We run AI inference on 20-year-old PowerPC servers" |
| Reddit r/homelab | Community post | Share RustChain mining on vintage hardware |
| Reddit r/LocalLLaMA | Community post | Share exotic-architecture inference benchmarks |

### Authority Backlinks (Relationship-Based)

| Source | Strategy |
|--------|----------|
| OpenSSL | Link from their contributors page |
| Ghidra | Mention in their contributor docs |
| vLLM docs | "Hardware Partners" section |
| CVPR 2026 proceedings | Link to paper + elyanlabs.ai |

---

## 8. Image SEO

**Current state**: Images have alt text ✅ but no other optimization.

**Fixes needed**:
- ❌ No `width`/`height` attributes (causes CLS - Cumulative Layout Shift)
- ❌ No WebP/AVIF versions of images
- ❌ No image sitemap
- ⚠️ `assets/sophia-portrait.jpg` — add descriptive filename like `sophia-elya-ai-research-persona.jpg`

---

## 9. Mobile SEO — Score: 8/10 ✅

- ✅ Viewport meta tag present
- ✅ Responsive design (CSS uses modern layout)
- ✅ Touch-friendly elements
- ⚠️ Need to verify Core Web Vitals on actual mobile devices

---

## 10. Priority Action Items

### 🔴 Critical (Do First)

1. **Create sitemap.xml** — Without this, Google may not discover all pages
2. **Create robots.txt** — Basic crawlability requirement
3. **Add canonical URLs** — Prevent duplicate content indexing
4. **Add JSON-LD structured data** — Organization + WebSite schema

### 🟡 Important (Do Soon)

5. **Create `/contributions` page** — Showcase 44+ upstream PRs (huge credibility signal)
6. **Create `/projects` page** — Dedicated project pages for RustChain, BoTTube, etc.
7. **Start a blog** — Even 1 post/month would dramatically improve organic traffic
8. **Add cross-linking between projects** — Internal link juice distribution

### 🟢 Nice to Have

9. **Self-host Google Fonts** — Eliminate 2 external DNS lookups
10. **Add image dimensions** — Prevent CLS
11. **Implement HSTS** — Force HTTPS
12. **Create WebP images** — Faster loading

---

## 11. Ready-to-Paste Code Snippets

### robots.txt
```
User-agent: *
Allow: /
Sitemap: https://elyanlabs.ai/sitemap.xml
```

### sitemap.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://elyanlabs.ai/</loc><priority>1.0</priority></url>
  <url><loc>https://elyanlabs.ai/contact.html</loc><priority>0.5</priority></url>
  <url><loc>https://elyanlabs.ai/vintage-voice.html</loc><priority>0.6</priority></url>
</urlset>
```

### Canonical (add to <head>)
```html
<link rel="canonical" href="https://elyanlabs.ai">
```

---

**Wallet**: zhaog100  
**Word count**: ~1,200 words  
**Estimated completion time**: 2-4 hours for all critical fixes
