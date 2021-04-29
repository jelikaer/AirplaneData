#################################################
#       Project name: Save Airplane Data        #
#           Author: Jelizaveta Kaerner          #
#         Curators: Jaanus Kaugerand            #
#                   Konstantin Bilozor          #
#                                               #
#                   April 2021                  #
#################################################

LAMIN = 59.40752            # Minumal latitude of checking area;  Example: 59.40752
LOMIN = 24.69251            # Minumal longitude of checking area; Example: 24.69251       
LAMAX = 59.435747           # Maximal latitude of checking area   Example: 59.40752
LOMAX = 24.74529            # Maximal longitude of checking area  Example: 24.69251
SENSOR_ID = 1               # put here your sensor ID in integers. It is used for file name generating
FILECOUNT = 6               # amount of recording files in integers. Every file contains 30 sec
DELAY = 10                  # time in sec between negative responses from Opensy in integers
USB_PORT = 'USB0'           # USB port used to connect the sensor; str type
