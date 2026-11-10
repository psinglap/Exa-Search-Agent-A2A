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
 ('gemini.google.com.png', 'Gemini Enterprise', 'Admins add Exa Agent from the Agent Marketplace; staff run web research from their workspace. "No code, no separate procurement."', i('Exa + Google Cloud, Apr 28, 2026.', [('Exa blog', 'https://exa.ai/blog/exa-google-cloud')])),
 ('claude.ai.png', 'Claude, Codex and other MCP clients', 'The <code>agent_run</code> tool in Exa MCP hands a research task to Exa Agent.', i('Exa changelog, Jul 1, 2026: "Exa Agent is now available within Exa MCP."', [('Changelog', 'https://exa.ai/docs/changelog')])),
 ('pydantic.dev.png', 'Pydantic AI', 'An <code>ExaAgent</code> capability lets any Pydantic AI agent "delegate a research task to an asynchronous Exa agent run".', i('Pydantic AI docs.', [('Pydantic AI', 'https://pydantic.dev/docs/ai/harness/exa-search/')])),
 ('agpt.co.jpg', 'AutoGPT', 'A no-code Exa Agent block for deep research, list building and enrichment.', i('AutoGPT integration docs.', [('AutoGPT', 'https://agpt.co/docs/integrations/block-integrations/agent')])),
]
runs = ''.join(f'<div class="rn"><div class="rh"><img src="logos/{lg}" alt="" width="28" height="28"><b>{n}</b></div><p>{d} {s}</p></div>' for lg, n, d, s in RUNS)

