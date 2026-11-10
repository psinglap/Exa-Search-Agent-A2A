"""Build agent-card/index.html (launch kit for an Exa A2A Agent Card) and agent-card/exa-agent-card.example.json.
Unofficial example by Pallavi Singla; not published or endorsed by Exa. Field names follow A2A spec v1.0 (a2a.proto)."""
import json, html, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / 'agent-card'
OUT.mkdir(exist_ok=True)
e = lambda x: html.escape(str(x), quote=False)
t = (HERE / 'templates/atlas_template.html').read_text()
style = t[t.find('<style'):t.find('</style>') + 8]
nav_style = re.search(r'<style>\.sitenav.*?</style>', t, re.S).group(0)
EVAL = 'https://psinglap.github.io/websearch-api-eval/'
SITE = 'https://psinglap.github.io/exa-search-atlas/'

# ---------- the example Agent Card (A2A v1.0 field names) ----------
CARD = {
  "name": "Exa Agent",
  "description": "Web research agent with its own search index. Send a task in plain language, optionally with a JSON Schema; get back schema-valid JSON with a citation for each field. Covers the open web plus people, company, paper and place indexes.",
  "supportedInterfaces": [
    {"url": "https://api.exa.ai/a2a/v1", "protocolBinding": "JSONRPC", "protocolVersion": "1.0"},
    {"url": "https://api.exa.ai/a2a/v1/rest", "protocolBinding": "HTTP+JSON", "protocolVersion": "1.0"}
  ],
  "provider": {"organization": "Exa", "url": "https://exa.ai"},
  "version": "0.1.0-example",
  "documentationUrl": "https://exa.ai/docs/reference/agent-api/overview",
  "iconUrl": "https://exa.ai/favicon.ico",
  "capabilities": {"streaming": True, "pushNotifications": True, "extendedAgentCard": False},
  "securitySchemes": {
    "exaApiKey": {"apiKeySecurityScheme": {"description": "Exa API key from dashboard.exa.ai", "location": "header", "name": "x-api-key"}},
    "bearer": {"httpAuthSecurityScheme": {"description": "Exa API key as a Bearer token", "scheme": "Bearer"}}
  },
  "securityRequirements": [{"schemes": {"exaApiKey": {"list": []}}}, {"schemes": {"bearer": {"list": []}}}],
  "defaultInputModes": ["text/plain", "application/json"],
  "defaultOutputModes": ["application/json", "text/plain"],
  "skills": [
    {"id": "web-research", "name": "Research a question",
     "description": "Searches the web, reads sources and returns a cited answer, or schema-valid JSON when a JSON Schema is sent. Effort sets depth: minimal $0.012 to xhigh $1.00 per task.",
     "tags": ["research", "search", "citations", "structured-output"],
     "examples": ["What changed in the EU AI Act implementation timeline this month? Cite primary sources.",
                  "Compare the pricing pages of the top 5 vector databases as JSON."]},
    {"id": "list-building", "name": "Build a list of companies or people",
     "description": "Finds every company or person that matches criteria, using Exa's company and 1B+ people indexes, and returns rows with a citation per field.",
     "tags": ["lead-generation", "companies", "people", "websets"],
     "examples": ["Series A-C fintechs in the EU that launched an AI agent in 2026, with a source for each.",
                  "Heads of data at US insurers with over 1,000 employees."]},
    {"id": "enrich-rows", "name": "Enrich rows you already have",
     "description": "Takes rows as JSON and fills in missing fields (funding, headcount, tech used, recent news) with a citation for each value.",
     "tags": ["enrichment", "crm", "data"],
     "examples": ["For these 50 accounts, add last funding round, HQ country and whether they mention SOC 2."]},
    {"id": "monitor", "name": "Watch for changes",
     "description": "Re-runs a search on a schedule and pushes new results to your webhook. Built on Exa Monitors ($2 per 1,000 runs).",
     "tags": ["monitoring", "alerts", "webhooks"],
     "examples": ["Tell me when any of these 20 competitors changes pricing or announces a funding round."]}
  ]
}
card_json = json.dumps(CARD, indent=2, ensure_ascii=False)
(OUT / 'exa-agent-card.example.json').write_text(card_json + '\n')

