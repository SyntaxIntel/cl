import requests
import pandas as pd
from io import StringIO
import os
from typing import Dict, List, Tuple


class WeatherDataFetcher:
    """Class to fetch and process weather data"""

    def __init__(self, base_url: str = "https://data.giss.nasa.gov/gistemp/"):
        self.base_url = base_url
        self.data_file = "GLB.Ts+dSST.csv"

    def fetch_data(self) -> pd.DataFrame:
        """Fetch global temperature data from NASA GISTEMP"""
        try:
            url = f"{self.base_url}{self.data_file}"
            response = requests.get(url)
            response.raise_for_status()

            # Parse CSV data
            df = pd.read_csv(StringIO(response.text), skiprows=1)
            return self._process_data(df)
        except Exception as e:
            print(f"Error fetching data: {e}")
            # If fetching fails, use sample data
            return self._generate_sample_data()

    def _process_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Process the raw temperature data"""
        # Drop unnecessary columns and rename Year
        df = df.rename(columns={"Year": "year"})
        # Convert monthly columns to numeric, replacing missing values with NaN
        for col in df.columns[1:13]:  # Skip year column
            df[col] = pd.to_numeric(df[col], errors="coerce")
        return df

    def _generate_sample_data(self) -> pd.DataFrame:
        """Generate sample weather data for testing"""
        years = range(1980, 2024)
        data = {
            "year": years,
            "Jan": [round(float(20 + i / 10), 2) for i in range(len(years))],
            "Feb": [round(float(22 + i / 10), 2) for i in range(len(years))],
            "Mar": [round(float(25 + i / 10), 2) for i in range(len(years))],
            "Apr": [round(float(28 + i / 10), 2) for i in range(len(years))],
            "May": [round(float(30 + i / 10), 2) for i in range(len(years))],
            "Jun": [round(float(32 + i / 10), 2) for i in range(len(years))],
            "Jul": [round(float(33 + i / 10), 2) for i in range(len(years))],
            "Aug": [round(float(31 + i / 10), 2) for i in range(len(years))],
            "Sep": [round(float(29 + i / 10), 2) for i in range(len(years))],
            "Oct": [round(float(26 + i / 10), 2) for i in range(len(years))],
            "Nov": [round(float(23 + i / 10), 2) for i in range(len(years))],
            "Dec": [round(float(21 + i / 10), 2) for i in range(len(years))],
        }
        return pd.DataFrame(data)


def map_function(data: pd.DataFrame) -> List[Tuple[int, Dict[str, float]]]:
    """
    Map function for temperature analysis
    Returns: List of (year, temperature_data) tuples
    """
    result = []
    for _, row in data.iterrows():
        year = int(row["year"])
        monthly_temps = {
            month: temp
            for month, temp in row.items()
            if month != "year" and not pd.isna(temp)
        }
        if monthly_temps:  # Only include years with data
            result.append((year, monthly_temps))
    return result


def reduce_function(
    mapped_data: List[Tuple[int, Dict[str, float]]],
) -> Dict[str, Tuple[int, float]]:
    """
    Reduce function to find hottest and coolest years
    Returns: Dictionary with hottest and coolest year information
    """
    year_avg_temps = {}

    # Calculate average temperature for each year
    for year, monthly_temps in mapped_data:
        avg_temp = sum(monthly_temps.values()) / len(monthly_temps)
        year_avg_temps[year] = avg_temp

    # Find hottest and coolest years
    hottest_year = max(year_avg_temps.items(), key=lambda x: x[1])
    coolest_year = min(year_avg_temps.items(), key=lambda x: x[1])

    return {
        "hottest": hottest_year,
        "coolest": coolest_year,
        "all_temps": year_avg_temps,
    }
