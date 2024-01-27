# Internshala Submission

This repo contains the code for the submission.

## Candidate Name: Siddharth

I have chosen to use Open source models instead of OpenAI API, beause it will give toy more control over the app + the cost savings.

### LLM Used: mistral-7b-instruct-v0.2.Q5_K_S.gguf

Although this model was not my first choice, it was originally Microsoft Phi-2 as it recently when open source, but in my testing mistral-7b-instruct-v0.2.Q5_K_S.gguf gave wayyyy better results and was more accurate.

### Embedding Model Used: BAAI/bge-large-en-v1.5

This model performs really high on the MTEB Leaderboard and is also open source, so I chose to use this model.

### How to run the code:

1. Clone the repo
2. Create a conda environment using the `environment.yml` file
3. Download the LLM model from [here](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/tree/main) and place it in the `same` folder.
4. Open terminal and do `python app.py`
