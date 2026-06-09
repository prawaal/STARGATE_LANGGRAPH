import subprocess
import sys


class ScoringAgent:

    def run(
        self,
        state
    ):

        print(
            "\nRunning Scoring Agent\n"
        )

        subprocess.run([
            sys.executable, "-m",
            "workflows.computeMoatScores.py"
        ])

        subprocess.run([
            sys.executable, "-m",
            "workflows.computeFinancialScores.py"
        ])

        subprocess.run([
            sys.executable, "-m",
            "computeAIExposureScores.py"
        ])

        subprocess.run([
            sys.executable, "-m",
            "workflows.computeForwardGrowthScores.py"
        ])

        subprocess.run([
            sys.executable, "-m",
            "computeDisruptionRiskScores.py"
        ])

        state[
            "scoring_ready"
        ] = True

        return state