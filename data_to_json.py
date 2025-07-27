# CONVERT EXCEL OR CSV TO JSON FORMAT 

import pandas as pd
import json
import os

# Input and output file paths
input_path = "D:/Projects/POCs/gov_scholarship_rag/data/dataset_combined.xlsx"  
output_path = "D:/Projects/POCs/gov_scholarship_rag/data/scraped.json"

exceluded_columns = ["Exservice-men", "Outcome"]

clean_column = "Name"

try:
    # File extension
    _, ext = os.path.splitext(input_path)

    # Read file based on extension
    if ext.lower() == '.csv':
        df = pd.read_csv(input_path)
    elif ext.lower() in ['.xls', '.xlsx']:
        df = pd.read_excel(input_path, engine='openpyxl')
    else:
        raise ValueError(f"Unsupported file format: {ext}")

    # Clean data (drop all empty rows where valus is NaN)
    df = df.dropna(how='all') 

    if clean_column in df.columns:
        df[clean_column] = df[clean_column].astype(str).str.replace("?", "", regex=False)

    df = df.drop(columns=[col for col in exceluded_columns if col in df.columns])

    # Convert to JSON 
    df.to_json(output_path, orient='records', indent=4)
    print(f"Data successfully converted to JSON and saved at: {output_path}")

except FileNotFoundError:
    print(f"File not found at: {input_path}")
except ValueError as ve:
    print(f"{ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
