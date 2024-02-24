import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(courses)
    class_counts = df.groupby('class').size()
    result = class_counts[class_counts >= 5].reset_index()
    result.columns = ['class', 'count']  
    del result['count']  
    return result 
