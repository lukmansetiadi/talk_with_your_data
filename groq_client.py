import os
from dotenv import load_dotenv

# We need to import the Groq client. This requires the 'groq' python package.
try:
    from groq import Groq
except ImportError:
    # We allow this file to exist even if groq is not installed,
    # but it will fail at runtime if they try to use it.
    Groq = None

def request_groq_llm(prompt: str, model_name: str = 'meta-llama/llama-4-scout-17b-16e-instruct') -> str:
    """
    Connects to the Groq LLM API and returns the response for a given prompt.
    
    Make sure to set the GROQ_API_KEY environment variable in your .env file.
    """
    # model_name = "openai/gpt-oss-20b"
    if Groq is None:
        raise ImportError("The 'groq' package is not installed. Please run: pip install groq")

    # Configure the API key from environment variable
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set. Please set it in the .env file.")
    
    client = Groq(api_key=api_key)
    
    # Generate content using the Groq SDK (OpenAI-compatible syntax)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model_name,
    )
    
    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    print("--- Making a Request to Groq ---")
    prompt_text = "Explain how to make a request to Groq API in 1 sentence."
    print(f"Prompt: {prompt_text}")
    try:
        result = request_groq_llm(prompt_text)
        print(f"Response:\n{result}")
    except Exception as e:
        print(f"Error: {e}")
