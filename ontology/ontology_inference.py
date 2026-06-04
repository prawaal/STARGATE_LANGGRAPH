from collections import defaultdict


class OntologyInferenceEngine:

    def __init__(self, prototypes):

        self.prototypes = prototypes

    def infer_category(self, phrase):

        scores = defaultdict(int)

        phrase_lower = phrase.lower()

        for category, prototype_terms in self.prototypes.items():

            for term in prototype_terms:

                if term in phrase_lower:

                    scores[category] += 1

        if not scores:
            return None

        best_category = max(scores, key=scores.get)

        return {
            "category": best_category,
            "score": scores[best_category]
        }