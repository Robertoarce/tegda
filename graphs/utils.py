#This file is for all non-core functions

""" Basic utility functions """

import pandas as pd
import numpy as np

def create_fake_dataset(period = 365, frequency = 'D') -> pd.DataFrame:
    """
    Creates a fake data set for testing purposes.
    
    Parameters
    ----------
    period : int, optional
          Length of the time series in days (default is 365).
         
    frequency : str, optional
         Frequency of the time series (default is 'D' for daily frequency).

    Returns
    -------
    pd.DataFrame
      The fake dataset.
    """
    # create a time index with daily frequency for a year
    time_index = pd.date_range('2022-01-01', periods = period, freq = frequency)

    # create categorical variables
    sector = np.random.choice(['Finance', 'Retail', 'Healthcare', 'Technology', 'Manufacturing', 'Energy'], size=( period,))
    zone = np.random.choice(['East', 'West', 'South', 'North'], size=( period,))
    business_size = np.random.choice(['Small', 'Medium', 'Large'], size=( period,))

    # create some random data
    error =  np.random.randint(0, 100, size=(period,))
    bias = np.random.randint(0, 100, size=(period,))
    var_1 = np.random.randint(1, 10000, size=(period,))
    var_2 = np.random.randint(1, 1000, size=(period,))
    var_3 = np.random.randint(1, 1000, size=(period,))
    
    sales_volume =  bias + var_1 + var_2 * (var_3 **(1/3)) + error
    
    
    
    
    # create the dataframe
    df = pd.DataFrame({'Time': time_index, 'Sector': sector, 'Zone': zone, 'Business_Size': business_size, 'Sales_Volume': sales_volume})

    # set the time index
    df.set_index('Time', inplace=True)
    
    return df
