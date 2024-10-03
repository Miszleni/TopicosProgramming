import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("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"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)