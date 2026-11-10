# Exa Search Atlas

Independent research on [Exa](https://exa.ai) as a search provider for AI agents: where it wins, where it should play next, and who to sell to.

**Live site:** https://psinglap.github.io/exa-search-atlas/

| Page | What it covers |
|---|---|
| [Exa Search Atlas](https://psinglap.github.io/exa-search-atlas/atlas/) | Decision map of the seven ways AI products get web search, scored for Exa. For each way: who leads, how the market is moving, where Exa stands and how to win. Strengths to lead with and moves to make. **Google for AI agents:** Exa as the search agent other agents hire through agent-to-agent (A2A) protocols, with the evidence and what to publish where. |
| [Exa Target Accounts](https://psinglap.github.io/exa-search-atlas/accounts/) | 59 target accounts across 6 agent use cases, with the search provider each uses today. Also 90 public developer complaints grouped into 8 themes, 7 GTM plays, and the default search provider on 16 distribution platforms. |
| [Exa Agent Card: launch kit](https://psinglap.github.io/exa-search-atlas/agent-card/) | An **unofficial example** A2A Agent Card for Exa Agent ([JSON](agent-card/exa-agent-card.example.json), A2A spec v1.0 field names, proposed endpoints that are not live). It also covers what already exists versus what is new, a walkthrough of a sales agent hiring Exa for one task, a launch plan, a draft launch post, and how to pitch it. |

Benchmark figures come from the open [Web Search API evaluation](https://psinglap.github.io/websearch-api-eval/) ([repo](https://github.com/psinglap/websearch-api-eval)), run on 8 Oct 2026. The other research was gathered from public sources on 10 Nov 2026. Each page cites its sources, and labels vendor claims and estimates as such.

## Rebuild

```sh
python3 build/build_atlas.py
python3 build/build_accounts.py
python3 build/build_agent_card.py
python3 build/build_index.py
```

- `build/data/`: research inputs (accounts, developer pain, distribution, research notes).
- `build/templates/`: the page designs, shared with the benchmark site.

Independent research by Pallavi Singla. Not affiliated with or endorsed by Exa.