# ---------- example use case: messages ----------
SCHEMA = {"type": "object", "properties": {"accounts": {"type": "array", "items": {"type": "object",
          "properties": {"company": {"type": "string"}, "website": {"type": "string"}, "lastRound": {"type": "string"}, "agentLaunch": {"type": "string"}},
          "required": ["company", "website", "lastRound", "agentLaunch"]}}}, "required": ["accounts"]}
REQ = {"jsonrpc": "2.0", "id": 1, "method": "SendMessage", "params": {
  "message": {"messageId": "msg-7f3a", "role": "ROLE_USER", "parts": [
    {"text": "Find EU fintechs (Series A-C) that launched a customer-facing AI agent in 2026."},
    {"data": {"outputSchema": SCHEMA}, "mediaType": "application/json"}]},
  "configuration": {"acceptedOutputModes": ["application/json"], "returnImmediately": True},
  "metadata": {"skill": "list-building", "effort": "medium", "budget": {"maxCostDollars": 2}}}}
WORKING = {"jsonrpc": "2.0", "id": 1, "result": {"task": {"id": "task-91c2", "contextId": "ctx-41d0",
  "status": {"state": "TASK_STATE_WORKING", "timestamp": "2026-11-10T18:02:11Z"}}}}
DONE = {"jsonrpc": "2.0", "id": 2, "result": {"id": "task-91c2", "contextId": "ctx-41d0",
  "status": {"state": "TASK_STATE_COMPLETED", "timestamp": "2026-11-10T18:02:49Z"},
  "artifacts": [{"artifactId": "accounts", "name": "EU fintechs with AI agents", "parts": [{"mediaType": "application/json", "data": {"accounts": [
     {"company": "Northwind Pay", "website": "northwind.example", "lastRound": "Series B, Mar 2026", "agentLaunch": "Support agent, Jun 2026"},
     {"company": "Contoso Lend", "website": "contoso.example", "lastRound": "Series A, Jan 2026", "agentLaunch": "Underwriting copilot, Sep 2026"}]}}],
     "metadata": {"grounding": [{"field": "accounts[0].lastRound", "url": "https://news.example/northwind-series-b"},
                                {"field": "accounts[1].agentLaunch", "url": "https://contoso.example/blog/copilot"}],
                  "costDollars": 0.10}}]}}
pj = lambda o: e(json.dumps(o, indent=2, ensure_ascii=False))

EXTRA = '''<style>
.code{font:12.5px/1.55 var(--mono);background:var(--soft);border:1px solid var(--line);border-radius:10px;padding:14px 16px;overflow-x:auto;white-space:pre;margin:8px 0 4px;max-height:560px}
.lede2{font-size:17px;max-width:760px}
.warnbox{border:1px dashed var(--you);border-radius:10px;padding:10px 14px;background:var(--you-soft);font-size:14px;margin:14px 0}
.steps{display:grid;gap:14px;margin-top:10px}
.step{display:grid;grid-template-columns:34px 1fr;gap:12px;align-items:start}
.step .n{width:30px;height:30px;border-radius:50%;background:var(--you);color:#fff;display:grid;place-items:center;font-weight:700;font-family:var(--display)}
.step h4{margin:2px 0 4px;font-size:16px}
.step p{margin:0 0 6px;font-size:14.5px}
.flow5{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:8px;margin:14px 0}
@media (max-width:820px){.flow5{grid-template-columns:1fr}}
.flow5 div{border:1px solid var(--line);border-radius:10px;background:var(--sheet);padding:10px 12px;font-size:13.5px}
.flow5 b{display:block;font-family:var(--display);font-size:15px}
.flow5 .who{font:11px var(--mono);text-transform:uppercase;letter-spacing:.04em;color:var(--muted)}
.mh{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin:10px 0}
@media (max-width:760px){.mh{grid-template-columns:1fr}}
.mh div{border:1px solid var(--line);border-radius:10px;background:var(--sheet);padding:12px 14px;font-size:14px}
.mh b{display:block;font-family:var(--display);font-size:16px;margin-bottom:4px}
.article{max-width:760px;border:1px solid var(--line);border-radius:12px;background:var(--sheet);padding:22px 26px}
.article h3{font-family:var(--display);font-size:24px;margin:0 0 4px}
.article .by{font:12px var(--mono);color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
.article p{margin:10px 0}
.small a,.article a{color:inherit}
</style>'''

