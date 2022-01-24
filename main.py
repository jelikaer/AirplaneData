import requests
import copy
import sensor
import time
import tools
import constants
from geopy import distance
from geopy import Point
import math

# Airplane Voice Data class
class AirplaneVoiceData:
    def __init__(self, airplaneData, voiceFileName, fileCount = constants.FILECOUNT):
        self.airplaneData = copy.copy(airplaneData)
        self.voiceFileName = voiceFileName
        self.fileCount = fileCount
    
# Function to check plane distance from the sensor
#
# PLANE
#   |\
#   | \
#  b|  \ c
#   |   \
#   |____\ 
#      a   SENSOR
#
def checkDistance(plane_la, plane_lo, plane_h):
    coords_1 = (constants.SENSOR_LA, constants.SENSOR_LO)
    coords_2 = (plane_la, plane_lo)
    a = distance.distance(coords_1, coords_2).km
    b = plane_h  / 1000
    c = math.sqrt(a**2 + b**2)
    print("\nPlane detected! Distance from sensor: ", c, " km.")
    return c

# TODO: At the moment, program gets all planes in given radius and starts recording the first one.
#       Can we record multiple planes at the same time? If no, then why and which plane should be recorded?
#       If yes, then implement the solution.
# TODO: Is it possible to record plane data from the moment it enters the dome till it leaves?
#       If no, then why and which solution is the best? If yes, then implement it.
# TODO: Instead of creating data files and add all of them in project folder, each plane should
#       have its own folder with its own data.
while(True):
    # Request from opensky
    response = requests.get('https://opensky-network.org/api/states/all?lamin=' + str(constants.LAMIN) + '&lomin=' + str(constants.LOMIN) + '&lamax=' + str(constants.LAMAX) + '&lomax=' + str(constants.LOMAX))
    # Response
    allStateVectors = response.json()
    airplaneDataList = {}
    # If plane(s) detected
    if allStateVectors["states"]:
        # Loop through the result
        for state in allStateVectors["states"]:
            # Check each plane distance from the sensor
            checkDistanceResult = checkDistance(state[6], state[5], state[13])
            # If distance is <= given max distance, start recording 
            if (checkDistanceResult <= constants.DISTANCE):
                airplaneDataList.update({'icao24': state[0], 'callsign': state[1], 'from': state[2], 'longitude': state[5], 'latitude': state[6], 'barometric altitude': state[7],
                                         'velocity': state[9], 'vertical rate': state[11], 'geometric altitude': state[13], 'position source': state[16], 'Distance from Sensor': checkDistanceResult})
                airplaneVoiceData = AirplaneVoiceData(airplaneDataList, tools.generateVoiceFileName())
                tools.saveLogData(airplaneVoiceData)
                sensor.saveAirplaneAudioData(airplaneVoiceData.voiceFileName, airplaneVoiceData.fileCount)
                # For statement loops through the result. There might be more than 1 plane.
                # If plane is in given range, program starts recording it. By default, it would
                # continue looping, but given data might be outdated (30 secs per 1 file = 3 mins in total).
                #So, break is needed to prevent false and fake recordings.
                break;
            else:
                print("\nPlane is not in given range. Not recording...")
    else:
        print("\nNo plane in sphere, checking again in " + str(constants.DELAY) + " seconds!")
        time.sleep(constants.DELAY)
        


