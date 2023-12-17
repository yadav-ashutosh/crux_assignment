import pandas as pd
from .openai_test import get_semantic_column_name_by_description

DESCRIPTION_COLUMN = 'column_description'
SEMENTIC_COLUMN = 'semantic_column_name'

def process_file(file_name):
    xls = pd.ExcelFile(file_name)

    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name)

        if DESCRIPTION_COLUMN in df.columns:
            description_column_index = df.columns.get_loc(DESCRIPTION_COLUMN)

            # Create a new column 'semantic_column_name' at the end of the sheet
            df[SEMENTIC_COLUMN] = df.iloc[:, description_column_index].apply(get_semantic_column_name_by_description)

            # Save the modified DataFrame back to the Excel file
            with pd.ExcelWriter(file_name, engine='openpyxl', mode='a',if_sheet_exists='replace') as writer:
                df.to_excel(writer, sheet_name, index=False)
        else:
            print(f"Skipping sheet '{sheet_name}' as it doesn't have 'column_description' column.")