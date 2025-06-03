import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client with API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# List fine-tuned models using the new API format
fine_tuned_models = client.fine_tuning.jobs.list()

for job in fine_tuned_models.data:
    print(job.fine_tuned_model)