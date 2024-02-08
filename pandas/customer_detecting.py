import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers_df=pd.DataFrame(customers)
    orders_df=pd.DataFrame(orders)

    result_df = customers_df.merge(orders_df, how='left', left_on='id', right_on='customerId')
    result_df = result_df[result_df['id_y'].isnull()]  
    result_df = result_df[['name']]  
    result_df.columns = ['Customers']  

    return result_df
