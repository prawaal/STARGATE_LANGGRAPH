import subprocess
import sys


class DiscoveryAgent:

    def run(
        self,
        state
    ):

        print(
            "\nRunning Discovery Agent\n"
        )

        subprocess.run([

                    sys.executable, "-m",
                    "identifyIngredientStack.py"
                ])

        subprocess.run([

            sys.executable, "-m",
            "workflows.discoverMarketLeaders.py"
        ])

        state[
            "universe_ready"
        ] = True

        return state