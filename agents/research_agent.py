class ResearchAgent:

    def run(
        self,
        state
    ):

        print(
            "\nRunning Research Agent\n"
        )

        # ontology already exists

        state[
            "ontology_ready"
        ] = True

        return state