import os
import sys

# Assuming the target date is passed as an environment variable
target_date = os.getenv('TARGET_DATE', '20240101')

for line in sys.stdin:
    line = line.strip()
    # Split the line into components based on commas
    parts = line.split(',')
    if len(parts) > 3:
        station_id, date, element_type, value = parts[0], parts[1], parts[2], parts[3]
        # Filter records by the target date and type of observation
        if date == target_date and element_type in ['TMAX', 'TMIN']:
            print(f"{station_id}\t{element_type},{value}")
