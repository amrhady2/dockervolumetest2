##This program to read data from PLC mirco 800- AB, creare log, update data in the cloud, send SMS and Emails in case of alarms

#import timeit
#from datetime import datetime
#from tags import *
#import matplotlib.pyplot as plt
#from lgx_gui_test import *
#from flask import Flask, render_template, request
# import os.path
# import quandl
# import csv
#from generic_messaging import *

from basic_reads import *
from basic_writes import *
from send_sms import *
from send_email import *
import time
import pandas as pd
import gspread
import os

# Print current workinbg directory
print("Current working directory: {0}".format(os.getcwd()))




#_____open API for google sheet to update the data log
try:

    gc = gspread.service_account(filename='fast-feed-alerts.json')
    sh=gc.open('fast-feed-alert')
    shProfile = sh.get_worksheet(1)
    shData_log = sh.get_worksheet(0)
    shData_log.append_row(['JETSON', 'NANO',  'CONNECTED TO', 'FASTFEED', ' Micro 800 - AB'])
    print('succesfully established connection with JETNANO an google spread sheet')
except Exception as e:
    print('Failed to open connection with gspread API, Error: ' + str(e))


#___________________Send SMS____________
#___________________Send Email____________
#___________________Send Data to google Sheet
#___________________Send Null Data to Google Sheet in case of lost connection_____________

df = pd.DataFrame()
start = time.time()

send_message = False
low_to_high =  True
high_to_low =  False
print_log = True
update_cloud = False
update_dataframe =True

print('_______________________Program_Start_______________________')

try:
    shData_log.append_row(['Time' ,'_IO_EM_DI_00: Button', '_IO_EM_DI_01: Capactive', '_IO_EM_DI_02: Inductive', '_IO_EM_DI_03', '_IO_EM_AI_00: Pressure', '_IO_EM_AI_01: Key', 'TEMP_Scaled_Value', '_IO_P1_AI_02','_IO_P1_AI_03','_IO_P3_AO_00','_IO_P3_AO_01' ,'_IO_EM_DO_08 Lamp' ])
    print('_____________open connection with google sheet API and updated row index_____________')
except Exception as e:
    print('Failed to open connection to gspread API, Error: ' + str(e))


