import json
import time

import anthropic


class ClaudeClient:

    def __init__(
        self,
        api_key,
        base_url
    ):

        self.client = anthropic.Anthropic(

            api_key=api_key,

            base_url=base_url
        )

    def generate(
        self,
        prompt,
        retries=3
    ):

        for attempt in range(retries):

            try:

                response = (

                    self.client.messages.create(

                        model=
                        "claude-sonnet-4-6",

                        max_tokens=4000,

                        temperature=0,

                        messages=[
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ]
                    )
                )

                return (
                    response.content[0]
                    .text
                )

            except Exception as e:

                msg = str(e).lower()

                print(
                    f"Claude error: {msg}"
                )

                if (
                    "rate_limit"
                    in msg
                    or
                    "overloaded"
                    in msg
                ):

                    sleep_time = (
                        2 ** attempt
                    )

                    print(
                        f"Retrying in "
                        f"{sleep_time}s"
                    )

                    time.sleep(
                        sleep_time
                    )

                else:

                    raise e

        return ""