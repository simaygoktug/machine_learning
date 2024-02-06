import pandas as pd 

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(animals)
    selected_animals_df=df[df["weight"]>100]
    sorted_animals_df=selected_animals_df.sort_values(by='weight', ascending=False)
    return sorted_animals_df[["names"]]
