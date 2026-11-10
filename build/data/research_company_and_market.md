# Exa (exa.ai): company research for a product-marketing briefing
Researched 2026-11-10. Every fact has a source URL. UNVERIFIED means no primary source was found. "Reasoned estimate" means my own sizing, not a published figure.

Background already verified in Oct 2026 and reused here without re-checking: Series B and Series C details, Exa Instant (Feb 12, 2026), Sacra's ~$10M ARR estimate (Sep 2025), Monitors (Mar 2026), Cloudflare Web Search beta, OpenRouter default, and the psinglap benchmark (run 2026-10-08).

---

## 0. Headline changes since the October brief
- **Exa passed $100M annualized revenue** (blog, Oct 13, 2026). The post says revenue grew about 10x a year for 3 years, Exa serves 2B requests a month and 200k+ teams, and Exa predicts "agents will search 1000x more than humans by 2030." https://exa.ai/blog/100m-run-rate
  - For comparison, Sacra estimated ~$10M ARR in Sep 2025, so that is about 10x in roughly 13 months. https://sacra.com/research/exa-at-10m-growing-11x-yoy
- **Exa 3.0** (Oct 19, 2026) claims #1 on all 8 benchmarks against Perplexity, Brave and Parallel, including BrowseComp 91.8%, WebCode 75.5% and FinSearchComp 68.0%. Exa also claims #1 on the Artificial Analysis Search Index (Auto 80.3, Lite 79.2). The release added a new **Lite** tier ($4/1k; Auto is $7/1k) and made Dynamic Highlights generally available at no extra charge. The index tracks 2T+ URLs and serves 100B pages. https://exa.ai/blog/exa-3 · https://exa.ai/blog/artificial-analysis-exa-3-best-search-api
- **Monitors v2** (Oct 29, 2026) cut the price from $15 to **$2 per 1k runs** and pushes results by webhook (`monitor.run.completed`). https://exa.ai/blog/monitors-v2
- **Firefox** (Aug 17, 2026): Exa powers Smart Window on desktop and Quick Answers on iOS, with zero data retention. https://exa.ai/blog/exa-firefox
- **Vercel AI Gateway** (Aug 19, 2026): Exa became a built-in tool, `gateway.tools.exaSearch()`, billed at list price with no markup. https://vercel.com/changelog/exa-joins-vercel-ai-gateway-agent-marketplace
- **Older search types are now legacy.** `fast`, `instant` and `deep-reasoning` were marked legacy on Oct 19, 2026, with `lite`, `auto`, `deep` and Exa Agent as replacements. This means "Exa Instant" (Feb 2026) has already been superseded. https://releasebot.io/updates/exa

## 1. Exa today

