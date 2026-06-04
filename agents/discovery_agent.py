import subprocess


class DiscoveryAgent:

    def run(
        self,
        state
    ):

        print(
            "\nRunning Discovery Agent\n"
        )

        subprocess.run([

            "python",

            "discoverMarketLeaders.py"
        ])

        state[
            "universe_ready"
        ] = True

        return state