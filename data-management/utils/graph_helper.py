import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import utils.df_helper as give_people
import plotly.express as px
import unidecode
from utils.df_helper import normalize_name

# Function to get a graph of the stratum distribution

def plot_stratum_distribution(df, year, typeDistribution, give_people):

    df_year = give_people(df, año = year)

    if typeDistribution == 'Bajo':
        c_year = df_year[df_year['estrato'].isin([1,2])].groupby('depto').size() / df_year.groupby('depto').size()
    
    elif typeDistribution == 'Medio':
        c_year = df_year[df_year['estrato'].isin([3,4])].groupby('depto').size() / df_year.groupby('depto').size()

    elif typeDistribution == 'Alto':
        c_year = df_year[df_year['estrato'].isin([5,6])].groupby('depto').size() / df_year.groupby('depto').size()
    
    # Data in ascending order
    c_year = c_year.sort_values()
    # Plot the graph

    plt.figure(figsize=(15, 8))

    sns.barplot(x = c_year.index, y = c_year)

    # Add the value of the percentage over the bars
    for i in range(len(c_year)):
        plt.text(i, c_year[i], round(c_year[i]*100, 2), ha = 'center', va = 'bottom')
    
    plt.title('Distribución de la población por estrato en el año ' + str(year) + ' en ' + typeDistribution + ' estrato')
    plt.xticks(rotation=90)
    plt.xlabel('Departamento')
    plt.ylabel('Porcentaje de la población')
    # Vary the color in the bars
    plt.bar(c_year.index, c_year, color = sns.color_palette('viridis', len(c_year)))
    plt.show()

# Function to get a graph of the regime distribution

def plot_regime_distribution(df, year, typeRegime, give_people):

    df_year = give_people(df, año = year)

    if typeRegime == 'Contributivo':
        r_year = df_year[df_year['regimen'] == 'Contributivo'].groupby('depto').size() / df_year.groupby('depto').size()
    
    elif typeRegime == 'Especial':
        r_year = df_year[df_year['regimen'] == 'Especial'].groupby('depto').size() / df_year.groupby('depto').size()

    elif typeRegime == 'Subsidiado':
        r_year = df_year[df_year['regimen'] == 'Subsidiado'].groupby('depto').size() / df_year.groupby('depto').size()
    
    elif typeRegime == 'No sabe, no informa':
        r_year = df_year[df_year['regimen'] == 'No sabe, no informa'].groupby('depto').size() / df_year.groupby('depto').size()
    
    # Data in ascending order
    r_year = r_year.sort_values()
    # Plot the graph

    plt.figure(figsize=(15, 8))

    sns.barplot(x = r_year.index, y = r_year)

    # Add the value of the percentage over the bars
    for i in range(len(r_year)):
        plt.text(i, r_year[i], round(r_year[i]*100, 2), ha = 'center', va = 'bottom')

    plt.title('Distribución de la población por régimen en el año ' + str(year) + ' en ' + typeRegime + ' régimen')
    plt.xticks(rotation=90)
    plt.xlabel('Departamento')
    plt.ylabel('Porcentaje de la población')
    # Vary the color in the bars
    plt.bar(r_year.index, r_year, color = sns.color_palette('viridis', len(r_year)))
    plt.show()

# Function to get a graph of the education distribution

def plot_education_distribution(df, year, typeEducation, give_people):

    df_year = give_people(df, año = year)

    if typeEducation == 'Ninguno':
        e_year = df_year[df_year['educacion'] == 'Ninguno'].groupby('depto').size() / df_year.groupby('depto').size()

    elif typeEducation == 'Preescolar':
        e_year = df_year[df_year['educacion'] == 'Preescolar'].groupby('depto').size() / df_year.groupby('depto').size()
    
    elif typeEducation == 'Básica primaria':
        e_year = df_year[df_year['educacion'] == 'Básica primaria'].groupby('depto').size() / df_year.groupby('depto').size()

    elif typeEducation == 'Básica secundaria':
        e_year = df_year[df_year['educacion'] == 'Básica secundaria'].groupby('depto').size() / df_year.groupby('depto').size()
    
    elif typeEducation == 'Media':
        e_year = df_year[df_year['educacion'] == 'Media'].groupby('depto').size() / df_year.groupby('depto').size()

    elif typeEducation == 'Superior o Universitaria':
        e_year = df_year[df_year['educacion'] == 'Superior o Universitaria'].groupby('depto').size() / df_year.groupby('depto').size()

    elif typeEducation == 'No sabe, no informa':
        e_year = df_year[df_year['educacion'] == 'No sabe, no informa'].groupby('depto').size() / df_year.groupby('depto').size()

    # The data in ascending order
    e_year = e_year.sort_values()

    # Plot the graph

    plt.figure(figsize=(15, 8))

    sns.barplot(x = e_year.index, y = e_year)

    # Add the value of the percentage over the bars
    for i in range(len(e_year)):
        plt.text(i, e_year[i], round(e_year[i]*100, 2), ha = 'center', va = 'bottom')
    
    # Labels and title
    plt.title('Distribución de la población por nivel de educación en el año ' + str(year) + ' en ' + typeEducation + ' educación')
    plt.xticks(rotation=90)
    plt.xlabel('Departamento')
    plt.ylabel('Porcentaje de la población')
    # Vary the color in the bars
    plt.bar(e_year.index, e_year, color = sns.color_palette('viridis', len(e_year)))
    plt.show()

