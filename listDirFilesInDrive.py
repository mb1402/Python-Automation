#This program takes input from the user for the drive/root name and lists all the directories and files within each dirs espectively under given drive/root
# If user input 'e'/'E', program will list all the dir names and the respective files present under 'e'/'E'

import os
#from retention import list_of_files


def dir_file_list(root_name):

    
    
    print('Fetching results for you under the drive {} '.format(root_name) + '.....')
    
    try:
        for root, dirs, files in os.walk(root_name):
            print(dirs)
            for d in dirs:									## Listing file names under each directories respectively 
                try:
                    x = input()
                    
                    file_names=os.listdir(d)					## and saving in the list 'file_names'
                    print(file_names)
                    print("\nFiles present under directory {}:".format(d))
                    abs_path = os.path.abspath(d)							## Saving absolute path of each directory in a variable

                    for i in range(0, len(file_names)):						## Looping through list file_names
                                   f_name=file_names[i]
                                   curr_path = os.path.join(abs_path, f_name)	## getting the absolute path of each file
                                   f_size = os.path.getsize(curr_path)			## etting size of each file
                                   print(f_name + ': ' + str(f_size) + ' bytes')

                except PermissionError:
                    print('You do not have access to this file: ')
                
                                   
                else:
                    print('recycle')
                    
                     
                         
#                                   list_of_files(curr_path)
    except PermissionError:
        print('You do not have access to this file: ')
    except FileNotFoundError:    
        x = input()



#Take drive/root as input from user
        
#print('In which drive you would want to search?\n')
#root_name = (str(input())).upper() + ':\\'
import time
print('In which drive you would want to search?\n')
drive = (str(input())).upper()

    
if drive == 'E':
    root_name = r"E:\\"
elif drive == 'C':
    root_name = r"C:\\"
elif drive == 'D':
    root_name = r"D:\\"
    
os.chdir(root_name)
        

# Calling the function while passing the drive name as argument
dir_file_list(root_name)

print('wait')
time.sleep(500)

