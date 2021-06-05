# This program is to check the status of local services running on windows
# Here, we are checking for Tomcat Server

import wmi
 
# Initializing the wmi constructor and an empty list
f = wmi.WMI()
list_of_running_process = []
	

# Iterating through all the running processes
for process in f.Win32_Process():

        list_of_running_process.append(process.Name)

if 'tomcat8.exe' in list_of_running_process:
        print('Tomcat is running')
else:
        print('Tomcat is not running, please investigate!')
    
