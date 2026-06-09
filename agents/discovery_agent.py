import subprocess
import sys
import json

class DiscoveryAgent:

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
            "\nRunning Discovery Agent\n"
        )

        runtime_status = {

            "agent": "Identifying Ingredient Stack",

            "progress": 25,

            "status": "Running"
        }


        self.update_status(runtime_status)

        subprocess.run([

                    sys.executable, "-m",
                    "identifyIngredientStack"
                ])

        runtime_status = {

            "agent": "Discovering Market Leaders",

            "progress": 35,

            "status": "Running"
        }


        self.update_status(runtime_status)

        subprocess.run([

            sys.executable, "-m",
            "workflows.discoverMarketLeaders"
        ])

        state[
            "universe_ready"
        ] = True

        return state