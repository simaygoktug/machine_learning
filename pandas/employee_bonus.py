import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary']
    employees.loc[(employees['employee_id'] % 2 == 0) | (employees['name'].str[0] == 'M'), 'bonus'] = 0
    return employees[['employee_id', 'bonus']].sort_values('employee_id', ascending = True)
