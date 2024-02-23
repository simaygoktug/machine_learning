import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(teacher)
    result_df = df.groupby('teacher_id')['subject_id'].nunique().reset_index()
    result_df.columns = ['teacher_id', 'cnt']
    return result_df
