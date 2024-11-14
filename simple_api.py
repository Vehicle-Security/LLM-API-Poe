import asyncio
import fastapi_poe as fp


"""
TODO: support long conversation
"""
class PoeClient:

    def __init__(self, api_key, bot_name):
        self.api_key = api_key
        self.bot_name = bot_name
        self.context = None


def poe_request(api_key, bot_name, question):
    all_response = []
    message = fp.ProtocolMessage(role="user", content=question)
    # Create an asynchronous function to encapsulate the async for loop
    async def get_responses(api_key, messages):
        async for partial in fp.get_bot_response(messages=messages, bot_name=bot_name, api_key=api_key):
            # print(partial)
            all_response.append(partial.text)
    asyncio.run(get_responses(api_key, [message]))
    return "".join(all_response)


# Replace <api_key> with your actual API key, ensuring it is a string.

print(poe_request("you-api-key",
                  "GPT-3.5-Turbo", "Who is Here v2"))