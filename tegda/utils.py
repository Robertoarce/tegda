#This file is for all non-core functions

""" Basic utility functions """

def create_fake_dataset(period = 365, frequency = 'D') -> Dataframe:
    """
    Creates a fake data set for testing purpuses.
    Parameters
    ----------
    period :
         (Default value = 365)
    frequency :
         (Default value = 'D')

    Returns
    -------
    The fake dataset.
    """


  # create a time index with daily frequency for a year
  time_index = pd.date_range('2022-01-01', periods = period, freq = frequency)

  # create categorical variables
  sector = np.random.choice(['Finance', 'Retail', 'Healthcare', 'Technology', 'Manufacturing', 'Energy'], size=( period,))
  zone = np.random.choice(['East', 'West', 'South', 'North'], size=( period,))
  business_size = np.random.choice(['Small', 'Medium', 'Large'], size=( period,))

  # create some random data
  sales_volume = np.random.randint(0, 100, size=(period,))

  # create the dataframe
  df = pd.DataFrame({'Time': time_index, 'Sector': sector, 'Zone': zone, 'Business_Size': business_size, 'Sales_Volume': sales_volume})

  # set the time index
  df.set_index('Time', inplace=True)
