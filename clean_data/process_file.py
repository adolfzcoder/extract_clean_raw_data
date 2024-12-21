import re
import json
import csv

def clean_line(line):
    # Remove quotes and extra whitespace
    return line.strip().strip('"').strip()

def parse_line(line):
    # Clean the line first
    line = clean_line(line)
    if not line:
        return None

    # Split into parts and remove empty strings
    parts = [p for p in line.split() if p]
    if len(parts) < 4:  # Minimum required parts
        return None

    candidate_number = parts[0]
    
    
    
    results = []
    # only for nssco and ommits A*
    a_star_count = line.count(' A* ') or line.count(' A*"')
    a_count = line.count(' A ') or line.count(' A"')  
    b_count = line.count(' B ') or line.count(' B"') 
    c_count = line.count(' C ') or line.count(' C"') 
    d_count = line.count(' D ') or line.count(' D"') 
    e_count = line.count(' E ') or line.count(' E"') 
    f_count = line.count(' F ') or line.count(' F"') 
    g_count = line.count(' G ') or line.count(' G"') 
    u_count = line.count(' U ') or line.count(' U"') 
    x_count = line.count(' X ') or line.count(' X"')     
    
    
    a_count_as = line.count(' a ') or line.count(' a"')
    b_count_as = line.count(' b ') or line.count(' b"')
    c_count_as = line.count(' c ') or line.count(' c"')
    d_count_as = line.count(' d ') or line.count(' d"')
    e_count_as = line.count(' e ') or line.count(' e"')
    u_count_as = line.count(' u ') or line.count(' u"')
    x_count_as = line.count(' x ') or line.count(' x"')
    points = 0
    is_nsscas = False
    subject_count = 0
    if a_star_count > 0 or a_count > 0 or b_count > 0 or c_count > 0 or d_count > 0 or e_count > 0 or f_count > 0 or g_count > 0 or u_count > 0 or x_count > 0:

        points = a_star_count * 8+ a_count * 7 + b_count * 6 + c_count * 5 + d_count * 4 + e_count * 3 + f_count * 2 + g_count * 1 + u_count * 0 + x_count * 0
        is_nsscas = False
        subjects = f"{a_star_count}  {a_count}  {b_count}  {c_count}  {d_count}  {e_count}  {f_count}  {g_count}  {u_count}  {x_count}"
        #print(subjects)
        subject_c = subjects.split()
        subject_count = sum(int(count) for count in subject_c)
    elif a_count_as > 0 or b_count_as > 0 or c_count_as > 0 or d_count_as > 0 or e_count_as > 0 or u_count_as > 0 or x_count_as > 0:
        points = a_count_as * 9 + b_count_as * 8 + c_count_as * 7 + d_count_as * 6 + e_count_as * 5 + u_count_as * 0 + x_count_as * 0
        is_nsscas = True
        subjects = f"{a_count_as}  {b_count_as}  {c_count_as}  {d_count_as}  {e_count_as}  {u_count_as}  {x_count_as}"

        #print(subjects)
        subject_c = subjects.split()
        subject_count = sum(int(count) for count in subject_c)  # Count the number of subjects
    #print(f"\nCandidate number: {candidate_number}")
    #print(f"Points: {points}\n\n\n\n")
    results.append({
        "candidate_number": candidate_number,
        "points": f"{points}",
        "is_nssac": f"{is_nsscas}",
        "subject_count": f"{subject_count}"
    })

    return results

def process_file(inp='storage/output2.txt', json_out='storage/output.json', csv_out='storage/output.csv'):
    output_data = []
    candidate_counter = 0

    with open(inp, 'r') as input_file:
        lines = input_file.readlines()
        for line in lines:
            parsed_results = parse_line(line)
            if parsed_results:
                output_data.extend(parsed_results)
                candidate_counter += 1  # Increment the candidate counter
    
    # Write to JSON file
    with open(json_out, "w") as json_file:
        json.dump(output_data, json_file, indent=4)
    
    # Write to CSV file
    with open(csv_out, "w", newline='') as csv_file:
        fieldnames = ["candidate_number", "points", "is_nssac", "subject_count"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        for data in output_data:
            writer.writerow(data)
    
    print("Done! Processed data written to output files")
    print(f"Total number of candidates processed: {candidate_counter}")

# Example usage
process_file('storage/output2.txt', 'storage/output.json', 'storage/output.csv')