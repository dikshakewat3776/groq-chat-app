from groq import Groq
import os
import pandas as pd
import numpy as np
from pydub import AudioSegment
from langchain.text_splitter import TokenTextSplitter
from langchain.docstore.document import Document
from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings

client = Groq(api_key = os.getenv('GROQ_API_KEY'))
model = 'whisper-large-v3'

# basic
# audio to text
# ask questions from audio

