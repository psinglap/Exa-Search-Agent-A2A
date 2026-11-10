# Exa as "the search agent other agents hire": research brief

Prepared 2026-11-10. Every bullet carries the URL that was actually opened or returned in search. **[VENDOR]** = the company's own claim about itself. **[ESTIMATE]** = my reasoning, not a published number. **[SECONDARY]** = only seen in third-party coverage, not the primary source.

Terms used: **A2A** = Agent2Agent, Google's open protocol that lets one AI agent find, call and delegate tasks to another agent. **MCP** = Model Context Protocol, Anthropic's open protocol that connects an agent to a tool or data source. **Agent Card** = the JSON file an A2A agent publishes, listing its skills, endpoint and sign-in method (like a business card for agents). **x402** = an open standard that uses the HTTP "402 Payment Required" code so an agent can pay per request. **MPP** = Machine Payments Protocol (Stripe and Tempo). **AP2** = Agent Payments Protocol (Google). **ACP** = Agentic Commerce Protocol (Stripe and OpenAI). **Context rot** = models get less accurate as you add more text to their input, even when the answer is in there.

---

## Headline takeaways

1. **The "agents are the main user of search" claim is now on the record.** Exa: "Today, by volume, agents are the primary users of the web" (Aug 28, 2026) [VENDOR]. Exa's Series C post: "AI agents will search the web more than humans this year" (May 20, 2026) [VENDOR]. Sacra estimates Exa went from about 1B to about 2B searches a month between April and October 2026, and from about $10M to $100M annualized revenue (Nov 3, 2026).
2. **No one publishes a measured breakdown of what agents search for.** An academic paper from Feb 2026 says query logs for agent search "do not yet exist". This gap is the biggest opening for Exa: a "State of Agent Search" report built from Exa's own query data would be the first of its kind.
3. **The token cost argument is strong and well sourced.** A single web page is about 16k tokens as HTML (Cloudflare). OpenAI bills mini-model searches as a flat 8,000 input tokens per call. Exa says Dynamic Highlights cut tokens by 95% compared with full pages, and by about 30% in agent loops compared with standard highlights [VENDOR]. Chroma tested 18 models and every one got worse as input grew. Anthropic says subagents should return summaries of 1,000-2,000 tokens.
4. **Exa already ships the "agent you hire" shape.** Exa Agent API: one natural-language task in, schema-validated JSON plus citations out, fixed price tiers from $0.012 to $1.00 per run. It is also an MCP tool. On Gemini Enterprise Agent Marketplace, Google requires every listed agent to speak A2A and publish an Agent Card. Exa also takes x402 payments.
5. **Others already use "Google of AI agents".** Calcalist's headline (Aug 2025) used it for Tavily, and Sacra's headline (Nov 2026) uses it for Exa. Parallel owns "the web's second user: AI agents". Brave says "search API for AI". So "Google for agents" on its own won't stand out. The fresh angle is **"the search agent that other agents hire"**: Exa as a peer agent on A2A, paid per task and returning verified, structured answers.

---

## 1. What AI agents mostly use web search for

**Direct data on agent queries is thin. These are the best available proxies, each dated.**

