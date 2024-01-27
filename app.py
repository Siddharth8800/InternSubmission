import gradio as gr
from model import generate_text

def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})

    response = generate_text(f"{message}")
    return response.response

title = "The 48 Laws of Power by Robert Greene"
description = "I made this app to showcase my submission for the Internshala Task. I used the Mistral-7b-instruct-v0.2.Q5_K_S.gguf model for the LLM and BAAI/bge-large-en-v1.5 for the embedding model. I chose these models because they performed well on the MTEB leaderboard and I didn't want to use the OpenAI API."
examples = ["Can you give me an example from history where the enemy was crushed totally from the book?",
            "What's the point of making myself less accessible?",
            "Can you tell me the story of Queen Elizabeth I from this 48 laws of power book?"
            ]
gr.ChatInterface(predict, title=title, examples=examples, description=description).launch(share=True)
