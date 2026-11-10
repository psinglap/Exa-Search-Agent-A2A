"""Build index.html: example writeup "Exa Agent, the search agent your agents can hire", in the style of Exa's blog.
Example writeup by Pallavi Singla; not an Exa publication."""
import pathlib, html
ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = 'https://psinglap.github.io/Exa-Search-Agent-A2A/'
EVAL = 'https://psinglap.github.io/websearch-api-eval/'
esc = html.escape

def i(text, links):
    a = ' · '.join(f'<a href="{u}" target="_blank" rel="noopener">{esc(l)}</a>' for l, u in links)
    return f'<span class="i" tabindex="0" aria-label="Source">ⓘ<span class="pop">{esc(text)}<br>{a}</span></span>'

# ---------- where Exa Agent runs today ----------
RUNS = [
 ('Gemini Enterprise', 'Admins add Exa Agent from the Agent Marketplace; staff run web research from their workspace. "No code, no separate procurement."', i('Exa + Google Cloud, Apr 28, 2026.', [('Exa blog', 'https://exa.ai/blog/exa-google-cloud')])),
 ('Claude, Codex and other MCP clients', 'The <code>agent_run</code> tool in Exa MCP hands a research task to Exa Agent.', i('Exa changelog, Jul 1, 2026: "Exa Agent is now available within Exa MCP."', [('Changelog', 'https://exa.ai/docs/changelog')])),
 ('Pydantic AI', 'An <code>ExaAgent</code> capability lets any Pydantic AI agent "delegate a research task to an asynchronous Exa agent run".', i('Pydantic AI docs.', [('Pydantic AI', 'https://pydantic.dev/docs/ai/harness/exa-search/')])),
 ('AutoGPT', 'A no-code Exa Agent block for deep research, list building and enrichment.', i('AutoGPT integration docs.', [('AutoGPT', 'https://agpt.co/docs/integrations/block-integrations/agent')])),
]
runs = ''.join(f'<div class="rn"><b>{n}</b><p>{d} {s}</p></div>' for n, d, s in RUNS)

# ---------- customers building agents on Exa (case studies) ----------
CUST = [
 ('Sales agents', 'HubSpot', 'Breeze agents pull live people and company data into CRM work; Monitors start workflows when a company changes.', '40% better latency', 'Search · Monitors', 'https://exa.ai/customers/hubspot'),
 ('Lead agents', 'monday.com', 'Reps ask for leads in plain language and get structured people and company records in monday CRM.', '2.7M enrichments · 50% less research time', 'Search', 'https://exa.ai/customers/monday'),
 ('AI SDRs', '11x', 'Alice and Julian find each prospect\'s buying signals before they write outreach.', '7.2M+ searches · 2.7M+ Webset items', 'Search · Websets', 'https://exa.ai/customers/11x'),
 ('Code review', 'CodeRabbit', 'One Deep search call, only when outside context could change a review comment.', '70–75% fewer search calls · P50 7.1 s', 'Deep', 'https://exa.ai/customers/coderabbit'),
 ('Market research', 'Obvious', 'Builds cohorts of similar companies, with contacts, in one enriched call.', '20x faster · 99% lower cost', 'Websets', 'https://exa.ai/customers/obvious'),
 ('Finance alerts', 'Revolut', 'When a stock moves, an agent fetches the news behind it and notifies users.', '1,500+ alerts a week · 2x opens', 'Search', 'https://exa.ai/customers/revolut'),
]
cust = ''.join(f'<div class="cu"><span class="cu-k">{k}</span><b>{n}</b><p>{h}</p><span class="cu-m">{m}</span><span class="cu-p">{p} {i(n + " case study.", [("exa.ai/customers", u)])}</span></div>' for k, n, h, m, p, u in CUST)

# ---------- benchmark table (Exa 3.0, Oct 19, 2026) ----------
BENCH = [('BrowseComp', 'Research that takes many steps', '91.8%', '91.5%', '83.5%', '63.1%'),
         ('ATLAS', 'Agentic search', '42.0%', '37.2%', '28.2%', '24.8%'),
         ('WideSearch', 'Complete lists', '56.1%', '54.0%', '54.8%', '53.7%'),
         ('Company FindAll', 'Every matching company', '15.4', '14.2', '13.3', '9.7'),
         ('People FindAll', 'Every matching person', '7.6', '6.8', '3.8', '3.8'),
         ('WebCode', 'Code and docs', '75.5%', '69.9%', '68.0%', '64.5%'),
         ('FinSearchComp', 'Finance questions', '68.0%', '63.4%', '57.6%', '66.0%')]
