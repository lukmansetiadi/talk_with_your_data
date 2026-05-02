import os
import json

try:
    import boto3
    from botocore.exceptions import ClientError
except ImportError:
    boto3 = None

def request_bedrock_llm(prompt: str, model_id: str = 'anthropic.claude-3-haiku-20240307-v1:0') -> str:
    """
    Connects to the AWS Bedrock API and returns the response for a given prompt.
    
    Defaults to Anthropic Claude 3 Haiku.
    Make sure to set AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_REGION in your .env file
    or have them configured in your standard AWS credentials file.
    """
    if boto3 is None:
        raise ImportError("The 'boto3' package is not installed. Please run: pip install boto3")

    # Boto3 will automatically look for AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, 
    # and AWS_REGION in the environment variables (which were loaded by dotenv).
    try:
        region = os.environ.get("AWS_REGION", "us-east-1")
        client = boto3.client(service_name='bedrock-runtime', region_name=region)
        
        # Claude 3 Messages API payload structure
        if "claude-3" in model_id.lower():
            body = {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 1000,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt
                            }
                        ]
                    }
                ]
            }
        else:
            # Fallback generic payload (you might need to adjust this depending on the exact model chosen)
            raise NotImplementedError(f"Payload structure for model {model_id} not explicitly handled in this example.")
            
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(body)
        )
        
        response_body = json.loads(response.get('body').read())
        
        # Extract text for Claude 3 format
        if "claude-3" in model_id.lower():
            return response_body['content'][0]['text']
            
    except ClientError as e:
        raise RuntimeError(f"AWS Bedrock error: {e.response['Error']['Message']}")
    except Exception as e:
        raise RuntimeError(f"Failed to query Bedrock: {str(e)}")

if __name__ == "__main__":
    print("--- Making a Request to AWS Bedrock ---")
    prompt_text = "Explain how to make a request to AWS Bedrock API in 1 sentence."
    print(f"Prompt: {prompt_text}")
    try:
        result = request_bedrock_llm(prompt_text)
        print(f"Response:\n{result}")
    except Exception as e:
        print(f"Error: {e}")
