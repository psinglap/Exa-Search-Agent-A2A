"""Build blog/exa/accounts/index.html: Exa target accounts, in the same design and pattern as the You.com Target Accounts page."""
import re, json, html, os
import pathlib
HERE = str(pathlib.Path(__file__).resolve().parent) + '/'
ROOT = str(pathlib.Path(__file__).resolve().parent.parent) + '/'
SP = HERE + 'data/'
SRC = HERE + 'templates/accounts_template.html'
OUT = ROOT + 'accounts/index.html'
s = open(SRC).read()
e = lambda x: html.escape(str(x), quote=True)
acc = json.load(open(SP + 'exa_accounts.json'))
# Research API was retired Apr 2026 (now Exa Agent); Instant is legacy on Exa 3.0 (now Lite)
FIX = [('Research API', 'Exa Agent'), ('Exa Instant/Lite', 'Exa Lite'), ('Instant/Lite', 'Lite'), ('Exa Instant (now Lite on Exa 3.0)', 'Exa Lite (formerly Instant)'),
       ('Exa Instant P50', 'Exa Instant (now Lite) P50'), ('with Exa Instant', 'with Exa Lite'), ('Exa Instant as', 'Exa Lite as'), ('Exa Instant inside', 'Exa Lite inside'),
       ('with Instant search', 'with Lite search'), ('Exa Instant with', 'Exa Lite with')]
def fx(t):
    for a, b in FIX: t = t.replace(a, b)
    return t
acc = json.loads(fx(json.dumps(acc, ensure_ascii=False)))
DROP = ['OpenRouter']  # covered in Distribution
for g in acc['groups']:
    g['rows'] = [r for r in g['rows'] if r['n'] not in DROP]
pd = json.load(open(SP + 'exa_pain_dist.json'))

# ---------- target data ----------
COL = {'coding': '#0891b2', 'res': '#c2410c', 'gtm': '#db2777', 'people': '#6c4cf1', 'voice': '#2563eb', 'mon': '#b45309'}
ORDER = ['coding', 'gtm', 'res', 'people', 'voice', 'mon']
def tipsrc(url, name):
    return f' <span class="tip src" tabindex="0">ⓘ<span class="pop" role="tooltip"><b>Source</b><br><a href="{e(url)}" target="_blank" rel="noopener">{e(name)}</a></span></span>'
groups = []
for g in sorted(acc['groups'], key=lambda g: ORDER.index(g['id']) if g['id'] in ORDER else 99):
    stp = g['strip']
    sig = stp.get('signal', '')
    if isinstance(sig, str):
        m = re.search(r'\s*(https?://\S+)\s*$', sig)
        sig = {'quote': sig[:m.start()].strip() if m else sig, 'url': m.group(1) if m else ''}
    if isinstance(sig, dict):
        q, u = sig.get('quote', ''), sig.get('url', '')
        dom = re.sub(r'^https?://(www\.)?([^/]+).*', r'\2', u)
        q = q.strip()
        if q.count('"') % 2 == 1 and q.startswith('"'): q = q + '"' if q.endswith(')') is False else q
        _n = [0]
        def _cq(m):
            _n[0] += 1
            return '“' if _n[0] % 2 else '”'
        q = re.sub('"', _cq, q)
        sig = f'<span class="tip " tabindex="0">{e(q)}<span class="pop" role="tooltip">{e(q)}<br><a href=\'{e(u)}\' target=\'_blank\' rel=\'noopener\'>{e(dom)}</a></span></span>'
    lead = stp.get('lead', '')
    if isinstance(lead, str): lead = [x.strip() for x in lead.split(' + ')]
    if isinstance(lead, list):
        lead = '<span class="row">' + ' '.join(f'<span class="tag">{e(x)}</span>' for x in lead) + '</span>'
    strip = [['Lead with', lead], ['Pain we solve', stp.get('pain', '')], ['Our proof', stp.get('proof', '')],
             ['Product', stp.get('product', '')], ['Live pain signal', sig]]
    rows = []
    for r in g['rows']:
        p = r.get('p', 'None found') or 'None found'
        tagc = 'good' if p == 'Exa' else ('' if p in ('None found', 'In-house') else 'warn')
        use = f'<span class="tip use" tabindex="0"><span class=\'tag {tagc}\'>{e(p)}</span><span class="pop" role="tooltip">{e(r.get("provnote", p))}</span></span>'
        rows.append({'n': r['n'], 'st': r.get('st', ''), 'p': p, 'i': r.get('i', 'Cross-industry'), 'use': use,
                     'sig': e(r.get('sig', '')) + (tipsrc(r['src'], r.get('srcname') or r['src']) if r.get('src') else ''),
                     'help': r.get('help', ''), 'fit': r.get('fit', 'med')})
    groups.append({'id': g['id'], 'name': g['name'], 'strip': strip, 'rows': rows, 'c': COL.get(g['id'], '#4b5bdc'),
                   'known': sum(1 for r in rows if r['p'] not in ('None found', '')), 'pain': re.sub(r'<[^>]+>', '', stp.get('pain', ''))})
