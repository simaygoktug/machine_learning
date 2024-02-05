import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df1=pd.DataFrame(df1)
    df2=pd.DataFrame(df2)
    result_df = pd.concat([df1, df2], axis=0, ignore_index=True)
    return result_df
