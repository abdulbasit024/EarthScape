import sys
import csv

def mapper():
    # Input comes from STDIN (standard input)
    reader = csv.reader(sys.stdin)
    
    for row in reader:
        # Skip header or empty lines
        if not row or row[0] == 'StationID':
            continue
            
        try:
            # Expected format: StationID, Date, Temperature, Humidity, Precipitation
            if len(row) < 3:
                continue

            date = row[1]
            temperature = float(row[2])
            
            # Emit key-value pair: Date \t Temperature
            print(f"{date}\t{temperature}")
            
        except ValueError:
            # Skip invalid data
            continue

if __name__ == "__main__":
    mapper()
