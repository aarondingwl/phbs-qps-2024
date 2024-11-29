import pandas as pd
from pandas_datareader import data as pdr
from datetime import datetime

def fetch_cpi_data(start_date='2000-01-01'):
    end_date = datetime.today().strftime('%Y-%m-%d')
    try:
        cpi_data = pdr.get_data_fred('CPIAUCSL', start=start_date, end=end_date)
    except Exception as e:
        raise RuntimeError(f"Error fetching data: {e}")
    
    cpi_data.rename(columns={'CPIAUCSL': 'CPI'}, inplace=True)
    return cpi_data


def calculate_inflation(cpi_data):
    cpi_data['Inflation(QoQ)'] = cpi_data['CPI'].pct_change(periods=3) * 100
    last_4_quarters = cpi_data.resample('QE').last().iloc[-4:]
    return last_4_quarters[['CPI', 'Inflation(QoQ)']]