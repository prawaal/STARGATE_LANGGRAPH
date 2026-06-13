import time
import requests


class OllamaClient:

    def __init__(

        self,

        model="llama3"
    ):

        self.model = model

        self.url = (
            "http://localhost:11434/api/generate"
        )


    def generate(

        self,

        prompt,

        retries=3,

        delay=2
    ):

        for attempt in range(retries):

            try:

                response = requests.post(

                    self.url,

                    json={

                        "model": self.model,

                        "prompt": prompt,

                        "stream": False
                    },

                    timeout=300
                )


                response.raise_for_status()


                result = response.json()


                return result[
                    "response"
                ]


            except Exception as e:

                if attempt < retries - 1:

                    sleep_time = (
                        delay * (2 ** attempt)
                    )

                    print(

                        f"⚠️ Ollama retry "
                        f"in {sleep_time}s..."
                    )

                    time.sleep(
                        sleep_time
                    )

                else:

                    raise RuntimeError(

                        "Ollama failed "
                        "after retries"

                    ) from e
