import pandas as pd
import os
from utils.df_helper import filter_disasters, get_disasters , get_filtered_data 

if __name__ == '__main__':

    # Load the data
    data = pd.read_csv('datasets/pend-gdis-1960-2018-disasterlocations.csv')

    # Clean the data
    data = get_disasters(data)

    # Apply the filter
    request = ('Colombia', 1992, 'earthquake', 'Medellin')
    country, year, disastertype, geolocation = request
    filter_disasters(data, country=country, year=year, disastertype=disastertype, geolocation=geolocation)

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

