
# Overview
This directory contains my solution to the DataCamp project *Exploring Airbnb Market Trends*.
# Project statement
As a consultant working for a real estate start-up, you have collected Airbnb listing data from various sources to investigate the short-term rental market in New York. You'll analyze this data to provide insights on private rooms to the real estate company.

There are three files in the `data` folder: `airbnb_price.csv`, `airbnb_room_type.xlsx`, and `airbnb_last_review.tsv`.

- What are the dates of the earliest and most recent reviews? Store these values as two separate variables with your preferred names.
- How many of the listings are private rooms? Save this into any variable.
- What is the average listing price? Round to the nearest two decimal places and save into a variable.
- Combine the new variables into one DataFrame called `review_dates` with four columns in the following order: `first_reviewed`, `last_reviewed`, `nb_private_rooms`, and `avg_price`. The DataFrame should only contain one row of values.
# Included files
## Data
`data/airbnb_price.csv`:
This is a CSV file containing data on Airbnb listing prices and locations.
- **`listing_id`**: unique identifier of listing
- **`price`**: nightly listing price in USD
- **`nbhood_full`**: name of borough and neighborhood where listing is located

`data/airbnb_room_type.xlsx`:
This is an Excel file containing data on Airbnb listing descriptions and room types.
- **`listing_id`**: unique identifier of listing
- **`description`**: listing description
- **`room_type`**: Airbnb has three types of rooms: shared rooms, private rooms, and entire homes/apartments

`data/airbnb_last_review.tsv`:
This is a TSV file containing data on Airbnb host names and review dates.
- **`listing_id`**: unique identifier of listing
- **`host_name`**: name of listing host
- **`last_review`**: date when the listing was last reviewed
## Solution
`project-notebook.ipynb`:
This is the Jupyter notebook containing my solution to the project. This notebook uses the graphic `nyc.jpg`.

`project.py`:
This python script also contains my solution to the project.

`environment.yml`:
The file to create the conda environment in which I prepared my solution. Included packages are:
- pandas and NumPy for my analysis, along with openpyxl, which is necessary to read excel files into pandas;
- Matplotlib and Seaborn for visualization.

`info.md`:
The output of `project.py`, containing the results of the project as solved in the script.

## Other
`exploring-notebook.ipynb`:
This Jupyter notebook contains some other calculations that I did while exploring the provided data, which did not end up being directly relevant to the project solution.