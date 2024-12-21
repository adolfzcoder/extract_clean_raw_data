import re

def clean_missed_data(inp='storage/output.txt', out='storage/output2.txt'):
    output = open(out, "a")
    with open(inp, 'r') as input_file:
        lines = input_file.readlines()
        for line in lines:
            if (len(line) < 40) or (bool(re.search(' """', line, 1))) or (bool(re.search('""', line, 1))) or ' """' in line  or ('"Science' in line):
                print("Line is too short, clearing it", line)
                output.write("\n")
            else:
                data = line.strip()
                # Use regex to split based on the pattern "23" followed by two letters and six digits
                parts = re.split(r'(?=23[A-Z]{2}\d{6})', data)

                if len(parts) > 1:
                    for part in parts:
                        output.write(f' "   {part.strip()}   "\n')
                        print("Part:", part.strip())
                else:
                    output.write(f'"{data}"\n')
                    print("Data is already sorted:", data)
                    
                

    print("Done! Cleaned data written to output file")
