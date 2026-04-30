import os
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
#load_dotenv() → loads variables from a .env file into environment variables

#os.getenv("HF_API_KEY", "") → fetches your Hugging Face API key

#os.getenv("GROQ_API_KEY", "") → fetches your Groq API key

#If the key is missing, it returns an empty string ""