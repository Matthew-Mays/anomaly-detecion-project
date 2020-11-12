import pandas as pd

def acquire_codeup_data():
    df = pd.read_csv('anonymized-curriculum-access.csv', sep=' ', header=None)
    cohorts = pd.read_csv('cohorts.csv')
    return df, cohorts

