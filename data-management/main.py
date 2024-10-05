import pandas as pd
from utils.df_helper import filter_disasters, filter_df_disaster

if __name__ == '__main__':

    # Load the data
    data = pd.read_csv('datasets/pend-gdis-1960-2018-disasterlocations.csv')

    # Clean the data
    data = filter_df_disaster(data)

    # Apply the filter
    request = ('Colombia', 1992, 'earthquake', 'Medellin')
    country, year, disastertype, geolocation = request
    filter_disasters(data, country=country, year=year, disastertype=disastertype, geolocation=geolocation)