# ---------- customers building agents on Exa (case studies) ----------
CUST = [
 ('hubspot.com.png', 'HubSpot', 'Sales agents', '40%', 'better latency', 'Breeze agents pull live people and company data into CRM work, and Monitors start a workflow when an account changes.', 'Search · Monitors', 'https://exa.ai/customers/hubspot'),
 ('monday.com.png', 'monday.com', 'Lead agents', '2.7M', 'enrichments, 50% less research time', 'Reps ask for leads in plain language and get structured people and company records in monday CRM.', 'Search', 'https://exa.ai/customers/monday'),
 ('11x.ai.png', '11x', 'AI SDRs', '7.2M+', 'searches, 2.7M+ Webset items', "Its agents Alice and Julian find each prospect's buying signals before they write outreach.", 'Search · Websets', 'https://exa.ai/customers/11x'),
 ('coderabbit.ai.png', 'CodeRabbit', 'Code review', '70–75%', 'fewer search calls', 'One Deep search call, made only when outside context could change a review comment. P50 is 7.1 s.', 'Deep', 'https://exa.ai/customers/coderabbit'),
 ('obvious.png', 'Obvious', 'Market research', '20x', 'faster, at 99% lower cost', 'Builds cohorts of similar companies, with contacts, in one enriched call.', 'Websets', 'https://exa.ai/customers/obvious'),
 ('revolut.com.png', 'Revolut', 'Finance alerts', '1,500+', 'alerts a week, 2x opens', 'When a stock moves, an agent fetches the news behind it and tells the user why.', 'Search', 'https://exa.ai/customers/revolut'),
]
cust = ''.join(f'''<div class="cu"><div class="cu-top"><img src="logos/{lg}" alt="{n} logo" width="36" height="36"><div><b>{n}</b><span class="cu-k">{k}</span></div></div>
<div class="cu-stat"><span class="num">{num}</span><span class="lab">{lab}</span></div><p>{h}</p><div class="cu-f">{''.join(f'<span class="chip">{x.strip()}</span>' for x in p.split('·'))}<span class="sp"></span>{i(n + " case study on exa.ai.", [("Read the case study", u)])}</div></div>''' for lg, n, k, num, lab, h, p, u in CUST)


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
.cus{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}}
.cu{{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px;display:flex;flex-direction:column;gap:10px;transition:box-shadow .15s,transform .15s}}
.cu:hover{{box-shadow:0 8px 24px rgba(17,24,39,.08);transform:translateY(-2px)}}
.cu-top{{display:flex;gap:10px;align-items:center}}
.cu-top img,.rh img{{border-radius:8px;border:1px solid var(--line);background:#fff;object-fit:contain;flex:none}}
.cu-top b{{display:block;font:500 17px/1.2 var(--sans)}}
.cu-k{{font:500 10.5px var(--mono);letter-spacing:.07em;text-transform:uppercase;color:var(--brand)}}
.cu-stat{{border-top:1px solid var(--line);padding-top:10px}}
.cu-stat .num{{display:block;font:400 34px/1 var(--serif);color:var(--brand)}}
.cu-stat .lab{{font-size:13px;color:var(--muted)}}
.cu p{{font-size:14px;margin:0;color:#374151;flex:1}}
.cu-f{{display:flex;gap:6px;align-items:center;flex-wrap:wrap}}
.chip{{font:500 11px var(--mono);background:#f1efed;color:var(--muted);border-radius:99px;padding:2px 8px}}
.sp{{flex:1}}
.rh{{display:flex;gap:10px;align-items:center}}
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

<p class="lead">If you've built an agent that does research, you've probably watched it do something a little painful. It searches, opens five pages, skims them, searches again, opens five more. It gets there in the end, but it spends a lot of tokens and time on work that isn't really its job.</p>
<p>Exa Agent is built for that moment. Instead of giving your agent links to read, you give Exa the question and the shape of the answer you want. Exa does the searching and reading on its side, then sends the answer back with a link behind every field, so you can check where each fact came from.</p>
<p>Google was designed for a person who runs two or three searches and clicks the best link. Agents don't work that way: one research task can set off as many as 186 searches {i('Measured across agentic search traces.', [('arXiv 2602.17518', 'https://arxiv.org/html/2602.17518')])}. Google gave people links. Exa gives agents answers.</p>

<h2>Why agent-to-agent, and why now</h2>
<p>Until recently, an agent that needed something it couldn't do itself had one option: call a tool and do the rest of the work on its own. A2A changes that. It's the open standard Google started in 2025 so that agents from different companies can find each other, hand over a task and get a result back. It now sits with the Linux Foundation, more than 150 organizations back it, and it's built into Google Cloud, AWS and Azure {i('A2A protocol: 150+ organizations, built into major cloud platforms.', [('Linux Foundation', 'https://linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year'), ('A2A spec', 'https://a2a-protocol.org/latest/specification/')])}.</p>
<p>That matters because companies are starting to buy agents the way they buy software. Google's Gemini Enterprise Agent Marketplace lists agents from partners that any employee's Gemini agent can call, and Google asks those agents to speak A2A {i("Google's guide to publishing agents in Gemini Enterprise and Google Cloud Marketplace.", [('Google Cloud', 'https://cloud.google.com/blog/topics/developers-practitioners/publish-agents-in-gemini-enterprise-and-google-cloud-marketplace')])}. Exa Agent was there at launch in April 2026 {i('Exa + Google Cloud, Apr 28, 2026: "No code, no separate procurement."', [('Exa blog', 'https://exa.ai/blog/exa-google-cloud')])}. So when a company's Gemini agent needs research done, Exa is already on the shelf, with no code to write and no new contract to sign.</p>
<p>Search is the job most agents hand off first. Almost every agent needs facts from the web, and very few want to read the web themselves. That's the opening for a search agent other agents can hire.</p>

<h2>What changes for your agent</h2>
<p><b>Most searches aren't typed by people anymore.</b> Exa says agents already make up most of the web's traffic by volume {i('Exa, Aug 28, 2026.', [('Dynamic Highlights', 'https://exa.ai/blog/dynamic-highlights')])}. Yet most search tools still return what a person wants to see, a list of links and snippets, and the agent has to read all of it before it can use any of it.</p>
<p><b>You pay for every page your agent reads, twice.</b> Once in tokens, and again in answer quality, because models get worse at finding the right fact as their context fills up. In one test, a focused 300-token input beat 113,000 tokens that held the same answer {i('Chroma tested 18 models.', [('Chroma', 'https://www.trychroma.com/research/context-rot')])}.</p>
<p><b>Your agent has better things to do.</b> A coding agent should be writing code, and a sales agent should be writing the email. Handing the research to Exa is like handing it to a colleague who comes back with a short summary and the sources attached.</p>

<h2>How it works</h2>
<div class="panel"><div class="steps">
  <div class="st"><span class="n on">1</span><div><b>Describe the task</b><span>Plain language, plus a JSON Schema for the answer you want.</span></div><code>query · outputSchema</code></div>
  <div class="st"><span class="n">2</span><div><b>Exa searches</b><span>Its own index: the web, 1B+ people, companies, papers and places.</span></div><code>effort: minimal → ultra</code></div>
  <div class="st"><span class="n">3</span><div><b>Exa reads and checks</b><span>Exa reads the sources, so your agent doesn't have to.</span></div><code>budget.maxCostDollars</code></div>
  <div class="st"><span class="n">4</span><div><b>Your agent gets the answer</b><span>Schema-valid JSON, with a source for every field.</span></div><code>output.structured · grounding</code></div>
</div></div>

<h2>Where Exa Agent runs today</h2>
<p>Exa Agent only launched in June, but you can already reach it from a few places developers and IT teams use every day.</p>
<div class="panel"><div class="runs">{runs}</div></div>

<h2>What teams are building on Exa</h2>
<p>Exa Agent is new, but the search underneath it isn't. Here's how some teams already use Exa inside their own agents.</p>
<div class="panel"><div class="cus">{cust}</div></div>

<h2>Why Exa fits agent-to-agent</h2>
<p>I tested four search APIs on 30 real agent tasks, three runs each, in an <a href="{EVAL}" target="_blank" rel="noopener">open benchmark you can rerun</a>. When one agent hands work to another, the calling agent cares about a few things above all: are the results on topic, is the answer right, how much text comes back to pay for, and what a correct answer costs. Exa led on relevance and on accuracy under pressure, and stayed near the top on tokens and cost.</p>
<div class="panel"><div class="bars2">
  <div class="ch"><span class="ch-h">On-topic share of the top 5 results</span>
    <div class="br"><span>Exa</span><span class="tr"><span class="fl" style="width:100%"></span></span><b>40%</b></div>
    <div class="br"><span>You.com</span><span class="tr"><span class="fl g" style="width:92%"></span></span><b>37%</b></div>
    <div class="br"><span>Tavily</span><span class="tr"><span class="fl g" style="width:65%"></span></span><b>26%</b></div>
    <div class="br"><span>Parallel</span><span class="tr"><span class="fl g" style="width:65%"></span></span><b>26%</b></div>
    <span class="cap">The best of the four. When the first results are the right ones, the calling agent needs fewer follow-up searches.</span></div>
  <div class="ch"><span class="ch-h">Tokens sent back per query</span>
    <div class="br"><span>You.com</span><span class="tr"><span class="fl g" style="width:100%"></span></span><b>41K</b></div>
    <div class="br"><span>Tavily</span><span class="tr"><span class="fl g" style="width:37%"></span></span><b>15K</b></div>
    <div class="br"><span>Exa</span><span class="tr"><span class="fl" style="width:20%"></span></span><b>8.4K</b></div>
    <div class="br"><span>Parallel</span><span class="tr"><span class="fl g" style="width:4%"></span></span><b>1.7K</b></div>
    <span class="cap">Top 5 results with page content. Exa sends back about a fifth of what You.com does. Parallel's short excerpts are smaller still, but less of what it returns is on topic.</span></div>
</div>
<div class="bt" style="margin-top:10px"><table><thead><tr><th>What the calling agent needs</th><th class="x">Exa</th><th>You.com</th><th>Tavily</th><th>Parallel</th></tr></thead><tbody>
<tr><td><b>On-topic results</b><span class="sub">Share of the top 5 that is relevant</span></td><td class="x">40%</td><td>37%</td><td>26%</td><td>26%</td></tr>
<tr><td><b>Right answer under pressure</b><span class="sub">Insurance: live catastrophe facts mid-call</span></td><td class="x">75%</td><td>65%</td><td>67%</td><td>67%</td></tr>
<tr><td><b>Small hand-back</b><span class="sub">Tokens per query, top 5 with content</span></td><td class="x">8.4K</td><td>41K</td><td>15K</td><td>1.7K</td></tr>
<tr><td><b>Cost of a correct answer</b><span class="sub">Search cost per correct answer</span></td><td class="x">$0.012</td><td>$0.026</td><td>$0.016</td><td>$0.008</td></tr>
<tr><td><b>Speed</b><span class="sub">Median response time</span></td><td class="x">1.1 s</td><td>0.6 s</td><td>1.9 s</td><td>2.0 s</td></tr>
</tbody></table></div>
<p class="cap" style="margin:8px 2px 0">Open benchmark, run Oct 8, 2026: 30 agent queries across GTM, insurance and finance, 3 runs each, every API on its default settings. The full scorecard, including empty results and accuracy by use case, is on the <a href="{EVAL}" target="_blank" rel="noopener">benchmark site</a>.</p>
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
<p style="margin-top:14px">Pricing is per task, so you know the cost up front: $0.012 for a quick lookup at <code>minimal</code> effort, up to $1.00 for a deep one at <code>xhigh</code>, and you can set a cap {i('Exa Agent pricing. auto and ultra are metered, with default caps of $5 and $20.', [('Agent API', 'https://exa.ai/docs/reference/agent-api/overview')])}. The <a href="https://exa.ai/docs/reference/agent-api/overview" target="_blank" rel="noopener">Agent API docs</a> have the full reference, or <a href="https://dashboard.exa.ai" target="_blank" rel="noopener">grab an API key</a> and try the snippet above.</p>

<p class="sign">Next time your agent opens its tenth browser tab, try handing the question to Exa instead.</p>
</div>
<footer class="col">Example writeup by Pallavi Singla, showing how Exa could position agent-to-agent search for customers. Not written, reviewed or endorsed by Exa. Customer stories come from Exa's public case studies. Benchmark numbers come from my open, rerunnable test of four search APIs.</footer>
<script>
document.querySelectorAll('.tb').forEach(b=>b.onclick=()=>{{document.querySelectorAll('.tb,.tp').forEach(x=>x.classList.toggle('on',x.dataset.t===b.dataset.t))}});
</script>
</body></html>'''
(ROOT / 'index.html').write_text(page)
print('wrote', ROOT / 'index.html')
