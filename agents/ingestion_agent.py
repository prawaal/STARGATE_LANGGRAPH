import subprocess
import sys
import json

class IngestionAgent:

    def update_status(self, runtime_status):
        with open(

            "outputs/runtime_status.json",

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(
                runtime_status,
                f,
                indent=2
            )

    def run(
        self,
        state
    ):

        print(
            "\nRunning Ingestion Agent\n"
        )

        runtime_status = {

            "agent": "Ingesting Data for Scoring",

            "progress": 50,

            "status": "Running"
        }


        self.update_status(runtime_status)

        subprocess.run([

            sys.executable, "-m",
            "workflows.ingestDataForScoring"
        ])

        state[
            "ingestion_ready"
        ] = True

        return state