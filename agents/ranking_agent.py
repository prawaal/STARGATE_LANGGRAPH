import subprocess


class RankingAgent:

    def run(
        self,
        state
    ):

        print(
            "\nRunning Ranking Agent\n"
        )

        subprocess.run([

            "python",

            "computeFinalAIRankings.py"
        ])

        state[
            "rankings_ready"
        ] = True

        state[
            "final_rankings_path"
        ] = (

            "outputs/"
            "final_ai_factory_rankings.json"
        )

        return state