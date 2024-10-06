import pandas as pd
from utils.df_helper import filter_disasters, get_disasters

if __name__ == '__main__':

    # Load the data
    data = pd.read_csv('datasets/pend-gdis-1960-2018-disasterlocations.csv')

    # Clean the data
    data = get_disasters(data)

    # Apply the filter
    request = ('Colombia', 1992, 'earthquake', 'Medellin')
    country, year, disastertype, geolocation = request
    filter_disasters(data, country=country, year=year, disastertype=disastertype, geolocation=geolocation)