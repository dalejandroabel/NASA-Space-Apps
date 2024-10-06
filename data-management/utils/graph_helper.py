import matplotlib.pyplot as plt
import seaborn as sns
import utils.df_helper as give_people

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