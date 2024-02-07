import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(world)
    big_population_countries_df=df[df["population"]>25000000]
    big_area_countries_df=df[df["area"]>3000000]
    requested_countries_df=pd.concat([big_population_countries_df, big_area_countries_df], axis=0, ignore_index=True)
    return requested_countries_df[["name","population","area"]]
