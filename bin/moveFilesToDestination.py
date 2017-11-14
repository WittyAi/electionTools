import os 
import fnmatch
import datetime

SOURCE_PATH = './source'
DESTINATION_PATH = './destination'
LOG_PATH = './log'

timeNowIs = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
logFileName = LOG_PATH + '/' + str(timeNowIs) + '.log'
logFile = open(logFileName, 'a')
logFile.write('process started at ' + str(timeNowIs) + '\n')

dir = os.listdir(SOURCE_PATH)

txtFiles = fnmatch.filter(os.listdir(SOURCE_PATH), '*.txt')
txtzipFiles = fnmatch.filter(os.listdir(SOURCE_PATH), '*.txt.zip')
xmlzipFiles = fnmatch.filter(os.listdir(SOURCE_PATH), '*.xml.zip')

logFile.write('txt Files: ' + str(txtFiles) + '\n')
logFile.write('txt.zip Files: ' + str(txtzipFiles) + '\n')
logFile.write('xml.zip Files: ' + str(xmlzipFiles) + '\n')

totalFiles = txtFiles + txtzipFiles + xmlzipFiles

for file in totalFiles:
  filebase = file.split('.')[0]
#  print filebase
  origin = SOURCE_PATH + '/' + file
  destination = DESTINATION_PATH + '/' + file
  ackFile = SOURCE_PATH + '/' + filebase + '.ACK'
#   print 'origin: ' + origin
#   print 'destination: ' + destination
  os.rename(origin, destination)
  ackFile = open(ackFile, 'w')
  ackFile.close()


logFile.write('process finished at ' + str(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")) + '\n')
logFile.close()