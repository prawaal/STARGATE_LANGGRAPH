import subprocess
import sys
import json

class ScoringAgent:

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

        runtime_status = {

            "agent": "Scoring MOAT",

            "progress": 60,

            "status": "Running"
        }


        self.update_status(runtime_status)

        print(
            "\nRunning Scoring Agent\n"
        )

        subprocess.run([
            sys.executable, "-m",
            "workflows.computeMoatScores"
        ])

        runtime_status = {

                    "agent": "Scoring Financial Quality",

                    "progress": 65,

                    "status": "Running"
                }

        self.update_status(runtime_status)

        subprocess.run([
            sys.executable, "-m",
            "workflows.computeFinancialScores"
        ])

        runtime_status = {

                    "agent": "Scoring AI Exposure",

                    "progress": 70,

                    "status": "Running"
                }

        self.update_status(runtime_status)

        subprocess.run([
            sys.executable, "-m",
            "workflows.computeAIExposureScores"
        ])

        runtime_status = {

                    "agent": "Scoring Forward Growth",

                    "progress": 75,

                    "status": "Running"
                }

        self.update_status(runtime_status)

        subprocess.run([
            sys.executable, "-m",
            "workflows.computeForwardGrowthScores"
        ])

        runtime_status = {

                    "agent": "Scoring Disruption Risk",

                    "progress": 80,

                    "status": "Running"
                }

        self.update_status(runtime_status)

        subprocess.run([
            sys.executable, "-m",
            "workflows.computeDisruptionRiskScores"
        ])

        runtime_status = {

                    "agent": "Scoring Complete",

                    "progress": 85,

                    "status": "Running"
                }

        self.update_status(runtime_status)

        state[
            "scoring_ready"
        ] = True

        return state