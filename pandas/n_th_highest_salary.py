import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N <= 0:
        return pd.DataFrame({'getNthHighestSalary({})'.format(N): [None]})
    
    df = pd.DataFrame(employee)
    # Remove duplicate salaries
    df = df.drop_duplicates(subset='salary')
    # Sort the DataFrame by 'salary' column in descending order
    sorted_df = df.sort_values(by='salary', ascending=False)
    # Check if there are enough unique salaries to get the nth highest salary
    if N <= len(sorted_df):
        # Get the nth highest salary using iloc
        nth_highest_salary = sorted_df.iloc[N - 1]['salary']
        # Return the result as a DataFrame
        return pd.DataFrame({'getNthHighestSalary({})'.format(N): [nth_highest_salary]})
    else:
        # Return null as a DataFrame
        return pd.DataFrame({'getNthHighestSalary({})'.format(N): [None]})
