import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:  
    df = pd.DataFrame(users)
    regex = r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$'
    valid_emails_df = df[df['mail'].str.match(regex)]
    return valid_emails_df
