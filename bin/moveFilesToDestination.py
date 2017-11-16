import os 
import fnmatch
import datetime

from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

SOURCE_PATH      = os.environ.get("SOURCE_PATH") if os.environ.get("SOURCE_PATH") else './source'
DESTINATION_PATH = os.environ.get("DESTINATION_PATH") if os.environ.get("DESTINATION_PATH") else './destination'
LOG_PATH         = os.environ.get("LOG_PATH") if os.environ.get("LOG_PATH") else './log'

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
  origin = SOURCE_PATH + '/' + file
  destination = DESTINATION_PATH + '/' + file
  ackFile = SOURCE_PATH + '/' + filebase + '.ACK'
  os.rename(origin, destination)
  ackFile = open(ackFile, 'w')
  ackFile.close()


logFile.write('process finished at ' + str(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")) + '\n')
logFile.close()