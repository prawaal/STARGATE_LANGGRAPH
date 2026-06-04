import subprocess


class ScoringAgent:

    def run(
        self,
        state
    ):

        print(
            "\nRunning Scoring Agent\n"
        )

        subprocess.run([
            "python",
            "computeMoatScores.py"
        ])

        subprocess.run([
            "python",
            "computeFinancialScores.py"
        ])

        subprocess.run([
            "python",
            "computeAIExposureScores.py"
        ])

        subprocess.run([
            "python",
            "computeForwardGrowthScores.py"
        ])

        subprocess.run([
            "python",
            "computeDisruptionRiskScores.py"
        ])

        state[
            "scoring_ready"
        ] = True

        return state