| Source (date) | Finding | URL |
|---|---|---|
| NBER w34255 "How People Use ChatGPT" (Sep 2025) | Practical Guidance, Seeking Information and Writing are "nearly 80%" of conversations. Non-work use rose from 53% to more than 70%. | https://www.nber.org/papers/w34255 |
| Same study, secondary coverage | "Seeking Information" rose from 14% (Jul 2024) to about 24% (Jul 2025), and the authors call it "a very close substitute for web search" [SECONDARY] | https://searchenginejournal.com/chatgpt-study-1-in-4-conversations-now-seek-information |
| Harvard and Perplexity, "Adoption and Usage of AI Agents" (arXiv 2512.07828, Dec 8 2025) | Comet browser agent, hundreds of millions of interactions: **Productivity & Workflow plus Learning & Research = 57% of agentic queries**. The top 10 of 90 tasks = 55%. Personal use 55%, professional 30%, educational 16%. | https://arxiv.org/abs/2512.07828 |
| LangChain "State of Agent Engineering" (survey Nov 18 to Dec 2 2025, n=1,340) | Primary agent use case: **customer service 26.5%, research & data analysis 24.4%**, internal workflow automation 18%. 57.3% have agents in production. | https://langchain.com/state-of-agent-engineering |
| LangChain "State of AI Agents" (2024) | Research & summarization was the top use case at 58% [SECONDARY summary] | https://www.infoq.com/news/2024/12/ai-agents-langchain |
| Exa Series C post, Will Bryk (May 20 2026) [VENDOR] | Three types of demand: "**GTM agents need extremely comprehensive search over people and companies**". "**Coding agents need complex searches over public code / technical documentation**". Chat agents need speed and low cost (sub-200ms API). | https://exa.ai/blog/announcing-series-c |
| Exa Deep launch (Mar 4 2026) [VENDOR] | About **20% of Deep queries are scientific literature surveys** | https://exa.ai/blog/exa-deep |
| Sacra on Exa (Nov 3 2026) | Use mix: coding tools (early driver), multi-step agents, GTM prospecting and lead lists (HubSpot, monday.com, 11x), and personal agents (Exa added ecommerce, local, weather, flights, transit and sports search in Oct 2026) | https://sacra.com/research/100m-year-google-for-ai-agents/ |
| Anthropic web search tool docs (current) | Claude searches for: recent events and news; current prices, rates, scores and stats; "specific organizations, people, or products that might have changed"; explicit look-ups. It does **not** search for stable facts, code concepts or creative tasks. "Single-fact queries typically use 1–3 searches; comparative or multientity research can use 10 or more." | https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool |
| Menlo Ventures, State of GenAI in the Enterprise (Dec 2025) | Coding was about $4B of enterprise spend in 2025, more than half of departmental AI spend. Total GenAI spend was $37B. | https://menlovc.com/perspective/2025-the-state-of-generative-AI-in-the-enterprise/ |
| "A Picture of Agentic Search", Pezzuti et al. (arXiv 2602.17518, Feb 19 2026) | Agents run far more searches than humans: up to 186 searches in one trace, while humans stop after 2-3 rewrites. Queries from the same question overlap 35-83% (Jaccard similarity), so caching works. The paper says "behavioural datasets, query logs… capturing how agents generate queries… do not yet exist." | https://arxiv.org/html/2602.17518 |
| AIMultiple agentic search benchmark | Test-set categories (not telemetry): research, fact-checking, technical docs, real-time events, product comparisons, tool discovery | https://aimultiple.com/agentic-search |

**[ESTIMATE] Working use-case mix for the narrative.** This is a reasoned ranking from the sources above, **not** measured shares. Don't publish it as data.
1. Research and synthesis (deep research, literature, due diligence). Evidence: Comet 57% combined; LangChain 24-58%; Exa Deep 20% sci-lit.
2. Coding and docs lookup. Evidence: coding is the largest enterprise spend line; Exa names it a core need; exa-code exists.
3. People, company and lead lists (GTM). Evidence: Exa names it; HubSpot, 11x and monday.com; Parallel lists Actively and Clay.
4. Freshness, news, prices and facts. Evidence: these are Anthropic's triggers for searching.
5. Grounding and fact-checking inside customer-service agents. Evidence: customer service is the top LangChain use case.
6. Shopping and local. Evidence: only 2.1% of ChatGPT info-seeking was about products; Exa added these verticals in Oct 2026.

**Volume signals**
- Exa: about 1B searches a month (Apr 2026) rising to about 2B a month (Oct 2026) per Sacra. Revenue about $100M annualized in Sep 2026, up 10x year over year (Sacra estimate). https://sacra.com/research/100m-year-google-for-ai-agents/
- Exa homepage: "Join 900,000+ developers"; "Up to 25T tokens passed to models each week" [VENDOR]. https://exa.ai
- Exa Series C: 5,000+ companies, 400,000+ developers (May 2026); crawlers track 500B+ URLs; plans for "100s of thousands of searches per second" [VENDOR]. https://exa.ai/blog/announcing-series-c
- OpenRouter web plugin (backed by Exa): 73M search queries to date, 400+ models connected [VENDOR]. https://exa.ai/customers/openrouter
- Brave: its LLM Context API powers 22M+ answers a day inside Brave Search (Feb 12 2026) [VENDOR]. https://brave.com/blog/most-powerful-search-api-for-ai/
- Anthropic: agents use about 4x the tokens of chat and multi-agent systems about 15x. A multi-agent setup beat single-agent Opus 4 by 90.2% on Anthropic's internal research eval (Jun 2025) [VENDOR]. https://www.anthropic.com/engineering/multi-agent-research-system

---

## 2. Which agents use search most, with named examples and providers

