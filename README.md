# NASA Space Apps Project

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Descripción

Este repositorio contiene un proyecto orientado al procesamiento y visualización de datos climáticos, geográficos y de salud relacionados con el ambiente y la calidad del aire. El objetivo principal es generar histogramas y mapas interactivos que permitan a los usuarios familiarizarse con la naturaleza de los datos y comprender cómo se relacionan entre sí, especialmente en el contexto de aspectos socioeconómicos.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Instalación](#instalación)
- [Uso](#uso)
  - [Procesamiento de Datos](#procesamiento-de-datos)
  - [Generación de Gráficos](#generación-de-gráficos)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Instalación

### Requisitos Previos

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/downloads)

### Pasos de Instalación

1. **Clonar el Repositorio**

    ```bash
    git clone https://github.com/tu_usuario/NASA-SPACE-APPS.git
    cd NASA-SPACE-APPS
    ```

2. **Crear un Entorno Virtual (Opcional pero Recomendado)**

    ```bash
    python3 -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate
    ```

3. **Instalar las Dependencias**

    ```bash
    pip install -r requirements.txt
    ```

## Uso

### Procesamiento de Datos

Para procesar los datos y generar los archivos necesarios, ejecuta el siguiente comando:

```bash
python main.py
```

Este script realizará las siguientes tareas:

- Limpieza y preparación de los datos.
- Agregación de información relevante.
- Almacenamiento de los datos procesados en la carpeta `datasets/`.

### Generación de Gráficos

Los gráficos se generan utilizando Plotly a través de los scripts en `data-management/utils/`. A continuación, se presentan algunos ejemplos de cómo crear histogramas y mapas interactivos.

#### Ejemplo: Generar un Histograma de Ingresos

```python
from data_management.utils.graph_helper import plot_histogram
import pandas as pd

# Cargar los datos
df = pd.read_csv('datasets/data_filtered_plot.csv')

# Generar el histograma
plot_histogram(df, column='ingreso', title='Histograma de Ingresos')
```

#### Ejemplo: Generar un Mapa de Calidad del Aire

```python
from data_management.utils.graph_helper import plot_map
import pandas as pd

# Cargar los datos geoespaciales y de calidad del aire
df = pd.read_json('datasets/data_with_location.json')
geojson = 'img/colgeo.geojson'

# Generar el mapa
plot_map(df, geojson, location_column='location', value_column='PM2.5', title='Mapa de Calidad del Aire PM2.5')
```

## Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje de programación principal.
- **Pandas**: Manipulación y análisis de datos.
- **Plotly**: Visualización interactiva de datos.
- **Jupyter Notebook**: Análisis exploratorio y documentación interactiva.
- **Docker**: Contenerización de la aplicación (si aplica).
- **GeoJSON**: Manejo de datos geoespaciales.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. **Fork** el repositorio.
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y asegúrate de que el código siga las guías de estilo.
4. Haz **commit** de tus cambios (`git commit -m 'Añadir nueva característica'`).
5. **Push** a la rama (`git push origin feature/nueva-caracteristica`).
6. Abre un **Pull Request**.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme:

- **Correo Electrónico**: tomassosa.23@gmail.com


¡Gracias por revisar este proyecto! Esperamos que las visualizaciones generadas te ayuden a comprender mejor la relación entre los factores climáticos, geográficos, de salud y socioeconómicos.