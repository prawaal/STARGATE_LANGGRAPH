ONTOLOGY_DECOMPOSITION_PROMPT = """
You are an expert in:
- hyperscale AI infrastructure,
- industrial supply chains,
- data center economics,
- public market infrastructure companies.

Your task is to decompose the following
AI Factory ontology category into:

- industrial subsegments,
- supply-chain categories,
- infrastructure procurement categories,

that can later map to:
- public companies,
- ETFs,
- industry classifications,
- market leaders.

IMPORTANT:
Return INDUSTRIAL PROCUREMENT CATEGORIES,
NOT technical architecture descriptions.

BAD EXAMPLES:
- AI-Optimized Server Platforms
- Advanced Data Center Cooling
- Hyperscale Power Delivery Systems

GOOD EXAMPLES:
- GPUs
- AI Servers
- Gas Turbines
- Generators
- UPS Systems
- Chillers
- Liquid Cooling
- Transformers
- Optical Networking
- Semiconductor Foundries
- HBM Memory

Category:
{category}

Rules:
- Focus ONLY on hyperscale AI factories.
- Return procurement-oriented industrial categories.
- Categories must be investable / company-mappable.
- Avoid generic phrases.
- Avoid architectural descriptions.
- Avoid long explanations.
- Return concise industrial segments.
- Return JSON only.

Output format:

{{
  "category": "...",
  "subcategories": [
    {{
      "name": "...",
      "description": "..."
    }}
  ]
}}
"""

ETF_DISCOVERY_PROMPT = """
You are a financial markets and industrial infrastructure expert.

Your task is to identify US-listed ETFs that provide exposure
to the following AI Factory infrastructure segment.

Infrastructure Segment:
{segment}

Subcategories:
{subcategories}

Rules:
- Focus on US-listed ETFs.
- Prefer liquid institutional ETFs.
- Focus on industrial, semiconductor,
  utilities, infrastructure,
  networking, or technology ETFs.
- Return only ETFs relevant to the segment.
- Include concise reasoning.
- Return JSON only.
- Dont rely on historic data and try to get latest information from the web.

Output format:

{{
  "segment": "...",
  "candidate_etfs": [
    {{
      "ticker": "...",
      "reason": "..."
    }}
  ]
}}
"""

MOAT_ANALYSIS_PROMPT = """

You are evaluating AI Factory
infrastructure companies.

Analyze the competitive moat
of the following company.

Company:
{company}

Documents:
{text}

Evaluate:

1. Ecosystem lock-in
2. Switching costs
3. Strategic importance
4. Supply chain bottleneck
5. Proprietary technology
6. Infrastructure criticality

Scoring Rules:
- Score each dimension from 0-10
- 10 = extremely strong
- 0 = extremely weak

Return STRICT JSON only.

{{
    "ecosystem_lockin": 0,
    "switching_costs": 0,
    "strategic_importance": 0,
    "supply_chain_bottleneck": 0,
    "proprietary_technology": 0,
    "infrastructure_criticality": 0,
    "summary": ""
}}
"""

AI_EXPOSURE_PROMPT = """

You are analyzing companies
benefiting from AI Factory
infrastructure expansion.

Company:
{company}

Documents:
{text}

Evaluate:

1. AI revenue exposure
2. Hyperscaler dependency
3. Future AI demand growth
4. Capacity expansion positioning

Score each from 0-10.

Return STRICT JSON only.

{{
    "ai_revenue_exposure": 0,
    "hyperscaler_dependency": 0,
    "future_ai_growth": 0,
    "capacity_scaling": 0,
    "summary": ""
}}
"""

FORWARD_GROWTH_PROMPT = """

You are evaluating companies
benefiting from long-term
AI Factory expansion.

Company:
{company}

Documents:
{text}

Evaluate:

1. AI demand acceleration
2. Future revenue growth potential
3. Capacity expansion readiness
4. Hyperscaler demand leverage
5. Long-term infrastructure growth

Score each from 0-10.

Return STRICT JSON only.

{{
    "ai_demand_acceleration": 0,
    "future_revenue_growth": 0,
    "capacity_scaling": 0,
    "hyperscaler_leverage": 0,
    "long_term_tailwinds": 0,
    "summary": ""
}}
"""

DISRUPTION_RISK_PROMPT = """

You are evaluating risks to the
AI Factory investment thesis.

Research Corpus:
{text}

Evaluate:

1. Efficient AI architectures
2. Reduced compute dependency
3. Low power AI trends
4. Open-source AI disruption
5. Alternative AI paradigms

Score each from 0-10.

10 means HIGH disruption risk
for AI Factory infrastructure.

Return STRICT JSON only.

{{
    "efficient_ai_risk": 0,
    "compute_reduction_risk": 0,
    "low_power_ai_risk": 0,
    "open_source_disruption": 0,
    "alternative_paradigm_risk": 0,
    "summary": ""
}}
"""