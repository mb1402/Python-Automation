## Find files older than a specific duration(here 30 days)

import os
from datetime import datetime

def list_of_files(curr_path):
    try:
        for root, dirs, files in os.walk(curr_path):
            for f_name in files:
                var = os.stat(os.path.abspath(f_name))
                var1 = var.st_ctime
                creation_time = datetime.fromtimestamp(var1)
                diff_time = (datetime.now().date() - creation_time.date()).days

                if diff_time > 30:
                    print('{} is {} days older'.format(f_name, diff_time))
#                   os.remove(f_name)
#                   print('{} has been deleted'.format(f_name))
        
    except FileNotFoundError:
        print('{} file was not found: '.format(f_name))

list_of_files('E:\\python\\my_github\\scripting\\')
