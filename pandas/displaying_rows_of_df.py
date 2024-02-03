import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(employees)
    result=df.head(3)
    return result
