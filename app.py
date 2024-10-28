from gettext import translation

from groq import Groq
import os
import pandas as pd
import numpy as np
from pydub import AudioSegment
from langchain.text_splitter import TokenTextSplitter
from langchain.docstore.document import Document
from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_ollama import OllamaLLM  # Importing the LLM interface

# llm_model = OllamaLLM(model="llama3.2", host="localhost", port=11434)

client = Groq(api_key = os.getenv('GROQ_API_KEY'))
model = 'whisper-large-v3'

# audio to text
def audio_to_text(path):
    with open(path, "rb") as file:
        translation = client.audio.translations.create(
            file = (path, file.read()),
            model='whisper-large-v3'
        )
    return translation.text

path = 'audio.mp3'
# translations = audio_to_text(path)
# print(translations[:5000])

response = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "Hello!"},
    ],
    model="llama3.2:latest",
)
print(response)

# ask questions from audio
# def transcript_chat_completion(client, transcript, user_question):
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "system",
#                 "content": '''Use this transcript or transcripts to answer any user questions, citing specific quotes:
#
#                 {transcript}
#                 '''.format(transcript=transcript)
#             },
#             {
#                 "role": "user",
#                 "content": user_question,
#             }
#         ],
#         model="llama3.2:latest",
#     )
#     print(chat_completion.choices[0].message.content)
#
# user_question = "Tell me the advantages of banking with HSBC?"
# transcript_chat_completion(client, translations, user_question)