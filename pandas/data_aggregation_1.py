import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(employees)
    # Converting event_day to datetime type
    df['event_day'] = pd.to_datetime(df['event_day'])
    # Calculating total_time
    df['total_time'] = df['out_time'] - df['in_time']
    # Grouping by emp_id and event_day, then sum total_time
    result = df.groupby(['emp_id', 'event_day']).agg({'total_time': 'sum'}).reset_index()
    # Renaming columns for clarity
    result.columns = ['emp_id', 'day', 'total_time']    
    return result
