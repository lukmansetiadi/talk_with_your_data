import os
from dotenv import load_dotenv
from ai_sql_agent import generate_and_execute_sql

# Load environment variables once at the entry point
load_dotenv()

def print_results(results):
    if results is not None:
        print(f"\n--- Query Results ({len(results)} rows) ---")
        for index, row in enumerate(results):
            print(f"{index + 1}. {row}")
    else:
        print("\nNo results returned (e.g. for an INSERT/UPDATE) or an empty result set.")

if __name__ == "__main__":
    user_request = "show me top 10 products sell most"
    print(f"User Request: {user_request}\n")
    
    # Run the SQL agent with up to 3 retries on failure
    final_query, results = generate_and_execute_sql(user_request, max_retries=3)
    # final_query, results = generate_and_execute_sql(user_request, max_retries=3, llm_provider = 'groq')
    
    if final_query:
        print(f"\n=========================================")
        print(f"FINAL EXECUTED QUERY:")
        print(f"{final_query}")
        print(f"=========================================")

    # Print the final result if execution succeeded
    if results is not None:
        print_results(results)
