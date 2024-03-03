import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # Merging both DataFrames to get the desired output
    result_df = pd.merge(employees, employee_uni, on='id', how='left')

    # Renaming columns as per the example output
    result_df = result_df[['unique_id', 'name']]   
    return result_df
