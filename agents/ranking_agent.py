import subprocess
import sys
import json


class RankingAgent:

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
            "\nRunning Ranking Agent\n"
        )

        runtime_status = {

            "agent": "Ranking",

            "progress": 90,

            "status": "Running"
        }


        self.update_status(runtime_status)

        subprocess.run([

            sys.executable, "-m",
            "workflows.computeFinalAIRankings"
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