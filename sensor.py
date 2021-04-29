#################################################
#       Project name: Save Airplane Data        #
#           Author: Jelizaveta Kaerner          #
#         Curators: Jaanus Kaugerand            #
#                   Konstantin Bilozor          #
#                                               #
#                   April 2021                  #
#################################################


import serial
import constants
NUMBEROFLINES = 300000

def whriteUsbDataToFile(fileName):
    new_file = open(fileName, mode="w")
    i = 0
    while i < NUMBEROFLINES:
        data = ser.read(2)
        if data:
            new_file.write("%d\n" % int.from_bytes(data, "big")) #or "little depending on if we read from first of last bit"
        i = i + 1
    new_file.close()

def saveAirplaneAudioData(fileName, n):
    #This function will record 
    #n files with audio data per 30 sec
    #every file is saving by fileName + index (1...n)
    i = 1
    while i <= n:
        print("The " + str(i) + "st voice file recording has started")
        whriteUsbDataToFile(fileName + "_" +str(i) + ".txt")
        i = i + 1
   

ser = serial.Serial('/dev/tty' + constants.USB_PORT, 921600)




