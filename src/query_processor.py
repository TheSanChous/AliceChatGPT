import openai

from .common import configuration, storage

openai.api_key = configuration["OpenAIAPIKey"]


def create_query(query_text: str, query_key: str):
    completion = openai.Completion.create(
        engine=configuration["OpenAI"]["ModelEngine"],
        prompt=query_text,
        max_tokens=configuration["OpenAI"]["MaxTokens"],
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

    response = completion.choices[0].text

    storage.set(query_key, response)

    pass
