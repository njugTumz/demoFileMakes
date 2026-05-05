import pandas as pd
import json
import os

def excel_to_json(
    input_file="vehicle.xlsx",
    output_file="vehicle.json",
    sheet_name=0
):
    try:
        # Resolve full path (root folder)
        input_path = os.path.abspath(input_file)
        output_path = os.path.abspath(output_file)

        # Read Excel file
        df = pd.read_excel(input_path, sheet_name=sheet_name)

        # Replace NaN with None for valid JSON
        df = df.where(pd.notnull(df), None)

        # Convert to list of dictionaries
        records = df.to_dict(orient="records")

        # Write to JSON file (ensure UTF-8 safe)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(records, f, indent=4, ensure_ascii=False)

        print(f"✅ Successfully converted '{input_file}' to '{output_file}'")

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        
excel_to_json()