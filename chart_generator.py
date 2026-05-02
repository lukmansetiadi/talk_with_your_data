import pandas as pd
import re
import json
from gemini_client import request_gemini_llm
from groq_client import request_groq_llm
from bedrock_client import request_bedrock_llm

def generate_chart_code(df: pd.DataFrame, question: str, llm_provider: str = 'gemini') -> str:
    """
    Asks the LLM to return a JSON object with chart specifications.
    We are returning JSON instead of Python code to prevent the LLM from
    attempting to re-filter or alter the dataframe.
    """
    columns = df.columns.tolist()
    dtypes = [str(dt) for dt in df.dtypes]
    sample_data = df.head(3).to_dict(orient='records')
    
    prompt = f"""
You are a data visualization expert. Based on the user's question and the provided data, decide the best way to plot it.

USER QUESTION: "{question}"

DATA SCHEMA:
Columns: {columns}
Data Types: {dtypes}
Sample Data: {sample_data}

Return a JSON object with the following keys:
- "chart_type": (string, e.g., "bar", "line", "pie", "scatter")
- "x_axis": (string, the column name for the X-axis or Names)
- "y_axis": (string, the column name for the Y-axis or Values)
- "title": (string, a descriptive title for the chart)

Example for sales by country:
{{
  "chart_type": "bar",
  "x_axis": "country",
  "y_axis": "totalSales",
  "title": "Total Sales by Country"
}}

Return ONLY the raw JSON string. Do not use markdown tags like ```json.
"""
        
    try:
        print(f"Generating chart specs using {llm_provider.capitalize()}...")
        if llm_provider.lower() == 'groq':
            response = request_groq_llm(prompt)
        elif llm_provider.lower() == 'bedrock':
            response = request_bedrock_llm(prompt)
        else:
            response = request_gemini_llm(prompt)
            
        return response
    except Exception as e:
        print(f"Error calling {llm_provider.capitalize()}: {e}")
        return None

def execute_chart_code(chart_specs_json: str, df: pd.DataFrame):
    """
    Parses the JSON specs and safely builds a Plotly figure without using exec().
    """
    try:
        import plotly.express as px
        
        # Clean the JSON response (in case the LLM still wraps it in markdown)
        chart_specs_json = chart_specs_json.strip()
        if chart_specs_json.startswith("```json"):
            chart_specs_json = chart_specs_json[7:]
        if chart_specs_json.startswith("```"):
            chart_specs_json = chart_specs_json[3:]
        if chart_specs_json.endswith("```"):
            chart_specs_json = chart_specs_json[:-3]
        
        chart_specs_json = chart_specs_json.strip()
        
        print(f"Parsed Chart Specs:\n{chart_specs_json}")
        
        chart_specs = json.loads(chart_specs_json)

        chart_type = chart_specs.get("chart_type", "").lower()
        x = chart_specs.get("x_axis")
        y = chart_specs.get("y_axis")
        title = chart_specs.get("title")

        if not all([chart_type, x, y, title]):
            return None, "The JSON response from the LLM was missing one or more required keys (chart_type, x_axis, y_axis, title)."

        # Make sure x and y are actually in the dataframe to prevent KeyError
        if x not in df.columns:
            return None, f"LLM suggested X-axis '{x}', but it is not in the data columns: {df.columns.tolist()}"
        if y not in df.columns:
            return None, f"LLM suggested Y-axis '{y}', but it is not in the data columns: {df.columns.tolist()}"

        if chart_type == 'bar':
            fig = px.bar(df, x=x, y=y, title=title)
        elif chart_type == 'line':
            fig = px.line(df, x=x, y=y, title=title)
        elif chart_type == 'pie':
            # For pie charts, 'names' and 'values' are used instead of x and y
            fig = px.pie(df, names=x, values=y, title=title)
        elif chart_type == 'scatter':
            fig = px.scatter(df, x=x, y=y, title=title)
        else:
            # Fallback to bar if type is unknown
            fig = px.bar(df, x=x, y=y, title=title)
            
        return fig, None
        
    except json.JSONDecodeError as e:
        return None, f"Failed to decode the JSON response from the LLM. Response was: {chart_specs_json}"
    except Exception as e:
        return None, f"An error occurred while creating the chart: {str(e)}"
