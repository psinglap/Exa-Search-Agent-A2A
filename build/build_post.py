"""Build agent-card/index.html: a short, customer-facing example post on Exa as the search agent other agents hire.
Styled after Exa's blog palette (brand blue #1F40ED, serif headlines). Example writeup by Pallavi Singla; not an Exa publication."""
import pathlib, html
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT
SITE = 'https://psinglap.github.io/Exa-Search-Agent-A2A/'
EVAL = 'https://psinglap.github.io/websearch-api-eval/'

def i(text, links):
    """ⓘ icon with a source popover."""
    a = ' · '.join(f'<a href="{u}" target="_blank" rel="noopener">{html.escape(l)}</a>' for l, u in links)
    return f'<span class="i" tabindex="0" aria-label="Source">ⓘ<span class="pop">{html.escape(text)}<br>{a}</span></span>'

USES = [
 ('Coding agents', '“Find how to stream responses with the current version of this SDK.”',
  'Working code examples from docs and repos, in hundreds of tokens, not thousands.',
  'Cursor, Cognition (Devin)', i('Exa names Cursor and Cognition as customers; exa-code returns "hundreds of tokens, not thousands".', [('exa.ai/customers', 'https://exa.ai/customers'), ('exa-code', 'https://exa.ai/blog/exa-code')])),
 ('Sales and GTM agents', '“List EU fintechs that launched an AI agent this year, with a source for each.”',
  'A complete list of companies or people, in your schema, one citation per field.',
  'HubSpot, 11x, monday.com', i('People search covers 1B+ profiles; HubSpot, 11x and monday.com are Exa case studies.', [('People search', 'https://exa.ai/blog/people-search-benchmark'), ('Customers', 'https://exa.ai/customers')])),
 ('Research copilots', '“What changed in this regulation in the last 12 months? Cite primary sources.”',
  'A cited brief, or schema-valid JSON, from the web, papers and filings.',
  'Notion AI Research Mode', i('Notion uses Exa in Research Mode.', [('Notion + Exa', 'https://exa.ai/blog/notion-exa')])),
 ('Support and voice agents', '“Is the payment outage still going on?”',
  'A fresh answer fast enough to fit inside a live turn.',
  'OpenRouter (73M searches)', i('Exa Lite is built for low latency; OpenRouter runs its web search through Exa.', [('Exa 3.0', 'https://exa.ai/blog/exa-3'), ('OpenRouter', 'https://exa.ai/customers/openrouter')])),
 ('Monitoring agents', '“Tell me when any of these competitors changes pricing.”',
  'New results pushed to your webhook as they appear, $2 per 1,000 runs.',
  'HubSpot, Revolut', i('Monitors v2 pushes results by webhook at $2 per 1,000 runs; Revolut sends 1,500+ alerts a week.', [('Monitors v2', 'https://exa.ai/blog/monitors-v2'), ('Revolut', 'https://exa.ai/customers/revolut')])),
]
cards = ''.join(f'''<div class="uc"><span class="uc-h">{h}</span><p class="ask">{a}</p><p><b>Exa returns</b> {r}</p><p class="who">Who does this today: {w} {src}</p></div>''' for h, a, r, w, src in USES)

CURL = '''curl -X POST https://api.exa.ai/agent/runs \\
  -H "x-api-key: $EXA_API_KEY" -H "Content-Type: application/json" \\
  -d '{
    "query": "EU fintechs that launched an AI agent in 2026",
    "effort": "medium",
    "outputSchema": {
      "type": "object",
      "properties": { "companies": { "type": "array", "items": {
        "type": "object",
        "properties": { "name": {"type": "string"}, "launch": {"type": "string"} }
      }}}
    }
  }\''''

page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Exa, the search agent your agents can hire</title>
<meta name="description" content="Example writeup: how Exa works as the search agent other AI agents hire, by use case. Not an Exa publication.">
<link rel="canonical" href="{SITE}">
<meta property="og:title" content="Exa, the search agent your agents can hire"><meta property="og:description" content="Google answered people's queries. Exa takes agents' assignments. An example writeup by Pallavi Singla.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500&family=Inter:wght@400;500;600&family=Geist+Mono:wght@400&display=swap">
<style>
:root{{--brand:#1F40ED;--brand-dark:#0d2189;--brand-soft:#eef1fe;--bg:#F7F6F4;--sheet:#ffffff;--ink:#0f172a;--muted:#5F5A54;--line:#E8E6E5;
  --serif:"Newsreader",Georgia,serif;--sans:"Inter","Trebuchet MS",system-ui,sans-serif;--mono:"Geist Mono",ui-monospace,Menlo,monospace}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16.5px/1.65 var(--sans)}}
