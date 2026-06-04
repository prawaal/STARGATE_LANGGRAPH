from collections import defaultdict


class OntologyBuilder:

    def __init__(self):

        self.ontology = defaultdict(list)

        self.category_scores = defaultdict(int)

    def add_inference(self, phrase, count, inference):

        category = inference["category"]

        self.ontology[category].append({
            "phrase": phrase,
            "count": count
        })

        self.category_scores[category] += count

    def build(self):

        results = []

        total = sum(self.category_scores.values())

        for category, phrases in self.ontology.items():

            importance = round(
                self.category_scores[category] / total,
                3
            )

            results.append({

                "category": category,

                "importance": importance,

                "evidence": sorted(
                    phrases,
                    key=lambda x: x["count"],
                    reverse=True
                )[:10]
            })

        return sorted(
            results,
            key=lambda x: x["importance"],
            reverse=True
        )