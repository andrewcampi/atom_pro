from time import sleep
from helper.project_info import *

from openai import OpenAI # Don't worry! This uses openai client library, but routes the request to your local server, never touching OpenAI's servers.
client = OpenAI(base_url=f"http://{LOCAL_LM_STUDIO_SERVER_IP}:{LOCAL_LM_STUDIO_SERVER_PORT}/v1", api_key="lm-studio")


def llm_endpoint_call(prompt): # In this OpenAI example, we are not using max_tokens
    
    print("PROMPT:", prompt)
    # Send the request to the API
    response = client.chat.completions.create(
        model=LLM_NAME,
        temperature=LLM_TEMPERATURE,
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content


def llm_chat_endpoint(pentest_data, chat_content):
    
    print("chat_content:", chat_content)
    # Send the request to the API
    response = client.chat.completions.create(
        model=LLM_NAME,
        temperature=LLM_TEMPERATURE,
        messages=[
            {"role": "system", "content": "You are a helpful pentesting assistant named Atom. Provided with data about a paticular authorized black box pentest, you answer questions as you are asked them, matching the precived knowledge level from the latest question, to add the most value to the user."},
            {"role": "assistant", "content": "Hello human, I am Atom. Please provide your pentest data in json format so I can best assist you."},
            {"role": "user", "content": str(pentest_data)},
            [{"role": msg["role"], "content": msg["content"]} for msg in chat_content],
        ]
    )
    return response.choices[0].message.content