### Product line (Nov 2026)
| Product | Status and facts | Source |
|---|---|---|
| **Search**: `lite`, `auto`, `deep-lite`, `deep`; legacy: `fast`, `instant`, `deep-reasoning` | Lite and Instant cost $4/1k; Auto and Fast $7/1k; Deep $12/1k; deep-reasoning $15/1k; each result over 10 adds $1/1k. Latency: Lite ~450 ms, Auto ~1 s, Deep 4–15 s. | https://exa.ai/pricing · https://exa.ai/enterprise |
| **Contents** | $1 per 1k pages per content type. Dynamic Highlights claims up to 95% fewer tokens than full page text. | https://exa.ai/pricing · https://exa.ai/blog/exa-3 |
| **Answer** | $5/1k | https://exa.ai/pricing |
| **Research API** (`/research`) | **Retired Apr 1, 2026**, replaced first by `deep-reasoning`, which became legacy on Oct 19, 2026. Exa now points long-running research to Exa Agent. | https://exa.ai/docs/changelog |
| **Exa Agent** (Jun 16, 2026) | Deep research, list building and enrichment, using subagents. Fixed effort levels cost $0.012 (minimal) to $1.00 (xhigh) per request. Metered `auto` defaults to a $5 cap. Usage is billed at $0.10 per ACU, $0.005 per search, $0.02 per email and $0.07 per phone number. Supports `outputSchema` (structured output). Added to MCP Jul 1, 2026. | https://exa.ai/blog/exa-agent · https://exa.ai/pricing |
| **Agent Ultra** (Sep 25, 2026) | Highest effort level. Defaults to a $20 cap, runs 5 min to 3 h, and keeps partial results if stopped. Exa claims it beats Opus 5.5 by 12.6% on WANDR. | https://exa.ai/blog/exa-agent-ultra · https://releasebot.io/updates/exa |
| **Exa Connect** (Jun 24, 2026) | A marketplace of paid data providers that Exa Agent can call through `dataSources`. Self-serve providers: Similarweb, Baselayer, Fiber.ai, Affiliate.com, Financial Datasets, Jinko, Particle. On request: ZoomInfo, Crunchbase, Harmonic, DefinitiveHealthcare, Faraday, Intellizence, Kernel. Calls cost $0.005–$0.03 each on top of Agent pricing. Providers set their own prices. | https://exa.ai/connect · https://alphasignal.ai/news/exa-connect-unlocks-private-commercial-data-for-ai-agents |
| **Monitors** (v1 Mar 2026; v2 Oct 29, 2026) | Scheduled search that delivers results by webhook. Each update can be a summary or JSON with a confidence level per field. $2/1k runs. | https://exa.ai/blog/monitors-v2 |
| **Websets** | Still in the nav and served from a separate site (websets.exa.ai). 2026 pricing UNVERIFIED because the page returned HTTP 429. | https://exa.ai/ |
| **People search** | Launched Dec 19, 2025 with 1B+ profiles; the `people` category replaced `linkedin`. Enriched person and organization profiles added Jul 23, 2026. | https://exa.ai/docs/changelog |
| **Company search** | Launched Jan 21, 2026 using a fine-tuned retrieval model. Added to Lite on Oct 19, 2026. | https://exa.ai/docs/changelog |
| **Publications** | Index of ~350M works (Jul 23, 2026); the `publication` category replaces `research paper`. | https://releasebot.io/updates/exa |
| **Places** (Oct 5, 2026) | 211M local businesses | https://exa.ai/blog/places-search |
| **Podcasts** (Oct 29, 2026) | 3.2M episodes with full transcripts, at no extra charge | https://exa.ai/blog/podcast-search |
| **Snapshot** (Sep 17, 2026, research preview) | Search the web as of a past date (`snapshotAsOf`), drawing on 400B+ snapshots. Use cases: reinforcement-learning (RL) evaluations without answer leakage, and financial backtesting. Price: contact sales. | https://exa.ai/blog/exa-snapshot |
| **Code search / exa-code** (Sep 25, 2025) | Web context for coding agents. Exa's comparison page cites 1B+ pages of code search and the WebCode benchmark (Mar 23, 2026). No 2026 changelog entry for a "Context API" (UNVERIFIED). | https://exa.ai/blog/exa-code · https://exa.ai/versus/parallel · https://exa.ai/blog/webcode |
| **MCP server** | Free tier added Feb 2, 2026: no key needed, 3 QPS (queries per second), 150 calls a day. `agent_run` tool added Jul 1, 2026. | https://exa.ai/docs/changelog |
| **Exa Library** | Listed on the enterprise page; no details found (UNVERIFIED). | https://exa.ai/enterprise |
| **Agent and A2A offering** | Exa Agent is listed in the **Gemini Enterprise Agent Marketplace** (Apr 2026). No A2A Agent Card: `exa.ai/.well-known/agent-card.json` returns 404 (checked 2026-11-10). | https://exa.ai/blog/exa-google-cloud |

### Pricing and free tier
- New accounts get **$10 a month in free credit** with no card required, plus a one-time $10 onboarding bonus. https://exa.ai/pricing
- According to a third-party tracker, the signup credit dropped from $20 to a $10 bonus on Oct 23, 2026, and the bonus is now paid only after onboarding is completed. https://www.usagepricing.com/blueprint/activity/exa-ai-2026-10-23-free-signup-credit-cut
- **Enterprise:** an annual plan at $12k upfront includes $12k of credit, 25 QPS and zero data retention (ZDR). Enterprise plans also offer up to 1,000 results per search, custom indexes, SLAs, a HIPAA mode with a business associate agreement (BAA), SSO and SCIM, a dedicated Slack channel and forward-deployed engineers. https://exa.ai/pricing · https://exa.ai/enterprise
- **Compliance:** SOC 2 Type II, GDPR, CCPA, HIPAA with a BAA, and ZDR. ZDR has applied across search products since Aug 18, 2025. https://exa.ai/ · https://exa.ai/blog/zdr-search-engine

### Funding, revenue and headcount
- **Series C:** $250M at a $2.2B valuation, led by a16z (May 20, 2026). Funds go to models, infrastructure and go-to-market (GTM) hires. **Marcus Holm**, formerly President of LaunchDarkly, joined as **Chief Revenue Officer (CRO)**. Exa also hired Meta's head of retrieval infrastructure, Yandex's head of search backend, and a research team from Google. https://exa.ai/blog/announcing-series-c
- **Revenue:** $100M+ annualized as of Oct 13, 2026. https://exa.ai/blog/100m-run-rate
- **Usage:** the homepage claims 900,000+ developers and up to 25T tokens passed to models each week. https://exa.ai/
  - This conflicts with the 400k developers and 5,000 companies cited in May 2026 and the 200k+ teams cited in October. Use the October figures.
- **Headcount:** about **100 people, mostly in San Francisco**, according to a job post dated Oct 12, 2026. https://jobs.a16z.com/jobs/exa/b526aedf-f7a0-41ee-a6f6-1d922473c916--head-of-marketing-emea
- **Offices:** Singapore office opened Mar 30, 2026. https://exa.ai/blog/exa-singapore

