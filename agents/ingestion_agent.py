import subprocess
import sys


class IngestionAgent:

    def run(
        self,
        state
    ):

        print(
            "\nRunning Ingestion Agent\n"
        )

        subprocess.run([

            sys.executable, "-m",
            "workflows.ingestDataForScoring.py"
        ])

        state[
            "ingestion_ready"
        ] = True

        return state