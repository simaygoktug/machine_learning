import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(tweets)
    invalid_tweet_ids=df[df["content"].str.len() > 15]["tweet_id"]
    result_df = pd.DataFrame({'tweet_id': invalid_tweet_ids})
    return result_df
