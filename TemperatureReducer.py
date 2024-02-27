import sys

def calculate_averages(temp_values):
    avg_max = sum(temp_values['TMAX']) / len(temp_values['TMAX']) if temp_values['TMAX'] else None
    avg_min = sum(temp_values['TMIN']) / len(temp_values['TMIN']) if temp_values['TMIN'] else None
    return avg_max, avg_min

def main():
    temp_values = {'TMAX': [], 'TMIN': []}

    for line in sys.stdin:
        _, value = line.strip().split('\t')
        measure_type, temp_value = value.split(',')
        temp_values[measure_type].append(float(temp_value))

    avg_max, avg_min = calculate_averages(temp_values)
    if avg_max is not None and avg_min is not None:
        print(f'Average Maximum Temperature: {avg_max}')
        print(f'Average Minimum Temperature: {avg_min}')
    else:
        print("No data available for the specified date.")

if __name__ == "__main__":
    main()
