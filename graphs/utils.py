# This file is for all non-core functions

""" Basic utility functions """

import pandas as pd
import numpy as np


def create_fake_dataset(period=365, frequency='D') -> pd.DataFrame:
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
    time_index = pd.date_range(
        '2022-01-01', periods=period, freq=frequency)

    # create categorical variables
    sector = np.random.choice(['Finance', 'Retail', 'Healthcare',
                              'Technology', 'Manufacturing', 'Energy'], size=(period,))
    zone = np.random.choice(['East', 'West', 'South', 'North'], size=(period,))
    business_size = np.random.choice(
        ['Small', 'Medium', 'Large'], size=(period,))

    # create some random data
    error = np.random.randint(0, 100, size=(period,))
    bias = np.random.randint(0, 100, size=(period,))
    var_1 = np.random.randint(1, 10000, size=(period,))
    var_2 = np.random.randint(1, 1000, size=(period,))
    var_3 = np.random.randint(1, 1000, size=(period,))

    sales_volume = bias + var_1 + var_2 * (var_3 ** (1/3)) + error

    # create the dataframe
    df = pd.DataFrame({'Time': time_index, 'Sector': sector, 'Zone': zone,
                      'Business_Size': business_size, 'Sales_Volume': sales_volume})

    # set the time index
    df.set_index('Time', inplace=False)

    return df


def classify_cols(df) -> pd.DataFrame:

    time_vars = [
        col for col in df.columns if pd.api.types.is_datetime64_any_dtype(df[col])]
    len_time = [df[col].nunique() for col in time_vars]

    # we will capture those of type *object*
    cat_vars = [var for var in df.columns if df[var].dtype ==
                'O' and var not in time_vars]
    len_cat = [df[col].nunique() for col in cat_vars]

    # cast all variables as categorical
    df[cat_vars] = df[cat_vars].astype('O')

    # now let's identify the numerical variables
    num_vars = [var for var in df.columns if (
        var not in cat_vars and var not in time_vars)]
    len_num = [df[col].nunique() for col in num_vars]

    return {'time': [time_vars, len_time],
            'categorical': [cat_vars, len_cat],
            'numeric': [num_vars, len_num]
            }


def rename_calls(df) -> pd.DataFrame:
    return df.columns, df.rename(columns=dict(zip(df.columns, df.columns.str.lower())))
