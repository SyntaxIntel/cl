from multiprocessing import Pool, cpu_count
import matplotlib.pyplot as plt
from weather_data import WeatherDataFetcher, map_function, reduce_function
import pandas as pd
from typing import List, Tuple, Dict
import numpy as np


class TemperatureAnalyzer:
    """MapReduce-based temperature analysis system"""

    def __init__(self, n_processes: int = None):
        self.n_processes = n_processes or cpu_count()
        self.data_fetcher = WeatherDataFetcher()

    def analyze(self) -> Dict:
        """
        Perform MapReduce analysis on temperature data
        Returns: Dictionary containing analysis results
        """
        # Fetch data
        print("Fetching weather data...")
        df = self.data_fetcher.fetch_data()

        # Split data for parallel processing
        chunks = np.array_split(df, self.n_processes)

        # Parallel mapping phase
        print(f"Running MapReduce analysis using {self.n_processes} processes...")
        with Pool(self.n_processes) as pool:
            mapped_data = pool.map(map_function, chunks)

        # Flatten mapped data
        flattened_data = [item for sublist in mapped_data for item in sublist]

        # Reduce phase
        results = reduce_function(flattened_data)

        # Generate visualization
        self._plot_results(results["all_temps"])

        return results

    def _plot_results(self, year_temps: Dict[int, float]):
        """Generate visualization of temperature trends"""
        years = list(year_temps.keys())
        temps = list(year_temps.values())

        plt.figure(figsize=(12, 6))
        plt.plot(years, temps, marker="o")
        plt.title("Global Temperature Trends")
        plt.xlabel("Year")
        plt.ylabel("Average Temperature (°C)")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("temperature_trends.png")
        plt.close()


def main():
    # Initialize analyzer
    analyzer = TemperatureAnalyzer()

    # Run analysis
    print("Starting temperature analysis...")
    results = analyzer.analyze()

    # Print results
    hottest_year, hottest_temp = results["hottest"]
    coolest_year, coolest_temp = results["coolest"]

    print("\nAnalysis Results:")
    print(
        f"Hottest Year: {hottest_year} with average temperature of {hottest_temp:.2f}°C"
    )
    print(
        f"Coolest Year: {coolest_year} with average temperature of {coolest_temp:.2f}°C"
    )
    print(
        "\nTemperature trend visualization has been saved as 'temperature_trends.png'"
    )


if __name__ == "__main__":
    main()
