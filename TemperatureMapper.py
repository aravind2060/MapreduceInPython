import os
import sys

# Assuming the target date is passed as an environment variable
target_date = os.getenv('TARGET_DATE', '20230523')

for line in sys.stdin:
    line = line.strip()
    # Assuming the line format is: date,station_id,element_type,value
    parts = line.split(',')
    if len(parts) == 4:
        date, station_id, element_type, value = parts
        # Filter records by the target date
        if date == target_date and element_type in ['TMAX', 'TMIN']:
            print(f"{station_id}\t{element_type},{value}")
