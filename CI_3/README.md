# Distributed MapReduce Weather Analysis

This project demonstrates a simple, explainable MapReduce application in Python to find the coolest and hottest year from weather data. It is designed for practical exams and easy explanation to instructors.

## Files
- `weather_data.csv`: Sample weather data (year, temperature).
- `mapper.py`: Emits (year, temperature) pairs from the data.
- `reducer.py`: Calculates average temperature per year and finds the coolest/hottest year.
- `main.py`: Simulates the MapReduce process locally by chaining the mapper and reducer.

## How it works
1. **Mapper**: Reads each line, outputs `year\ttemperature`.
2. **Sort**: Groups all records by year (simulating Hadoop's shuffle/sort phase).
3. **Reducer**: For each year, computes the average temperature, then prints the coolest and hottest year.

## To Run
Make sure you have Python 3 installed. In a terminal, run:

```bash
python3 main.py
```

## Output Example
```
Coolest year: 2020 with avg temp 29.20
Hottest year: 2021 with avg temp 35.10
```

## How to Explain
- This is a classic MapReduce pattern: map, shuffle/sort, reduce.
- The code is split into small, clear scripts for each phase.
- The main script simulates distributed processing locally for easy demonstration.
- You can easily swap in a larger dataset or run the scripts on Hadoop/other platforms with minor changes.