bench = ''.join(f'<tr><td><b>{b}</b><span class="sub">{w}</span></td><td class="x">{a}</td><td>{p}</td><td>{br}</td><td>{pa}</td></tr>' for b, w, a, p, br, pa in BENCH)

PY = '''from exa_py import Exa

exa = Exa()  # reads EXA_API_KEY
run = exa.agent.runs.create(
    query="EU fintechs that launched an AI agent in 2026",
    effort="medium",
    output_schema={"type": "object", "properties": {"companies": {"type": "array"}}},
)
run = exa.agent.runs.poll_until_finished(run.id, poll_interval=4000)
print(run.output.structured)   # your JSON
print(run.output.grounding)    # a source for each field'''
OAI = '''from openai import OpenAI
client = OpenAI(base_url="https://api.exa.ai", api_key=EXA_API_KEY)

response = client.responses.create(
    model="exa-agent",
    input="Top 5 AI startups founded in 2025, with funding",
    reasoning={"effort": "medium"},
)
print(response.output_text)'''
CURL = '''curl -X POST https://api.exa.ai/agent/runs \\
  -H "x-api-key: $EXA_API_KEY" -H "Content-Type: application/json" \\
  -d '{"query": "EU fintechs that launched an AI agent in 2026", "effort": "medium"}\''''
MCP = '''# Claude Code
claude plugin install exa@claude-plugins-official

# Codex
codex mcp add exa --url "https://mcp.exa.ai/mcp?tools=web_search_exa,agent_run"

# Cursor and other MCP clients (mcp.json)
{"mcpServers": {"exa": {"type": "streamable-http",
  "url": "https://mcp.exa.ai/mcp?tools=web_search_exa,agent_run"}}}'''
TABS = [('python', 'Python SDK', PY, '<code>pip install exa-py</code> · also <code>npm i exa-js</code>'),
        ('openai', 'OpenAI SDK', OAI, 'Already on the OpenAI SDK? Point it at Exa and set <code>model="exa-agent"</code>.'),
        ('mcp', 'MCP', MCP, 'In Claude Code, Cursor or Codex, your agent gets an <code>agent_run</code> tool.'),
        ('curl', 'HTTP', CURL, 'Any language. You get a run ID at once; poll <code>GET /agent/runs/{id}</code> or stream.')]
tabs_btn = ''.join(f'<button type="button" class="tb{" on" if k == 0 else ""}" data-t="{t[0]}">{t[1]}</button>' for k, t in enumerate(TABS))
tabs_pan = ''.join(f'<div class="tp{" on" if k == 0 else ""}" data-t="{t[0]}"><p class="tn">{t[3]}</p><pre>{esc(t[2])}</pre></div>' for k, t in enumerate(TABS))

page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Exa Agent, the search agent your agents can hire</title>
<meta name="description" content="Example writeup: Exa Agent as the search agent other AI agents hire. Why it matters, where it runs, why it fits agent-to-agent, and how to call it. Not an Exa publication.">
<link rel="canonical" href="{SITE}">
<meta property="og:title" content="Exa Agent, the search agent your agents can hire"><meta property="og:description" content="Google answered people's queries. Exa takes agents' assignments.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500&family=Inter:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap">
<style>
:root{{--brand:#1F40ED;--brand-soft:#e9edfd;--ink:#111827;--muted:#6b6661;--line:#E8E6E5;--panel:#F9F8F7;--gray:#c9c4bf;
  --serif:"Newsreader",Georgia,serif;--sans:"Inter","Trebuchet MS",system-ui,sans-serif;--mono:"Geist Mono",ui-monospace,Menlo,monospace}}