# Function to get a graph of the activity distribution

def plot_activity_distribution(df, year, typeActivity, give_people):

    df_year = give_people(df, año = year)

    if typeActivity == 'Trabajando':
        a_year = df_year[df_year['actividad'] == 'Trabajando'].groupby('depto').size() / df_year.groupby('depto').size()

    elif typeActivity == 'Buscando trabajo':
        a_year = df_year[df_year['actividad'] == 'Buscando trabajo'].groupby('depto').size() / df_year.groupby('depto').size()

    elif typeActivity == 'Estudiando':
        a_year = df_year[df_year['actividad'] == 'Estudiando'].groupby('depto').size() / df_year.groupby('depto').size()

    elif typeActivity == 'Oficios del hogar':
        a_year = df_year[df_year['actividad'] == 'Oficios del hogar'].groupby('depto').size() / df_year.groupby('depto').size()

    elif typeActivity == 'Incapacitado permanente':
        a_year = df_year[df_year['actividad'] == 'Incapacitado permanente'].groupby('depto').size() / df_year.groupby('depto').size()

    elif typeActivity == 'Otra actividad':
        a_year = df_year[df_year['actividad'] == 'Otra actividad'].groupby('depto').size() / df_year.groupby('depto').size()

    # The data in ascending order
    a_year = a_year.sort_values()

    # Plot the graph

    plt.figure(figsize=(15, 8))

    sns.barplot(x = a_year.index, y = a_year)

    # Add the value of the percentage over the bars
    for i in range(len(a_year)):
        plt.text(i, a_year[i], round(a_year[i]*100, 2), ha = 'center', va = 'bottom')

    # Labels and title
    plt.title('Distribución de la población por actividad en el año ' + str(year) + ' en ' + typeActivity + ' actividad')
    plt.xticks(rotation=90)
    plt.xlabel('Departamento')
    plt.ylabel('Porcentaje de la población')
    # Vary the color in the bars
    plt.bar(a_year.index, a_year, color = sns.color_palette('viridis', len(a_year)))
    plt.show()

# Prepare the graph of the poverty distribution

def plot_poverty_distribution(df, year, give_home):

    df_year = give_home(df, año = year)

    p_year = df_year[df_year['pobre'] == 1].groupby('depto').size() / df_year.groupby('depto').size()

    # The data in ascending order
    p_year = p_year.sort_values()

    plt.figure(figsize=(15, 8))

    # Graph of the poor population with seaborn
    sns.barplot(x = p_year.index, y = p_year)

    # Add the value of the percentage over the bars
    for i in range(len(p_year)):
        plt.text(i, p_year[i], round(p_year[i]*100, 2), ha = 'center', va = 'bottom')

    plt.title('Distribución de la población por pobreza en el año ' + str(year) + ' en pobreza')
    plt.xticks(rotation=90)
    plt.xlabel('Departamento')
    plt.ylabel('Porcentaje de la población')
    # Vary the color in the bars
    plt.bar(p_year.index, p_year, color = sns.color_palette('viridis', len(p_year)))
    plt.show()

# Function to get a graph of the extreme poverty distribution

def plot_extreme_poverty_distribution(df, year, give_home):

    df_year = give_home(df, año = year)

    ep_year = df_year[df_year['indigente'] == 1].groupby('depto').size() / df_year.groupby('depto').size()

    # The data in ascending order
    ep_year = ep_year.sort_values()

    plt.figure(figsize=(15, 8))

    # Graph of the poor population with seaborn
    sns.barplot(x = ep_year.index, y = ep_year)

    # Add the value of the percentage over the bars
    for i in range(len(ep_year)):
        plt.text(i, ep_year[i], round(ep_year[i]*100, 2), ha = 'center', va = 'bottom')

    plt.title('Distribución de la población por pobreza en el año ' + str(year) + ' en pobreza')
    plt.xticks(rotation=90)
    plt.xlabel('Departamento')
    plt.ylabel('Porcentaje de la población')
    # Vary the color in the bars
    plt.bar(ep_year.index, ep_year, color = sns.color_palette('viridis', len(ep_year)))

