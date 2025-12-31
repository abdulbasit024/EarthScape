import os
import subprocess
import sys

# Define Paths
BASE_DIR = os.getcwd()
INPUT_DIR = os.path.join(BASE_DIR, 'hdfs_mock', 'raw_data')
OUTPUT_DIR = os.path.join(BASE_DIR, 'hdfs_mock', 'processed_data')
MAPPER_SCRIPT = os.path.join(BASE_DIR, 'data_processing', 'mapreduce', 'mapper.py')
REDUCER_SCRIPT = os.path.join(BASE_DIR, 'data_processing', 'mapreduce', 'reducer.py')

os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_job():
    input_file = os.path.join(INPUT_DIR, 'weather_stations.csv')
    output_file = os.path.join(OUTPUT_DIR, 'daily_avg_temp.csv')
    
    if not os.path.exists(input_file):
        print("Input file not found.")
        return

    # Simulate: type input.csv | python mapper.py | sort | python reducer.py > output.csv
    # Note: 'sort' is OS dependent. In Windows 'sort' command exists.
    
    print("Running MapReduce Job...")
    
    with open(input_file, 'r') as infile:
        # Step 1: Map
        mapper_proc = subprocess.Popen(
            [sys.executable, MAPPER_SCRIPT],
            stdin=infile,
            stdout=subprocess.PIPE,
            text=True
        )
        
        # Step 2: Sort (Using Python internal sort for cross-platform reliability)
        mapped_output, _ = mapper_proc.communicate()
        sorted_output = "".join(sorted(mapped_output.splitlines(keepends=True)))
        
        # Step 3: Reduce
        reducer_proc = subprocess.Popen(
            [sys.executable, REDUCER_SCRIPT],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True
        )
        
        final_output, _ = reducer_proc.communicate(input=sorted_output)
        
    # Write Output
    with open(output_file, 'w') as outfile:
        outfile.write("Date,AverageTemperature\n") # Add Header
        outfile.write(final_output)
        
    print(f"Job Complete. Output written to {output_file}")

if __name__ == "__main__":
    run_job()
