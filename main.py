#################################################
#       Project name: Save Airplane Data        #
#           Author: Jelizaveta Kaerner          #
#         Curators: Jaanus Kaugerand            #
#                   Konstantin Bilozor          #
#                                               #
#                   April 2021                  #
#################################################

import requests
import copy
import sensor
import time
import tools
import constants

class AirplaneVoiceData:
    def __init__(self, airplaneData, voiceFileName, fileCount = constants.FILECOUNT):
        self.airplaneData = copy.copy(airplaneData)
        self.voiceFileName = voiceFileName
        self.fileCount = fileCount

while(True):
    response = requests.get('https://opensky-network.org/api/states/all?lamin=' + str(constants.LAMIN) + '&lomin=' + str(constants.LOMIN) + '&lamax=' + str(constants.LAMAX) + '&lomax=' + str(constants.LOMAX))
    allStateVectors = response.json()
    airplaneDataList = []
    if allStateVectors["states"]:
        for state in allStateVectors["states"]:
            airplaneDataList.append("icao24 = %r, callsign = %r, from = %r, longitude = %r, latitude = %r," 
               " baro altitude = %r, plane velocity = %r m/s" % (state[0], state[1], state[2], state[5], state[6], state[7], state[9]))
        airplaneVoiceData = AirplaneVoiceData(airplaneDataList, tools.generateVoiceFileName())
        tools.saveLogData(airplaneVoiceData)
        sensor.saveAirplaneAudioData(airplaneVoiceData.voiceFileName, airplaneVoiceData.fileCount)
        airplaneDataList.clear()
    else:
        print("Ask again after " + str(constants.DELAY) + " sec\n")
        time.sleep(constants.DELAY)









