import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Active Database Connection (Can be overridden by Streamlit UI)
# Options: "mysql", "redshift", "postgresql", "sqlite"
ACTIVE_DB_TYPE = os.getenv("ACTIVE_DB_TYPE", "mysql")

# Database credentials from environment variables
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "classicmodels")

# Connection Strings
DB_CONNECTIONS = {
    # MySQL connection string format: mysql+mysqlconnector://user:password@host:port/database
    "mysql": f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    
    # Redshift connection string format: redshift+redshift_connector://user:password@host:port/database
    "redshift": os.getenv("REDSHIFT_URL", "redshift+redshift_connector://your_user:your_password@your-cluster.redshift.amazonaws.com:5439/your_db"),
    
    # PostgreSQL connection string format: postgresql+psycopg2://user:password@host:port/database
    "postgresql": os.getenv("POSTGRES_URL", f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"),
    
    # SQLite connection string format: sqlite:///path/to/database.db
    "sqlite": os.getenv("SQLITE_URL", "sqlite:///my_local_data.db")
}

def get_active_connection_string():
    return DB_CONNECTIONS.get(ACTIVE_DB_TYPE)