### Named customers
| Company | Status | Source |
|---|---|---|
| Cursor | Confirmed: named in the Series C post | https://exa.ai/blog/announcing-series-c |
| Cognition (Devin) | Confirmed. Case study quote: "Exa powers all parts of Devin." | https://exa.ai/customers/cognition |
| HubSpot | Confirmed. Exa powers people and company search plus Monitors for Breeze agents. Exa claims 40% better latency. | https://exa.ai/customers/hubspot |
| monday.com, OpenRouter | Confirmed | https://exa.ai/blog/announcing-series-c |
| Revolut | Confirmed. Exa powers a securities-move alert agent: 1,500+ alerts a week, 1M+ users notified daily, 2x message opens. | https://exa.ai/customers/revolut |
| Firefox (Mozilla) | Confirmed | https://exa.ai/blog/exa-firefox |
| Notion | Confirmed. Exa-hosted case study on Notion Research Mode. | https://exa.ai/blog/notion-exa |
| Vercel | Confirmed as a partner (AI Gateway and Marketplace); customer status UNVERIFIED | https://vercel.com/changelog/exa-joins-vercel-ai-gateway-agent-marketplace |
| Databricks | **UNVERIFIED.** No primary source found. | — |
| Other logos on the customers page | 11x, CodeRabbit, HockeyStack, Anara, WebFX, WhyHow.AI, StackAI, Obvious | https://exa.ai/customers |
| Google (partner) | Confirmed. Grounding with Exa in Gemini Enterprise Agent Platform (private preview, Apr 2026) and Exa Agent in the Gemini Enterprise Agent Marketplace. | https://exa.ai/blog/exa-google-cloud |
| ZoomInfo | Confirmed through Exa Connect | https://pipeline.zoominfo.com/sales/zoominfo-exa-integration |

### Partnerships and integrations, 2025–2026 (dated)
- **Aug 18, 2025:** ZDR across all search products. https://exa.ai/blog/zdr-search-engine
- **Apr 7, 2026:** x402 support on `/search` and `/contents`, announced by Coinbase. https://www.coinbase.com/developer-platform/discover/launches/exa
- **Apr 28, 2026:** Google partnership (grounding and Agent Marketplace). https://exa.ai/blog/exa-google-cloud
- **May 6, 2026:** Nevermined card-delegation payments, so an agent can buy a $7 Exa key with a Visa or Mastercard. https://nevermined.ai/blog/exa-nevermined-autonomous-ai-agent-payments
- **May 11, 2026:** an AWS blog post on building agents with Strands, Exa and AgentCore. This comes from a secondary summary (UNVERIFIED). Exa also has an AWS Marketplace listing. https://aws.amazon.com/marketplace/reviews/reviews-list/prodview-d5kxpjxyrsdkw
- **Jun 24, 2026:** Exa Connect, with ZoomInfo, Crunchbase, Similarweb and others. https://alphasignal.ai/news/exa-connect-unlocks-private-commercial-data-for-ai-agents
- **Aug 17, 2026:** Firefox. **Aug 19, 2026:** Vercel AI Gateway.
- **Oct 2, 2026:** Cloudflare Web Search beta. Exa is $7/1k there; Ceramic is the default at $0.25/1k and Linkup is $5/1k. https://developers.cloudflare.com/web-search/providers/
- **Ongoing:** OpenRouter's web plugin uses Exa as its default (from the October brief).

### Launches, Jul–Nov 2026
- **Jul 23:** publications, people and organization search. https://exa.ai/blog/publications-search
- **Aug 17:** Firefox. https://exa.ai/blog/exa-firefox
- **Aug 28:** Dynamic Highlights. https://exa.ai/blog/dynamic-highlights
- **Sep 17:** Snapshot. https://exa.ai/blog/exa-snapshot
- **Sep 25:** Agent Ultra. https://exa.ai/blog/exa-agent-ultra
- **Oct 5:** Places. https://exa.ai/blog/places-search
- **Oct 8:** ATLAS benchmark, a new benchmark for search-heavy agent tasks. https://exa.ai/blog/atlas-benchmark
- **Oct 13:** $100M annualized revenue. https://exa.ai/blog/100m-run-rate
- **Oct 19:** Exa 3.0 and Lite. https://exa.ai/blog/exa-3
- **Oct 29:** Monitors v2 and Podcasts. https://exa.ai/blog/monitors-v2 · https://exa.ai/blog/podcast-search
- **Nov 1–10:** nothing new on the blog as of 2026-11-10. https://exa.ai/blog

