#################################################
#       Project name: Save Airplane Data        #
#           Author: Jelizaveta Kaerner          #
#         Curators: Jaanus Kaugerand            #
#                   Konstantin Bilozor          #
#                                               #
#                   April 2021                  #
#################################################
from geopy import Point                                                                                                                                                                       
from geopy.distance import geodesic

# Sensor ID in integers. It is used for file name generating
SENSOR_ID = 1
# Amount of recording files in integers. Every file contains 30 sec
FILECOUNT = 6
# Time in seconds between negative responses from Opensy in integers
DELAY = 10
# USB port used to connect the sensor; str type
USB_PORT = 'USB0'

# Latitude of sensor (Example: Tartu)
SENSOR_LA = 58.378025       
# Longitude of sensor (Example: Tartu)
SENSOR_LO = 26.728493
# Checking area radius in km
DISTANCE = 100       

# Calculations for GEO location points
# North, south, east and west location points, DISTANCE KM from SENSOR location points
north = geodesic(kilometers=DISTANCE).destination(Point(SENSOR_LA, SENSOR_LO), 0).format_decimal().replace(',', "").split()
south = geodesic(kilometers=DISTANCE).destination(Point(SENSOR_LA, SENSOR_LO), 180).format_decimal().replace(',', "").split()
east = geodesic(kilometers=DISTANCE).destination(Point(SENSOR_LA, SENSOR_LO), 90).format_decimal().replace(',', "").split()
west = geodesic(kilometers=DISTANCE).destination(Point(SENSOR_LA, SENSOR_LO), 270).format_decimal().replace(',', "").split()

# Latitude and longitude maximums and minimums of checking area
LAMIN = float(south[0])
LAMAX = float(north[0])
LOMIN = float(west[1])
LOMAX = float(east[1])

# TODO: Find a better and cleaner solution for storing LAMIN, LAMAX, LOMIN, LOMAX.