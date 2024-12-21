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
    git clone https://github.com/yourusername/TablesToData.git
    cd TablesToData
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

To clean and process the data, simply run:
```sh
python main.py