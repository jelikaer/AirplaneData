#################################################
#       Project name: Save Airplane Data        #
#           Author: Jelizaveta Kaerner          #
#         Curators: Jaanus Kaugerand            #
#                   Konstantin Bilozor          #
#                                               #
#                   April 2021                  #
#################################################

This is README file on project created to collect airplane noise.
Prgram is written with Python 3.9.3
Main actions: The program makes a request for a real-time aircraft tracking service and asks if there is an aircraft in a specific area. 
In this updated version, user must know the exact location of sensor. Program will automatically calculate needed LA/LO MIN/MAX
for Opensky requests. Further more, user can now choose range between the sensor and plane. When plane enters the "dome", its noise 
is being recorded. To get some better understanding of the "dome", go to Google.com and search "Simpsons Dome".
At the moment, these characteristics are driven in manually in a special file with constants. If the plane is not fixed, the program waits 
for 10 seconds and then makes another request. Information about negative responses is not recorded in the activity log.

As soon as an answer is received about a fixed aircraft in a given area, the program starts recording sound files. Sound files are saved 
for 30 seconds in txt format. The number of files by default is specified as 6 pieces (3 minutes in total) and can be changed in the 
constant.py file. The name of sound files consists of three parts: sensor ID, start time of recording files in the yyyy-mmm-dd hh:mm:ss format,
 file ID from 1 to 6 (by default). The program also makes a record of the saved information in logData.txt each time the sound recording starts. 
One record consists of information:
- file name from sensor ID and recording start time, excluding identifiers;
- the number of files per sound recording;
- data on the aircraft or aircraft that flew over the sensor at that moment.
At the moment, sound files, a file with a log date and program files are recorded in one folder.
At the moment, the program is running in one thread. This means that while the sound is being recorded, the program does not ask for new aircraft 
until all the files have been recorded.

Set Parameters: the constant.py file stores data that can be configured, such as:
- sensor ID
- FILECOUNT = number of files to write (each file is 30 seconds long). By default is set as 6 files. If you want decrease or increase recording 
time - change this parameter;
- DELAY = time in seconds that the program waits (in the case when there are no planes in the sensor coverage area) before asking again
- USB_PORT = address of USB port is used to connect the voice sensor
- SENSOR_LA = sensor latitude
- SENSOR_LO = sensor longitude
- DISTANCE = radius between sensor and plane (or radius of the dome).

Libraries to installation:
- requests (https://docs.python-requests.org/en/master/) Program was written with Release v2.25.1.
- serial (https://pyserial.readthedocs.io/en/latest/pyserial.html)  Program was written with Release 2.7
- Geopy (https://pypi.org/project/geopy/) Program was written with Release 2.2.0

To run the program:
1. Install all required libraries;
2. Define number of USB port where voice sensor is connected
3. Open constant.py file and set all the parameters
4. Check if all program files (constants.py, sensor.py, tools.py, main.py) are in one folder 
5. Run main.py file from command line

To test without microphone, follow guidelines in sensor.py file.

Project includes some TODOs, which are added in the comments in each file. 