import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(customers)
    df_no_duplicates = df.drop_duplicates(['email']) 
    return df_no_duplicates
