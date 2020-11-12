import pandas as import pd
from acquire import acquire_codeup_data

def prep_codeup_data():
    df = acquire_codeup_data()
    df.timestamp = df.timestamp.str.replace(r'(\[|\])', '', regex=True)
    df.timestamp = pd.to_datetime(df.timestamp.str.replace(':', ' ', 1))
    df = df.set_index('timestamp')
    for col in ['request_method', 'request_agent', 'destination']:
        df[col] = df[col].str.replace('"', '')
    df['request_method'] = df.request_method.str.replace(r'\?page=[0-9]+', '', regex=True)
    df[['request_call','api_version','endpoints','http']] = \
    df.request_method.str.extract(r'(?P<request_call>^[A-Z]+)\s(?P<api_version>\/api\/v[0-9])(?P<endpoints>.+)(?P<http_version>HTTP\/[0-9]\.[0-9])', expand = True)
    df['size_mb'] = [n/1024/1024 for n in df['size']]
    return df