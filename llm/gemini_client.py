import time

from google import genai


class GeminiClient:

    def __init__(self, api_key):

        self.client = genai.Client(
            api_key=api_key
        )

    def generate(
        self,
        prompt,
        retries=3,
        delay=2
    ):

        for attempt in range(retries):

            try:

                response = (
                    self.client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=prompt
                    )
                )

                return response.text

            except Exception as e:

                msg = str(e).lower()

                if (
                    "503" in msg
                    or "overloaded" in msg
                ):

                    if attempt < retries - 1:

                        sleep_time = (
                            delay * (2 ** attempt)
                        )

                        print(
                            f"⚠️ Gemini overloaded. "
                            f"Retrying in {sleep_time}s..."
                        )

                        time.sleep(sleep_time)

                    else:

                        raise RuntimeError(
                            "Gemini unavailable "
                            "after retries"
                        ) from e

                else:
                    raise