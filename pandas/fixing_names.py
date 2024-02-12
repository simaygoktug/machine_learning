import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(users)
    df['name'] = df['name'].str.capitalize()
    df = df.sort_values(by='user_id')
    return df