| Agent type | Named examples, with the provider they publicly use | Source |
|---|---|---|
| **Coding agents** | Cursor (Exa), Cognition/Devin (Exa), CodeRabbit (Exa), Sourcegraph (Parallel), Warp (You.com MCP, Jul 2026) | https://exa.ai/blog/announcing-series-c ; https://exa.ai ; https://select.keenable.ai/r/ai-labs-agent-platforms-using-exa-parallel-and-tavily/SCzEfb17FNJWjTpWWJp3lw ; https://you.com/resources/the-ydc-mcp-server-comes-to-warp |
| **Sales / GTM agents** | HubSpot (Exa Monitors API: track companies, trigger workflows), 11x (Exa), monday.com (Exa), Clay (Parallel), Actively (Parallel, "track every potential lead 24/7") | https://exa.ai/customers/hubspot ; https://sacra.com/research/100m-year-google-for-ai-agents/ ; https://parallel.ai/blog/series-b |
| **Deep research / knowledge-work agents** | Notion (Parallel), Harvey legal (Parallel, 60+ jurisdictions), Manus (Parallel), Lindy (Parallel), Profound (Parallel), Opendoor HOA research (Parallel); Claude Research (Anthropic's own multi-agent setup) | https://parallel.ai/blog/series-b ; https://select.keenable.ai/r/ai-labs-agent-platforms-using-exa-parallel-and-tavily/SCzEfb17FNJWjTpWWJp3lw ; https://www.anthropic.com/engineering/multi-agent-research-system |
| **Model gateways / any-model chat** | OpenRouter web plugin (Exa, 400+ models); Databricks (Exa); NVIDIA (Tavily) | https://exa.ai/customers/openrouter ; Keenable report above |
| **Voice agents** | ElevenLabs ElevenAgents ships built-in integrations for Exa (webhook tool), Tavily, Perplexity, Parallel and Firecrawl. Exa runs a voice demo using Exa Instant. | https://elevenlabs.io/docs/eleven-agents/customization/integrations/exa.md ; https://docs.tavily.com/documentation/integrations/elevenlabs ; https://demo.exa.ai/voice/how-it-works |
| **Browser / computer-use agents** | Perplexity Comet uses Perplexity's own index (the 57% research/productivity stat above) | https://arxiv.org/abs/2512.07828 |
| **Enterprise assistants** | Gemini Enterprise: Exa Agent on Agent Marketplace, plus "Grounding with Exa" for Gemini models (Apr 2026). Exa homepage also names StackAI and Firefox. | https://exa.ai/blog/exa-google-cloud ; https://exa.ai |
| **Insurance / finance** | Two large US P&C insurers halved claims time; banks and hedge funds use it for underwriting intel (Parallel, unnamed) [VENDOR] | https://parallel.ai/blog/series-b |

Note: a Keenable report (Sep 9 2026) counts 45 public vendor-customer links across Exa, Parallel and Tavily, including "two frontier labs, 32 agent platforms".

---

## 3. Why a search *agent* beats a raw search API: the evidence

### 3a. Token cost (the strongest proof point)
- **Size of a raw page:** one Cloudflare blog post is 16,180 tokens as HTML and 3,150 as Markdown, an 80% cut (Feb 12 2026). https://blog.cloudflare.com/markdown-for-agents
- **What platforms bill:** OpenAI web search costs $10 per 1k calls plus search-content tokens at model rates. On gpt-4o-mini and gpt-4.1-mini, those tokens are billed as **"a fixed block of 8,000 input tokens per call."** https://developers.openai.com/api/docs/pricing
- **Anthropic:** web search costs **$10 per 1,000 searches** plus tokens. "Web search results retrieved throughout a conversation are counted as input tokens… in subsequent conversation turns," so raw results are paid for again on every later turn. Anthropic added "dynamic filtering" (`web_search_20260209`), where Claude writes code to trim results "before they reach the context window". In other words, the platform itself now accepts that raw results are too big. https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool
- **Exa Dynamic Highlights (Aug 28 2026) [VENDOR]:**
  - The answer to "the current mayor of SF" is 9 tokens, yet typical tools return 10,000+.
  - **95% average token cut compared with full page content.**
  - Standard highlights had already cut search tokens about 5x.
  - 40% fewer tokens than standard highlights with +3.8% quality (single-turn, 12k-character budget).
  - **About 30% fewer agent tokens with +2.1% quality in agent loops** (BrowseComp, WideSearch).
  - Reasoning traces are more than half of an agentic searcher's tokens.
  - https://exa.ai/blog/dynamic-highlights
- **Exa Series C [VENDOR]:** text extraction cuts LLM token counts by "over 20x". https://exa.ai/blog/announcing-series-c
- **exa-code (Sep 25 2025) [VENDOR]:** returns code context in "hundreds of tokens, not thousands"; its example uses under 500 tokens. https://exa.ai/blog/exa-code
- **Exa on Google Cloud [VENDOR]:** Highlights replace "tens of thousands of characters of page boilerplate". https://exa.ai/blog/exa-google-cloud
- **[ESTIMATE] Worked example for an article.** A research step pulls 10 pages.
  - Raw: about 10 × 10k = 100k input tokens (Exa's "10,000+" figure, consistent with Cloudflare's 16k-token page).
  - With a 95% cut: about 5k tokens.
  - In a 20-turn agent loop where results stay in context (Anthropic's billing rule), the raw path re-bills about 100k tokens per turn.
  - Cost formula: savings ≈ 95k tokens × turns × the model's input price. Plug in real model prices before you publish.

### 3b. Context rot: quality, not just cost
- **Chroma "Context Rot"** (Hong, Troynikov, Huber; Jul 14 2025): tested 18 LLMs (GPT-4.1, Claude 4, Gemini 2.5, Qwen3). On LongMemEval, focused inputs of about 300 tokens did "significantly" better than full inputs of about 113k tokens holding the same answer. Distractors made accuracy worse. https://www.trychroma.com/research/context-rot
- **Anthropic "Effective context engineering for AI agents"** (Sep 29 2025):
  - Find "the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome."
  - Models have an "attention budget" that every token spends.
  - Subagents should return "a condensed, distilled summary… often 1,000-2,000 tokens."
  - Tools should return "information that is token efficient."
  - **This is the main source for the "hire a search agent" idea:** Anthropic itself recommends delegating to a subagent that returns a short summary.
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

### 3c. Delegation, fewer round-trips and parallel fan-out
- **Exa Deep [VENDOR]:** "an agent that breaks down the query, searches in parallel, and iterates until it has what it needs". "One API call replaces a complex orchestration layer." `deep` takes 4-12s at $12 per 1k requests; `deep-reasoning` takes 12-50s at $15 per 1k. https://exa.ai/blog/exa-deep
- **Exa Agent API (launched Jun 16 2026; docs current):**
  - Takes a natural-language task plus an `effort` level (minimal through ultra).
  - Returns `outputSchema` → validated JSON in `output.structured`, and `output.grounding` with citations.
  - Runs async with polling or SSE (server-sent events, a stream of status updates).
  - Fixed per-run prices: minimal $0.012, low $0.025, medium $0.10, high $0.50, xhigh $1.00. `auto` and `ultra` are metered at $0.10 per compute unit (ACU), with cost caps of $5 and $20.
  - `budget.maxCostDollars` sets a $1-$100 ceiling.
  - Exposed as the `agent_run` tool in Exa MCP (mcp.exa.ai).
  - https://exa.ai/docs/reference/agent-api/overview.md ; https://runtimewire.com/article/exa-agent-api-web-research-launch
- **Anthropic multi-agent:** parallel subagents. Token usage explained about 80% of performance differences. Research time fell by up to 90% on complex queries [VENDOR]. https://www.anthropic.com/engineering/multi-agent-research-system
- **Agents vs humans:** humans stop after 2-3 query rewrites; agent traces reach 186 searches (arXiv 2602.17518). Handing the loop to a specialist agent keeps those searches out of the caller's context window.

### 3d. Structured outputs, verification and citations
- Exa Deep and Agent return JSON with **field-level citations and confidence ratings**. Deep allows up to 10 properties and 2 levels of nesting. https://exa.ai/blog/exa-deep
- Parallel Task API: Pydantic schema in, with "calibrated" confidence scores per field. It returns `null` instead of making up a missing field [VENDOR]. https://parallel.ai/blog/parallel-task-api
- Anthropic web search: citations are always on, and `cited_text` is capped at 150 characters and does not count toward tokens. https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool

### 3e. Caching and freshness
- Agent queries from the same question overlap 35-83% (Jaccard), which supports semantic caching (arXiv 2602.17518). https://arxiv.org/html/2602.17518
- Grounding with Exa fetches "fresh web results that Exa retrieves at request time" and matters most for news, product data and technical docs [VENDOR]. https://exa.ai/blog/exa-google-cloud
- Exa Monitors API watches the web for meaningful changes, and HubSpot uses it [VENDOR]. https://exa.ai/customers/hubspot

### 3f. Paying per task
- **Exa + x402:** Coinbase's launch page (Apr 7 2026) says agents can pay for Exa `/search` and `/contents` over HTTP 402 [SECONDARY: page returned 403 to me; seen in search results]. https://www.coinbase.com/developer-platform/discover/launches/exa
- **Nevermined:** a $7 x402 purchase buys Exa API credits (about 1,000 searches) [SECONDARY]. https://nevermined.ai/docs/integrations/exa.md
- **Parallel on MPP and x402:** Search $0.01, Extract $0.01 per URL, Task $0.30 (ultra) or $0.10 (pro). Paid in Stripe card or Tempo stablecoins via MPP, or USDC on Base via x402. https://docs.parallel.ai/integrations/agentic-payments ; https://www.parallel.ai/blog/tempo-stripe-mpp
- Market reality check on x402 volume: one analysis cites about $28k a day in real volume and about half of transactions flagged as artificial [SECONDARY]. https://forkast.news/half-of-x402s-transaction-volume-is-artificial-the-infrastructure-layer-keeps-building-anyway/

### 3g. Trust and identity
- A2A v1.0 adds **Signed Agent Cards**, giving cryptographic proof of identity (LF, Apr 9 2026). https://linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year
- Gemini Enterprise Marketplace agents must: comply with A2A, publish an Agent Card (skills, auth, endpoints), and use public access or OAuth 2.0 Authorization Code. Google reviews "functionality, security, and pricing model" before listing (Jul 7 2026). https://cloud.google.com/blog/topics/developers-practitioners/publish-agents-in-gemini-enterprise-and-google-cloud-marketplace

---

## 4. Protocol and marketplace landscape (as of Nov 2026)

### Protocols
| Protocol | Status | URL |
|---|---|---|
| **A2A** | Launched Apr 2025 with 50+ orgs. Donated to the Linux Foundation in Jun 2025. **150+ orgs; 22k+ GitHub stars; SDKs in Python, JS, Java, Go and .NET; v1.0 the first stable spec (Mar 2026)** with multi-tenancy and Signed Agent Cards. Built into Azure AI Foundry, Copilot Studio, Amazon Bedrock AgentCore Runtime and Google platforms (LF, Apr 9 2026). **Became an AAIF hosted project on Aug 17 2026.** | https://linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year ; https://aaif.io/blog/a2a-joins-aaif |
| **MCP** | 97M+ monthly SDK downloads and 10,000+ active public servers. Adopted by ChatGPT, Cursor, Gemini, Copilot and VS Code. Donated to AAIF on Dec 9 2025. | https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation |
| **AAIF (Agentic AI Foundation, Linux Foundation)** | Launched Dec 9 2025 with MCP, goose and AGENTS.md. 146 members (Feb 24 2026). Has working groups on identity/trust and agentic commerce. Added agentgateway (Jun 2026) and A2A (Aug 2026). About 247 orgs by Aug 2026 [SECONDARY]. | https://aaif.io/blog/aaifs-first-quarter-success-story-new-members-technical-wins-and-open-governance ; https://latent.space/wiki/aaif/ |
| **AP2** | Google, Sep 2025. Signed "mandates" record what the user authorized. Works as an A2A or MCP extension. 60+ partners at launch (Mastercard, PayPal, AmEx, Adyen…). Includes an A2A x402 extension built with Coinbase. | https://www.computerweekly.com/news/366631360/Google-Cloud-unveils-open-protocol-for-agentic-payments |
| **x402** | Coinbase and Cloudflare, Sep 2025. x402 Foundation under the Linux Foundation (Apr 2 2026); 40 members at launch, premier members include AWS, AmEx, Cloudflare, Coinbase, Google, Mastercard, Shopify, Solana, Stripe and Visa. | https://docs.cdp.coinbase.com/x402/support/x402-foundation |
| **MPP** | Stripe and Tempo, Mar 18 2026. Session-based and works across payment rails (cards via Visa, plus stablecoins). Parallel was listed in the MPP directory at launch. | https://www.theblock.co/post/394131/tempo-mainnet-goes-live-with-machine-payments-protocol-for-agents ; https://www.parallel.ai/blog/tempo-stripe-mpp |
| **ACP** | Stripe and OpenAI, Sep 2025 (Instant Checkout). OpenAI scaled Instant Checkout back in Mar 2026; the protocol is still active [SECONDARY]. | https://www.digitalcommerce360.com/2026/02/16/openai-expands-agentic-commerce-push/ |
| **AGNTCY** | Cisco, moved to the Linux Foundation Jul 29 2025, 75+ orgs. Agent Directory Service: a federated, signed registry built on OCI (the container-image standard). OASF describes agents across A2A and MCP. | https://www.linuxfoundation.org/press/linux-foundation-welcomes-the-agntcy-project-to-standardize-open-multi-agent-system-infrastructure-and-break-down-ai-agent-silos |
| **NANDA** | MIT Media Lab (Ramesh Raskar) agent index (AgentFacts). Designed to work with AGNTCY ADS. | https://ar5iv.labs.arxiv.org/html/2509.18787 |

### Agent marketplaces and registries
- **Gemini Enterprise Agent Platform + Agent Gallery/Marketplace** (Cloud Next, Apr 22 2026). Partners include Adobe, Atlassian, Deloitte, Lovable, Oracle, Replit, S&P Global, Salesforce, ServiceNow and Workday. There is a $750M partner fund. A2A and an Agent Card are required. https://cloud.google.com/blog/topics/partners/how-google-cloud-partner-ecosystem-is-building-the-agentic-enterprise
- **AWS Marketplace "AI Agents and Tools"** (Jul 16 2025) launched with 800-900+ listings and works with Bedrock AgentCore [SECONDARY counts]. Usage and contract pricing were added in Oct 2025. https://aws.amazon.com/about-aws/whats-new/2025/10/aws-marketplace-pricing-ai-agents-tools ; https://www.channelinsider.com/ai/the-new-aws-marketplace-category-for-ai-agents-and-tools/
- **Salesforce AgentExchange:** 100 public listings (Oct 2025). Merged with AppExchange and Slack Marketplace at TDX in Apr 2026 (13k+ listings, $50M fund) [SECONDARY]. https://www.globenewswire.com/news-release/2025/10/08/3163642/0/en/AgentExchange-Hits-Milestone-of-100-Public-Listings.html
- **Microsoft Agent Store:** no sourced numbers found. A2A is built into Copilot Studio and Foundry (see the LF release above).

### What Exa has shipped for agent-to-agent use
- **Exa Agent on Gemini Enterprise Agent Marketplace** as a launch partner (blog Apr 28 2026). "No code, no separate procurement." It does web research, similar-page search and URL extraction. **Grounding with Exa** for Gemini is in Private Preview. https://exa.ai/blog/exa-google-cloud ; https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-exa
  - **[ESTIMATE / inference]** Google requires every Marketplace agent to comply with A2A and publish an Agent Card. So Exa Agent is very likely already an A2A agent with a card. Exa's own post never says "A2A", which leaves the story untold and free for Exa to claim.
- **Exa Agent API** (Jun 2026). **Exa Deep** (revamped Mar 2026). **Websets**, **Monitors**, **Exa Connect** (Jun 2026: web research plus paid data sources like Similarweb, ZoomInfo and Crunchbase). **Exa MCP** (mcp.exa.ai, with `web_search_exa`, `get_code_context_exa` and `agent_run`). https://exa.ai ; https://exa.ai/docs/changelog.md ; https://sacra.com/research/100m-year-google-for-ai-agents/
- **x402 payments** for /search and /contents (Apr 2026) [SECONDARY].
- **Funding:** Series B $85M (2025); **Series C $250M at a $2.2B valuation led by a16z (May 20 2026)**. https://exa.ai/blog/announcing-series-c

### What competitors have done
- **Parallel:**
  - Task API (structured deep research with per-field confidence), Search, Extract and FindAll.
  - Series B of $100M at a $2B valuation (Sequoia, Apr 2026); $230M raised in total; 100k+ developers.
  - Takes payments over MPP and x402.
  - No A2A found.
  - https://parallel.ai/blog/series-b
- **Tavily:**
  - Bought by Nebius (agreement Feb 10 2026; reported up to $400M, $275M upfront [SECONDARY]).
  - Research API with JSON-schema output; MCP server.
  - Calcalist headline: "the Google of AI agents" (Aug 2025).
  - No A2A found.
  - https://www.storagenewsletter.com/2026/02/16/nebius-announces-agreement-to-acquire-tavily-to-add-agentic-search-to-its-ai-cloud-platform/ ; https://www.calcalistech.com/ctechnews/article/bj9q00tgdee
- **Perplexity:**
  - Search API launched Sep 25 2025 on the same index as its answer engine, plus the open-source `search_evals`.
  - Agent API launched Aug 13 2026 and is replacing Sonar, with end of support Sep 27 2026 [SECONDARY].
  - https://www.testingcatalog.com/perplexity-unveils-search-api-for-startups-enterprises-and-agent-builders ; https://usagepricing.com/blueprint/activity/perplexity-ai-2026-08-14-deprecation
- **You.com:**
  - Remote MCP server (Oct 2025) with you-search, you-research and you-contents, plus a keyless free profile.
  - Integrated with Warp (Jul 2026).
  - No A2A found.
  - https://docs.you.com/developer-resources/mcp-server
- **Brave:** LLM Context API (Feb 12 2026), "most powerful search API for AI". https://brave.com/blog/most-powerful-search-api-for-ai/

**White space:** none of the five competitors publicly markets itself as an **A2A peer agent**. Exa already meets Google's A2A listing bar and has the Agent API shape. That makes Exa the most credible company to claim "the search agent other agents hire".

---

## 5. Who already uses "Google for AI agents" (so we can stand apart)

- **Tavily:** Calcalist headline, Aug 6 2025: "Tavily raises $20M Series A to build the Google of AI agents". It's the headline's phrase; CEO Rotem Weiss is not quoted saying it. https://www.calcalistech.com/ctechnews/article/bj9q00tgdee
- **Exa (third-party label):** Sacra, Nov 3 2026: "$100M/year Google for AI agents". https://sacra.com/research/100m-year-google-for-ai-agents/
- **Exa's own wording over time:**
  - Started as Metaphor, a consumer search engine. Then "we're a search engine for AI" [VENDOR]. https://cerebralvalley.beehiiv.com/p/exa-prev-metaphor-aims-reshape-web-search
  - Series B and Series C headlines: **"…to Build the Search Engine for AIs"** (Series C May 20 2026). https://exa.ai/blog/announcing-series-c ; https://exa.ai/blog/announcing-series-b
  - Current homepage: **"The world's data for AI agents"**. https://exa.ai
  - Bryk (Sep 2025 talk write-up): it would be strange for "the same search engine that was optimal for humans" to suit AI too. "Give the AI system full control to get what information they want." "Perfect search requires test-time compute." https://jxnl.co/writing/2025/09/11/why-google-search-sucks-for-ai-will-bryk-exa/
  - "Today, by volume, agents are the primary users of the web" (Aug 2026). https://exa.ai/blog/dynamic-highlights
  - "the number of searches from LLMs will be 1000x more than Google searches today" (May 2026). https://exa.ai/blog/announcing-series-c
- **Parallel:** "scale the web for its second user: AI agents". "Web Infrastructure for AI Agents". https://parallel.ai/blog/series-b ; https://parallel.ai/
- **Insight Partners on Tavily:** "Power the Internet of Agents". https://www.insightpartners.com/ideas/tavily-raises-25-million-to-power-the-internet-of-agents/
- **Brave:** "search API for AI". https://brave.com/blog/most-powerful-search-api-for-ai/
- **Google itself** is now "agentic search" in its consumer product (I/O, May 19 2026), which muddies the "Google for agents" framing. https://techcrunch.com/2026/05/19/how-to-use-googles-new-ai-agents-to-go-beyond-your-standard-searches/

**How to stand apart:** "search engine for AIs" and "Google for agents" both describe a **tool**. The new claim is a **colleague**: *"Google answered humans' queries. Exa takes agents' assignments."* Supporting points:
- **Task in, verified JSON out:** fewer tokens and citations on every field.
- **Discoverable via Agent Card.**
- **Paid per task** (x402).
- **Already listed where enterprises buy agents** (Gemini Enterprise).

---

## 6. Where to publish, and what to write

### Channels, ranked by leverage for reaching agent builders
| Channel | Reach (sourced where possible) | Why it matters | URL |
|---|---|---|---|
| **TLDR AI** | 1.1M subscribers [VENDOR signup page]; 1M with 44% open rate on the ad page | Biggest technical AI newsletter; paid placement is available | https://signup.tldr.tech/ai ; https://advertise.tldr.tech/audiences/ai-engineers/ |
| **Latent Space** (newsletter + pod + AINews) | AINews brought about 80k subscribers when it joined in Jan 2026; combined reach 200k+ [SECONDARY] | The AI-engineer community hub; runs AI Engineer events | https://latent.space/wiki/ainews-3db8768a/ ; https://www.fast.io/resources/best-ai-newsletters-2026.md |
| **AI Engineer World's Fair** | 6,000+ attendees, 300 speakers, 29 tracks (Jun 29 to Jul 2 2026, Moscone West) | The premier room for agent builders; a talk there sets the narrative | https://www.snappr.com/news/story/ai-engineer-worlds-fair-2026 ; https://www.ai.engineer/faq |
| **Ben's Bites** | 115k-150k subscribers, 37% open rate [VENDOR ad page] | Builder and prosumer audience | https://ads.bensbites.com/ |
| **The Batch** (DeepLearning.AI) | No reliable count found (7M course learners is a different number) | Credibility with practitioners | https://www.deeplearning.ai/the-batch/about |
| **Hacker News** | No sourced figure | Technical benchmarks and open-source repos do well; marketing doesn't | — |
| **Simon Willison's blog** | No sourced figure | He covers agent and tool pricing closely (he wrote up Anthropic web search and multi-agent posts); a clean reproducible benchmark is the kind of thing he links | https://simonwillison.net/2025/Jun/14/multi-agent-research-system/ |
| **arXiv + Hugging Face blog/datasets** | — | The agent-query-log gap (arXiv 2602.17518) is an open invitation for a dataset paper | https://arxiv.org/html/2602.17518 |
| **Partner engineering blogs** (Google Cloud, LangChain, Vercel, Cloudflare, Anthropic cookbook) | — | Google already publishes A2A Marketplace guides; LangChain already runs Exa case studies | https://www.langchain.com/blog/exa ; https://cloud.google.com/blog/topics/developers-practitioners/publish-agents-in-gemini-enterprise-and-google-cloud-marketplace |
| **a16z blog/podcast** (Exa's Series C lead) | — | a16z podcast has already run "Building search for AI agents with Exa CEO Will Bryk" | https://www.audioscrape.com/podcast/a16z-podcast/episode/building-search-for-ai-agents-with-exa-ceo-will-bryk-40000 |
| **AAIF / Linux Foundation working groups** (identity and trust, agentic commerce) | — | Being in the room where A2A and MCP are governed makes Exa the reference search agent | https://aaif.io/blog/aaifs-first-quarter-success-story-new-members-technical-wins-and-open-governance |
| **X / YouTube** | — | Launch videos and demo clips; Bryk's own account | — |

### 10 assets to own the narrative
1. **"The Token Tax: what raw web search costs your agent"**
   - Format: open benchmark plus repo.
   - Content: run the same 100 agent tasks through raw pages, standard snippets, Exa Highlights and Exa Agent. Report tokens per answer, cost per answer, accuracy and latency.
   - Channels: HN, Simon Willison, TLDR AI.
   - Why it lands: Exa already has the 95% and 30% numbers; an outside, reproducible version turns a vendor claim into a reference people cite. Base it on Chroma's context-rot method.
2. **"State of Agent Search 2026"**
   - Format: data report built from Exa's anonymized query telemetry.
   - Content: query mix (coding, people/company, news, research), query length, searches per task, freshness needs.
   - Channels: a16z blog, Latent Space, press.
   - Why it lands: no one has published this; the arXiv paper says agent query logs "do not yet exist". This is the single most defensible asset.
3. **"An Agent Card for search"**
   - Format: spec post plus a live `/.well-known/agent-card.json` for Exa Agent, with signed card, skills, pricing and SLAs.
   - Channels: A2A GitHub discussions, the AAIF identity working group, Google Cloud blog co-post.
   - Why it lands: it positions Exa as the reference implementation of "search as an A2A peer".
4. **"Hire Exa from any agent in 10 lines: A2A quickstart"**
   - Format: tutorial covering ADK, LangGraph, Claude Agent SDK and Vercel AI SDK.
   - Channels: dev.to, LangChain blog, Vercel blog, YouTube.
   - Why it lands: it turns the narrative into a working habit for developers.
5. **"Delegate, don't query"**
   - Format: essay by Will Bryk.
   - Content: why agents should send tasks, not keywords. Ties Anthropic's "1,000-2,000 token subagent summary" guidance, Exa's "agents are the primary users of the web" line, and the Google-for-humans parallel together.
   - Channels: Exa blog, cross-posted to Latent Space; pitch to The Batch.
   - Why it lands: it defines the category in Exa's words.
6. **"Pay-per-answer: search priced like a contractor"**
   - Format: post plus live demo of an agent finding Exa via its Agent Card and paying over x402 or MPP for a medium-effort run.
   - Channels: Coinbase/x402, Stripe and Cloudflare dev blogs.
   - Why it lands: payments companies amplify working examples, and it compares well with Parallel's MPP listing.
7. **"Context-rot calculator"**
   - Format: interactive web tool.
   - Content: paste a task and model, and see tokens, cost and expected accuracy loss for raw results vs Exa output.
   - Channels: X, TLDR, product pages.
   - Why it lands: a shareable visual that makes the cost argument concrete.
8. **"Exa for coding agents: hundreds of tokens, not thousands"**
   - Format: case study with Cursor, Cognition or CodeRabbit, showing fewer hallucinations and fewer tokens.
   - Channels: AI Engineer World's Fair coding track, Latent Space pod.
   - Why it lands: coding is the largest enterprise AI spend line ($4B in 2025, Menlo).
9. **"The GTM agent's search stack"**
   - Format: case study with HubSpot (Monitors) or 11x, plus Websets examples.
   - Channels: SaaStr, Pavilion, LinkedIn, Salesforce AgentExchange listing.
   - Why it lands: GTM is the second named need in Exa's Series C post.
10. **An "Agents as users of the web" talk at AI Engineer World's Fair 2027, plus an arXiv dataset paper**
    - Content: release an anonymized agent query set (fills the ASQ gap).
    - Channels: AIEWF, arXiv, Hugging Face datasets.
    - Why it lands: academic credibility, and it becomes the dataset everyone cites.

---

## Open items / not verified
- No public, measured query-category percentages from any search provider. The use-case ranking in §1 is reasoned.
- The Exa x402 Coinbase page returned 403. The claim rests on search snippets and Nevermined docs.
- Exa's Gemini Enterprise listing being an A2A agent is an inference from Google's listing requirements. Exa has not stated it.
- Several counts are secondary only: Microsoft Agent Store, AWS listing count, Salesforce 13k, AAIF 247 members, x402 volumes and Perplexity Agent API dates.