*{{box-sizing:border-box}}
body{{margin:0;background:#fff;color:var(--ink);font:16.5px/1.65 var(--sans)}}
a{{color:var(--brand);text-decoration:none}}a:hover{{text-decoration:underline}}
.wide{{max-width:1120px;margin:0 auto;padding:0 20px}}
.col{{max-width:720px;margin:0 auto;padding:0 20px}}
h1{{font:400 clamp(30px,4.5vw,40px)/1.15 var(--serif);margin:48px 0 22px}}
h2{{font:400 28px/1.2 var(--serif);margin:52px 0 12px}}
p{{margin:0 0 16px}}
.hero{{border-radius:14px;padding:clamp(18px,4vw,44px);background:radial-gradient(120% 90% at 20% 10%,#7d94ff 0%,#2f4cf0 38%,#1328b8 75%,#0b1a86 100%)}}
.hero-in{{background:#f7f6f4;border-radius:12px;padding:18px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;align-items:stretch;position:relative}}
.hc{{background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px 14px;font-size:13.5px}}
.hc .lb{{font:500 10.5px var(--mono);letter-spacing:.07em;text-transform:uppercase;color:var(--muted);display:flex;justify-content:space-between;gap:8px}}
.hc .lb i{{font-style:normal;background:#f1efed;border-radius:5px;padding:1px 6px}}
.hc .q{{display:block;margin:10px 0;font-size:14.5px}}
.hc .sm{{font:11.5px/1.55 var(--mono);color:var(--muted)}}
.hc.mid{{text-align:center;display:grid;align-content:center;gap:8px;border-color:var(--brand)}}
.hc.mid .big{{font:400 30px var(--serif)}}
.dots{{display:flex;gap:6px;justify-content:center}}.dots span{{width:8px;height:8px;border-radius:50%;background:var(--brand);opacity:.25;animation:p 1.6s infinite}}.dots span:nth-child(2){{animation-delay:.2s}}.dots span:nth-child(3){{animation-delay:.4s}}.dots span:nth-child(4){{animation-delay:.6s}}
@keyframes p{{50%{{opacity:1}}}}
@media (prefers-reduced-motion:reduce){{.dots span{{animation:none;opacity:.6}}}}
.hc pre{{background:none;border:0;color:var(--ink);padding:0;margin:8px 0;font:11.5px/1.5 var(--mono);white-space:pre-wrap}}
.hc .s{{color:#16794c}}
.byline{{display:flex;gap:12px;align-items:center;margin:26px 0 22px;font-size:14px}}
.byline .av{{width:34px;height:34px;border-radius:50%;background:var(--brand-soft);color:var(--brand);display:grid;place-items:center;font:500 13px var(--mono)}}
.byline small{{display:block;color:var(--muted);font-size:12.5px}}
.lead{{font-size:18px}}
.panel{{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px;margin:18px 0}}
.steps{{background:#fff;border:1px solid var(--line);border-radius:10px}}
.st{{display:grid;grid-template-columns:30px 1fr 170px;gap:12px;padding:14px 16px;border-bottom:1px solid var(--line);align-items:start}}.st:last-child{{border-bottom:0}}
.st .n{{width:24px;height:24px;border-radius:50%;border:1px solid #cfcac5;display:grid;place-items:center;font:500 12px var(--mono);color:var(--muted)}}.st .n.on{{background:var(--brand);border-color:var(--brand);color:#fff}}
.st b{{display:block;font-weight:500}}.st span{{font-size:14px;color:var(--muted)}}
.st code{{font:11.5px var(--mono);color:var(--muted);text-align:right}}
.runs{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}}
.rn{{background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px 14px}}.rn b{{font-weight:500}}.rn p{{font-size:14px;margin:4px 0 0;color:#374151}}
.cus{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}}
.cu{{background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px 14px;display:grid;gap:4px;align-content:start}}
.cu-k{{font:500 10.5px var(--mono);letter-spacing:.07em;text-transform:uppercase;color:var(--brand)}}
.cu b{{font:400 21px/1.2 var(--serif)}}.cu p{{font-size:14px;margin:0;color:#374151}}
.cu-m{{font:500 13px var(--sans);color:var(--ink);background:var(--brand-soft);border-radius:6px;padding:3px 8px;justify-self:start}}
.cu-p{{font:11.5px var(--mono);color:var(--muted)}}
.bars2{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}}
.ch{{background:#fff;border:1px solid var(--line);border-radius:10px;padding:14px 16px;display:grid;gap:9px;align-content:start}}
.ch-h{{font:500 10.5px var(--mono);letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}}
.br{{display:grid;grid-template-columns:110px 1fr 48px;gap:10px;align-items:center;font-size:13.5px}}
.br b{{font:500 13px var(--mono);text-align:right}}
.tr{{height:12px;background:#f1efed;border-radius:99px;overflow:hidden}}.fl{{display:block;height:100%;border-radius:99px;background:var(--brand)}}.fl.g{{background:var(--gray)}}
.cap{{font-size:13px;color:var(--muted)}}
.tg{{font:500 10px var(--mono);letter-spacing:.05em;text-transform:uppercase;padding:1px 6px;border-radius:5px;background:#f1efed;color:var(--muted)}}.tg.ind{{background:var(--brand-soft);color:var(--brand)}}
.bt{{background:#fff;border:1px solid var(--line);border-radius:10px;overflow-x:auto}}
table{{border-collapse:collapse;width:100%;font-size:14px;min-width:520px}}
th{{font:500 12.5px var(--sans);color:var(--muted);text-align:center;padding:12px 10px}}th:first-child{{text-align:left}}
td{{padding:10px;text-align:center;border-top:1px solid var(--line)}}td:first-child{{text-align:left}}
td .sub{{display:block;font-size:12px;color:var(--muted)}}
th.x{{color:var(--ink);background:var(--brand-soft)}}td.x{{background:var(--brand-soft);font-weight:600}}
.hub{{display:grid;grid-template-columns:1fr auto 1fr;gap:16px;align-items:center}}
.hub .side{{display:grid;gap:8px}}
.hub .nd{{background:#fff;border:1px solid var(--line);border-radius:10px;padding:9px 12px;font-size:13.5px}}
.hub .nd b{{display:block;font-weight:500}}.hub .nd span{{font:11px var(--mono);color:var(--muted)}}
.hub .nd.next{{border-style:dashed}}
.hub .core{{width:150px;height:150px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#7d94ff,#1F40ED 70%);color:#fff;display:grid;place-items:center;text-align:center;font:400 22px/1.15 var(--serif);box-shadow:0 0 0 10px var(--brand-soft)}}
.hub .core small{{display:block;font:11px var(--mono);opacity:.85;margin-top:4px}}
.tabs{{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:10px}}
.tb{{font:500 13px var(--sans);border:1px solid var(--line);background:#fff;border-radius:99px;padding:6px 14px;cursor:pointer;color:var(--muted)}}.tb.on{{background:var(--ink);color:#fff;border-color:var(--ink)}}
.tp{{display:none}}.tp.on{{display:block}}.tn{{font-size:14px;color:var(--muted);margin:0 0 8px}}
pre{{background:#f3f2f0;border:1px solid var(--line);color:#1f2937;border-radius:10px;padding:14px 16px;overflow-x:auto;font:12.5px/1.6 var(--mono);margin:0}}
code{{font-family:var(--mono);font-size:.88em}}
.i{{position:relative;display:inline-block;color:var(--brand);cursor:help;font-size:12.5px;vertical-align:1px}}
.i .pop{{display:none;position:absolute;z-index:10;bottom:calc(100% + 6px);left:50%;transform:translateX(-50%);width:min(280px,78vw);background:#fff;color:var(--ink);border:1px solid var(--line);border-radius:10px;padding:10px 12px;font:12.5px/1.45 var(--sans);box-shadow:0 10px 30px rgba(17,24,39,.14);text-transform:none;letter-spacing:0}}
.i:hover .pop,.i:focus .pop,.i:focus-within .pop{{display:block}}
.sign{{font:400 26px/1.3 var(--serif);margin:40px 0 0;padding-top:22px;border-top:1px solid var(--line)}}
footer{{margin:28px auto 70px;color:var(--muted);font-size:13px}}
@media (max-width:860px){{.cus{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
@media (max-width:760px){{.hero-in,.cus,.bars2,.hub,.runs{{grid-template-columns:1fr}}.hub .core{{margin:6px auto}}.st{{grid-template-columns:30px 1fr}}.st code{{display:none}}.i .pop{{left:auto;right:-8px;transform:none}}.br{{grid-template-columns:92px 1fr 46px}}}}
</style></head><body>
<div class="col"><h1>Exa Agent, the search agent your agents can hire</h1></div>

<div class="wide"><div class="hero" role="img" aria-label="Your agent hands a task to Exa Agent and gets JSON with sources back">
  <div class="hero-in">
    <div class="hc"><span class="lb">Your agent <i>task</i></span><span class="q">“EU fintechs that launched an AI agent in 2026, with a source for each.”</span><span class="sm">schema: name · launch · source<br>effort: medium · cap: $2</span></div>
    <div class="hc mid"><span class="lb" style="justify-content:center">Exa Agent</span><span class="big">working</span><div class="dots"><span></span><span></span><span></span><span></span></div><span class="sm">search → read → check</span></div>
    <div class="hc"><span class="lb">Back to your agent <i>JSON</i></span><pre>{{"companies": [
  {{"name": "…",
   "launch": "Jun 2026",
   "source": <span class="s">"https://…"</span>}},
  … ]}}</pre><span class="sm">a source for every field</span></div>
  </div>
</div></div>

<div class="col">
<div class="byline"><span class="av">PS</span><div>Pallavi Singla<small>Example writeup · Nov 10, 2026 · not an Exa publication</small></div></div>

<p class="lead"><b>Exa Agent is search you can delegate.</b> Your agent describes the job. Exa does the searching and the reading, and returns one answer in the shape you asked for, with a source for every field.</p>
<p>Google gave people ten links and let them read. That works for a person who runs two or three searches. An agent can run up to 186 searches for one task {i('Measured across agentic search traces.', [('arXiv 2602.17518', 'https://arxiv.org/html/2602.17518')])}, and it pays for every page it reads in tokens, time and context. Where Google gave you links, Exa Agent gives your agent the answer.</p>

<h2>Why it matters</h2>
<p><b>Agents are now the main users of search.</b> By volume, agents already use the web more than people do {i('Exa, Aug 28, 2026.', [('Dynamic Highlights', 'https://exa.ai/blog/dynamic-highlights')])}. Search built for human clicks doesn't fit them.</p>
<p><b>Context is the budget.</b> Every token your agent reads costs money, and answers get worse as the context fills up {i('Chroma tested 18 models: ~300 focused tokens beat ~113K tokens holding the same answer.', [('Chroma', 'https://www.trychroma.com/research/context-rot')])}.</p>
<p><b>Delegation is how agents scale.</b> Hand research to a specialist, the way you'd hand it to a colleague, and get back a result your code can use straight away.</p>

<h2>How it works</h2>
<div class="panel"><div class="steps">
  <div class="st"><span class="n on">1</span><div><b>Describe the task</b><span>Plain language, plus a JSON Schema for the answer you want.</span></div><code>query · outputSchema</code></div>
  <div class="st"><span class="n">2</span><div><b>Exa searches</b><span>Its own index: the web, 1B+ people, companies, papers and places.</span></div><code>effort: minimal → ultra</code></div>
  <div class="st"><span class="n">3</span><div><b>Exa reads and checks</b><span>Exa reads the sources, so your agent doesn't have to.</span></div><code>budget.maxCostDollars</code></div>
  <div class="st"><span class="n">4</span><div><b>Your agent gets the answer</b><span>Schema-valid JSON, with a source for every field.</span></div><code>output.structured · grounding</code></div>
</div></div>

<h2>Where Exa Agent runs today</h2>
<p>Exa Agent launched in June 2026. It already sits inside the places where agents get built and bought.</p>
<div class="panel"><div class="runs">{runs}</div></div>

<h2>What teams are building on Exa</h2>
<p>Exa Agent runs on the same search layer that these teams already build their own agents on.</p>
<div class="panel"><div class="cus">{cust}</div></div>

<h2>Why Exa fits agent-to-agent</h2>
<p>When your agent hires another agent, check four things: how many tokens come back, whether the first results are the right ones, whether lists are complete, and whether it can handle research that takes many steps.</p>
<div class="panel"><div class="bars2">
  <div class="ch"><span class="ch-h">Tokens sent back to your agent</span>
    <div class="br"><span>Full page</span><span class="tr"><span class="fl g" style="width:100%"></span></span><b>100%</b></div>
    <div class="br"><span>Exa highlights</span><span class="tr"><span class="fl" style="width:5%"></span></span><b>5%</b></div>
    <span class="cap">95% fewer tokens for the same answer; 30% fewer tokens in agent loops, with 2.1% better quality. <span class="tg">Exa-reported</span> {i('Dynamic Highlights, Aug 28, 2026.', [('Dynamic Highlights', 'https://exa.ai/blog/dynamic-highlights')])}</span></div>
  <div class="ch"><span class="ch-h">On-topic share of the top 5 results</span>
    <div class="br"><span>Exa</span><span class="tr"><span class="fl" style="width:100%"></span></span><b>40%</b></div>
    <div class="br"><span>You.com</span><span class="tr"><span class="fl g" style="width:92%"></span></span><b>37%</b></div>
    <div class="br"><span>Tavily</span><span class="tr"><span class="fl g" style="width:65%"></span></span><b>26%</b></div>
    <div class="br"><span>Parallel</span><span class="tr"><span class="fl g" style="width:65%"></span></span><b>26%</b></div>
    <span class="cap">The right results first means fewer follow-up searches. <span class="tg ind">Independent</span> {i('Open, rerunnable benchmark: 30 agent queries x 3 runs per API, 8 Oct 2026.', [('Open benchmark', EVAL)])}</span></div>
</div>
<div class="bt" style="margin-top:10px"><table><thead><tr><th>Benchmark</th><th class="x">Exa 3.0</th><th>Perplexity</th><th>Brave</th><th>Parallel</th></tr></thead><tbody>{bench}</tbody></table></div>
<p class="cap" style="margin:8px 2px 0">Exa-reported, Oct 2026: each provider's best single-step search endpoint, run in the same agent harness. FindAll counts matching entities found per task {i('Exa 3.0 benchmark table.', [('Exa 3.0', 'https://exa.ai/blog/exa-3')])}. Agents trained on Exa also needed 69% fewer tokens to match agents trained on Google results {i('Exa RL study, May 13, 2026: 0.58B vs 1.89B tokens.', [('RL study', 'https://exa.ai/blog/rl-search-outcomes')])}.</p>
</div>

<h2>Where to find it</h2>
<div class="panel"><div class="hub">
  <div class="side">
    <div class="nd"><b>Exa Agent API</b><span>POST api.exa.ai/agent/runs</span></div>
    <div class="nd"><b>Python and JS SDKs</b><span>exa-py · exa-js</span></div>
    <div class="nd"><b>OpenAI SDK</b><span>model="exa-agent"</span></div>
  </div>
  <div class="core"><div>Exa Agent<small>one API key</small></div></div>
  <div class="side">
    <div class="nd"><b>MCP</b><span>agent_run · Claude Code, Cursor, Codex</span></div>
    <div class="nd"><b>Gemini Enterprise</b><span>Agent Marketplace</span></div>
    <div class="nd next"><b>Any A2A agent · next</b><span>Agent Card {i('A2A is the open agent-to-agent standard (Linux Foundation, 150+ organizations). A public card at exa.ai/.well-known/agent-card.json is a proposal in this example, not live.', [('A2A spec', 'https://a2a-protocol.org/latest/specification/'), ('Example card', 'exa-agent-card.example.json')])}</span></div>
  </div>
</div></div>
<p>Need only fast search inside a model call? Exa Search is the default web search on OpenRouter, and it's built into Vercel AI Gateway and Cloudflare {i('Exa Search, not the full agent.', [('OpenRouter', 'https://exa.ai/customers/openrouter'), ('Vercel', 'https://vercel.com/changelog/exa-joins-vercel-ai-gateway-agent-marketplace'), ('Cloudflare', 'https://developers.cloudflare.com/web-search/providers/')])}.</p>

<h2>How to call it</h2>
<div class="tabs" role="tablist">{tabs_btn}</div>
{tabs_pan}
<p style="margin-top:14px">You pay per task: $0.012 at <code>minimal</code> effort up to $1.00 at <code>xhigh</code>, with a spending cap you set {i('Exa Agent pricing. auto and ultra are metered, with default caps of $5 and $20.', [('Agent API', 'https://exa.ai/docs/reference/agent-api/overview')])}. Read the <a href="https://exa.ai/docs/reference/agent-api/overview" target="_blank" rel="noopener">Agent API docs</a> or <a href="https://dashboard.exa.ai" target="_blank" rel="noopener">get an API key</a> to start.</p>

<p class="sign">Give your agents a search agent.</p>
</div>
<footer class="col">Example writeup by Pallavi Singla, showing how Exa could position agent-to-agent search for customers. Not written, reviewed or endorsed by Exa. Customer stories and Exa benchmark numbers come from Exa's public pages; open-benchmark numbers come from an independent test.</footer>
<script>
document.querySelectorAll('.tb').forEach(b=>b.onclick=()=>{{document.querySelectorAll('.tb,.tp').forEach(x=>x.classList.toggle('on',x.dataset.t===b.dataset.t))}});
</script>
</body></html>'''
(ROOT / 'index.html').write_text(page)
print('wrote', ROOT / 'index.html')
