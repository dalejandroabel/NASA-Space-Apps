import pandas as pd
import os
from utils.df_helper import remove_accents, convert_coordinate, give_disasters, filter_dataset_disasters, filter_dataset_weather, give_weather, replace_dataset_people, filter_dataset_people, filter_datasets_people, give_people, replace_dataset_home, filter_dataset_home, filter_datasets_home, give_home, get_filtered_data
from utils.constants import deptos
from utils.graph_helper import plot_stratum_distribution, plot_regime_distribution, plot_education_distribution, plot_activity_distribution

if __name__ == '__main__':

    # ----------------------------------------
    # Code to work with disaster data
    # ----------------------------------------
    path_disasters = 'datasets/pend-gdis-1960-2018-disasterlocations.csv'
    # Load the data
    data_disasters = pd.read_csv(path_disasters)

    # Clean the data
    data_disasters = filter_dataset_disasters(data_disasters)

    # Apply the filter
    give_disasters(data_disasters)

    # # ----------------------------------------
    # # Code to work with weather data
    # # ----------------------------------------
    path_weather = 'datasets/global_temperatures_by_city.csv'
    # Load the data
    data_weather = pd.read_csv(path_weather)

    # Clean the data
    data_weather = filter_dataset_weather(data_weather, remove_accents, convert_coordinate)

    # Apply the filter
    give_weather(data_weather)

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

    # ----------------------------------------
    # Code to work with national data (people)
    # ----------------------------------------
    # Load the data
    path_people_2017 = 'datasets/Personas_2017.csv'
    path_people_2018 = 'datasets/Personas_2018.csv'
    path_people_2019 = 'datasets/Personas_2019.csv'
    path_people_2020 = 'datasets/Personas_2020.csv'
    path_people_2021 = 'datasets/Personas_2021.csv'
    path_people_2022 = 'datasets/Personas_2022.csv'
    path_people_2023 = 'datasets/Personas_2023.csv'

    df_per2023 = pd.read_csv(path_people_2023, sep = ',')
    df_per2022 = pd.read_csv(path_people_2022, sep = ',')
    df_per2021 = pd.read_csv(path_people_2021, sep = ',')
    df_per2020 = pd.read_csv(path_people_2020, sep = ';')
    df_per2019 = pd.read_csv(path_people_2019, sep = ';')
    df_per2018 = pd.read_csv(path_people_2018, sep = ';')
    df_per2017 = pd.read_csv(path_people_2017, sep = ';')

    dfs = [df_per2017, df_per2018, df_per2019, df_per2020, df_per2021, df_per2022, df_per2023]
    years = list(range(2017,2024))

    df_per = filter_datasets_people(dfs, deptos, years, remove_accents, filter_dataset_people)

    df_per = replace_dataset_people(df_per)

    # Give the people
    give_people(df_per)

    # Plot the stratum graph
    plot_stratum_distribution(df_per, 2020, 'Bajo', give_people)

    # Plot the regime graph
    plot_regime_distribution(df_per, 2021, 'Contributivo', give_people)

    # Plot the education graph
    plot_education_distribution(df_per, 2022, 'Superior o Universitaria', give_people)

    # Plot the activity graph
    plot_activity_distribution(df_per, 2023, 'Estudiando', give_people)

    # ----------------------------------------
    # Code to work with national data (home)
    # ----------------------------------------
    # Load the data
    path_home_2016 = 'datasets/Hogares_2016.txt'
    path_home_2017 = 'datasets/Hogares_2017.csv'
    path_home_2018 = 'datasets/Hogares_2018.csv'
    path_home_2019 = 'datasets/Hogares_2019.csv'
    path_home_2020 = 'datasets/Hogares_2020.csv'
    path_home_2021 = 'datasets/Hogares_2021.csv'
    path_home_2022 = 'datasets/Hogares_2022.csv'

    df_hog2022 = pd.read_csv(path_home_2022, sep = ',')
    df_hog2021 = pd.read_csv(path_home_2021, sep = ',')
    df_hog2020 = pd.read_csv(path_home_2020, sep = ';')
    df_hog2019 = pd.read_csv(path_home_2019, sep = ';')
    df_hog2018 = pd.read_csv(path_home_2018, sep = ';')
    df_hog2017 = pd.read_csv(path_home_2017, sep = ';')
    df_hog2016 = pd.read_csv(path_home_2016, sep = '	')

    dfs = [df_hog2016, df_hog2017, df_hog2018, df_hog2019, df_hog2020, df_hog2021, df_hog2022]
    years = list(range(2016,2023))

    df_hog = filter_datasets_home(dfs, deptos, years, remove_accents, filter_dataset_home)

    df_hog = replace_dataset_home(df_hog)

    # Give the home
    give_home(df_hog)

    # Plot the stratum graph