import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import utils.df_helper as give_people
import plotly.express as px
import unidecode

# Function to get a graph of the stratum distribution

def plot_stratum_distribution(df, year, typeDistribution, give_people):

    df_year = give_people(df, año = year)

    if typeDistribution == 'Bajo':
        c_year = df_year[df_year['estrato'].isin([1,2])].groupby('depto').size() / df_year.groupby('depto').size()
    
    elif typeDistribution == 'Medio':
        c_year = df_year[df_year['estrato'].isin([3,4])].groupby('depto').size() / df_year.groupby('depto').size()

    elif typeDistribution == 'Alto':
        c_year = df_year[df_year['estrato'].isin([5,6])].groupby('depto').size() / df_year.groupby('depto').size()
    
    # Plot the graph with seaborn

    plt.figure(figsize=(15, 8))

    sns.barplot(x = c_year.index, y = c_year)
    plt.title('Distribución de la población por estrato en el año ' + str(year) + ' en ' + typeDistribution + ' estrato')
    plt.xticks(rotation=90)
    plt.xlabel('Departamento')
    plt.ylabel('Porcentaje de la población')
    plt.show()

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
