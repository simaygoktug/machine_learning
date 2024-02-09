import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = pd.DataFrame(views)
    result_df = views[views['author_id'] == views['viewer_id']]
    result_df = result_df[['author_id']].drop_duplicates()
    result_df.columns = ['id']
    result_df.sort_values(by='id', inplace=True)
    result_df.reset_index(drop=True, inplace=True)
    return result_df
