import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # Initially, we group 'actor_id' and 'director_id'.
    grouped_actor_director = actor_director.groupby(['actor_id', 'director_id'])
    
    # In the next step, we count the number of 'actor_id' and 'director_id'.
    counted_actor_director = grouped_actor_director.size()
    
    # Then, we resets the index of the DataFrame.
    indexed_actor_director = counted_actor_director.reset_index(name='cooperated')

    # After, that, we can filter the subquery to select rows where 'cooperated' count is >= 3.
    filtered_actor_director = indexed_actor_director[indexed_actor_director['cooperated'] >= 3]
    
    # Finally, we select and return a subset of 'actor_id', 'director_id' columns from the DataFrame .
    cooperated_actor_director = filtered_actor_director[['actor_id', 'director_id']]

    return cooperated_actor_director   