#while i<2:                   # Activated if we want to run the program forever
x = 60*60*1                   # Activated if we want to run the program for specific duration (seconds * minutes *hours)
for i in range(2):                              # we can just specifiy how many datalog we want
    #time.sleep(.7)
    seconds = time.time()
    local_time = time.ctime(seconds)
    
    #__________print datalog locally___________
    try:
        if print_log:
            print(local_time,read_single0().value, read_single1().value, read_single2().value, read_single3().value,
                read_singleAI0().value, read_singleAI1().value,  TEMP_Scaled_Value().value, read_singleAI2().value, read_singleAI3().value, 
                read_singleAO0().value, read_singleAO1().value,
                read_singleO8().value)
    except Exception as e:
        print(' cannot print Log, Error: ', str(e))
        
    
    #_________update the cloud_google spread sheet_______________
    try:
        if update_cloud:
            shData_log.append_row([local_time ,read_single0().value, read_single1().value, read_single2().value, 
                                read_single3().value, read_singleAI0().value, read_singleAI1().value, TEMP_Scaled_Value().value, read_singleAI2().value, read_singleAI3().value, read_singleAO0().value,
                                read_singleAO1().value,read_singleO8().value])        
            print('_______________________Cloud_succefully_updated_______________________')
    except Exception as e:
        print("Failed to send data to google sheet; Error: ", str(e) ) 

        try:
            shData_log.append_row([local_time ,'Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null'])
            print('Datalog updated with null for same timestamp')
        except Exception as e:
            print("Failed to update to the cloud with NULL, Error: ", str(e) ) 
        #time.sleep(5)
        
        
    #__________sending an alarm by email and/or message________________
    try:        
        if read_singleAI0().value > 50000 and send_message and low_to_high:
            message = 'You have exceeded the high-level limit. Take an immediate action please, current reading of the valve position is:    ' + str(read_singleAI0().value)
            print(message)
            send_sms(message)
            send_email(message)

            low_to_high =  False
            high_to_low = True
    except Exception as e:
        print('Alert SMS for high level limit cannot be sent, Error: ' , str(e))
            
    #__________sending a confirmation message that everyhing is okay by email and/or message________________   
    try:
        if read_singleAI0().value < 30000 and send_message and  high_to_low:
            message = 'You are all set, Current Reading for valve position:    ' + str(read_singleAI0().value)
            print(message)
            send_sms(message)
            send_email(message)

            low_to_high = True
            high_to_low = False  
    except Exception as e:
        print('Alert SMS for low level limit cannot be sent, Error: ', str(e))
        
    #___________________Save the log to DataFrame____________________________        
    try:
        if update_dataframe:
            df1 = pd.DataFrame(data=(read_single0().value, read_single1().value, read_single2().value, read_single3().value,
                                    read_singleAI0().value, read_singleAI1().value, TEMP_Scaled_Value().value,  read_singleAI2().value, read_singleAI3().value,read_singleAO0().value, 
                                    read_singleAO1().value,read_singleO8().value), columns= {local_time}, 
                            index = ['_IO_EM_DI_00: Button', '_IO_EM_DI_01: Capactive', '_IO_EM_DI_02: Inductive',
                                        '_IO_EM_DI_03', '_IO_EM_AI_00: Pressure', '_IO_EM_AI_01: Key', 'TEMP_Scaled_Value', '_IO_P1_AI_02','_IO_P1_AI_03', '_IO_P3_AO_00',
                                        '_IO_P3_AO_01' ,'_IO_EM_DO_08 Lamp' ]).T        
            df = pd.concat([df, df1])
            print('_______________DataFrame_updated_____________')
        
    except Exception as e:
        print('DataFrame_log cannot be updated, Error: ', str(e))
        print('_______update_DataFrame_with_NULL_Instead________')
        try:
            df1 = pd.DataFrame(data=('Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null','Null','Null', 'Null'),
                           columns= {local_time}, index = ['_IO_EM_DI_00: Button', '_IO_EM_DI_01: Capactive', 
                                                           '_IO_EM_DI_02: Inductive', '_IO_EM_DI_03', 
                                                           '_IO_EM_AI_00: Pressure', 'TEMP_Scaled_Value', '_IO_P1_AI_02','_IO_P1_AI_03','_IO_EM_AI_01: Key', 
                                                           '_IO_P3_AO_00','_IO_P3_AO_01' ,'_IO_EM_DO_08 Lamp' ]).T

            print('DataFrame_Successfully_updated_with_NULL')
            df = pd.concat([df, df1])
        
        except Exception as e:
            print("Failed to update dataframe with NULL", str(e))
                                                                  
       
    
end = time.time()
print('Program time taken:  ', end - start)
print(local_time)

##_______________Save_data_log_________________
try:
    filename = str(local_time.replace(":","-"))
    name_of_file = filename.replace(" ", "_")
    #__Save Log at windows__
    # PATH1 = r'C:\ML_Projects\ABB_Pycomm_ver_3\examples\Datasets\Datalog_' + name_of_file + '.csv' #(use "r" before the path string to address special character, such as '\'). Don't forget to put the file name at the end of the path + '.csv'
    # print('PATH1', PATH1)
    # df.to_csv(PATH1)
    df.to_csv(name_of_file)

    # #____Save Log at Linux environment__
    # PATH2 = r'/mnt/c/ML_Projects/AB_Pycomm_ver_4/examples_ver4.3/data_log/' + name_of_file + '.csv' #(use "r" before the path string to address special character, such as '\'). Don't forget to put the file name at the end of the path + '.csv'
    # print('PATH2', PATH2)
    # df.to_csv(PATH2)


    # #____save_inside_docker_volume__
    # #Change the current working directory to mount with it in Docker container
    # os.chdir('/app/in')
    # # Print current workinbg directory
    # print("Current working directory2: {0}".format(os.getcwd()))
    # PATH3 = r'' + name_of_file+ '.csv'
    # df.to_csv(PATH3)
    # print('Successfuly update log file into docker container')

except Exception as e:
    print("Fail to save log data into mentioned path, Error: ", str(e))



# #___________read muliple tags at once_________
# try:
#     print('read_multiple tags at once: \n' ,read_multiple(), '\n tags read successfully \n')
# except Exception as e:
#     print('Failed to read_multiple tags, ERROR: ', str(e))
    


# Write tags to the controller
print('___________Start writing_____________')
try:
    write_single_setA(-7)
except Exception as e:
    print("Failed to update Position_SetpointA ,ERROR: " , str(e))

try:
    write_single_setB(-9)
except Exception as e:
    print("Failed to update Position_SetpointA ,ERROR: " , str(e))






