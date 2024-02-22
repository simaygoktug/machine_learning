import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(activity)
    df['event_date'] = pd.to_datetime(df['event_date'])
    first_login_df = df.groupby('player_id')['event_date'].min().reset_index()
    first_login_df.columns = ['player_id', 'first_login']
    return first_login_df
