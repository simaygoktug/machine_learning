import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(patients)
    def has_diab1_condition(conditions):
        if pd.isna(conditions):
            return False
        return any(condition.startswith('DIAB1') for condition in conditions.split())
    patients_with_diabetes_1_df=df[df["conditions"].apply(has_diab1_condition)]
    return patients_with_diabetes_1_df
