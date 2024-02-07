import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(products)
    requested_products_df=df[(df["low_fats"]=="Y") & (df["recyclable"]=="Y")]
    return requested_products_df[["product_id"]]