total = sum(len(g['rows']) for g in groups)
provs = {}
for g in groups:
    for r in g['rows']:
        provs[r['p']] = provs.get(r['p'], 0) + 1
on_exa = provs.get('Exa', 0)
on_comp = sum(v for k, v in provs.items() if k not in ('Exa', 'None found', 'In-house', 'Several'))
inds = sorted({r['i'] for g in groups for r in g['rows']}, key=lambda x: (x != 'Cross-industry', x))
data = json.dumps({'groups': groups}, ensure_ascii=False).replace('</', '<\\/')

# ---------- overview charts ----------
dl = pd['downloads']
def num(v):
    return v if isinstance(v, (int, float)) else int(re.sub(r'[^0-9]', '', str(v)) or 0)
def fmt(v): return f'{v/1e6:.1f}M' if v >= 1e6 else f'{v/1e3:.0f}K'
NPM = [('firecrawl-mcp', 'https://github.com/firecrawl/firecrawl-mcp-server'), ('exa-mcp-server', 'https://github.com/exa-labs/exa-mcp-server'),
       ('@brave/brave-search-mcp-server', 'https://github.com/brave/brave-search-mcp-server'), ('tavily-mcp', 'https://github.com/tavily-ai/tavily-mcp'),
       ('@youdotcom-oss/mcp', 'https://github.com/youdotcom-oss/mcp')]
PYP = [('tavily-python', 'https://pypi.org/project/tavily-python/'), ('exa-py', 'https://pypi.org/project/exa-py/'), ('firecrawl-py', 'https://pypi.org/project/firecrawl-py/'),
       ('parallel-web', 'https://pypi.org/project/parallel-web/'), ('youdotcom', 'https://pypi.org/project/youdotcom/'), ('linkup-sdk', 'https://pypi.org/project/linkup-sdk/')]
def getv(d, k):
    for kk, v in d.items():
        if kk == k: return num(v if not isinstance(v, dict) else v.get('downloads', v.get('last_month', 0)))
    return 0
def bars(items, d):
    vals = [(n, u, getv(d, n)) for n, u in items]
    vals = [x for x in vals if x[2]]
    vals.sort(key=lambda x: -x[2]); mx = vals[0][2]
    out = ''
    for n, u, v in vals:
        mine = n.startswith('exa')
        out += (f'<div class="bar-row wide"><span class="bar-label"><a href="{u}" target="_blank" rel="noopener">{n}</a></span><span class="bar-track">'
                f'<span class="bar-fill{" you" if mine else ""}" style="width:{max(2, round(v / mx * 100))}%"></span></span><span class="bar-val">{fmt(v)}</span></div>')
    return out
