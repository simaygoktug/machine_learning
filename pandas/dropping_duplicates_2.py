import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id',ascending=True,inplace=True)
    person.drop_duplicates(['email'], inplace=True, keep='first')
