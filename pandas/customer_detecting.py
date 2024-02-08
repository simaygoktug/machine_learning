import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers_df=pd.DataFrame(customers)
    orders_df=pd.DataFrame(orders)

    result_df = customers_df.merge(orders_df, how='left', left_on='id', right_on='customerId')
    result_df = result_df[result_df['customerId'].isnull()]  
    result_df = result_df[['name']]  
    result_df.columns = ['Customers']  

    return result_df

#how: Bu parametre, birleştirme işleminin nasıl gerçekleştirileceğini belirler. Genellikle kullanılan değerler şunlardır:
#'left': Sol tablodaki (ilk belirtilen tablo) tüm satırları korur ve eşleşen satırlar sağ tablodan (ikinci belirtilen tablo) alınır. Eşleşmeyen sağ tablo satırları için NaN değerler eklenir.
#'right': Sağ tablodaki tüm satırları korur ve eşleşen satırlar sol tablodan alınır. Eşleşmeyen sol tablo satırları için NaN değerler eklenir.
#'inner': Sadece her iki tabloda da bulunan satırları korur, diğer satırları atar.
#'outer': Her iki tablodaki tüm satırları korur, eşleşmeyen değerler için NaN değerler eklenir.

    #left_on: Bu parametre, sol tablodaki birleştirme sütununun adını belirtir.
#right_on: Bu parametre, sağ tablodaki birleştirme sütununun adını belirtir.