npm, pypi = dl['npm'], dl['pypi']
exa_mcp, tav_mcp = getv(npm, 'exa-mcp-server'), getv(npm, 'tavily-mcp')
WIN = dl.get('window', 'npm 2026-10-11 to 2026-11-09; PyPI trailing 30 days to 2026-11-10')
def pop(t): return f'<span class="pop" role="tooltip">{t}</span>'
NPM_SRC = f'npm is the JavaScript package registry. Sources: <a href="https://api.npmjs.org/downloads/point/last-month/exa-mcp-server" target="_blank" rel="noopener">npm registry</a> and <a href="https://pypistats.org/" target="_blank" rel="noopener">pypistats.org</a>. JavaScript SDKs, last month: @mendable/firecrawl-js {fmt(getv(npm,"@mendable/firecrawl-js"))}, exa-js {fmt(getv(npm,"exa-js"))}, @tavily/core {fmt(getv(npm,"@tavily/core"))}, parallel-web {fmt(getv(npm,"parallel-web"))}. Window: {e(WIN)}.'
PY_SRC = f'Source: <a href="https://pypistats.org/" target="_blank" rel="noopener">pypistats.org</a> (PyPI download counts), last month. Framework packages: langchain-tavily {fmt(getv(pypi,"langchain-tavily"))} vs langchain-exa {fmt(getv(pypi,"langchain-exa"))}, the clearest gap in framework defaults. firecrawl-py also covers scraping, so not all of its installs are for search.'
charts = (f'<div class="charts"><div class="panel mcp"><div class="ph"><h3>MCP server downloads, last month</h3><span class="tip src" tabindex="0">Sources ⓘ{pop(NPM_SRC)}</span></div><div class="bars">{bars(NPM, npm)}</div></div>'
          f'<div class="panel mcp"><div class="ph"><h3>Python SDK downloads, last month</h3><span class="tip src" tabindex="0">Sources ⓘ{pop(PY_SRC)}</span></div><div class="bars">{bars(PYP, pypi)}</div></div></div>')

overview = f'''<div class="part" id="overview">1 · Overview</div><h2>Exa in agent search at a glance</h2>
  <div class="glance"><div class="kstack">
    <div class="kpi"><b>{total}</b><span>target accounts across {len(groups)} use cases</span></div>
    <div class="kpi"><b>{on_exa} + {on_comp}</b><span>already on Exa to expand + on another named search API to win</span></div>
    <div class="kpi"><b>{fmt(exa_mcp)} vs {fmt(tav_mcp)}</b><span>monthly MCP downloads: Exa vs Tavily <span class="tip src" tabindex="0">ⓘ{pop("npm registry, " + e(WIN) + ". Exa's MCP server is also in the official MCP Registry as ai.exa/exa, and its hosted endpoint (mcp.exa.ai) is not counted by npm.")}</span></span></div>
  </div></div>{charts}
  <h3>What we lead with</h3>
  <div class="pillars"><div class="pillar"><span class="tag">P1</span><b>Finds the right thing</b><span>Best precision@5 (40%) and insurance accuracy (75%) in the open test</span></div><div class="pillar"><span class="tag">P2</span><b>Entities, not just pages</b><span>People (1B+), companies, places, papers in one API</span></div><div class="pillar"><span class="tag">P3</span><b>Search to agent, one platform</b><span>Search, Exa Agent, Websets, Monitors at $2/1k</span></div><div class="pillar"><span class="tag">P4</span><b>Where agents are built</b><span>OpenRouter default, Vercel, Google, Firefox, MCP</span></div></div>
'''

# ---------- developer pain ----------
TAG = {'Ahead': ('good', 'Ahead'), 'Even': ('', 'Even'), 'Weak spot': ('warn', 'Next move')}
pains = sorted(pd['pain'], key=lambda p: -p['n'])
mxn = pains[0]['n']
def srcli(x):
    q = e(x['quote'])
    qt = f'<i>{q}</i> (paraphrase)' if x.get('paraphrase') else f'“{q}”'
    dom = re.sub(r'^https?://(www\.)?([^/]+).*', r'\2', x['url'])
    return f'<li>{e(x["kind"])}, {e(x["date"])}, {e(x["who"])}: {qt} [<a href="{e(x["url"])}" target="_blank" rel="noopener">{dom}</a>]</li>'
def short(t, n=150):
    t = t.split('. ')[0].rstrip('.')
    return t if len(t) <= n else t[:n].rsplit(' ', 1)[0] + '…'
