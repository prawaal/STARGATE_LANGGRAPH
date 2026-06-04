import json

from ontology.corpus_loader import CorpusLoader
from ontology.Ontology_Extractor import PhraseExtractor

from ontology.infra_scorer import (
    InfrastructureScorer
)

from ontology.ontology_prototype import (
    ONTOLOGY_PROTOTYPES
)

from ontology.ontology_inference import (
    OntologyInferenceEngine
)

from ontology.ontology_builder import (
    OntologyBuilder
)


# LOAD DOCUMENTS
loader = CorpusLoader("data/raw")

documents = loader.load_documents()


# INIT COMPONENTS
extractor = PhraseExtractor()

scorer = InfrastructureScorer()

inference_engine = OntologyInferenceEngine(
    ONTOLOGY_PROTOTYPES
)

builder = OntologyBuilder()


# GLOBAL PHRASES
global_phrases = {}


# EXTRACT PHRASES
for doc in documents:

    phrases = extractor.extract_phrases(
        doc["text"]
    )

    for phrase, count in phrases.items():

        global_phrases[phrase] = (
            global_phrases.get(phrase, 0) + count
        )


# SORT PHRASES
sorted_phrases = sorted(
    global_phrases.items(),
    key=lambda x: x[1],
    reverse=True
)


# INFRASTRUCTURE FILTERING
for phrase, count in sorted_phrases:

    infra_score = scorer.score_phrase(phrase)

    if infra_score == 0:
        continue

    inference = inference_engine.infer_category(
        phrase
    )

    if inference:

        builder.add_inference(
            phrase,
            count,
            inference
        )


# BUILD FINAL ONTOLOGY
ontology = builder.build()



ontology_json = {}


for node in ontology:

    category = node["category"]

    ontology_json[category] = {

        "importance": node["importance"],

        "evidence": [
            e["phrase"]
            for e in node["evidence"]
        ]
    }

with open(
"outputs/ontology.json",
"w",
encoding="utf-8"
) as f:

    json.dump(
        ontology_json,
        f,
        indent=4
    )

print("\nOntology saved to outputs/ontology.json")