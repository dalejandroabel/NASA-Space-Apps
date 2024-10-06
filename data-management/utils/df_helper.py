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

# Información de las hojas a cargar y los detalles de procesamiento
sheet_info = {
    'Country PM2.5 Exceedance': {
        'filter_prefix': 'PMEXDC_',
        'country_column': 'COUNTRY'
    },
    'Urban PM2.5 Exposure': {
        'filter_prefix': 'AVPMU_',
        'country_column': 'COUNTRYENG',
        'city_column': 'STNDRDNAME'
    }
}

# Función para normalizar nombres (países y ciudades)
def normalize_name(name):
    # Convertir a string por si hay valores nulos
    name = str(name)
    # Eliminar tildes y caracteres especiales
    name_without_accents = unidecode.unidecode(name)
    # Convertir a minúsculas y luego capitalizar
    name_formatted = name_without_accents.lower().capitalize()
    return name_formatted

# Función para leer y procesar cada hoja
def load_and_process_sheet(excel_data, sheet_name, filter_prefix, country_column, city_column=None):
    # Cargar la hoja
    df = excel_data.parse(sheet_name)
    
    # Filtrar las columnas que empiezan con el prefijo
    data_columns = [col for col in df.columns if col.startswith(filter_prefix)]
    
    # Renombrar las columnas eliminando el prefijo y espacios
    renamed_columns = {col: col.replace(filter_prefix, '').strip() for col in data_columns}
    df.rename(columns=renamed_columns, inplace=True)
    
    # Crear lista de columnas filtradas (sin prefijos)
    key_columns = [country_column]
    if city_column:
        key_columns.append(city_column)
    filtered_columns = key_columns + list(renamed_columns.values())
    
    # Seleccionar las columnas filtradas
    df = df[filtered_columns]
    
    # Normalizar los nombres de los países y ciudades
    df[country_column] = df[country_column].apply(normalize_name)
    if city_column:
        df[city_column] = df[city_column].apply(normalize_name)
    
    # Renombrar las columnas de país y ciudad para consistencia
    df = df.rename(columns={country_column: 'COUNTRY'})
    if city_column:
        df = df.rename(columns={city_column: 'CITY'})
    
    # Agregar una columna para indicar el indicador (nombre de la hoja)
    df['Indicator'] = sheet_name
    
    # Convertir a formato largo
    id_vars = ['COUNTRY', 'Indicator']
    if city_column:
        id_vars.insert(1, 'CITY')  # Insertar CITY después de COUNTRY
    df_long = pd.melt(df, id_vars=id_vars, var_name='Year', value_name='Value')
    
    # Convertir 'Year' a entero
    df_long['Year'] = df_long['Year'].astype(int)
    
    # Eliminar filas con valores nulos en 'Value'
    df_long = df_long.dropna(subset=['Value'])
    
    return df_long

# Procesar y combinar las hojas seleccionadas
df_list = []
for sheet_name, info in sheet_info.items():
    df_sheet = load_and_process_sheet(
        excel_data=excelData,
        sheet_name=sheet_name,
        filter_prefix=info['filter_prefix'],
        country_column=info['country_column'],
        city_column=info.get('city_column')  # Puede ser None si no está definido
    )
    df_list.append(df_sheet)

# Combinar las hojas en un solo DataFrame
df_combined = pd.concat(df_list, ignore_index=True)

# Función para filtrar datos
def filter_data(df, indicator=None, countries=None, cities=None, start_year=None, end_year=None):
    if indicator is not None:
        df = df[df['Indicator'] == indicator]
    if countries is not None:
        # Normalizar los nombres de los países en el filtro
        countries_normalized = [normalize_name(country) for country in countries]
        df = df[df['COUNTRY'].isin(countries_normalized)]
    if cities is not None and 'CITY' in df.columns:
        # Normalizar los nombres de las ciudades en el filtro
        cities_normalized = [normalize_name(city) for city in cities]
        df = df[df['CITY'].isin(cities_normalized)]
    if start_year is not None:
        df = df[df['Year'] >= start_year]
    if end_year is not None:
        df = df[df['Year'] <= end_year]
    return df
    

