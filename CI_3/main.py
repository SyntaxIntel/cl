import subprocess


def run_mapreduce():
    """
    Runs the mapper, sorts the output, and then runs the reducer.
    Prints the final output from the reducer.
    """
    # Open the weather data file and run the mapper
    with open("weather_data.csv", "r") as infile:
        mapper = subprocess.Popen(
            ["python3", "mapper.py"], stdin=infile, stdout=subprocess.PIPE
        )
        # Sort the mapper output (simulating Hadoop's shuffle/sort phase)
        sorter = subprocess.Popen(["sort"], stdin=mapper.stdout, stdout=subprocess.PIPE)
        # Run the reducer
        reducer = subprocess.Popen(
            ["python3", "reducer.py"], stdin=sorter.stdout, stdout=subprocess.PIPE
        )
        output, _ = reducer.communicate()
        print(output.decode())


if __name__ == "__main__":
    run_mapreduce()
