
from clean_data import clean_missed_data as cmd

def clean_data(inp = "storage/results.txt", out="storage/output.txt"):
    print("Cleaning data")
    output = open(out, "a")

    count = 0
    with open(inp, "r") as input:


        rows = []
        space_to_split ="                         "
        
        for line in input:
            line = input.readline()
            
            row = line.split(space_to_split)
            #print(f"Row: {len(row)}")
            
            if(len(row) > 1):
                first, second = row[0], row[1]
                print(f'{row[0]}')
                print(f'{row[1]} \n')
                
                rows.append(first)
                rows.append(second)
                first_stripped, second_stripped = first.lstrip(), second.lstrip()
                output.write(f'   {first_stripped}   "\n')
                output.write(f'   {second_stripped}   "\n')
                count += 2
            elif(len(row) == 1):
                first = row[0]
                print(f'{row[0]} "')
                rows.append(first)
                first_stripped = first.lstrip()
                output.write(f'"   {first_stripped}   "\n')
                count += 1
            else:
                
                print("Row is invalid length")
                #print(f"First: {first} Second: {second}")
            # first, second = row[0], row[1]
        print(f"Rows: {count}")
        print("Done! Cleaned data writted to output file")
        print("Cleaning Data once more, for the stubbon data left in one row")
        
        cmd.clean_missed_data()
        
    