def tbl(head, rows, ycol=None):
    return ('<div class="tw"><table class="vt"><thead><tr>' + ''.join(f'<th>{h}</th>' for h in head) + '</tr></thead><tbody>' +
            ''.join('<tr' + (' class="y"' if ycol and r[0] in ycol else '') + '>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table></div>')

EXISTS = [
 ('<b>The agent</b>', 'Exa Agent API: a task plus an optional <code>outputSchema</code> returns schema-valid JSON in <code>output.structured</code>, with citations in <code>output.grounding</code>.', '<span class="pill g">Exists</span>'),
 ('<b>Depth and price</b>', '<code>effort</code> from <code>minimal</code> ($0.012) to <code>xhigh</code> ($1.00) per task; <code>budget.maxCostDollars</code> caps spend.', '<span class="pill g">Exists</span>'),
 ('<b>Long tasks</b>', 'Runs return an ID at once; poll <code>GET /agent/runs/{id}</code> or stream events (SSE).', '<span class="pill g">Exists</span>'),
 ('<b>Alerts</b>', 'Monitors v2 pushes new results to a webhook, $2 per 1,000 runs.', '<span class="pill g">Exists</span>'),
 ('<b>Enterprise listing</b>', 'Exa Agent is a launch partner in the Gemini Enterprise Agent Marketplace, which asks agents to support A2A.', '<span class="pill g">Exists</span>'),
 ('<b>The public card</b>', 'One JSON file at <code>exa.ai/.well-known/agent-card.json</code>, signed. Today that path returns 404.', '<span class="pill a">New: a file</span>'),
 ('<b>The A2A endpoint</b>', 'A thin layer that maps <code>SendMessage</code> → <code>POST /agent/runs</code> and <code>GetTask</code> → <code>GET /agent/runs/{id}</code>. May already exist behind the Gemini listing.', '<span class="pill a">New: a thin wrapper</span>'),
 ('<b>The story</b>', 'Name it, explain it, show it working, list it everywhere agents are bought.', '<span class="pill y">Product marketing</span>'),
]
MAP = [
 ('<code>name</code>, <code>description</code>', 'What a calling agent reads first to decide whether to hire Exa.', 'Exa Agent; one sentence on cited, schema-valid JSON.'),
 ('<code>supportedInterfaces</code>', 'Where and how to call: URL, protocol binding (<code>JSONRPC</code>, <code>HTTP+JSON</code>), protocol version.', 'Proposed <code>api.exa.ai/a2a/v1</code> (not live).'),
 ('<code>capabilities</code>', 'Streaming progress and push notifications to a webhook.', 'Agent API streams today; push maps to Monitors webhooks.'),
 ('<code>securitySchemes</code>', 'How the caller authenticates.', 'The same Exa API key, as <code>x-api-key</code> or Bearer.'),
 ('<code>skills</code>', 'The jobs Exa can be hired for, with examples a model can match against.', 'Research, list building, enrichment, monitoring.'),
 ('<code>signatures</code>', 'A signature (JWS) proving Exa published the card.', 'Left out here; the real card should be signed.'),
]
LAUNCH = [
 ('<b>T−4 weeks</b>', 'Positioning and naming', 'Lock the line ("Google answered people\'s queries. Exa takes agents\' assignments."), skill names and pricing per task. Confirm the A2A endpoint behind the Gemini listing.'),
 ('<b>T−3 weeks</b>', 'Build the assets', 'Signed card live in staging; docs page "Hire Exa from any agent"; 10-line quickstart (Python and JS); a 60-second demo video of one agent hiring Exa.'),
 ('<b>T−2 weeks</b>', 'Line up partners', 'Google Cloud (Gemini Enterprise), AWS (Marketplace A2A), Salesforce (AgentExchange), Coinbase (x402); a customer quote from a GTM or research agent team.'),
 ('<b>Launch day</b>', 'Publish', 'Card live at <code>/.well-known/agent-card.json</code>; Exa blog post; founder thread on X; Hacker News "Show HN"; PR to the A2A samples repo; listings updated.'),
 ('<b>T+1 to 4 weeks</b>', 'Prove it', 'Case study with numbers (tasks, tokens saved, time to answer); talk pitch for AI Engineer World\'s Fair; "Agent Card for search" write-up for the A2A community.'),
]
METRICS = [
 ('<b>Discovery</b>', 'Fetches of the Agent Card; distinct calling agents'),
 ('<b>Adoption</b>', 'A2A tasks a week; share of Agent API traffic that comes through A2A'),
 ('<b>Money</b>', 'Paid tasks; revenue per task; per-call payments (x402, MPP) once added'),
 ('<b>Story</b>', 'Mentions of "search agent" with Exa; listings live; partner co-marketing posts'),
]

ARTICLE = f'''<div class="article"><span class="by">Draft launch post · written as Exa might publish it · example only</span>
<h3>Hire Exa from any agent</h3>
<p><b>Exa Agent now has a public A2A Agent Card.</b> Any agent that speaks A2A, the open agent-to-agent protocol run by the Linux Foundation, can now find Exa, read what it can do and hand it a task. Gemini Enterprise, AWS AgentCore and Azure agents can all call it, as can your own agent.</p>
<p><b>Google answered people's queries. Exa takes agents' assignments.</b> A search API sends back links and leaves your agent to read them, so it pays in tokens and context for every page. Exa Agent takes the whole job instead: search, read, check, and return one schema-valid JSON result with a source for every field.</p>
<p><b>What you can hire it for.</b> The card lists four skills: research a question, build a list of companies or people, enrich rows you already have, and watch for changes. Each task has a set price, from $0.012 at minimal effort to $1.00 at xhigh, with a spending cap you control.</p>
<p><b>How it works.</b> Your agent fetches <code>exa.ai/.well-known/agent-card.json</code>, sends a <code>SendMessage</code> request with the task and an optional JSON Schema, follows progress by streaming or polling, and receives the result as an artifact. It uses the same Exa API key, so there is nothing new to sign up for.</p>
<p><b>Why a search agent and not just a search API.</b> Your agent's context stays small: one cited result instead of dozens of pages. Exa's own research found agents trained on Exa matched agents trained on Google results while using 69% fewer tokens. And Exa runs its own index of the web, people, companies, papers and places, so lists come back complete.</p>
<p><b>Get started.</b> Read the card, copy the 10-line quickstart, or find Exa Agent in the Gemini Enterprise Agent Marketplace.</p></div>'''

TALK = [
 '<b>Open with their win:</b> "Exa Agent is already in the Gemini Enterprise marketplace, which runs on A2A. The card is the public front door for what Exa already ships."',
 '<b>Make it small:</b> "No new product: one signed JSON file plus a thin A2A layer over <code>/agent/runs</code>. The work is naming, docs and distribution, which is product marketing."',
 '<b>Make it a category moment:</b> "No search company markets itself as an A2A agent yet. Being first lets Exa own \'the search agent other agents hire\'."',
 '<b>Offer the kit:</b> the example card, the use-case walkthrough, the draft post and the launch plan on this page.',
]

body = f'''</head><body>
{nav_style}
<div class="sitenav"><div class="in"><a class="b" href="../">Exa Search Atlas</a><a href="../atlas/">Atlas</a><a href="../accounts/">Target accounts</a><a class="on" href="./"><b>Agent Card</b></a><a href="{EVAL}">Benchmark</a></div></div>
<div class="deck" id="top">
  <div class="topline"><div class="brand">Exa Agent <span>Card</span></div><span class="eyebrow">launch kit · 10 Nov 2026 · Pallavi Singla</span></div>
  <div class="warnbox"><b>Unofficial example.</b> This is a proposal written by Pallavi Singla, not something Exa has published or endorsed. The endpoint URLs in the card are proposed and are not live. Field names follow the A2A spec v1.0.</div>

  <section class="slide" id="what">
    <div class="sl-head"><span class="sl-n">1</span><span class="eyebrow">What an Agent Card is, and why this is positioning</span></div>
    <h2 class="sl-h">A public business card for an agent: what it does, how to call it, how to pay.</h2>
    <p class="lede2">In <b>A2A</b> (Agent2Agent, the open protocol Google started and the Linux Foundation now runs; 150+ organizations), an agent publishes an <b>Agent Card</b>: a JSON file at <code>/.well-known/agent-card.json</code> that tells other agents its skills, endpoint and sign-in method. A calling agent reads the card, sends a task, and gets a result back. Exa already ships every part except the card itself.</p>
    <div class="flow5">
      <div><span class="who">Calling agent</span><b>1 · Discover</b>Fetches Exa's Agent Card</div>
      <div><span class="who">Calling agent</span><b>2 · Pick a skill</b>Matches its job to "Build a list"</div>
      <div><span class="who">Calling agent → Exa</span><b>3 · Send a task</b><code>SendMessage</code> with task + JSON Schema</div>
      <div><span class="who">Exa</span><b>4 · Work</b>Searches, reads, checks; streams status</div>
      <div><span class="who">Exa → calling agent</span><b>5 · Deliver</b>Cited JSON as an artifact, priced per task</div>
    </div>
    <h3 style="margin:18px 0 6px">What exists today vs what is new</h3>
    {tbl(['Part', 'Detail', 'Status'], EXISTS)}
    <p class="small" style="margin-top:6px">Sources: <a href="https://exa.ai/docs/reference/agent-api/overview" target="_blank" rel="noopener">Exa Agent API</a>, <a href="https://exa.ai/blog/monitors-v2" target="_blank" rel="noopener">Monitors v2</a>, <a href="https://exa.ai/blog/exa-google-cloud" target="_blank" rel="noopener">Exa + Google Cloud</a>, <a href="https://cloud.google.com/blog/topics/developers-practitioners/publish-agents-in-gemini-enterprise-and-google-cloud-marketplace" target="_blank" rel="noopener">Gemini Enterprise listing guide</a>, <a href="https://a2a-protocol.org/latest/specification/" target="_blank" rel="noopener">A2A spec v1.0</a>, <a href="https://linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year" target="_blank" rel="noopener">A2A at 150+ organizations</a>.</p>
  </section>

  <section class="slide" id="card">
    <div class="sl-head"><span class="sl-n">2</span><span class="eyebrow">The example card <span class="tag ours">proposal</span></span></div>
    <h2 class="sl-h">Four skills that match what buyers already use Exa for.</h2>
    {tbl(['Field', 'What it tells the calling agent', 'In this card'], MAP)}
    <p class="small" style="margin:12px 0 0"><a href="exa-agent-card.example.json">Download the JSON</a> · valid against the A2A v1.0 field names</p>
    <div class="code">{e(card_json)}</div>
  </section>

  <section class="slide" id="usecase">
    <div class="sl-head"><span class="sl-n">3</span><span class="eyebrow">Example use case: a sales agent hires Exa</span></div>
    <h2 class="sl-h">A CRM's sales agent needs a target list. It hires Exa for one task.</h2>
    <p class="lede2">A sales agent running on any A2A platform (Gemini Enterprise, Salesforce Agentforce, AWS AgentCore) is asked for "EU fintechs that launched an AI agent this year". Rather than running dozens of searches and reading every page itself, it hires Exa. The company data below is made up.</p>
    <div class="steps">
      <div class="step"><span class="n">1</span><div><h4>Discover</h4><p>The sales agent fetches <code>https://exa.ai/.well-known/agent-card.json</code>, sees the <code>list-building</code> skill and the API-key sign-in.</p></div></div>
      <div class="step"><span class="n">2</span><div><h4>Send the task</h4><p>One <code>SendMessage</code> call: the task in plain text, the JSON Schema it wants back, and the effort and budget. <code>returnImmediately</code> lets it carry on while Exa works.</p><div class="code">{pj(REQ)}</div></div></div>
      <div class="step"><span class="n">3</span><div><h4>Exa works</h4><p>Exa answers at once with a task in <code>TASK_STATE_WORKING</code>, then streams progress or lets the caller poll with <code>GetTask</code>. Behind the card this is <code>POST /agent/runs</code> with <code>effort: "medium"</code>.</p><div class="code">{pj(WORKING)}</div></div></div>
      <div class="step"><span class="n">4</span><div><h4>Deliver</h4><p>The finished task carries one artifact: schema-valid JSON, a source for each field, and the cost.</p><div class="code">{pj(DONE)}</div></div></div>
      <div class="step"><span class="n">5</span><div><h4>What the sales agent saved</h4><p>About 2K tokens came back instead of the pages themselves. In our <a href="{EVAL}">open test</a>, one Exa search with page content returned 4.7K–10.6K tokens, so 15 searches would add roughly 70K–160K tokens to the agent's context (an estimate). The cost was $0.10 for a medium-effort task.</p></div></div>
    </div>
  </section>

  <section class="slide" id="launch">
    <div class="sl-head"><span class="sl-n">4</span><span class="eyebrow">How to launch it: the product marketing plan</span></div>
    <h2 class="sl-h">Position it as the search agent other agents hire, then show it working.</h2>
    <div class="mh">
      <div><b>Fewer tokens</b>One cited result instead of dozens of pages. Proof: Exa's RL study (69% fewer tokens), Dynamic Highlights (95% fewer than full pages).</div>
      <div><b>Complete answers</b>Its own index of the web, 1B+ people, companies, papers and places. Proof: best precision@5 in the open benchmark.</div>
      <div><b>Found where agents are bought</b>Gemini Enterprise today; AWS Marketplace A2A, Salesforce AgentExchange and Microsoft next. Priced per task.</div>
    </div>
    <h3 style="margin:16px 0 6px">Timeline</h3>
    {tbl(['When', 'Step', 'What ships'], LAUNCH, ycol=['<b>Launch day</b>'])}
    <h3 style="margin:16px 0 6px">How to measure it</h3>
    {tbl(['Area', 'Metric'], METRICS)}
  </section>

  <section class="slide" id="article">
    <div class="sl-head"><span class="sl-n">5</span><span class="eyebrow">The launch article (draft)</span></div>
    <h2 class="sl-h">The post Exa could publish on launch day.</h2>
    {ARTICLE}
  </section>

  <section class="slide" id="talk">
    <div class="sl-head"><span class="sl-n">6</span><span class="eyebrow">How to pitch it on the call</span></div>
    <h2 class="sl-h">Four lines for the conversation.</h2>
    <div class="callout"><ul class="small" style="margin:0;padding-left:18px;display:grid;gap:6px">{''.join(f'<li>{x}</li>' for x in TALK)}</ul></div>
    <p class="small" style="margin-top:10px">Independent research by Pallavi Singla; not affiliated with or endorsed by Exa. More context: the <a href="../atlas/#a2a">Google for AI agents</a> section of the Atlas.</p>
  </section>
</div>
</body></html>'''

DESC = 'An example A2A Agent Card for Exa Agent, a walkthrough of one agent hiring Exa, a launch plan and a draft launch post. Unofficial proposal.'
head = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Exa Agent Card</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="{SITE}agent-card/"><meta property="og:type" content="website"><meta property="og:site_name" content="Exa Search Atlas"><meta property="og:title" content="Exa Agent Card: launch kit"><meta property="og:description" content="{DESC}"><meta property="og:url" content="{SITE}agent-card/">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
'''
(OUT / 'index.html').write_text(head + style + '\n' + EXTRA + '\n' + body)
print('wrote', OUT / 'index.html')
