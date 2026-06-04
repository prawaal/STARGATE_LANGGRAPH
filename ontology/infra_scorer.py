INFRASTRUCTURE_TERMS = {

    "gpu",
    "gpus",
    "power",
    "cooling",
    "thermal",
    "network",
    "networking",
    "interconnect",
    "cluster",
    "data center",
    "data centers",
    "substation",
    "generator",
    "electricity",
    "grid",
    "rack",
    "server",
    "chip",
    "semiconductor",
    "storage",
    "facility",
    "construction",
    "capacity",
    "heat",
    "training",
    "inference"
}


class InfrastructureScorer:

    def score_phrase(self, phrase):

        score = 0

        for term in INFRASTRUCTURE_TERMS:

            if term in phrase:
                score += 1

        return score