"""Build blog/exa/atlas/index.html: the Exa Search Atlas, in the same design and pattern as the You.com Search Atlas."""
import re, os, html
import pathlib
HERE = str(pathlib.Path(__file__).resolve().parent) + '/'
ROOT = str(pathlib.Path(__file__).resolve().parent.parent) + '/'
SRC = HERE + 'templates/atlas_template.html'
OUT = ROOT + 'atlas/index.html'
s = open(SRC).read()
style = s[s.find('<style'):s.find('</style>') + 8]
nav_style = re.search(r'<style>\.sitenav.*?</style>', s, re.S).group(0)
e = lambda x: html.escape(str(x), quote=True)

TITLE = 'Exa Search Atlas'
DESC = 'Seven ways AI products get web search, where Exa stands in each, how Exa becomes the search agent other agents hire, and how to win.'
URL = 'https://psinglap.github.io/exa-search-atlas/atlas/'
IMG = 'https://psinglap.github.io/websearch-api-eval/img/social-preview.png'
head = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{e(DESC)}">
<link rel="canonical" href="{URL}"><meta property="og:type" content="website"><meta property="og:site_name" content="Exa Search Atlas"><meta property="og:title" content="{TITLE}"><meta property="og:description" content="{e(DESC)}"><meta property="og:url" content="{URL}"><meta property="og:image" content="{IMG}"><meta property="og:image:width" content="1280"><meta property="og:image:height" content="640"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{TITLE}"><meta name="twitter:description" content="{e(DESC)}"><meta name="twitter:image" content="{IMG}">
<title>{TITLE}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
'''
EXTRA_CSS = '''<style>
table.vt td.st3{min-width:240px}table.vt td.st3 span{display:block;margin-top:4px}
.a2a-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin:14px 0 6px}
@media (max-width:820px){.a2a-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:480px){.a2a-grid{grid-template-columns:1fr}}
.a2a-c{border:1px solid var(--line);border-radius:10px;background:var(--sheet);padding:12px 14px;display:grid;gap:4px;align-content:start}
.a2a-c b.big{font-family:var(--display);font-size:24px;line-height:1.1;color:var(--you)}
.a2a-c .small{color:var(--muted)}
.flowx{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
@media (max-width:720px){.flowx{grid-template-columns:1fr}}
.flowx .fx{border:1px solid var(--line);border-radius:10px;background:var(--sheet);padding:12px 14px}
.flowx .fx.on{border-color:var(--you);background:var(--you-soft)}
.flowx ol{margin:6px 0 0;padding-left:18px;font-size:14px}
.flowx .fx-h{font-weight:600}
.small a{color:inherit}
</style>'''
nav = ('<div class="sitenav"><div class="in"><a class="b" href="../">Exa Search Atlas</a><a class="on" href="./"><b>Atlas</b></a>'
       '<a href="../accounts/">Target accounts</a><a href="https://psinglap.github.io/websearch-api-eval/">Benchmark</a></div></div>')


def src(label, url):
    return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'

# ---------- 1. decision map ----------
# (cls, extra, left, bottom, o, n, name, size, maturity, exa pill cls, exa pill, verdict pill cls, verdict, line, steps)
DOTS = [
 ('g', 'dn', 22, 86, 35, 16, 'Pull on demand', '$0.6B → $3B', 'Mainstream', 'g', 'Exa: Leader', 'g', 'Defend, then expand', 'Agent asks, gets results back.',
  ['Agent sends a query', 'Exa searches its own index', 'Ranked results + highlights', 'Model answers']),
 ('g', 'rt dn', 84, 74, 66, 18, 'Agent to agent', '$0.8B → $10.5B', 'Early', 'g', 'Exa: First mover', 'g', 'Enter', 'A search agent that other agents hire for a task.',
  ['Read the Agent Card', 'Send a task', 'Get live status updates', 'Receive the result']),
 ('g', 'dn', 58, 62, 50, 25, 'Search for training', '$1.5B → $6B', 'Growing', 'y', 'Exa: Snapshot ready', 'g', 'Enter', 'Sell index snapshots or feeds, often for model training.',
  ['Lab licenses data or API', 'Bulk or dated Snapshot calls', 'Model learns from results', 'Better at research']),
 ('g', '', 44, 70, 46, 25, 'Push monitors', '$1.5B → $5B', 'Early', 'g', 'Exa: Shipped (v2)', 'g', 'Defend, then expand', 'Provider alerts the agent when facts change.',
  ['Register a query + schedule', 'Exa re-checks', 'Detects a change', 'Webhook to the agent']),
 ('b', 'rt', 86, 20, 63, 37, 'Private web layer', '$3.3B → $9.5B', 'Mainstream', 'a', 'Exa: ZDR, US region', 'b', 'Partner', "Search runs where the customer's data lives.",
  ['Agent in customer\'s cloud', 'Zero-retention search call', 'Results, nothing logged', 'Billed via cloud contract']),
 ('b', 'rt', 70, 42, 61, 23, 'Bundled supplier', '$1.3B → $9B', 'Mainstream', 'g', 'Exa: Default supplier', 'b', 'Partner, grow the slots', "Search sold inside a model's or gateway's API.",
  ['Model decides to search', 'Gateway calls Exa', 'Results enter context', 'Cited answer']),
 ('r', '', 28, 14, 38, 21, 'Browsing (no provider)', '$1.1B → $3.5B', 'Growing', 'a', 'Exa: Via Contents', 'r', 'Avoid building', 'Agents browse sites themselves, or sites answer agents (NLWeb, llms.txt).',
  ['Agent opens a browser', 'Reads pages directly', 'Answers with no search API']),
]
def dot(d):
    c, x, l, b, o, n, name, sz, mt, ec, ep, vc, v, line, steps = d
    return (f'<div class="mk {c} bb {x}" style="left:{l}%;bottom:{b}%" tabindex="0"><span class="bub" style="--o:{o};--n:{n}" aria-hidden="true"><span></span></span>'
            f'<b>{name}</b><i class="sz2">{sz}</i><i class="mt">{mt}</i><span class="pill {ec} ycp">{ep}</span><span class="tip" role="tooltip">'
            f'<span class="tt-h">{name}</span><span class="tt-m"><span class="pill {vc}">{v}</span><span>{mt}</span></span><span class="tt-l">{e(line)}</span>'
            f'<span class="tt-k">How it works</span><ol class="tt-f">' + ''.join(f'<li>{e(x)}</li>' for x in steps) + '</ol></span></div>')
sec1 = f'''
  <section class="slide" id="verdicts">
    <div class="sl-head"><span class="sl-n">1</span><span class="eyebrow">The decision map <span class="tag ours">my view</span></span></div>
    <h2 class="sl-h">Defend the core, lead agent to agent, grow as the default supplier.</h2>
    <div class="dm-wrap">
      <div class="dm" role="img" aria-label="Map of seven markets by 2030 size and Exa's right to win">
        <span class="ax y">Exa's right to win →</span><span class="ax x">Market size in 2030 →</span><span class="ax hint">Hover or tap a dot for details</span>
        <span class="q q1">Enter</span><span class="q q2">Defend</span><span class="q q3">Partner</span><span class="q q4">Avoid</span>
        {''.join(dot(d) for d in DOTS)}
      </div>
    </div>
  </section>'''

# ---------- 2. each way ----------
def ex(items):
    return '<span class="exl">Example buyers</span><span class="exb2">' + ''.join(
        (f'<span class="ycx">' if mine else '<span>') + f'<b>{n}</b> · {ind} · {p}</span>' for n, ind, p, mine in items) + '</span>'
def hw(how, target, verts):
    out = f'<span class="hwl"><b>How:</b> {how}</span><span class="hwl"><b>Target first:</b> {target}</span>'
    return out + ''.join(f'<span class="vtg"><b>{k}:</b> {v}</span>' for k, v in verts)
ROWS = [
 ('', 'Pull on demand', 'g', 'Defend', 'Exa, Parallel, Tavily (Nebius), You.com, Brave, Perplexity, Linkup',
  '<b>Prices fall, bake-offs rise.</b> Microsoft retired the Bing Search APIs (Aug 2025); Nebius bought Tavily (Feb 2026); Parallel raised at $2B (Apr 2026); Exa Lite at $4/1k and Ceramic at $0.25/1k on Cloudflare (Oct 2026). <i>Targeting:</i> Parallel in insurance, finance, sales; Tavily in banks and dev tools; You.com in finance and legal.'
  + ex([('Cognition', 'coding agents', 'Exa', 1), ('Revolut', 'fintech', 'Exa', 1), ('Genpact', 'insurance', 'Parallel', 0), ('JetBrains', 'dev tools', 'Tavily', 0)]),
  ('g', 'Leader', ['$100M+ annualized revenue (Oct 2026), 2B requests a month, 200k+ teams. Customers: Cursor, Cognition, Notion, HubSpot, monday.com. Best precision@5 (40%) in our open test.',
                   '<b>Next:</b> make every call match the precision lead: no empty results and a p95 under 2 s.']),
  hw('Lead with relevance and entity search; prove it on the buyer\'s own queries', 'Coding agents, GTM platforms, research copilots',
     [('Coding', 'docs and code lookup for coding agents (Cursor, Cognition: "Exa powers all parts of Devin", CodeRabbit)'),
      ('Sales / GTM', 'people and company search for sales agents (HubSpot Breeze, 11x, HockeyStack)'),
      ('Finance', 'event-driven research agents (Revolut: 1,500+ alerts a week to 1M+ users)')])),
 ('', 'Bundled in the model', 'b', 'Partner, grow the slots', 'Google (Gemini grounding), OpenAI, Anthropic, AWS AgentCore',
  '<b>Gateways add search as a line item; hyperscalers build their own.</b> AWS AgentCore Web Search runs on its own index (Jun 2026); Vercel AI Gateway added Exa as a built-in tool (Aug 2026); Cloudflare Web Search beta launched with Ceramic as default, Exa and Linkup as options (Oct 2026). <i>Targeting:</i> labs keep search in-house; gateways and inference clouds pick suppliers.'
  + ex([('Firefox', 'browser', 'Exa', 1), ('OpenRouter users', 'model router', 'Exa default', 1), ('Salesforce Agentforce', 'CRM', 'OpenAI search', 0), ('Poe', 'chat app', 'Anthropic search', 0)]),
  ('g', 'Default supplier', ['Default engine in OpenRouter\'s web plugin; built-in tool on Vercel AI Gateway; launch provider on Cloudflare; Grounding with Exa in Gemini (private preview); powers Firefox Smart Window.',
                             '<b>Next:</b> take Gemini grounding to GA and fill the open inference-cloud slots.']),
  hw('Grounding with Exa GA on Google Cloud; Exa Lite as the gateway SKU; benchmark data for the Cloudflare default slot',
     'Google Gemini grounding, Cloudflare, Together AI, Fireworks, Cerebras, Groq.<br><b>Inference clouds</b> (checked 10 Nov 2026):<br>• <b>OpenRouter</b>: Exa is the fallback engine for models without native search.<br>• <b>Groq Compound</b>: built-in search, provider not named.<br>• <b>No built-in search yet</b> (open slot): Together AI, Fireworks, Cerebras.', [])),
 ('y', 'Push as a stream', 'g', 'Defend, then expand', 'Exa Monitors, Parallel Monitor API, Dataminr, AlphaSense',
  '<b>Monitors shipped in the last year.</b> Exa Monitors (Mar 2026), then v2 at $2 per 1k runs with webhooks (Oct 29, 2026); Parallel Monitor API; Firecrawl web-scale monitor (Jul 2026); Bloomberg Enterprise MCP (Sep 2026). <i>Targeting:</i> agent builders, CRM and finance; Dataminr and AlphaSense own risk and research teams.'
  + ex([('HubSpot', 'CRM', 'Exa Monitors', 1), ('Revolut', 'fintech', 'Exa', 1), ('Formation Bio', 'biotech', 'Parallel Monitor', 0), ('Exiger', 'supply-chain risk', 'Webz.io', 0)]),
  ('g', 'Shipped (v2)', ['Monitors v2: $2 per 1k runs (7x cheaper), webhook delivery, over 211M places and 3.2M podcast episodes. HubSpot Breeze agents trigger workflows from Exa Monitors.',
                         '<b>Next:</b> named finance and risk customers next to CRM.']),
  hw('Ready-made monitor templates: competitor moves, funding, adverse media, price moves', 'HubSpot (expand), Klue, Crayon, Profound, Sigma360, Scalable Capital',
     [('Finance', 'price and event alerts (the Revolut pattern)'), ('Risk and compliance', 'adverse-media screening, named in the Monitors v2 launch'),
      ('Marketing / GTM', 'competitor and buying-signal monitors (HubSpot Breeze)')])),
 ('', 'Deploy privately', 'b', 'Partner', 'Elastic, Glean, cloud marketplaces, AWS AgentCore',
  '<b>Selling compliance and residency.</b> Parallel, Linkup and Staan document EU processing (Oct 2026); AWS AgentCore keeps search inside AWS; Cohere to combine with Aleph Alpha for EU sovereignty (Sep 2026); Brave launched zero data retention (Jan 2026). <i>Targeting:</i> regulated and sovereign buyers.'
  + ex([('Firefox', 'browser', 'Exa (ZDR)', 1), ('HSBC', 'banking', 'Mistral', 0), ('Wealthsimple', 'fintech', 'Glean', 0), ('US GSA', 'government', 'Perplexity', 0)]),
  ('a', 'ZDR, US region', ['SOC 2 Type II, zero data retention (ZDR), HIPAA with a BAA, SSO and SCIM; sold through AWS Marketplace and Gemini Enterprise. Firefox chose Exa partly for ZDR.',
                          '<b>Next:</b> an EU region, as Exa hires its first EMEA marketing head.']),
  hw('"Exa Private": EU region, ZDR on every route (including Cloudflare and Vercel), ISO 27001, DORA terms', 'EU banks and fintechs (Revolut expansion), Glean, Databricks, Snowflake, Mistral',
     [('Finance and insurance', 'EU banks and insurers needing ZDR, an EU region and DORA terms')])),
 ('y', 'License in bulk', 'g', 'Enter', 'Common Crawl, Reddit deals with Google and OpenAI, You.com (NVIDIA)',
  '<b>Search moves into training.</b> Exa\'s RL study: agents trained on Exa matched Google-results-trained agents with 69% fewer tokens (May 2026); Exa Snapshot searches the web as of a past date (Sep 2026); NVIDIA Nemotron trained with You.com search; Mercor bought Deeptune (Jul 2026). <i>Targeting:</i> AI labs and RL-environment builders.'
  + ex([('NVIDIA', 'AI lab', 'You.com', 0), ('Google', 'AI lab', 'Reddit licence', 0), ('OpenAI', 'AI lab', 'News Corp licence', 0)]),
  ('y', 'Snapshot ready', ['The RL study (69% fewer tokens) and Snapshot (dated search with no answer leakage) are the two proof points; "AI labs" is a named segment in the $100M post.',
                           '<b>Next:</b> a named AI-lab result to put next to the study.']),
  hw('Snapshot + replayable results + burst capacity, priced per training run; no raw dumps', 'Thinking Machines, AI2, Mistral, Qwen, Prime Intellect', [])),
 ('y', 'Agent to agent', 'g', 'Enter', 'Google, Microsoft, AWS, Salesforce, SAP (150+ orgs)',
  '<b>Platforms building agent marketplaces.</b> AWS Marketplace took A2A servers (Nov 2025); A2A v1.0 (Mar 2026); Google Agent Gallery with a $750M partner fund (Apr 2026); Coinbase agentic.market (Apr 2026); Tavily on x402 (May 2026); Parallel on Stripe MPP. <i>Targeting:</i> Google, AWS, Salesforce and Microsoft own the marketplaces.'
  + ex([('Gemini Enterprise tenants', 'enterprise', 'Exa Agent', 1), ('Thomson Reuters', 'info services', 'AWS AgentCore', 0), ('1-800Accountant', 'accounting', 'Agentforce', 0), ('Tyson ↔ Gordon Food', 'food supply', 'A2A', 0)]),
  ('g', 'First mover', ['Exa Agent is a launch partner in the Gemini Enterprise Agent Marketplace (Apr 2026); x402 on search and contents (Apr 2026); Nevermined payments; Exa Connect data marketplace; <code>agent_run</code> in MCP.',
                        '<b>Next:</b> publish the A2A Agent Card on exa.ai (the Gemini listing already requires one) and per-call pricing on Exa Agent.']),
  hw('Signed Agent Card for Exa Agent (skills: research, list building, enrichment, monitoring); per-call x402 and Stripe MPP', 'Gemini Enterprise, AWS AgentCore and Marketplace A2A, Salesforce AgentExchange, Microsoft Foundry, Coinbase agentic.market',
     [('Sales / GTM', 'a list-building agent that Agentforce and HubSpot agents hire'), ('Finance', 'research agents that pay per task via x402 or MPP')])),
]
def vrow(r):
    ycls, way, vc, v, lead, cmp_, (ec, ep, lines), win = r
    return (f'<tr{" class=\"y\"" if ycls else ""}><td><b>{way}</b><br><span class="pill {vc}" style="margin-top:6px">{v}</span></td><td>{lead}</td>'
            f'<td class="cmp">{cmp_}</td><td class="ych3"><span class="pill {ec}">{ep}</span>' + ''.join(f'<span>{x}</span>' for x in lines) + f'</td><td class="hwin">{win}</td></tr>')
sec2 = f'''
  <section class="slide" id="verdict-table">
    <div class="sl-head"><span class="sl-n">2</span><span class="eyebrow">Each way: where Exa stands, how, who</span></div>
    <h2 class="sl-h">Where Exa stands, how to win, and who to target first.</h2>
    <div class="tw"><table class="vt">
      <thead><tr><th>Way</th><th>Who leads</th><th>How the market is moving</th><th>Exa here</th><th>How to win</th></tr></thead>
      <tbody>
        {''.join(vrow(r) for r in ROWS)}
      </tbody>
    </table></div>
    <div class="callout"><b class="h">Across all seven ways</b><ul class="small" style="margin:6px 0 0;padding-left:18px;display:grid;gap:4px"><li><b>Why buyers pick Exa:</b> its own index with people, company and place search, the most on-topic results, and one platform from search to agents and monitors.</li><li><b>Where Exa stands:</b> leads pull by revenue ($100M+ run rate) and is the default supplier behind OpenRouter, Vercel and Firefox.</li><li><b>Next wins:</b> an Agent Card with per-call payments, an EU region, and a tighter tail (no empty results, p95 under 2 s).</li></ul></div>
  </section>'''

# ---------- 3. strengths and next moves ----------
SW = [
 ('good', 'Lead with', 'Relevance', 'Best precision@5 (40%) and best insurance accuracy (75%) in our open test; #1 on the Artificial Analysis Search Index; Exa 3.0 claims #1 on 8 of 8 benchmarks.', 'You.com 37%, Tavily 26%, Parallel 26% precision@5.', 'Publish independent, rerunnable bake-offs, not only Exa-run benchmarks.'),
 ('good', 'Lead with', 'Entity indexes', 'People (1B+ profiles), companies, 350M publications, 211M places, 3.2M podcasts.', 'Parallel\'s core Search has no people or company category.', 'Lead GTM, recruiting and research pitches with entity search and Websets.'),
 ('good', 'Lead with', 'Scale and distribution', '$100M+ run rate, 2B requests a month; default on OpenRouter, built-in on Vercel, Firefox, Gemini grounding (preview). MCP server 160K downloads a month, 1.8x tavily-mcp.', 'Tavily leads LangChain (langchain-tavily 599K vs langchain-exa 171K a month).', 'Win the LangChain quickstarts and the Cloudflare default slot.'),
 ('good', 'Lead with', 'Product breadth', 'Search (Lite, Auto, Deep), Contents, Exa Agent up to Ultra, Monitors, Connect, Snapshot.', 'Parallel: Search, Extract, Task, FindAll, Monitor.', 'One stable naming map: Research API retired, instant and fast now legacy.'),
 ('warn', 'Next move', 'The tail', '12 empty responses of 90 and p95 3,997 ms in our test; zero failed calls.', 'You.com: 0 empty, p95 804 ms.', 'A "why empty" hint, filter auto-relax, p95 under 2 s.'),
 ('warn', 'Next move', 'Freshness and finance', '44% of results inside the date window; newest relevant result 8.2 h; finance accuracy 40%.', 'You.com 59% and 4.1 h; Parallel 88% finance accuracy.', '<code>maxAgeHours</code> defaults for news and finance; a finance query pack.'),
 ('warn', 'Next move', 'First five minutes', '95 s in 13 steps from sign-in to API key, slowest of four; signup credit cut Oct 23, 2026.', 'Tavily 25 s in 3 steps.', 'Key on the first screen; the keyless MCP tier as the front door.'),
 ('warn', 'Next move', 'Residency and payments', 'No documented EU region; x402 buys a $7 key rather than paying per call; no Stripe MPP.', 'Parallel and Linkup document EU processing; Parallel and You.com take MPP per call.', 'EU region; per-call x402 and MPP on Search, Agent and Monitors.'),
]
sec3 = '''
  <section class="slide" id="strengths">
    <div class="sl-head"><span class="sl-n">3</span><span class="eyebrow">Strengths to lead with, moves to make</span></div>
    <h2 class="sl-h">Exa wins on relevance, entities and reach; the next gains are in the tail.</h2>
    <div class="tw"><table class="vt">
      <thead><tr><th>Area</th><th>Exa today</th><th>The field</th><th>Next move</th></tr></thead>
      <tbody>''' + ''.join(
    f'<tr><td><b>{a}</b><br><span class="pill {"g" if t=="good" else "a"}" style="margin-top:6px">{lab}</span></td><td class="st3">{x}</td><td>{f}</td><td>{n}</td></tr>'
    for t, lab, a, x, f, n in SW) + '''</tbody>
    </table></div>
    <p class="small" style="margin-top:8px">"Our open test": the <a href="https://psinglap.github.io/websearch-api-eval/">Web Search API evaluation</a>, 30 agent queries × 3 runs per API, run 8 Oct 2026, defaults as shipped.</p>
  </section>'''

SEC4 = open(HERE + 'atlas_agents_section.html').read()

srcs = '''
    <details class="srcs"><summary>Sources and method</summary>
      <p class="small" style="margin-top:8px">Research passes on 10 Nov 2026 read Exa's blog, docs, changelog, pricing and customer pages, competitor docs, press, GitHub issues, Hacker News and npm/PyPI download counts, from 2025 to Nov 2026. Benchmark numbers come from the open <a href="https://psinglap.github.io/websearch-api-eval/">Web Search API evaluation</a> (run 8 Oct 2026). Market sizes for 2030 are the same estimates as the You.com Search Atlas. Key sources: '''
srcs += ', '.join(src(l, u) for l, u in [
 ('Exa $100M run rate', 'https://exa.ai/blog/100m-run-rate'), ('Exa 3.0', 'https://exa.ai/blog/exa-3'), ('Monitors v2', 'https://exa.ai/blog/monitors-v2'),
 ('Exa + Google Cloud', 'https://exa.ai/blog/exa-google-cloud'), ('Exa + Firefox', 'https://exa.ai/blog/exa-firefox'), ('Vercel AI Gateway', 'https://vercel.com/changelog/exa-joins-vercel-ai-gateway-agent-marketplace'),
 ('Cloudflare providers', 'https://developers.cloudflare.com/web-search/providers/'), ('RL search study', 'https://exa.ai/blog/rl-search-outcomes'), ('Exa pricing', 'https://exa.ai/pricing'),
 ('Exa enterprise', 'https://exa.ai/enterprise'), ('Exa customers', 'https://exa.ai/customers'), ('Coinbase x402 + Exa', 'https://www.coinbase.com/developer-platform/discover/launches/exa'),
 ('AWS AgentCore Web Search', 'https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-web-search/'), ('AWS Marketplace A2A', 'https://aws.amazon.com/about-aws/whats-new/2025/11/marketplace-a2a-server-bedrock-agentcore-runtime/'),
 ('Parallel on Stripe MPP', 'https://parallel.ai/blog/tempo-stripe-mpp'), ('Parallel EU residency', 'https://parallel.ai/articles/best-web-search-apis-eu-data-residency'), ('A2A spec', 'https://a2a-protocol.org/latest/specification/')])
srcs += '.</p>\n    </details>'

body = f'''</head><body>
{nav_style}
{nav}

<div class="deck" id="top">
  <div class="topline"><div class="brand">Exa Search <span>Atlas</span></div><span class="eyebrow">one source at a time · 10 Nov 2026 · Pallavi Singla</span></div>

  <div class="partlabel"><span class="eyebrow">Where Exa should play next: a verdict for each of the seven ways · deep research, 10 Nov 2026</span></div>
{sec1}
{sec2}
{sec3}
{SEC4}
  <section class="slide" style="padding-top:0">{srcs}</section>
</div>
</body>
</html>'''
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w').write(head + style + '\n' + EXTRA_CSS + '\n' + body)
print('wrote', OUT, len(head + style + body))
