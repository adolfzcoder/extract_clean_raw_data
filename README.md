# TablesToData

TablesToData is a Python project designed to clean, process, and convert tabular data into JSON and CSV formats. This project includes several scripts to handle data cleaning, processing, and output generation.

## Features

- **Data Cleaning**: Cleans and processes raw data from text files.
- **Data Conversion**: Converts cleaned data into JSON and CSV formats.
- **Customizable**: Allows for easy modification and extension of data cleaning and processing rules.

## Project Structure

- `clean_data.py`: Contains functions to clean the raw data.
- `clean_missed_data.py`: Handles additional cleaning for stubborn data.
- `process_file.py`: Processes cleaned data and outputs it to JSON and CSV files.
- `plot.py`: Contains utility functions for data manipulation.
- `main.py`: Main script to run the entire data cleaning and processing pipeline.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages (can be installed via `requirements.txt` if provided)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/adolfzcoder/extract_clean_raw_data.git
    cd extract_clean_raw_data
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

1. Place your raw data files in the  directory.

2. Run the main script to clean and process the data:
    ```sh
    python main.py
    ```

3. The cleaned data will be output to  and .

### Example

Raw data:
"23OA020017       A02     Erenst Jager CS   1st Lang Khoek-      6098A     C   Eng 2nd Lang    6109A     D    Mathematics     6131A     U   Dev Studies    6136A     F    Geography     6137A     G   History           6138A     G                                 23OA060006   A06   Lordsville SS      Afrikaans 2nd Lang    6108A   A* Eng 2nd Lang    6109A   A*   Biology         6116A   A   Chemistry     6117A   B    Physics         6118A   B   Mathematics       6131A   C"

Semi cleaned data (output.txt):
   "23OA020017       A02     Erenst Jager CS   1st Lang Khoek-      6098A     C   Eng 2nd Lang    6109A     D    Mathematics     6131A     U   Dev Studies    6136A     F    Geography     6137A     G   History           6138A     G   "
   23OA060006   A06   Lordsville SS      Afrikaans 2nd Lang    6108A   A* Eng 2nd Lang    6109A   A*   Biology         6116A   A   Chemistry     6117A   B    Physics         6118A   B   Mathematics       6131A   C"

Full cleaned (otput.csv)
 "   23OA060006   A06   Lordsville SS      Afrikaans 2nd Lang    6108A   A* Eng 2nd Lang    6109A   A*   Biology         6116A   A   Chemistry     6117A   B    Physics         6118A   B   Mathematics       6131A   C"   "


How it looks in csv ( i selected specific columns to be here and applied it to it, but you can also change which columns you want)
ie i chose
index 0: candidate number
index 1: center number (candidate_number[3:6])
index 3: last 4 digits (candidate_number[-4:])
23OA060006,06,OA,0006,40,False,6




To clean and process the data, simply run:
```sh
python main.py
