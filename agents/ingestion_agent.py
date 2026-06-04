import subprocess


class IngestionAgent:

    def run(
        self,
        state
    ):

        print(
            "\nRunning Ingestion Agent\n"
        )

        subprocess.run([

            "python",

            "ingestDataForScoring.py"
        ])

        state[
            "ingestion_ready"
        ] = True

        return state