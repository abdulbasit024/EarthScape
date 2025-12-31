import sys

def reducer():
    current_date = None
    current_temp_sum = 0
    current_count = 0
    
    # Input comes from STDIN and assumed to be sorted by key (Date)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
            
        try:
            date, temp = line.split('\t')
            temp = float(temp)
        except ValueError:
            continue
            
        if current_date == date:
            current_temp_sum += temp
            current_count += 1
        else:
            if current_date:
                # Output result for previous date
                avg_temp = current_temp_sum / current_count
                print(f"{current_date},{avg_temp:.2f}")
                
            current_date = date
            current_temp_sum = temp
            current_count = 1
            
    # Output last date
    if current_date:
        avg_temp = current_temp_sum / current_count
        print(f"{current_date},{avg_temp:.2f}")

if __name__ == "__main__":
    reducer()
