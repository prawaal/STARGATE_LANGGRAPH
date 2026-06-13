import time

class DummyClient:

    def __init__(self):

        pass

    def generate(
        self,
        prompt,
        retries=3,
        delay=2
    ):

        try:

            response = ""
            time.sleep(1)
            return response.text

        except Exception as e:

            raise