# Función para graficar histograma
def plot_histogram(df, title='Histograma'):
    fig = px.histogram(df, x='Value', nbins=30, title=title)
    fig.update_layout(xaxis_title='Valor', yaxis_title='Frecuencia')
    fig.show()

# Función para graficar mapa
def plot_map(df, year, title='Mapa'):
    # Filtrar por el año especificado
    df_year = df[df['Year'] == year].copy()
    
    # Asegurarnos de que 'Value' es numérico
    df_year['Value'] = pd.to_numeric(df_year['Value'], errors='coerce')
    
    # Eliminar filas con 'Value' nulo
    df_year = df_year.dropna(subset=['Value'])
    
    # Verificar si hay datos de ciudad
    if 'CITY' in df_year.columns:
        # Agrupar por país y calcular la media de 'Value'
        df_grouped = df_year.groupby('COUNTRY')['Value'].mean().reset_index()
    else:
        df_grouped = df_year.groupby('COUNTRY')['Value'].mean().reset_index()
    
    fig = px.choropleth(
        df_grouped,
        locations='COUNTRY',
        locationmode='country names',
        color='Value',
        hover_name='COUNTRY',
        color_continuous_scale=px.colors.sequential.Plasma,
        title=title
    )
    fig.update_geos(showframe=False, projection_type='equirectangular')
    fig.update_layout(legend_title_text='Valor')
    fig.show()

# Función para graficar gráfico de barras de ciudad o pais
def plot_city_or_country_data(df, indicator, year, level='city', countries=None):
    """
    Grafica los datos por ciudades o países, ordenados de mayor a menor valor en el eje horizontal.
    
    Parámetros:
    - df: DataFrame con los datos.
    - indicator: Indicador a analizar (por ejemplo, 'Urban PM2.5 Exposure').
    - year: Año a analizar.
    - level: 'city' para graficar por ciudades, 'country' para graficar por países.
    - countries: Lista de países a incluir (opcional). Si es None, se incluyen todos.
    """
    # Validar el parámetro 'level'
    if level not in ['city', 'country']:
        print("El parámetro 'level' debe ser 'city' o 'country'.")
        return
    
    # Normalizar los nombres de los países si se proporcionan
    if countries is not None:
        countries_normalized = [normalize_name(country) for country in countries]
    else:
        countries_normalized = None
    
    # Filtrar los datos según el indicador y el año
    df_filtered = df[
        (df['Indicator'] == indicator) &
        (df['Year'] == year)
    ].copy()
    
    # Filtrar por países si se proporcionan
    if countries_normalized is not None:
        df_filtered = df_filtered[df_filtered['COUNTRY'].isin(countries_normalized)]
    
    # Verificar si se va a graficar por ciudades y si la columna 'CITY' existe
    if level == 'city':
        if 'CITY' not in df_filtered.columns:
            print(f"No hay datos de ciudad para el indicador '{indicator}'.")
            return
        group_field = 'CITY'
    else:
        group_field = 'COUNTRY'
    
    # Asegurarnos de que 'Value' es numérico
    df_filtered['Value'] = pd.to_numeric(df_filtered['Value'], errors='coerce')
    df_filtered = df_filtered.dropna(subset=['Value'])
    
    # Agrupar los datos y calcular la media si es necesario
    df_grouped = df_filtered.groupby(group_field)['Value'].mean().reset_index()
    
    # Ordenar los datos de mayor a menor valor
    df_grouped = df_grouped.sort_values('Value', ascending=False)
    
    # Verificar si hay datos después del filtrado
    if df_grouped.empty:
        print("No hay datos disponibles para los filtros especificados.")
        return
    
    # Crear el gráfico
    fig = px.bar(
        df_grouped,
        x=group_field,
        y='Value',
        title=f"{indicator} en {year} por {'Ciudad' if level == 'city' else 'País'}",
        labels={'Value': 'Valor', group_field: 'Ciudad' if level == 'city' else 'País'}
    )
    fig.update_layout(
        xaxis_title='Ciudad' if level == 'city' else 'País',
        yaxis_title='Valor',
        xaxis_tickangle=-45
    )
    # Actualizar el orden de las categorías en el eje x para reflejar el orden deseado
    fig.update_xaxes(categoryorder='total descending')
    fig.show()
