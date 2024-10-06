import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import json
import unidecode

# Important functions to work with the data
# Function to remove accents
def remove_accents(word):
    return unidecode.unidecode(word)

# Function to convert the coordinates
def convert_coordinate(value):
    if 'N' in value or 'E' in value:
        return float(value[:-1])
    elif 'S' in value or 'W' in value:
        return -float(value[:-1])
    return float(value)

# Functions to filter the data of disasters

def filter_dataset_disasters(df):
    return df[['country', 'year', 'geolocation', 'disastertype', 'latitude', 'longitude']]

# Functions to give the data of disasters

def give_disasters(df, **kwargs):
    # Check if the country, year, disaster type and geolocation are not None
    for key, value in kwargs.items():
        if value is not None:
            df = df[df[key] == value]
    return df

# Functions to plot the data

def plot_disaster_locations(df, year):
    df_year = df[df['year'] == year]
    plt.figure(figsize=(10, 10))
    sns.scatterplot(x='longitude', y='latitude', hue='disastertype', data=df_year)
    plt.title(f'Disaster locations in {year}')
    plt.show()

def plot_disaster_locations_by_country(df, year, country):
    df_year_country = df[(df['year'] == year) & (df['country'] == country)]
    plt.figure(figsize=(10, 10))
    sns.scatterplot(x='longitude', y='latitude', hue='disastertype', data=df_year_country)
    plt.title(f'Disaster locations in {year} in {country}')
    plt.show()

# Functions to filter the data of weather
def filter_dataset_weather(df, remove_accents, convert_coordinate):
    # Remove accents from the columns
    df['City'] = df['City'].apply(remove_accents)
    df['Country'] = df['Country'].apply(remove_accents)
    # Filter the columns
    df = df[['dt', 'AverageTemperature', 'City', 'Country', 'Latitude', 'Longitude']]
    # Delete the rows with NaN values
    df = df.dropna()
    # Get year and month from the date
    df['dt'] = pd.to_datetime(df['dt'])
    df['year'] = df.dt.dt.year
    df['month'] = df.dt.dt.month
    df.drop('dt', axis=1, inplace=True)
    # Convert the coordinates
    df['Latitude'] = df['Latitude'].apply(convert_coordinate)
    df['Longitude'] = df['Longitude'].apply(convert_coordinate)
    # Replace -0.00 values with 0.00
    df['Longitude'] = df['Longitude'].replace(-0.00, 0.00)
    df['Latitude'] = df['Latitude'].replace(-0.00, 0.00)
    # Sort the values
    df = df.sort_values(by=['year', 'month'])
    return df

# Functions to give the data of weather
def give_weather(df, **kwargs):
    # Check if the country, year, disaster type and geolocation are not None
    for key, value in kwargs.items():
        if value is not None:
            df = df[df[key] == value]
    return df

# Información de las hojas a cargar y los filtros a aplicar del excel de PM2.5
sheet_info = {
    'Country PM2.5 Exposure': {
        'filter_prefix': 'AVPMC_',
        'filter_cols': ['COUNTRY']
    },
    'Country PM2.5 Exceedance': {
        'filter_prefix': 'PMEXDC_',
        'filter_cols': ['COUNTRY']
    },
    'Urban PM2.5 Exposure': {
        'filter_prefix': 'AVPMU_',
        'filter_cols': ['COUNTRYENG']
    }
}

def load_and_filter_sheet(excel_data, sheet_name, filter_prefix, filter_cols):
    # Cargar la hoja
    df = excel_data.parse(sheet_name)
    # Filtrar las columnas que empiezan con el prefijo
    data_columns = [col for col in df.columns if col.startswith(filter_prefix)]
    # Renombrar las columnas eliminando el prefijo y espacios
    renamed_columns = {col: col.replace(filter_prefix, '').strip() for col in data_columns}
    df.rename(columns=renamed_columns, inplace=True)
    # Crear lista de columnas filtradas (sin prefijos)
    filtered_columns = filter_cols + list(renamed_columns.values())
    # Seleccionar las columnas filtradas
    filtered_df = df[filtered_columns]
    return filtered_df

# Cargar y filtrar cada hoja
def cargarYfiltrarhojas(excelData):
    filtered_dataframes = {}
    for sheet_name, info in sheet_info.items():
        filtered_df = load_and_filter_sheet(
            excelData,
            sheet_name,
            info['filter_prefix'],
            info['filter_cols']
        )
        filtered_dataframes[sheet_name] = filtered_df
    return filtered_dataframes

def get_filtered_data(excelData, sheet_name=None, country=None, year=None, nameFileJson='../datasets/data.json'):
    """
    Devuelve los datos filtrados según los parámetros proporcionados.
    """
    results = []
    filtered_dataframes = cargarYfiltrarhojas(excelData=excelData)
    sheets_to_check = [sheet_name] if sheet_name else filtered_dataframes.keys()
    
    for sheet in sheets_to_check:
        df = filtered_dataframes.get(sheet)
        if df is not None:
            df_filtered = df.copy()
            
            # Filtrar por país
            if country is not None:
                country_col = None
                if 'COUNTRY' in df_filtered.columns:
                    country_col = 'COUNTRY'
                elif 'COUNTRYENG' in df_filtered.columns:
                    country_col = 'COUNTRYENG'
                else:
                    continue
                df_filtered = df_filtered[df_filtered[country_col] == country]
                if df_filtered.empty:
                    continue

            # Filtrar por año
            if year is not None:
                year = str(year)
                if year in df_filtered.columns:
                    columns_to_keep = [col for col in df_filtered.columns if not col.isdigit()] + [year]
                    df_filtered = df_filtered[columns_to_keep]
                else:
                    continue
            else:
                # Incluir todas las columnas de años
                year_columns = [col for col in df_filtered.columns if col.isdigit()]
                columns_to_keep = [col for col in df_filtered.columns if not col.isdigit()] + year_columns
                df_filtered = df_filtered[columns_to_keep]
            
            # Añadir el nombre de la hoja
            df_filtered['Sheet'] = sheet
            results.append(df_filtered)
    
    if results:
        df_result = pd.concat(results, ignore_index=True)
        df_result.to_json(path_or_buf=nameFileJson, orient='records')
        return df_result
    else:
        return json.dumps([])