STATUS = {  # concise "Exa today" lines, same length as the You.com page
 'Rate limits and free-tier throttling': 'Zero failed calls with a paid key in our 90 calls; throttling shows up in the keyless MCP tier',
 'Credits, cost and pricing clarity': '$7/1k searches + $1/1k extra results; 402s can surface mid-run. <code>costDollars</code> on every response is a head start',
 'Empty results and filters (includeDomains / excludeDomains / dates)': 'Best precision@5 (40%), but 12 empty responses of 90 (You.com 0, Parallel 3)',
 'Stale cache and livecrawl fallback': '44% of results in window; newest relevant 8.2 h. Cache-first unless <code>maxAgeHours</code> is set',
 'Latency, hangs and timeouts': 'p50 1.1 s, p95 4.0 s in our test: fast typical calls, long tail',
 'Signup, auth and API-key friction': '95 s in 13 steps to an API key, slowest of four; MCP OAuth sign-in gaps',
 'SDK changes, changelogs and docs drift': 'exa-js 4.4M and exa-py 5.4M downloads a month; users ask for per-version changelogs',
 'MCP server packaging and tool exposure': f'{fmt(exa_mcp)} MCP downloads a month, {exa_mcp / tav_mcp:.1f}x tavily-mcp; in the official MCP Registry',
}
PLAY = {
 'Rate limits and free-tier throttling': 'A real 429 with Retry-After from the keyless tier; published free limits; retry built into exa-py and exa-js',
 'Credits, cost and pricing clarity': 'Credits-low webhook and soft limits; a cost-per-correct-answer page using the precision lead',
 'Empty results and filters (includeDomains / excludeDomains / dates)': 'A "why empty" hint naming the filter; auto-relax on request; subdomain matching',
 'Stale cache and livecrawl fallback': 'A "served stale" flag; <code>maxAgeHours</code> documented in every SDK; fixes sent to wrappers',
 'Latency, hangs and timeouts': 'Default client timeouts; a public status page with p95 for mcp.exa.ai',
 'Signup, auth and API-key friction': 'Key on the first screen; 401 for unauthenticated MCP calls so OAuth works; allowlist agent clouds',
 'SDK changes, changelogs and docs drift': 'Release notes per version with a breaking-change label; typed errors; docs examples tested in CI',
 'MCP server packaging and tool exposure': 'A client test matrix on every release (Claude Code, Codex, Cursor, opencode); capped tool output',
}
NAME = {'Empty results and filters (includeDomains / excludeDomains / dates)': 'Empty results and strict filters', 'Stale cache and livecrawl fallback': 'Stale cache and live-crawl fallback'}
ft = ''
for p in pains:
    c, lab = TAG.get(p['status_tag'], ('', p['status_tag']))
    th = p['theme']
    ft += (f'<div class="ft-row"><div class="ft-theme"><b>{e(NAME.get(th, th))}</b><span class="ft-bar"><span style="width:{round(p["n"] / mxn * 100)}%"></span></span><span class="ft-n">{p["n"]}</span></div>'
           f'<div class="ft-ans"><span class="tag {c}">{lab}</span> {STATUS.get(th, e(short(p["status"])))}</div><div class="ft-play">{PLAY.get(th, e(short(p["play"])))}</div>'
           f'<div class="ft-src"><span class="src-tip" tabindex="0">Sources <span aria-hidden="true">ⓘ</span><span class="src-pop" role="tooltip"><ul>{"".join(srcli(x) for x in p["sources"])}</ul></span></span></div></div>\n  ')
community = f'''<div class="part" id="community">2 · Why developers switch</div><h2>Developer pain and the community play</h2><p class="lead-s">{pd["pain_total"]} public complaints and requests that name Exa, from GitHub and Hacker News, Nov 10, 2026 (a sample, not market size; Discord and X were not read).</p>
  <div class="ft-head"><h3>Frustrations, Exa today and the community play</h3></div>
  <div class="ft-list">
  <div class="ft-row ft-cols" aria-hidden="true"><span>Theme</span><span>Exa today</span><span>Community play</span><span></span></div>
  {ft}</div>
'''

