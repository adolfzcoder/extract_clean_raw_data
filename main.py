from clean_data import clean_data as cd
from clean_data import reset_txt as reset
from clean_data import process_file as process
from clean_data import clean_missed_data as cmd
 
  
    

# reset.reset_txts()        
# cd.clean_data() 
# cmd.clean_missed_data()
print("resetting the files")
reset.reset_txts()    
print("cleaning the data")
cd.clean_data()


print("Outputting the cleaned data to json")
process.process_file()
print("Done! All data cleaned and written to output file")




# if '__name__' == '__main__':
#     print("Running main...")
#     # got annoying deleting data every single time i have to run it...so i just made a package for that or module idk, java messin me up fr
    
#     reset.reset_txts()        
#     cd.clean_data() 
#     cmd.clean_missed_data()
     
#     process.process_file()
#     print("Done! All data cleaned and written to output file")
