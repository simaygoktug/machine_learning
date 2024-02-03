import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(students)
    selected_student = df[df['student_id'] == 101][['name', 'age']]
    return selected_student
