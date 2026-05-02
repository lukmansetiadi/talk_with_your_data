import os
from google import genai

def list_gemini_models():
    """
    Connects to the Gemini API and prints a list of all available models,
    specifically those that support generating content.
    """
    # Configure the API key from environment variable
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set. Please set it in the .env file.")
    
    client = genai.Client(api_key=api_key)
    
    print("Available Models supporting generateContent:")
    models = []
    
    # In the new google.genai package, we can get models via models.list()
    for m in client.models.list():
        # Models in the new SDK return properties. We can check their name directly.
        # Support operations are slightly different, but we'll list all visible models
        if m.name.startswith("models/gemini"):
             print(f"- {m.name}")
             models.append(m.name)
            
    return models

def request_gemini_llm(prompt: str, model_name: str = 'gemini-2.5-flash') -> str:
    """
    Connects to the Gemini LLM and returns the response for a given prompt.
    
    Make sure to set the GOOGLE_API_KEY environment variable before running.
    """
    # Configure the API key from environment variable
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set. Please set it in the .env file.")
    
    client = genai.Client(api_key=api_key)
    
    # Generate content using the new SDK syntax
    # The new SDK prefers names without the "models/" prefix for generation
    clean_model_name = model_name.replace("models/", "")
    response = client.models.generate_content(
        model=clean_model_name,
        contents=prompt
    )
    
    return response.text

if __name__ == "__main__":
    # List available models
    print("--- Listing Models ---")
    try:
        available_models = list_gemini_models()
    except Exception as e:
        print(f"Error listing models: {e}")

    print("\n--- Making a Request ---")
    # Example usage
    prompt_text = "Explain how to make a request to Gemini API in 1 sentence."
    print(f"Prompt: {prompt_text}")
    try:
        # Use a model from the list if available, else default
        chosen_model = 'gemini-2.5-flash'
        if available_models and chosen_model not in available_models and 'models/' + chosen_model not in available_models:
            fallback_model = available_models[0].replace('models/', '') # Try the first available model
            print(f"{chosen_model} not found, falling back to {fallback_model}")
            chosen_model = fallback_model

        result = request_gemini_llm(prompt_text, model_name=chosen_model)
        print(f"Response:\n{result}")
    except Exception as e:
        print(f"Error: {e}")
