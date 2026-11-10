"""Build the landing page (index.html) in the same design as the Atlas."""
import pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
t = (HERE / 'templates/atlas_template.html').read_text()
style = t[t.find('<style'):t.find('</style>') + 8]
nav_style = re.search(r'<style>\.sitenav.*?</style>', t, re.S).group(0)
EVAL = 'https://psinglap.github.io/websearch-api-eval/'
SITE = 'https://psinglap.github.io/exa-search-atlas/'
DESC = 'Independent research on Exa: where it wins, how it becomes the search agent other agents hire, target accounts, GTM plays and distribution.'
page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Exa Search Atlas</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="{SITE}"><meta property="og:type" content="website"><meta property="og:site_name" content="Exa Search Atlas"><meta property="og:title" content="Exa Search Atlas"><meta property="og:description" content="{DESC}"><meta property="og:url" content="{SITE}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
{style}
<style>
.cards{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:18px}}
@media (max-width:900px){{.cards{{grid-template-columns:1fr}}}}
.card2{{display:grid;gap:8px;align-content:start;border:1px solid var(--line);border-radius:12px;background:var(--sheet);padding:18px 20px;color:var(--ink);text-decoration:none}}
.card2:hover,.card2:focus-visible{{border-color:var(--you);outline:none}}
.card2 b{{font-family:var(--display);font-size:22px}}
.card2 .go{{color:var(--you);font-weight:600;font-size:14px}}
.card2 ul{{margin:0;padding-left:18px;font-size:14px;color:var(--muted)}}
</style>
</head><body>
{nav_style}
<div class="sitenav"><div class="in"><a class="b on" href="./">Exa Search Atlas</a><a href="atlas/">Atlas</a><a href="accounts/">Target accounts</a><a href="agent-card/">Agent Card</a><a href="{EVAL}">Benchmark</a></div></div>
<div class="deck" id="top">
  <div class="topline"><div class="brand">Exa Search <span>Atlas</span></div><span class="eyebrow">independent research · 10 Nov 2026 · Pallavi Singla</span></div>
  <section class="slide">
    <div class="sl-head"><span class="eyebrow">What Google is for humans, Exa is for AI agents</span></div>
    <h2 class="sl-h">Where Exa wins, where it plays next, and who to sell to.</h2>
    <p style="max-width:720px">Three pages of independent research on Exa, built from public sources and an <a href="{EVAL}">open, rerunnable web search API benchmark</a> (Exa, You.com, Tavily, Parallel; 30 agent queries × 3 runs, 8 Oct 2026).</p>
    <div class="cards">
      <a class="card2" href="atlas/"><b>Exa Search Atlas</b><ul><li>Decision map: seven ways AI products get web search, scored for Exa</li><li>Each way: who leads, how the market moves, Exa here, how to win</li><li>Strengths to lead with, moves to make</li><li>Google for AI agents: Exa as the search agent other agents hire, and what to publish where</li></ul><span class="go">Open the Atlas →</span></a>
      <a class="card2" href="accounts/"><b>Exa Target Accounts</b><ul><li>59 accounts across 6 agent use cases, with the provider each uses today</li><li>90 developer complaints in 8 themes, with the community play</li><li>Seven GTM plays and how to measure them</li><li>Distribution: 16 platforms, the default today, the action for Exa</li></ul><span class="go">Open the accounts →</span></a>
      <a class="card2" href="agent-card/"><b>Exa Agent Card: launch kit</b><ul><li>What an A2A Agent Card is, and why this is positioning, not a product change</li><li>An example card for Exa Agent with four skills (unofficial proposal)</li><li>Walkthrough: a sales agent hires Exa for one task</li><li>Launch plan, draft launch post, and how to pitch it</li></ul><span class="go">Open the launch kit →</span></a>
    </div>
    <p class="small" style="margin-top:16px">Independent research by Pallavi Singla; not affiliated with or endorsed by Exa. Facts are sourced on each page (hover ⓘ); vendor claims and estimates are labelled.</p>
  </section>
</div>
</body></html>'''
(ROOT / 'index.html').write_text(page)
print('wrote', ROOT / 'index.html')
