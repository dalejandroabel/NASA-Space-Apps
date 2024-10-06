import pandas as pd
import os
from utils.df_helper import give_disasters, filter_dataset_disasters, filter_dataset_weather, give_weather, get_filtered_data 

if __name__ == '__main__':

    # ----------------------------------------
    # Code to work with disaster data
    # ----------------------------------------
    path_disasters = 'datasets/pend-gdis-1960-2018-disasterlocations.csv'
    # Load the data
    data = pd.read_csv(path_disasters)

    # Clean the data
    data = filter_dataset_disasters(data)

    # Apply the filter
    request = ('Colombia', 1992, 'earthquake', 'Medellin')  # Modify the request
    country, year, disastertype, geolocation = request
    data = give_disasters(data, country=country, year=year, disastertype=disastertype, geolocation=geolocation)

    # ----------------------------------------
    # Code to work with weather data
    # ----------------------------------------
    path_weather = 'datasets/global_temperatures_by_city.csv'
    # Load the data
    data = pd.read_csv(path_weather)

    # Clean the data
    data = filter_dataset_weather(data)

    # Apply the filter
    request = (13, 1900, 8.7, 'Leicester', 'United Kingdom') # Modify the request
    year, month, temperature, city, country = request
    data = give_weather(data, year=year, month=month, AverageTemperature=temperature, City=city, Country=country)

    # ----------------------------------------
    # Código para trabajar con datos de PM2.5
    # ----------------------------------------

    # Ruta del archivo Excel
    filePath = '../sdei-annual-pm2-5/sdei-annual-pm2-5-concentrations-countries-urban-areas-v1-1998-2016-xlsx.xlsx'

    # Verificar si el archivo existe
    if not os.path.exists(filePath):
        print(f"No se encontró el archivo: {filePath}")
        exit()

    # Cargar el archivo Excel
    excelData = pd.ExcelFile(filePath)

    #  Filtrar por país, año y hoja distinta
    get_filtered_data(excelData,sheet_name='Urban PM2.5 Exposure', country='Colombia', year=2015)

