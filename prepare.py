import pandas as pd
from acquire import acquire_codeup_data

def prep_codeup_data():
    df, cohorts = acquire_codeup_data()
    df.columns = ['date', 'time', 'page_viewed', 'user_id', 'cohort_id', 'ip']
    df['datetime'] = df['date'] + ' ' + df['time']
    df['datetime'] = pd.to_datetime(df.datetime)
    df['year'] = df.datetime.dt.year
    df['month'] = df.datetime.dt.month
    df['day'] = df.datetime.dt.day
    df['hour'] = df.datetime.dt.hour
    df['weekday'] = df.datetime.dt.day_name()
    df = df.astype(object)
    df.drop(columns=['date', 'time'], inplace=True)
    combine = pd.merge(left = df, right = cohorts, how = 'left', left_on = 'cohort_id', right_on = 'cohort_id')
    combine = combine.set_index('datetime')
    return combine

def handle_nulls(df):
    df['cohort_id'] = df['cohort_id'].fillna(0)
    df['name'] = df['name'].fillna('unknown')
    df['start_date'] = df['start_date'].fillna('01-01-1900')
    df['end_date'] = df['end_date'].fillna('01-01-1900')
    df['program_id'] = df['program_id'].fillna(0)
    return df