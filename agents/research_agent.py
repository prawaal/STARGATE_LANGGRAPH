import subprocess
import sys
import json

class ResearchAgent:
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
            "\nRunning Research Agent\n"
        )

        runtime_status = {

            "agent": "Research",

            "progress": 10,

            "status": "Running"
        }


        self.update_status(runtime_status)
        # ontology already exists

        state[
            "ontology_ready"
        ] = True

        return state