# ---------- GTM plays ----------
TYPE_COL = {'Fix': '#b42318', 'Asset': '#4b5bdc', 'Launch': '#b45309', 'Distribution': '#15803d'}
PLAYS = [
 ('Open bake-off: run your own evals', 'Asset', 'Side-by-side test on the buyer\'s own queries, with precision@5 and empty rate shown',
  'Buyers rerun the open harness on their own queries and see Exa next to Tavily, Parallel and You.com, with precision@5, empty rate and p95 on one page.',
  'Accounts on Tavily, Parallel or You.com today; research and finance copilots comparing vendors', 'Bake-offs → paid; harness reruns by outside developers'),
 ('Become the default', 'Distribution', 'LangChain quickstarts, Cloudflare\'s default slot, crewAI and smolagents',
  'Own the integration code where developers pick tools: a refreshed langchain-exa in the quickstarts, the Cloudflare Web Search default, crewAI and smolagents examples, and search on Together, Fireworks and Cerebras.',
  'LangChain, Cloudflare, crewAI, Hugging Face (smolagents), LlamaIndex, Together AI, Fireworks, Cerebras', f'Merged integration PRs; langchain-exa downloads (baseline {fmt(getv(pypi, "langchain-exa"))}/mo)'),
 ('The search agent for agents', 'Launch', 'An A2A Agent Card for Exa Agent, with per-call x402 and Stripe MPP',
  'Publish a signed A2A Agent Card for Exa Agent (skills: research, list building, enrichment, monitoring), price each task per call, and list it in Gemini Enterprise, AWS Marketplace A2A, Salesforce AgentExchange and Coinbase agentic.market.',
  'Enterprise agent platforms and autonomous agents that pay per call', 'Tasks from other agents; paid per-call agents'),
 ('Websets for GTM and recruiting', 'Launch', 'Ready-made list-building templates on the people and company indexes',
  'Templates for target-account lists, buying-signal enrichment and candidate sourcing, built on 1B+ people and the company index, each with a one-click Websets run.',
  'Sales and GTM agents, recruiting platforms (see tables below)', 'Websets started from templates → paid'),
 ('Monitor templates', 'Launch', 'Competitor, funding, adverse-media and price-move monitors at $2 per 1k runs',
  'Pre-built Monitors v2 recipes with webhooks into HubSpot, Slack and agent frameworks, led by the HubSpot Breeze and Revolut stories.',
  'Monitoring and alerting accounts, CRM platforms, finance teams', 'Active monitors; webhook deliveries'),
 ('Fix the first five minutes', 'Fix', 'Key on the first screen, a real 429 on the free tier, a "why empty" hint',
  'One-screen key creation, a 401 for unauthenticated MCP calls so OAuth clients can sign in, a real 429 with Retry-After from the keyless tier, and a hint naming the filter that emptied a result.',
  'Every developer who signs up; keyless MCP users in opencode and Hermes', 'Sign-in → first call time; empty-result rate'),
 ('Google for AI agents report', 'Asset', 'Tokens per correct answer and what agents search for, published as a yearly report',
  'A rerunnable token-cost benchmark (tokens per correct answer by provider and content mode) plus a "State of agent search" report from aggregate query mix, to own the search-for-agents story.',
  'Agent builders, analysts and press; the channels in the Exa Search Atlas', 'Citations and backlinks; signups from the report'),
]
plays = '<div class="play-list">' + ''.join(
    f'<div class="play-row" style="--c:{TYPE_COL[t]}"><span class="pnum">{i}</span><div class="ptitle"><b>{e(n)}</b><span class="ptype">{t}</span></div>'
    f'<div class="pwhat">{e(w)} <span class="tip src" tabindex="0">ⓘ<span class="pop" role="tooltip">{e(d)}<br><br><b>Who it reaches</b><br>{e(who)}</span></span></div>'
    f'<div class="pmeas"><span class="k">Measure</span>{e(m)}</div></div>' for i, (n, t, w, d, who, m) in enumerate(PLAYS, 1)) + '</div>'
plays_sec = f'<div class="part" id="plays">3 · Strategy</div><h2>GTM plays</h2>{plays}\n'