### Leadership
- **Will Bryk:** co-founder and CEO since June 2021. https://siliconvalleyinvestclub.com/companies/exa/team/will-bryk/
- **Jeff Wang:** co-founder. He studied at Harvard (2015–19, Bryk's roommate) and built data and web infrastructure at Plaid (2019–22). His exact title is UNVERIFIED. https://siliconvalleyinvestclub.com/companies/exa/team/jeff-wang/
- **Marcus Holm:** CRO since May 2026. https://exa.ai/blog/announcing-series-c
- **Marketing lead:**
  - **Thais Castello Branco** was "Head of Strategy & Marketing" in March 2025. Whether she still holds the role is UNVERIFIED. https://forwardfuture.com/p/inside-exa-the-startup-building-a-search-engine-for-the-ai-age
  - No VP of Marketing or CMO was found.
  - Open roles in Oct 2026: Head of Marketing EMEA (London, Exa's first senior marketer outside the US, a team of one), Head of Marketing APJ (Sydney), Head of Marketing Operations (San Francisco), Product Marketing Manager (enablement-focused, $175–240k), and Technical Product Marketing Content.
  - Sources: https://jobs.a16z.com/jobs/exa/b526aedf-f7a0-41ee-a6f6-1d922473c916--head-of-marketing-emea · https://jobs.a16z.com/jobs/exa/ea4a90d1-db51-4fb3-a7a6-a7ff82e8be30--head-of-marketing-apj · https://www.choppingblock.ai/jobs/head-of-marketing-operations-at-exa · https://simplify.jobs/p/3fe0d8b3-43e5-4cca-92e2-635d6a3e5a65/Product-Marketing-Manager · https://www.choppingblock.ai/jobs/technical-product-marketing-content-at-exa

## 3. Marketing and GTM motions

### What's visible
- **Content and blog:** about 13 posts from Jul to Oct 2026, mostly launch posts and research. https://exa.ai/blog
- **Benchmarks as marketing:**
  - Exa built its own benchmarks: ATLAS, WebCode, and people and company FindAll. The people and company benchmarks are open-sourced at github.com/exa-labs/benchmarks.
  - Exa promotes third-party rankings: Artificial Analysis #1 and BrowseComp 91.8%.
  - Sources: https://exa.ai/blog/atlas-benchmark · https://exa.ai/versus/parallel
- **Research posts:** "How Search Quality Shapes RL Outcomes" (May 13, 2026), exa-d, and infrastructure write-ups. https://exa.ai/blog/rl-search-outcomes
- **Versus pages:** /versus/parallel and /versus/you, both updated Oct 19, 2026.
  - The You.com page says plainly "We have not measured it" on accuracy. It does cite You.com errors on 95 of 200 SimpleQA queries.
  - The Parallel page claims 1.4–2.5x accuracy at the same latency, and Agent High at $0.50 against Parallel Ultra 8x at $2.40.
  - Sources: https://exa.ai/versus/you · https://exa.ai/versus/parallel
- **Programmatic SEO and generative engine optimization (GEO):** unbylined, undated Q&A articles on subdomains such as tpc.exa.ai and tpc-search.exa.ai (for example, "most transparent search API for enterprise AI"). Some of these pages include instructions aimed at AI agents. https://tpc.exa.ai/task/blog/transparent-search-apis-enterprise-ai
- **Customer case studies:** 14 on /customers (Revolut, HubSpot, Cognition, Firefox and others). https://exa.ai/customers
- **Events and hackathons:**
  - Co-hosted "Inside the Agent Stack" in San Francisco with Fireworks and Vercel. https://luma.com/nq14wi4o
  - Co-hosted the Discovery AI Agent Hackathon with Anthropic, AWS and Lightspeed (75 engineers). https://luma.com/sikose73
  - Ran an event with Nevermined, Coinbase and Visa on agent payments. https://nevermined.ai/blog/exa-nevermined-autonomous-ai-agent-payments
  - Gave $50 credits per participant at the Build Club hackathon, which ended Jan 9, 2026. https://build-club-staging.vercel.app/challenges
- **Talks and video:** an a16z Deep Dive (Jun 4, 2026) and SuperAI 2026 (Jun 17). https://exa.ai/blog
- **Developer programs:** the free MCP tier (Feb 2026), $10 a month in free credit, an API Playground, and native framework integrations. https://exa.ai/docs/changelog · https://exa.ai/pricing
- **Enterprise sales:** CRO hired, forward-deployed engineers, Slack support, and a $12k annual plan. https://exa.ai/enterprise
- **Channel distribution:** OpenRouter, Vercel AI Gateway, Cloudflare, Google Gemini Enterprise, AWS Marketplace, Coinbase x402 Bazaar and AgentCore Gateway. https://news.bitcoin.com/coinbase-gives-amazon-bedrock-agents-wallet-tools-with-usdc-settlement/
- **Community and social:** historically developer-first on X and LinkedIn, building on the Y Combinator network. https://forwardfuture.com/p/inside-exa-the-startup-building-a-search-engine-for-the-ai-age

### What's missing or thin
- **No formal startup credits program.** Searches found no "Exa for Startups" page; only hackathon codes exist. The signup credit was cut on Oct 23, 2026.
- **Regional marketing is just starting.** The EMEA and APJ heads are first hires.
- **Case studies are thin on numbers.** The Cognition page has no metrics.
- **Most benchmarks are self-run.** On the WANDR comparison, Exa ran the evaluation itself with a modified grader. https://exa.ai/blog/exa-agent-ultra
- **No published EU data residency.** A Parallel article dated Oct 14, 2026 lists Exa as not documenting an EU option. Parallel is a competitor. https://parallel.ai/articles/best-web-search-apis-eu-data-residency
- **No A2A Agent Card.**
- **No certification or partner program for agencies or systems integrators** was found (UNVERIFIED).
- **No public user conference.**

## 4. Seven ways AI products get web search

### (a) Pull on demand: the agent calls a search API
- **Exa's position:**
  - Category leader by revenue: $100M+ annualized, 2B requests a month. https://exa.ai/blog/100m-run-rate
  - Strongest on benchmarks per its own claims. https://exa.ai/blog/exa-3
  - Best precision@5 in the independent psinglap run, but worst on empty responses and p95 latency. https://psinglap.github.io/websearch-api-eval
- **Who leads:** Exa. Close followers:
  - Parallel: $100M Series B at $2B, Apr 29, 2026. https://techcrunch.com/2026/04/29/parallel-web-systems-hits-2b-valuation-five-months-after-its-last-big-raise/
  - Tavily: acquired by Nebius, closed Feb 19, 2026, reportedly for ~$275M (UNVERIFIED). https://nebius.com/newsroom/nebius-announces-agreement-to-acquire-tavily-to-add-agentic-search-to-its-ai-cloud-platform
  - You.com, Brave, Linkup ($10M seed, Feb 2026), and Firecrawl. https://www.pulse.bot/ai/news/linkup-raises-10m-seed-round-led-by-gradient-to-build-web-search-for-ai-c68161d6-6af6-43e0-ae4e-36a40075ddc7/
- **Market movement:**
  - Microsoft retired the Bing Search APIs on Aug 11, 2025. https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement
  - Price compression: Exa Lite at $4/1k (Oct 2026), Ceramic at $0.25/1k on Cloudflare (Oct 2026).
- **Example buyers:**
  - Cognition · coding agents · Exa
  - Revolut · fintech · Exa
  - HubSpot · CRM · Exa
  - Notion · productivity · Exa
- **2030 size (reasoned estimate):** $3–6B. This assumes the category leader is at $0.1B with roughly 10x growth slowing to about 2x a year by 2028–30, and that Exa holds a 25–35% share.

### (b) Bundled in the model: search sold inside an LLM API
- **Exa's position:** a wholesale supplier to the bundlers.
  - Google Gemini grounding with Exa (private preview, Apr 2026). https://exa.ai/blog/exa-google-cloud
  - Default provider in OpenRouter's web plugin.
  - Built-in tool in Vercel AI Gateway (Aug 19, 2026). https://vercel.com/changelog/exa-joins-vercel-ai-gateway-agent-marketplace
  - Selectable provider in Cloudflare (Oct 2, 2026). https://developers.cloudflare.com/web-search/providers/
- **Who leads:**
  - Model vendors' own tools: OpenAI and Anthropic both charge ~$10/1k searches. https://nesyona.com/articles/ai-web-search-tool-prices-per-1000-calls-2026
  - Anthropic's provider is "presumably Brave" (UNVERIFIED). https://simonwillison.net/2025/May/7/anthropic-api-search
  - Google Search grounding.
  - AWS built its **own** AgentCore Web Search on an Amazon-run index (GA Jun 16, 2026, us-east-1 only). https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-web-search/
  - Nebius bundles Tavily.
- **Market movement:**
  - Inference clouds and gateways are adding search as a line item: Nebius + Tavily (Feb 2026), Vercel (Aug 2026), Cloudflare (Oct 2026).
  - Hyperscalers are vertically integrating: AWS (Jun 2026), Microsoft Grounding with Bing (2025).
  - Perplexity reportedly ends Sonar Chat Completions support on Sep 27, 2026 and points new builds to its Agent API (UNVERIFIED). https://developer.puter.com/tutorials/perplexity-api-pricing/
- **Example buyers:**
  - Firefox · browser · Exa (direct)
  - Developers on OpenRouter · AI gateway · Exa default
  - Salesforce Agentforce · CRM · OpenAI web search (beta Jan 2026, third-party blog). https://dev.to/hemantj/beyond-the-firewall-unlocking-trusted-web-search-for-agentforce-with-openai-2921
  - Gemini Enterprise customers · enterprise · Google or Exa grounding
- **2030 size (reasoned estimate):** $5–10B in search fees embedded in model and gateway bills. This is the largest volume channel, but the margin largely goes to the bundler.

### (c) Push monitors: alerts when facts change
- **Exa's position:**
  - Monitors v2 at $2 per 1k runs, delivered by webhook, covering 211M businesses and 3.2M podcast episodes. https://exa.ai/blog/monitors-v2
  - HubSpot uses Monitors to trigger workflows. https://exa.ai/customers/hubspot
- **Who leads:** Exa and Parallel (Parallel has a Monitor API, per Exa's comparison page). Google Alerts is the legacy incumbent but has no API. https://exa.ai/versus/parallel
- **Market movement:**
  - Exa Monitors launched in Mar 2026; v2 cut the price 7x in Oct 2026.
  - Revolut's alert agent shows a pull-based version of this pattern. https://exa.ai/customers/revolut
- **Example buyers:**
  - HubSpot · CRM · Exa Monitors
  - Revolut · fintech · Exa Search (triggered by price moves)
  - Prediction-market settlement and adverse-media screening are named use cases, not named customers. https://exa.ai/blog/monitors-v2
- **2030 size (reasoned estimate):** $0.5–1.5B. This assumes it becomes a 10–20% add-on to pull spend once agents run continuously.

### (d) Private deployment: ZDR, VPC, marketplaces, SOC 2, EU region
- **Exa's position:**
  - Offers SOC 2 Type II, ZDR, HIPAA with a BAA, SSO and SCIM. https://exa.ai/enterprise
  - Sold through AWS Marketplace and Gemini Enterprise.
  - **No documented EU region and no VPC or self-hosted option.** The sources are a competitor article and a third-party course (UNVERIFIED as official). https://parallel.ai/articles/best-web-search-apis-eu-data-residency · https://theneuralbase.com/exa-api/learn/advanced/data-residency-considerations/
- **Who leads:**
  - Parallel, Linkup and Staan document EU processing (Oct 14, 2026). https://parallel.ai/articles/best-web-search-apis-eu-data-residency
  - AWS AgentCore Web Search keeps data inside AWS ("zero data egress").
- **Market movement:**
  - Firefox chose Exa partly for its ZDR commitment (Aug 2026).
  - Parallel's own comparison claims Exa does not offer ZDR through Cloudflare. That comes from a competitor (UNVERIFIED). https://parallel.ai/articles/cloudflare-web-search-api
- **Example buyers:**
  - Firefox · browser · Exa (ZDR)
  - Revolut · regulated fintech · Exa
  - AWS-native enterprises · various · AgentCore Web Search
- **2030 size (reasoned estimate):** about 30–40% of (a) + (b) spend flows through enterprise and private terms, roughly $2.5–6B. This is not a separate pool of money.

### (e) License in bulk: search for model training and RL
- **Exa's position:**
  - The May 13, 2026 study found agents trained with RL on Exa matched SERP-trained agents' scores with 69% fewer tokens. SERP means search-engine results pages (Google results through a proxy). https://exa.ai/blog/rl-search-outcomes
  - Snapshot (Sep 2026) targets RL evaluation without answer leakage.
  - "Model training" is listed as a use case. https://exa.ai/enterprise
  - The 100M post names "AI labs" as a customer segment, but no lab is named as a customer. https://exa.ai/blog/100m-run-rate
- **Who leads:** UNVERIFIED. No public deals between labs and search vendors were found.
- **Market movement:** search-augmented RL is now a selling point (Exa, May 2026).
- **Example buyers:** none confirmed publicly. Thinking Machines (Tinker) and Qwen appear only as tools in Exa's study, not as customers.
- **2030 size:**
  - The AI training dataset market is about $8.6B by 2030, from an older Grand View Research edition (newer edition: $16.3B by 2033). https://gii.tw/report/grvi1611213-ai-training-dataset-market-size-share-trends.html · https://www.gii.tw/report/grvi1908657-ai-training-dataset-market-size-share-trends.html
  - The search and RL-environment slice is a reasoned estimate of $0.5–2B.

### (f) Agent to agent: A2A, Agent Cards, agent marketplaces, agent payments
- **Exa's position:**
  - Exa Agent is listed in the Gemini Enterprise Agent Marketplace (Apr 2026).
  - x402 payments on `/search` and `/contents` (Apr 7, 2026).
  - Nevermined card-delegated purchases (May 6, 2026).
  - Discoverable through Coinbase's tools in AgentCore Gateway.
  - Exa Connect works as an agent-side data marketplace (Jun 2026).
  - **Gap:** no A2A Agent Card (`/.well-known/agent-card.json` returns 404), and no Stripe Machine Payments Protocol (MPP) support found.
- **Competitors:**
  - **Parallel** has been live on Stripe and Tempo MPP since launch, at $0.01 per search, and runs parallelmpp.dev. https://parallel.ai/blog/tempo-stripe-mpp
  - **Tavily** launched x402 on May 27, 2026 at $0.01 USDC per call, with listings on agentic.market and x402scan. https://yage.ai/share/tavily-x402-agent-payments-en-20260603.html
  - **You.com** supports x402 ($0.005 per search) and MPP ($0.01), including Finance Research. https://you.com/docs/administration/machine-payments
  - No competitor A2A agent launch was found (UNVERIFIED).
- **Market movement:**
  - A2A was handed to the Linux Foundation in Jun 2025; v1.0 reportedly shipped in Mar 2026. https://www.olostep.com/blog/a2a-protocol-agent2agent
  - AWS Marketplace added A2A servers for AgentCore Runtime (Nov 2025). https://aws.amazon.com/about-aws/whats-new/2025/11/marketplace-a2a-server-bedrock-agentcore-runtime/
  - Google Next (Apr 22, 2026) put partner agents in the Gemini Enterprise Agent Gallery, backed by a $750M partner fund. https://siliconangle.com/?p=740782
  - Coinbase launched agentic.market (Apr 2026). https://invezz.com/news/2026/04/21/coinbase-backed-x402-launches-agentic-market-to-power-ai-agent-services/
- **Example buyers:**
  - Gemini Enterprise tenants · enterprise · Exa Agent
  - Autonomous agents on x402 · crypto and dev tools · Exa, Tavily or You.com
  - Developers using Stripe MPP · dev tools · Parallel or You.com
- **2030 size:**
  - Agentic commerce is forecast at $1.5T (Juniper) to $5T (McKinsey, as cited) in transaction volume by 2030. https://www.fintechfutures.com/press-releases/agentic-commerce-set-to-generate-1-5-trillion-globally-by-2030-as-payments-infrastructure-leaders-revealed · https://tenten.co/shopify/agentic-commerce-market-size/
  - The search and research slice paid agent to agent is a reasoned estimate of $0.3–1.5B.

### (g) Browsing with no provider: computer-use agents, NLWeb, llms.txt
- **Exa's position:**
  - Indirect. Exa itself publishes `llms.txt`, and its pages include instructions aimed at agents.
  - Firecrawl (crawling) is the nearer competitor here. Its deep-research API was deprecated in early 2026. https://www.firecrawl.dev/blog/best-ai-search-engines-agents
- **Who leads:** model vendors' computer-use agents and browser agents. Named vendor share is UNVERIFIED.
- **Market movement:** sites are publishing llms.txt and agent-facing pages, and Exa itself serves agent instructions on its pages.
- **Example buyers:** none confirmed for this report.
- **2030 size:**
  - The broader AI agents market is about $48.3B by 2030 (BCC Research, as cited). https://www.speechtechmag.com/Articles/News/Speech-Technology-News/AI-Agents-Market-to-Be-Worth-%2447.1-Billion-by-2030--165922.aspx
  - Computer-using agents: about $54.8B by 2034, from $0.5B in 2025. https://marketintelo.com/report/computer-using-agents-market
  - The browsing-as-search-substitute slice is a reasoned estimate of $1–3B.

## 5. Exa vs competitors: strengths and weaknesses

### Strengths, with evidence
- **Scale and momentum:** $100M+ annualized revenue (Oct 2026), about 10x growth a year, and 2B requests a month. https://exa.ai/blog/100m-run-rate
- **Own index:**
  - 2T+ URLs tracked, 100B pages served.
  - Specialized indexes: people (1B+), companies, 350M publications, 211M places, 3.2M podcasts, 1.27B e-commerce listings.
  - Sources: https://exa.ai/blog/exa-3 · https://exa.ai/docs/changelog
- **Benchmark leadership:**
  - Self-reported: #1 on 8 of 8 benchmarks.
  - Third party: #1 on the Artificial Analysis Search Index.
  - Independent: best precision@5 (40%) in the psinglap run.
- **Distribution:** Google, Vercel, Cloudflare, OpenRouter, Firefox, AWS Marketplace and Coinbase x402.
- **Price:** Lite at $4/1k is below You.com Search at $5/1k. Exa's own page says the gap widens once page content is needed. https://exa.ai/versus/you
- **Breadth:** one platform covering Search, Contents, Agent (up to Ultra), Monitors, Connect and Snapshot. Parallel's core Search has no people or company category. https://exa.ai/versus/parallel

### Weaknesses, with evidence
- **Reliability:**
  - 12 empty responses out of 90 and p95 latency of 3,997 ms in the psinglap run. https://psinglap.github.io/websearch-api-eval
  - A tracker logged 12 outages totaling 33 h 16 m since Apr 22, 2026 (third-party). https://pingoru.io/providers/exa-ai/outage-history
- **Freshness:** only 44% of results fell inside the date window, and finance accuracy was 40% (psinglap).
- **Onboarding friction:** 95 s and 13 steps to get an API key (psinglap). The signup credit was cut on Oct 23, 2026.
- **Product churn:**
  - Research API retired Apr 2026.
  - `instant`, `fast` and `deep-reasoning` marked legacy Oct 2026.
  - `pdf`, `github` and `tweet` categories deprecated.
  - This creates migration burden and makes messaging harder. https://releasebot.io/updates/exa
- **Data residency:** no documented EU region, while Parallel and Linkup document one.
- **Price on gateways:** on Cloudflare, Exa is the most expensive provider ($7/1k against Ceramic at $0.25/1k).
- **Agent payments:** no Stripe MPP; Parallel and You.com have it.
- **No finance-specific endpoint:** You.com has Finance Research, per Exa's own versus page.
- **Benchmarks largely self-run:** for example, WANDR used Exa's own grader.

### Head-to-head snapshots
| Competitor | Where they beat Exa | Where Exa beats them | Sources |
|---|---|---|---|
| **You.com** | Finance Research endpoint; x402 and MPP payments; $100 starter credit | Lower price, Monitors, people and company categories, highlights, revenue scale | https://exa.ai/versus/you · https://you.com/docs/administration/machine-payments |
| **Tavily** (Nebius) | x402 product line (May 2026); bundled in the Nebius AI cloud | Own index, benchmarks, entity search | https://yage.ai/share/tavily-x402-agent-payments-en-20260603.html |
| **Parallel** | Stripe MPP; EU data residency; Task API compute tiers; harder PDF and JavaScript extraction (Exa's own concession) | Latency (Lite ~450 ms vs ~0.9–1.1 s), BrowseComp, price per task | https://exa.ai/versus/parallel |
| **Brave** | Own large index; price from ~$4–5/1k (aggregators); reportedly powers Anthropic search (UNVERIFIED) | Semantic retrieval, agent products, entity indexes | https://costbench.com/changelog/brave-search-api-price-decrease-2026-05/ |
| **Perplexity Sonar / Search API** | Consumer brand; Search API at $5/1k (aggregator) | Exa says Perplexity errored on SimpleQA; Exa leads on its benchmarks | https://exa.ai/versus/parallel · https://developer.puter.com/tutorials/perplexity-api-pricing/ |
| **Firecrawl** | Crawling and extraction depth | Search index and quality; Exa says Firecrawl errored on SimpleQA | https://exa.ai/versus/parallel |
| **Linkup** | EU residency; SOC 2 and ISO 27001; cheaper on Cloudflare ($5 vs $7 per 1k) | Scale, benchmarks, product breadth | https://www.edenai.co/providers/linkup · https://developers.cloudflare.com/web-search/providers/ |

## 6. Agent to agent: how Exa could expand

### Already in place
- Exa Agent in the Gemini Enterprise Agent Marketplace (Apr 2026).
- x402 on `/search` and `/contents` (Apr 2026).
- Nevermined card delegation (May 2026).
- Exa Connect provider marketplace (Jun 2026).
- `agent_run` tool in MCP (Jul 2026).

### Concrete next moves
1. **Publish an A2A Agent Card** for Exa Agent at `/.well-known/agent-card.json`. Skills could include deep research, list building, enrichment and monitoring.
   - Today that path returns 404.
   - A2A v1.0 shipped in Mar 2026 and the Agent Card format is standardized. https://a2a-protocol.org/latest/specification/
2. **Websets as a hireable agent.** Expose list-building and enrichment as an A2A task with long-running status and webhooks. Agent Ultra's 5 min to 3 h runtime already fits A2A's long-running task model.
3. **Research as an A2A agent.** The `/research` endpoint is retired, so make Exa Agent the A2A-addressable research agent across Gemini Enterprise, the AWS Marketplace A2A path and Salesforce.
   - AWS Marketplace has supported A2A servers since Nov 2025. https://aws.amazon.com/about-aws/whats-new/2025/11/marketplace-a2a-server-bedrock-agentcore-runtime/
   - Salesforce Agentforce currently uses OpenAI for web search (beta).
4. **Per-call payments:**
   - Extend x402 from search and contents to Agent and Monitors.
   - Add **Stripe MPP**, which Parallel and You.com already support.
   - Exa's current x402 flow buys a $7 key, not a per-call charge. Tavily charges $0.01 per call and You.com $0.005 per call.
5. **Marketplace listings:**
   - Coinbase agentic.market and x402 Bazaar.
   - AWS AgentCore Gateway as an A2A target, beyond the Coinbase MCP route.
   - Microsoft Foundry: Bing's API is retired and Grounding with Bing gives no raw results, which leaves an opening (UNVERIFIED as an active Exa pursuit).
6. **Exa Connect as a two-sided agent economy.** Let provider agents, not just provider APIs, register and be paid through Exa. It already has a self-serve provider form and lets providers set their own prices. https://exa.ai/connect

### What competitors have done
- **Parallel:** MPP since launch, plus the parallelmpp.dev gateway.
- **Tavily:** x402 product line listed on agentic.market (May 27, 2026).
- **You.com:** x402 and MPP across Search, Agents Search and Finance Research.
- **Search vendors and A2A:** none found with A2A Agent Cards (UNVERIFIED).
- **Hyperscalers:**
  - AWS built its own AgentCore Web Search (Jun 2026).
  - Google's Agent Gallery lists partner agents such as Salesforce, ServiceNow and Oracle. https://cloud.google.com/blog/products/ai-machine-learning/the-new-gemini-enterprise-one-platform-for-agent-development
