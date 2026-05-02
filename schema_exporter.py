import os
from database_client import get_database_schema_metadata, get_foreign_keys
from db_config import ACTIVE_DB_TYPE

def export_schema_to_markdown(output_filename: str = "database_schema.md"):
    """
    Retrieves the database schema using SQLAlchemy metadata
    and exports it to a structured Markdown file. This file can be
    used as additional context for the LLM.
    """
    print(f"Fetching database schema from {ACTIVE_DB_TYPE}...")
    columns_info = get_database_schema_metadata()
    foreign_keys = get_foreign_keys()
    
    if not columns_info:
        print("Failed to retrieve database schema.")
        return False
        
    # Group columns by table
    schema_dict = {}
    for row in columns_info:
        table = row['TABLE_NAME']
        if table not in schema_dict:
            schema_dict[table] = []
        schema_dict[table].append(row)
        
    # Using the active database type as the label
    db_name = f'{ACTIVE_DB_TYPE}_database'
    
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(f"# Database Schema: `{db_name}` ({ACTIVE_DB_TYPE})\n\n")
            f.write("This document provides a detailed overview of the tables and columns in the database.\n\n")
            
            for table, cols in schema_dict.items():
                f.write(f"## Table: `{table}`\n\n")
                f.write("| Column Name | Data Type | Nullable | Key | Extra |\n")
                f.write("|-------------|-----------|----------|-----|-------|\n")
                
                for col in cols:
                    col_name = col.get('COLUMN_NAME', '')
                    col_type = col.get('COLUMN_TYPE', '')
                    is_nullable = col.get('IS_NULLABLE', '')
                    col_key = col.get('COLUMN_KEY', '')
                    extra = col.get('EXTRA', '')
                    
                    f.write(f"| `{col_name}` | `{col_type}` | {is_nullable} | {col_key} | {extra} |\n")
                
                f.write("\n")
                
            # Add Table Relationships Section
            f.write("## Table Relationships\n")
            if foreign_keys and len(foreign_keys) > 0:
                f.write("The following foreign key relationships exist between tables. Use these to correctly JOIN tables in SQL queries.\n\n")
                for fk in foreign_keys:
                    table_name = fk.get('table_name', '')
                    column_name = fk.get('column_name', '')
                    ref_table = fk.get('referenced_table_name', '')
                    ref_column = fk.get('referenced_column_name', '')
                    
                    if table_name and ref_table:
                        f.write(f"- The `{table_name}.{column_name}` column joins with the `{ref_table}.{ref_column}` column.\n")
                f.write("\n")
            else:
                print("No foreign keys found in the database. Adding note to schema.")
                f.write("No explicit foreign key relationships are defined in this database schema. You must infer relationships based on column names (e.g., matching `customerNumber` to `customerNumber`).\n\n")
                
        print(f"Successfully exported schema to {output_filename}")
        return True
        
    except Exception as e:
        print(f"Error writing to markdown file: {e}")
        return False

if __name__ == "__main__":
    export_schema_to_markdown()
