# groq-chat-app

This application powered by GROQ Whisper used as a RAG provides a natural language interface for users to ask queries and receive accurate, context-aware responses. The app understands and processes user queries in a conversational manner, making interactions smooth and intuitive.

# Key Features

- **Natural Language Processing:** Powered by GROQ Whisper, the app understands and processes user queries in a conversational manner, making interactions smooth and intuitive.
- **Real-time Responses:** Users can ask questions and receive instant answers, allowing for efficient information retrieval without delays.
- **Contextual Awareness:** The chatbot retains context throughout the conversation, ensuring relevant follow-up responses based on previous interactions.
- **User-Friendly Interface:** The app features a clean, intuitive interface that makes it easy for users of all ages to engage and navigate.
- **Multi-Topic Support:** From general knowledge to specific queries, QueryBot can handle a wide range of topics, making it a versatile assistant for users.

## Architecture

### 1. Processing the MP3
Input: MP3 File
Function: Load and preprocess the MP3 audio file.
Components:
Audio Loader: Reads the MP3 file and converts it into a suitable format for processing (e.g., waveform).
Preprocessing: Normalizes audio, removes silence, and prepares it for chunking.

### 2. Converting the MP3 to Chunks
Input: Preprocessed audio waveform
Function: Split the audio into manageable chunks for analysis.
Components:
Chunking Algorithm: Divides the audio into segments based on time duration or silence detection.
Chunk Storage: Temporarily stores audio chunks for further processing.

### 3. Spect to Text Using GROQ Whisper
Input: Audio Chunks
Function: Convert audio chunks into text using GROQ Whisper.
Components:
GROQ Whisper Model: Processes each audio chunk to transcribe spoken content into text.
Transcription Storage: Stores the transcribed text for each chunk, maintaining a reference to the original audio.

### 4. Ask Questions
Input: User Queries
Function: Allow users to ask questions related to the transcribed content.
Components:
Query Interface: A frontend interface for users to input their questions.
Text Processing: Analyzes the query to determine intent and relevant context.
Response Generation: Matches the query against the transcriptions to generate appropriate responses.

### 5. Store Embeddings in Pinecone
Input: Transcribed Text
Function: Generate and store embeddings for efficient retrieval.
Components:
Embedding Generation: Converts transcribed text into vector embeddings using a suitable model (e.g., Sentence Transformers).
Pinecone Integration: Stores the embeddings in Pinecone, a vector database, for scalable and fast retrieval.
Metadata Storage: Maintains metadata for each embedding, including chunk identifiers and timestamps for traceability.


### Create API keys

- Go to [groq official page](groq.com) to create GROQ API KEY
- Go to [pinecone official page](pinecone.com) to create PINECONE API KEY
- Set up the environment variables
```
export PINECONE_API_KEY=xxxxxxxxxxx
export GROQ_API_KEY=xxxxxxxxxxxx
```