# ----------------------------------------
# Code to work with national data
# ----------------------------------------

# Function to filter the data of people
def filter_dataset_people(df, deptos, year, remove_accents):
    
    # Apply the title case to the columns
    df.columns = df.columns.str.lower()

    # Check for the presence of the department column
    if 'depto' in df.columns:
        df['depto'] = df['depto'].apply(lambda x: [depto[1] for depto in deptos if depto[0] == x][0])
    elif 'dpto' in df.columns:
        df['depto'] = df['dpto'].apply(lambda x: [depto[1] for depto in deptos if depto[0] == x][0])

    # Remove rows where depto is None (optional, based on your needs)
    df = df.dropna(subset=['depto'])
    
    # Remove accents from the columns
    df['depto'] = df['depto'].apply(remove_accents)
    df['dominio'] = df['dominio'].apply(remove_accents)
    
    # Applying the title case to the dominio column
    df['dominio'] = df['dominio'].str.title()
    
    # Delete 'Resto Urbano' and 'Rural' from the dominio column
    df = df[df['dominio'] != 'Resto Urbano']
    df = df[df['dominio'] != 'Rural']
    
    # Add the year column
    df['año'] = year
    df['regimen'] = df['p6100']
    df['actividad'] = df['p6240']
    
    if year in list(range(2021, 2024)):
        # Filter the columns
        df['estrato'] = None
        if year == 2021:
            df['educacion'] = df['p6210']
        else:
            df['educacion'] = df['p3042']
        df = df[['depto', 'dominio', 'año', 'estrato', 'regimen', 'educacion', 'actividad']]
    else:
        # Filter the columns
        df['estrato'] = df['estrato1']
        df['educacion'] = df['p6210']
        df = df[['depto', 'dominio', 'año', 'estrato', 'regimen', 'educacion', 'actividad']]
    
    return df

# Function to filter some data of people
def filter_datasets_people(dfs, deptos, years, remove_accents, filter_dataset_people):
    df_17, df_18, df_19, df_20, df_21, df_22, df_23 = [filter_dataset_people(dfs[i], deptos, years[i], remove_accents) for i in range(len(dfs))]
    df = pd.concat([df_17, df_18, df_19, df_20, df_21, df_22, df_23])
    return df

# Function to replace the dataset of people
def replace_dataset_people(df):
    df['regimen'] = df['regimen'].replace({'1': 'Contributivo', '2': 'Especial', '3': 'Subsidiado', '9': 'No sabe, no informa'})
    df['regimen'] = df['regimen'].replace({1.0: 'Contributivo', 2.0: 'Especial', 3.0: 'Subsidiado', 9.0: 'No sabe, no informa'})
    df['actividad'] = df['actividad'].replace({'1': 'Trabajando', '2': 'Buscando trabajo', '3': 'Estudiando', '4': 'Oficios del hogar', '5': 'Incapacitado permanente', '6': 'Otra actividad'})
    df['actividad'] = df['actividad'].replace({1.0: 'Trabajando', 2.0: 'Buscando trabajo', 3.0: 'Estudiando', 4.0: 'Oficios del hogar', 5.0: 'Incapacitado permanente', 6.0: 'Otra actividad'})
    df['educacion'] = df['educacion'].replace({'1': 'Ninguno', '2': 'Preescolar', '3': 'Básica primaria', '4': 'Básica secundaria', '5': 'Media', '6': 'Superior o Universitaria', '9': 'No sabe, no informa'})
    df['educacion'] = df['educacion'].replace({1.0: 'Ninguno', 2.0: 'Preescolar', 3.0: 'Básica primaria', 4.0: 'Básica secundaria', 5.0: 'Media', 6.0: 'Superior o Universitaria', 9.0: 'No sabe, no informa'})
    return df

# Function to give the data of people
def give_people(df, **kwargs):
    # Check if the country, year, disaster type and geolocation are not None
    for key, value in kwargs.items():
        if value is not None:
            df = df[df[key] == value]
    df.to_json('datasets/people.json',orient='records')