# ---------- distribution ----------
DIST = [
 ('OpenRouter', 'Model router', 'Exa is the default engine for models without native search', 'Turning the fallback slot into the named default for open-weight models, with a volume tier'),
 ('Vercel AI Gateway', 'Gateway / marketplace', 'Built-in: Exa, Perplexity, Parallel side by side', 'Shipping AI SDK starter templates that wire <code>exaSearch</code> in by default'),
 ('Cloudflare Web Search', 'Cloud', 'Ceramic default; Exa and Linkup launch providers', 'Earning the default slot with benchmark data and Workers templates'),
 ('LangChain', 'Agent framework', 'Tavily (langchain-tavily 599K vs langchain-exa 171K/mo)', 'Refreshing langchain-exa for the new search types and getting it into the quickstarts'),
 ('crewAI', 'Agent framework', 'Serper in the quickstart; Exa and Tavily tools ship', 'Contributing an Exa version of the quickstart crew'),
 ('smolagents (Hugging Face)', 'Agent library', 'DuckDuckGo default; Exa opt-in', 'Proposing Exa as the auto-selected engine when an Exa key is set'),
 ('Mastra, Agno', 'Agent frameworks', 'Mastra: Exa native tool. Agno: Exa, Tavily, DDG toolkits', 'Making Exa the search step in Mastra templates; fixing ExaTools upstream in Agno'),
 ('ElevenLabs, Vapi, LiveKit', 'Voice platforms', 'ElevenLabs: Tavily built in, Exa in alpha. Vapi, LiveKit: none built in', 'Promoting the ElevenLabs alpha to built-in; shipping a low-latency Lite search plugin for Vapi and LiveKit'),
 ('Together, Fireworks, Cerebras, Groq', 'Inference hosts', 'Groq Compound: provider not named; others: no search tool found', 'Pitching Exa as the bundled search tool for open-weight endpoints'),
 ('Google Gemini Enterprise', 'Cloud', 'Grounding with Exa in private preview; Exa Agent in the Agent Marketplace', 'Moving Exa grounding from private preview to GA'),
 ('AWS AgentCore / Marketplace', 'Cloud', 'AgentCore Web Search on its own index; Exa listed on Marketplace', 'Listing Exa MCP as an AgentCore Gateway target with Marketplace billing'),
 ('Microsoft Copilot Studio, Foundry', 'Cloud', 'Grounding with Bing; no Exa connector found', 'Publishing an Exa connector for Copilot Studio and a Foundry MCP tool'),
 ('Databricks, Snowflake', 'Data clouds', 'Snowflake: Brave (secondary source); Databricks: Bright Data MCP', 'Listing Exa MCP in both marketplaces'),
 ('Coding agents', 'opencode, Claude Code, Cursor', 'opencode: random among Exa, Parallel, Firecrawl, Tavily; Claude Code: Exa plugin', 'Hardening the keyless tier so opencode\'s rotation keeps landing on Exa'),
 ('n8n, Zapier', 'Automation', 'Exa node (verified) and Exa app', 'Adding ready-made research and Websets templates'),
 ('MCP registries', 'Tool directories', f'Exa {fmt(exa_mcp)}, Tavily {fmt(tav_mcp)} npm downloads/mo; ai.exa/exa in the official registry', 'Keeping registry metadata, tool lists and auth notes current on each release'),
]
dist = ('<div class="part" id="distribution">4 · Where to reach them</div><h2>Distribution</h2><p class="lead-s">Developers pick the search tool their framework, platform or marketplace ships by default. Checked Nov 10, 2026.</p>\n'
        '  <div class="tablewrap scroll"><table><thead><tr><th>Platform</th><th>Default today</th><th>Action</th></tr></thead><tbody>' +
        ''.join(f'<tr><td><b>{p}</b><div class="small">{t}</div></td><td>{d}</td><td>{a}</td></tr>' for p, t, d, a in DIST) + '</tbody></table></div>\n\n')

# ---------- targets ----------
tiles = (f'<button type="button" class="tile all" data-u="all" aria-pressed="false"><span class="t-dot"></span><span class="t-name">All use cases</span><span class="t-n">{total}</span></button>' +
         ''.join(f'<button type="button" class="tile" data-u="{g["id"]}" style="--c:{g["c"]}" aria-pressed="false"><span class="t-dot"></span><span class="t-name">{g["name"]}</span><span class="t-n">{len(g["rows"])}</span></button>' for g in groups))
segs = '<button type="button" class="seg" data-i="All" aria-pressed="true">All</button>' + ''.join(f'<button type="button" class="seg" data-i="{i}" aria-pressed="false">{i}</button>' for i in inds)
opts = '<option value="All">All providers</option>' + ''.join(f'<option value="{e(k)}">{e(k)} ({v})</option>' for k, v in sorted(provs.items(), key=lambda kv: -kv[1]))
targets = f'''<div class="part" id="targets">5 · Who to target</div><h2>Targets by use case</h2>
<p class="lead-s">Pick a use case to see its playbook and accounts, then narrow by industry or the search API they use today. Green = already on Exa (expand); amber = on another provider (win). Hover <span class="tip src">ⓘ</span> for sources.</p>
<div class="tiles" role="group" aria-label="Use case">{tiles}</div>
<div class="fbar" role="group" aria-label="Filters">
 <div class="fgroup"><span class="flab">Industry</span><span class="segs">{segs}</span></div>
 <div class="fgroup"><label class="flab" for="prov">Providers used</label><select id="prov">{opts}</select></div>
 <div class="fgroup fsearch"><label class="flab" for="q">Search</label><input type="search" id="q" placeholder="Search accounts"></div>
 <div class="freset"><button type="button" class="reset" id="reset">Reset filters</button></div>
</div>
<div id="strip"></div>
<div class="count" id="count" aria-live="polite"></div>
<div class="tablewrap acc-wrap"><table class="acc-t"><thead id="thead"></thead><tbody id="cards"></tbody></table></div>
<div class="empty" id="empty" hidden>No accounts match these filters. <button type="button" class="reset" onclick="document.getElementById('reset').click()">Reset filters</button></div>
'''
aside = ('<aside><div class="t">On this page</div><a href="#overview">Overview</a><a href="#community">Developer pain</a><a href="#plays">GTM plays</a><a href="#distribution">Distribution</a><a href="#targets">Target accounts</a>' +
         ''.join(f'<a class="sub" href="#targets" data-jump="{g["id"]}">{g["name"]}</a>' for g in groups) + '</aside>')

