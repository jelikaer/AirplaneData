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

# Function to write USB data to file
def writeUsbDataToFile(fileName):
    new_file = open(fileName, mode="w")
    i = 0
    while i < NUMBEROFLINES:
        # To test requesting without sensor, comment out next line
        data = ser.read(2)
        # And add something like this:
        # data = bytes("Data: ", 'utf-8')
        if data:
            new_file.write("%d\n" % int.from_bytes(data, "big")) #or "little depending on if we read from first of last bit"
        i = i + 1
    new_file.close()


# TODO: Test with microphone
# TODO: Find a better/alternative solution for saving 1...n files per 30sec.
# TODO: Maybe check inbetween if the plane is still in given radius?
def saveAirplaneAudioData(fileName, n):
    # This function will record 
    # n files with audio data per 30 sec
    # every file is saving by fileName + index (1...n)
    i = 1
    while i <= n:
        print("The " + str(i) + ". voice file recording has started.")
        writeUsbDataToFile(fileName + "_" +str(i) + ".txt")
        i = i + 1
   
# To test requesting without sensor, comment out next line 
ser = serial.Serial('/dev/tty' + constants.USB_PORT, 921600)




