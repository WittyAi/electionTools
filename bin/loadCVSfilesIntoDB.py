import os 
import fnmatch
import datetime
import codecs
import zipfile
import mysql.connector

from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

db = mysql.connector.connect(user     = os.environ.get('MYSQL_USER'),
                             password = os.environ.get('MYSQL_PASSWORD'),
                             host     = os.environ.get('MYSQL_HOST'),
                             database = os.environ.get('MYSQL_DATABASE'))

cursor = db.cursor()

DESTINATION_PATH = os.environ.get('DESTINATION_PATH') if os.environ.get('DESTINATION_PATH') else './destination'
PROCESSED_PATH   = os.environ.get('PROCESSED_PATH')   if os.environ.get('PROCESSED_PATH')   else './processed'

dir      = os.listdir(DESTINATION_PATH)
zipfiles = fnmatch.filter(os.listdir(DESTINATION_PATH), 'VOTACION_4*.txt.zip')

print datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

def unzipCVSFile (fullFile):
  zip_ref = zipfile.ZipFile(fullFile, 'r' )
  zip_ref.extractall(DESTINATION_PATH)
  zip_ref.close()
  return fullFile.split('.zip')[0]

def loadCVSFileIntoDB(db, unzippedFile, tableName, voteProgress):
  if tableName == 'votaciones_4':
    sql = """LOAD DATA LOCAL INFILE '{}'
             INTO TABLE votaciones_4
             FIELDS TERMINATED BY ';'
             OPTIONALLY ENCLOSED BY ''
             LINES TERMINATED BY '\\n';;"""
  
  if tableName == 'votaciones_5':
    sql = """LOAD DATA LOCAL INFILE '{}'
             INTO TABLE votaciones_5
             FIELDS TERMINATED BY ';'
             OPTIONALLY ENCLOSED BY ''
             LINES TERMINATED BY '\\n';;"""
             
  if tableName == 'votaciones_6':
    sql = """LOAD DATA LOCAL INFILE '{}'
             INTO TABLE votaciones_6
             FIELDS TERMINATED BY ';'
             OPTIONALLY ENCLOSED BY ''
             LINES TERMINATED BY '\\n';;"""

  if tableName == 'votaciones_7':
    sql = """LOAD DATA LOCAL INFILE '{}'
             INTO TABLE votaciones_7
             FIELDS TERMINATED BY ';'
             OPTIONALLY ENCLOSED BY ''
             LINES TERMINATED BY '\\n';;"""
    
  try:
    cursor.execute(sql.format(unzippedFile))
    db.commit()
    statement = 'UPDATE %s SET PORCENTAJE_TOTAL=\"%s\" where PORCENTAJE_TOTAL=\"\";' % (tableName, voteProgress)
    print statement
    cursor.execute(statement)
    db.commit()
      
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
    db.rollback()


for file in zipfiles:
  fullFile      = DESTINATION_PATH + '/' + file
  nameExpansion = file.split('.')[0].split('_')
  electionType  = nameExpansion[1]
  tableName     = 'votaciones_' + electionType
  voteProgress  = nameExpansion[2] 
  print tableName, electionType, voteProgress
    
  # unzip file
  unzippedFile = unzipCVSFile(fullFile)
  
  #load CVS file into DB
  loadCVSFileIntoDB(db, unzippedFile, tableName, voteProgress)
  
  #Move files
  print file, fullFile, unzippedFile
  os.rename(fullFile, PROCESSED_PATH + '/' + file)
  os.rename(unzippedFile, PROCESSED_PATH + '/' + file.split('.zip')[0])

try:
  now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  statement = 'INSERT INTO ultimocomputo (PROGRESO, ACTUALIZADO) VALUES (%s, \"%s\")' % (voteProgress, now)
  print statement
  cursor.execute(statement)
  db.commit()
except mysql.connector.Error as err:
  print("Something went wrong: {}".format(err))
  db.rollback()

cursor.close()
db.close()
print datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

