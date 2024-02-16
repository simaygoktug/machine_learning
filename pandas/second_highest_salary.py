import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(employee)
    df = df.drop_duplicates(subset='salary')
    sorted_df = df.sort_values(by='salary', ascending=False)
    second_highest_salary = sorted_df.iloc[1]['salary'] if len(sorted_df) > 1 else None
    output_df = pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})
    return output_df
