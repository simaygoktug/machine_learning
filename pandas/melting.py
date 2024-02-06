import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(report)
    reshaped_df = pd.melt(df, id_vars=['product'], var_name='quarter', value_name='sales')
    return reshaped_df
