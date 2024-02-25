import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(orders)
    largest_number_of_orders_df=df.groupby('customer_number')['order_number'].count().reset_index()
    expected_customer_number_df = largest_number_of_orders_df[largest_number_of_orders_df['order_number'] == largest_number_of_orders_df['order_number'].max()]
    return expected_customer_number_df[['customer_number']]
