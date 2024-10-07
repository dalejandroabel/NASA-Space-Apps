# NASA Space Apps Project

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Description

This repository contains a project focused on the processing and visualization of climate, geographic, and health data related to the environment and air quality. The main goal is to generate histograms and interactive maps that allow users to familiarize themselves with the nature of the data and understand how they relate to each other, especially in the context of socioeconomic aspects.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
  - [Data Processing](#data-processing)
  - [Graph Generation](#graph-generation)
- [Technologies Used](#technologies-used)
- [Contributions](#contributions)
- [License](#license)
- [Contact](#contact)

## Installation

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/downloads)

### Installation Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your_user/NASA-SPACE-APPS.git
    cd NASA-SPACE-APPS
    ```

2. **Create a Virtual Environment (Optional but Recommended)**

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Data Processing

To process the data and generate the necessary files, run the following command:

```bash
python main.py
```

This script will perform the following tasks:

Data cleaning and preparation.

Aggregation of relevant information.

Storage of processed data in the datasets/ folder.


Graph Generation

The graphs are generated using Plotly through the scripts in data-management/utils/. Below are some examples of how to create histograms and interactive maps.

Example: Generate an Income Histogram
```
from data_management.utils.graph_helper import plot_histogram
import pandas as pd

# Load the data
df = pd.read_csv('datasets/data_filtered_plot.csv')

# Generate the histogram
plot_histogram(df, column='income', title='Income Histogram')
```

Example: Generate an Air Quality Map
```
from data_management.utils.graph_helper import plot_map
import pandas as pd

# Load geospatial and air quality data
df = pd.read_json('datasets/data_with_location.json')
geojson = 'img/colgeo.geojson'

# Generate the map
plot_map(df, geojson, location_column='location', value_column='PM2.5', title='PM2.5 Air Quality Map')
```

Technologies Used

Python 3.8+: Main programming language.

Pandas: Data manipulation and analysis.

Plotly: Interactive data visualization.

Jupyter Notebook: Exploratory analysis and interactive documentation.

Docker: Application containerization (if applicable).

GeoJSON: Handling geospatial data.


Contributions

Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. Fork the repository.


2. Create a branch for your feature (git checkout -b feature/new-feature).


3. Make your changes and ensure the code follows style guidelines.


4. Commit your changes (git commit -m 'Add new feature').


5. Push to the branch (git push origin feature/new-feature).


6. Open a Pull Request.



License

This project is licensed under the MIT License. See the LICENSE file for more details.

Contact

If you have any questions or suggestions, feel free to contact me:

Email: tomassosa.23@gmail.com


Thank you for checking out this project! We hope the generated visualizations help you better understand the relationship between climate, geographic, health, and socioeconomic factors.