# ---------- assemble ----------
TITLE = 'Exa Target Accounts · Web Search API GTM'
DESC = f'Who Exa should target next: {total} accounts by agent use case, the developer pain behind them, GTM plays and distribution.'
URL = 'https://psinglap.github.io/exa-search-atlas/accounts/'
out = s
out = out.replace('Target Accounts · Web Search API GTM', TITLE)
out = re.sub(r'(<meta (?:name|property)="(?:description|og:description|twitter:description)" content=")[^"]*"', lambda m: m.group(1) + e(DESC) + '"', out)
out = out.replace('https://psinglap.github.io/websearch-api-eval/accounts/', URL)
out = out.replace('content="Web Search API Eval"', 'content="Exa Search Atlas"')
out = re.sub(r'<div class="top">.*?</div></div>', '<div class="top"><div class="in"><a class="brand" href="../">Exa Search Atlas</a><a class="n" href="../atlas/">Atlas</a>'
             '<a class="n keep on" href="./"><b>Target accounts</b></a><a class="n" href="https://psinglap.github.io/websearch-api-eval/">Benchmark</a></div></div>', out, count=1, flags=re.S)
hero = f'''<header class="hero">
 <div>
  <div class="eyebrow">GTM / Exa target accounts<span>November 10, 2026</span></div>
  <h1>Who Exa should target next, and why they buy</h1>
  <p class="dek">{total} accounts across {len(groups)} agent use cases, the developer pain behind them, seven GTM plays and where to reach buyers. Built on the live evaluation and public research.</p>
  <div class="author"><i></i><span>Pallavi Singla</span></div>
 </div>
 <div class="card"><div class="eyebrow" style="position:relative">Accounts · plays · distribution</div>
  <div class="big">Google for<br>AI agents</div>
  <div class="stats"><div><b>{total}</b><small>target accounts</small></div><div><b>{len(groups)}</b><small>agent use cases</small></div><div><b>{pd["pain_total"]}</b><small>developer complaints</small></div></div></div>
</header>'''
out = re.sub(r'<header class="hero">.*?</header>', lambda m: hero, out, count=1, flags=re.S)
out = re.sub(r'<article>.*?</article>', lambda m: '<article>\n' + overview + '\n' + community + '\n' + plays_sec + dist + targets + '</article>', out, count=1, flags=re.S)
out = re.sub(r'<aside>.*?</aside>', lambda m: aside, out, count=1, flags=re.S)
out = re.sub(r'<footer>.*?</footer>', '<footer>Research run Nov 10, 2026 from public sources (hover ⓘ). Funding marked UNVERIFIED could not be re-checked at source. Benchmark figures from the open <a href="https://psinglap.github.io/websearch-api-eval/">Web Search API evaluation</a> (run Oct 8, 2026). Independent research by Pallavi Singla; not affiliated with Exa.</footer>', out, count=1, flags=re.S)
out = re.sub(r'const DATA=\{.*?\};\n', lambda m: 'const DATA=' + data + ';\n', out, count=1, flags=re.S)
out = out.replace("const st={u:'voice'", f"const st={{u:'{groups[0]['id']}'")
out = out.replace('<th>How You.com helps</th>', '<th>How Exa helps</th>')
assert 'You.com helps' not in out
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w').write(out)
print('wrote', OUT, len(out), 'accounts', total, provs)
