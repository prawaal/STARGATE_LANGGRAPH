import json

from llm.llm_factory import (
    LLMFactory
)

from ontology.ontology_loader import (
    OntologyLoader
)

from ontology.ontology_decomposer import (
    OntologyDecomposer
)

from market.etf_discovery import (
    ETFDiscovery
)

from market.etf_validator import (
    ETFValidator
)

from market.etf_mapper import (
    ETFMapper
)

# LOAD EXISTING ONTOLOGY
loader = OntologyLoader(
    "outputs/ontology.json"
)

ontology = loader.load()


# INIT GEMINI CLIENT
client = (
    LLMFactory.create_llm()
)


# INIT DECOMPOSER
decomposer = OntologyDecomposer(
    client
)


expanded_ontology = []


# RUN DECOMPOSITION
for category in ontology.keys():

    print(f"\nDecomposing: {category}")

    result = decomposer.decompose(
        category
    )

    expanded_ontology.append(result)


# SAVE OUTPUT
with open(
    "outputs/expanded_ontology.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        expanded_ontology,
        f,
        indent=4
    )


print(
    "\nExpanded ontology saved "
    "to outputs/expanded_ontology.json"
)

etf_discovery = ETFDiscovery(
    client
)

validator = ETFValidator()

etf_mapper = ETFMapper(
    etf_discovery,
    validator
)

# LOAD EXISTING ONTOLOGY
loader = OntologyLoader(
    "outputs/expanded_ontology.json"
)

expanded_ontology = loader.load()

etf_mappings = (
    etf_mapper.build_mappings(
        expanded_ontology
    )
)

with open(
    "outputs/etf_mappings.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        etf_mappings,
        f,
        indent=4
    )