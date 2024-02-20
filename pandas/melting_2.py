import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(products)
    reshaped_df = pd.melt(df, id_vars=['product_id'], var_name='store', value_name='price')
    null_values_price = reshaped_df['price'].isna()
    final_df = reshaped_df.dropna(subset=['price'])
    return final_df