a{{color:var(--brand)}}
.bar{{border-bottom:1px solid var(--line);background:var(--sheet);font-size:13px}}
.bar .in{{max-width:760px;margin:0 auto;padding:10px 20px;display:flex;gap:16px;flex-wrap:wrap;align-items:center;color:var(--muted)}}
.bar a{{color:var(--muted);text-decoration:none}}.bar a:hover{{color:var(--ink)}}.bar .b{{color:var(--ink);font-weight:600;margin-right:auto}}
main{{max-width:760px;margin:0 auto;padding:40px 20px 80px}}
.note{{display:inline-block;font:12px var(--mono);color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:3px 10px;background:var(--sheet)}}
h1{{font:400 clamp(34px,6vw,50px)/1.08 var(--serif);letter-spacing:-.01em;margin:18px 0 12px}}
.dek{{font:400 22px/1.4 var(--serif);color:var(--muted);margin:0 0 28px}}
h2{{font:400 28px/1.2 var(--serif);margin:44px 0 10px}}
p{{margin:0 0 14px}}
.flow{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin:18px 0 8px}}
.flow div{{background:var(--sheet);border:1px solid var(--line);border-radius:12px;padding:14px 16px;font-size:14.5px}}
.flow b{{display:block;color:var(--brand);font:500 12px var(--mono);text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}}
.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-top:16px}}
.uc{{background:var(--sheet);border:1px solid var(--line);border-radius:12px;padding:16px 18px}}
.uc:first-child{{grid-column:1/-1}}
.uc-h{{font:500 12px var(--mono);text-transform:uppercase;letter-spacing:.06em;color:var(--brand)}}
.uc p{{font-size:15px;margin:8px 0 0}}
.uc .ask{{font:italic 400 19px/1.35 var(--serif);color:var(--ink)}}
.uc .who{{color:var(--muted);font-size:13.5px}}
.why{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-top:14px}}
.why div{{border-top:2px solid var(--brand);padding-top:10px;font-size:15px}}
.why b{{display:block;font:500 20px/1.25 var(--serif);margin-bottom:4px}}
pre{{background:#0f172a;color:#e2e8f0;border-radius:12px;padding:16px 18px;overflow-x:auto;font:13px/1.55 var(--mono);margin:12px 0}}
code{{font-family:var(--mono);font-size:.9em}}
.cta{{background:var(--brand);color:#fff;border-radius:14px;padding:22px 24px;margin-top:40px}}
.cta h2{{margin:0 0 6px;color:#fff;font-size:26px}}.cta p{{margin:0;color:#dfe5ff}}
.i{{position:relative;display:inline-block;color:var(--brand);cursor:help;font-size:13px;vertical-align:1px}}
.i .pop{{display:none;position:absolute;z-index:10;bottom:calc(100% + 6px);left:50%;transform:translateX(-50%);width:min(300px,80vw);background:var(--sheet);color:var(--ink);border:1px solid var(--line);border-radius:10px;padding:10px 12px;font:13px/1.45 var(--sans);box-shadow:0 10px 30px rgba(15,23,42,.14)}}
.i:hover .pop,.i:focus .pop,.i:focus-within .pop{{display:block}}
footer{{margin-top:48px;padding-top:16px;border-top:1px solid var(--line);color:var(--muted);font-size:13px}}
details summary{{cursor:pointer}}
@media (max-width:640px){{.flow,.grid,.why{{grid-template-columns:1fr}}.i .pop{{left:auto;right:-10px;transform:none}}}}
</style></head><body>
<main>
<span class="note">Example writeup by Pallavi Singla · not an Exa publication</span>
<h1>Exa, the search agent your agents can hire</h1>
<p class="dek">Google answered people's queries. Exa takes agents' assignments.</p>

<p>Agents search far more than people do: up to 186 searches for one task, against two or three for a person {i('Measured across agentic search traces.', [('arXiv 2602.17518', 'https://arxiv.org/html/2602.17518')])}. A search API hands your agent links and pages to read, and your agent pays for every one of those tokens. Exa Agent takes the whole job instead and hands back one answer with its sources.</p>

<h2>How it works</h2>
<div class="flow">
  <div><b>1 · Hand off</b>Your agent sends a task in plain language, plus the JSON shape it wants back.</div>
  <div><b>2 · Exa works</b>Exa searches its own index of the web, people, companies and papers, reads and checks.</div>
  <div><b>3 · Answer</b>Your agent gets schema-valid JSON with a source for every field.</div>
</div>
<p>Any agent can find Exa through its <b>Agent Card</b>, a public file that tells other agents what Exa can do and how to call it, under the open A2A (agent-to-agent) standard {i('A2A is run by the Linux Foundation, with 150+ organizations. Exa Agent is listed in the Gemini Enterprise Agent Marketplace. Example card:', [('A2A', 'https://a2a-protocol.org/latest/specification/'), ('Exa + Google Cloud', 'https://exa.ai/blog/exa-google-cloud'), ('example card (JSON)', 'exa-agent-card.example.json')])}. You use the same Exa API key, and you pay per task.</p>

<h2>What your agents can hand to Exa</h2>
<div class="grid">{cards}</div>

<h2>Why hire a search agent, not just call a search API</h2>
<div class="why">
  <div><b>Smaller context</b>One cited result instead of dozens of pages: up to 95% fewer tokens than full pages {i('Exa Dynamic Highlights. Separately, agents trained on Exa matched Google-results-trained agents with 69% fewer tokens.', [('Dynamic Highlights', 'https://exa.ai/blog/dynamic-highlights'), ('RL study', 'https://exa.ai/blog/rl-search-outcomes')])}</div>
  <div><b>More complete answers</b>Exa's own index, plus 1B+ people and company records. Most on-topic results in an open benchmark {i('Best precision@5 (40%) of four APIs, run 8 Oct 2026.', [('Open benchmark', EVAL)])}</div>
  <div><b>A price per task</b>From $0.012 to $1.00, depending on depth, with a spending cap you set {i('Exa Agent effort levels: minimal $0.012, low $0.025, medium $0.10, high $0.50, xhigh $1.00.', [('Agent API', 'https://exa.ai/docs/reference/agent-api/overview')])}</div>
</div>

<h2>Try it</h2>
<p>This is the call your agent makes today, on Exa's Agent API.</p>
<pre>{html.escape(CURL)}</pre>
<p>You get back a run ID right away. Poll it or stream it; the finished run holds <code>output.structured</code> (your JSON) and <code>output.grounding</code> (the sources).</p>

<div class="cta"><h2>Give your agents a search agent.</h2><p>One task in, one cited answer out, wherever your agents run.</p></div>

<footer>
<p>Example writeup by Pallavi Singla to show how Exa could position agent-to-agent search for customers. Not written, reviewed or endorsed by Exa. Customer names are from Exa's public pages.</p>
<details><summary>Sources</summary><p style="margin-top:8px"><a href="https://exa.ai/docs/reference/agent-api/overview">Exa Agent API</a> · <a href="https://exa.ai/blog/exa-3">Exa 3.0</a> · <a href="https://exa.ai/blog/monitors-v2">Monitors v2</a> · <a href="https://exa.ai/blog/dynamic-highlights">Dynamic Highlights</a> · <a href="https://exa.ai/blog/rl-search-outcomes">RL study</a> · <a href="https://exa.ai/blog/exa-code">exa-code</a> · <a href="https://exa.ai/customers">Exa customers</a> · <a href="https://exa.ai/blog/exa-google-cloud">Exa + Google Cloud</a> · <a href="https://a2a-protocol.org/latest/specification/">A2A spec</a> · <a href="https://arxiv.org/html/2602.17518">arXiv 2602.17518</a> · <a href="{EVAL}">Open benchmark</a></p></details>
</footer>
</main>
</body></html>'''
(OUT / 'index.html').write_text(page)
print('wrote', OUT / 'index.html')
