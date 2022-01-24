#################################################
#       Project name: Save Airplane Data        #
#           Author: Jelizaveta Kaerner          #
#         Curators: Jaanus Kaugerand            #
#                   Konstantin Bilozor          #
#                                               #
#                   April 2021                  #
#################################################

import datetime
import constants

METERTODEGREE = 1.11

# Function to generate voice filename
def generateVoiceFileName():
    output_date = "sen" + str(constants.SENSOR_ID) + "_" + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return (output_date)

# Function to save log data
def saveLogData(airplaneVoiceData):
    # Save airplane voice data to the log file
    # Open the file
    log_file = open("log_file", mode="a")
    # Start writing data
    log_file.write("\nVoice file name is: ")
    log_file.write(str(airplaneVoiceData.voiceFileName))
    log_file.write("\nNumber of recorded files is: ")
    log_file.write(str(airplaneVoiceData.fileCount))
    log_file.write("\nAirplane data is: \n")
    log_file.write(str(airplaneVoiceData.airplaneData))
    log_file.write("\n")
    # Close the file
    log_file.close()
    print("Log data is written to the log_file")
