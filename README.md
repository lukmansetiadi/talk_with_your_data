# Talk With Your Data 🤖📊

An AI-powered, Text-to-SQL chatbot application built with Streamlit and Python. This tool allows you to ask plain English questions about your SQL database, and it automatically translates them into dialect-specific SQL queries, executes them, and displays the results in a clean, interactive data table. 

It also includes a powerful **Deep Research Analysis** suite that allows you to collect data over time and perform complex meta-analysis on it using LLMs, as well as an automated **Data Visualization** engine.

## Features

- **Natural Language to SQL**: Ask questions in plain English and get database results instantly.
- **Universal Multi-Database Support**: Thanks to `SQLAlchemy`, this app can connect to almost any SQL database. Currently configured connection strings support:
  - MySQL, Amazon Redshift, PostgreSQL, SQLite.
- **Dynamic Chart Generation**: Generate interactive Plotly charts directly from your SQL results with a single click.
- **Export to Excel**: Download the results of any SQL query or AI-generated table to `.xlsx` files.
- **Multi-LLM Support**: Dynamically switch between **Groq**, **Google Gemini**, and **AWS Bedrock**.
- **Automatic Self-Correction**: Agent automatically retries and fixes invalid SQL queries by feeding database errors back to the LLM.
- **Deep Research Analysis Suite**: 
  - Save SQL data tables to `research_context.md`.
  - Upload `.docx` documents to enrich research context.
  - Perform complex analytical questions against aggregated data.
- **Advanced Template & Batch Execution**:
  - **Save to Template**: Save successful prompts and SQL queries (excluding data) to a `research_template.md` library.
  - **Batch Run**: Execute all queries in your library with a single click.
  - **Automated Reporting**: Batch runs generate a timestamped `research_template_output.md` report.
  - **Multi-Context Analysis**: Upload documents to analyze batch SQL results against external requirements or goals.
- **Query Recommendations**:
  - Upload multiple `.md` files (like schema and research outputs) and prompt the AI to recommend new insights or queries.
  - Generates multiple separated SQL statements based on your context.
  - **Execute Recommendations**: A one-click button runs all AI-recommended queries dynamically, automatically separating and titling them using SQL comments.
- **Context-Aware Schema**: Automatically reflects database metadata and foreign keys into a `database_schema.md` for precise LLM context.
- **Business Rules & Golden Queries**: Inject custom definitions and examples via `business_rules.md`.
- **Default Prompt Templates**: Pre-configured prompts help speed up analysis and query recommendation tasks across all context forms.

## Prerequisites

- **Python 3.8+**
- A local or remote **SQL Database** running.

## Installation

1. Clone this repository.
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your credentials:

```env
# Database Configuration
DB_USER=root
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=classicmodels
ACTIVE_DB_TYPE=mysql

# LLM API Keys
GOOGLE_API_KEY=your_gemini_api_key_here
GROQ_API_KEY=your_groq_api_key_here
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_REGION=us-east-1
```

## Usage

To run the web application:

```bash
streamlit run run.py
```

1. **Select LLM**: Choose your preferred AI model from the sidebar.
2. **Context Management**: Use the collapsible sidebar sections:
    - **📂 Database Context**: Manage schema reflection.
    - **⚖️ Business Rules**: Inject custom logic and Golden Queries.
    - **🔍 Research Context**: Collect and analyze ad-hoc data and documents.
    - **🛠️ Research Context Advanced**: Manage your query template library and batch execution reports.
    - **💡 Query Recommendations**: Upload markdown context files, generate new insights and queries from the AI, and seamlessly execute them.
3. **Initialize Schema**: Click **Generate/Refresh Schema from DB** in the sidebar.
4. **Chat & Build**: Ask questions, then use **📝 Save to Template** to build your library or **💾 Save to Research** to collect data.
5. **Batch Reporting**: Go to **🛠️ Research Context Advanced** and click **🚀 Run All Queries** to generate a full business report.

## File Structure

- `run.py`: The main Streamlit web application orchestrating the UI and chat flow.
- `ai_sql_agent.py`: Core orchestrator for prompting, LLM routing, query splitting, and error retry logic.
- `prompt_template.py`: Storage for standard template prompts used in the UI.
- `chart_generator.py`: Generates and executes dynamic Plotly charts.
- `schema_exporter.py`: Utility to export schemas and foreign keys to Markdown.
- `db_config.py`: Centralized database configuration using environment variables.
- `database_client.py`: Handles SQLAlchemy connections and raw SQL execution.
- `gemini_client.py`, `groq_client.py`, `bedrock_client.py`: LLM SDK wrappers.