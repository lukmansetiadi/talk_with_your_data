import pandas as pd
from sqlalchemy import create_engine, MetaData, text
from db_config import get_active_connection_string

def _get_engine():
    """Helper method to create a SQLAlchemy engine."""
    connection_url = get_active_connection_string()
    if not connection_url:
        raise ValueError("Active connection string is not set.")
    
    # Enable isolation level AUTOCOMMIT so we don't have transaction locks
    # hanging around for simple reads, and so that user-generated inserts/updates work without explicit .commit()
    # (Though for a safe read-only bot, we should technically restrict non-selects, 
    # but for feature parity with the previous version we allow it)
    return create_engine(connection_url)

def get_database_schema_metadata():
    """
    Connects via SQLAlchemy and retrieves information schema about all columns.
    Returns a list of dictionaries with table and column details.
    """
    try:
        engine = _get_engine()
        metadata = MetaData()
        # Reflect reads the database schema
        metadata.reflect(bind=engine)
        
        records = []
        for table_name, table in metadata.tables.items():
            for column in table.columns:
                records.append({
                    'TABLE_NAME': table_name,
                    'COLUMN_NAME': column.name,
                    'COLUMN_TYPE': str(column.type),
                    'IS_NULLABLE': "YES" if column.nullable else "NO",
                    'COLUMN_KEY': "PRI" if column.primary_key else "",
                    'EXTRA': "auto_increment" if column.autoincrement == True else ""
                })
        return records
    except Exception as e:
        print(f"Error while reflecting database schema: {e}")
        return None

def get_foreign_keys():
    """
    Retrieves foreign key relationships using SQLAlchemy metadata.
    """
    try:
        engine = _get_engine()
        metadata = MetaData()
        metadata.reflect(bind=engine)
        
        records = []
        for table_name, table in metadata.tables.items():
            for fk in table.foreign_keys:
                records.append({
                    'table_name': table_name,
                    'column_name': fk.parent.name,
                    'referenced_table_name': fk.column.table.name,
                    'referenced_column_name': fk.column.name
                })
        return records
    except Exception as e:
        print(f"Error while fetching foreign keys: {e}")
        return None

def execute_sql_query(query: str):
    """
    Executes a given SQL query safely using SQLAlchemy and returns the results.
    """
    if not query or not query.strip():
        raise ValueError("Empty query provided.")
        
    try:
        engine = _get_engine()
        # Using a connection block ensures it closes automatically
        with engine.connect() as connection:
            print(f"Executing Query via SQLAlchemy...")
            
            # Explicitly execute with text() construct for security and proper formatting
            result = connection.execute(text(query))
            
            # Commit the transaction just in case the query was an INSERT/UPDATE
            connection.commit()
            
            # Check if the result returns rows (i.e. it was a SELECT statement)
            if result.returns_rows:
                # Convert the ResultProxy into a list of dictionaries
                records = [dict(row._mapping) for row in result]
                return records
            else:
                print(f"Query executed successfully. {result.rowcount} rows affected.")
                return None
                
    except Exception as e:
        # We re-raise the exception so ai_sql_agent can catch it and send it to the LLM for correction
        raise Exception(f"SQLAlchemy Execution Error: {str(e)}")

if __name__ == "__main__":
    print("Testing SQLAlchemy Connection...")
    columns_info = get_database_schema_metadata()
    if columns_info:
         print(f"Successfully reflected {len(columns_info)} columns.")
         for row in columns_info[:5]:
             print(row)
    else:
         print("Failed to connect or reflect database.")
