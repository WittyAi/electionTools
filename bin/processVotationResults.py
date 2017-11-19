import os 
import fnmatch
import datetime
import codecs
import zipfile
import mysql.connector
import json

from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

db = mysql.connector.connect(user     = os.environ.get('MYSQL_USER'),
                             password = os.environ.get('MYSQL_PASSWORD'),
                             host     = os.environ.get('MYSQL_HOST'),
                             database = os.environ.get('MYSQL_DATABASE'))

def getLatestUpdate(db):
  try:
    statement = 'select * from ultimocomputo order by ACTUALIZADO DESC limit 1'
    cursor = db.cursor()
    cursor.execute(statement)
    return cursor.fetchall()
  
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

def getCandidatesForPresidentList(db):
  try:
    statement = 'select * from candidatos where COD_ELEC=4'
    cursor = db.cursor()
    cursor.execute(statement)
    return cursor.fetchall()
  
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

def getTotalVoteCountForCandidate(db, candidate_id, percentage_id):
  try:
    statement = 'select VOTOS from votaciones_4 where COD_ELEC=4 and AMBITO=4 and COD_AMBITO=%s and COD_ELEC=4 and PORCENTAJE_TOTAL=%s and COD_ZONA=19001' % (candidate_id, percentage_id)
    #statement = 'select sum(votos) as votosTotales from votaciones_4 where COD_AMBITO=%s and AMBITO=4 and PORCENTAJE_TOTAL=%s' % (candidate_id, percentage_id)
    cursor = db.cursor()
    cursor.execute(statement)
    return cursor.fetchall()
  
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

def getValidVotes(db, percentage_id):
  try:
    statement = 'select VOTOS as votosValidos from votaciones_4 where AMBITO=7 and COD_AMBITO=1 and PORCENTAJE_TOTAL=%s and COD_ZONA=19001' % (percentage_id)
    cursor = db.cursor()
    cursor.execute(statement)
    return cursor.fetchall()
  
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

def getNullVotes(db, percentage_id):
  try:
    statement = 'select VOTOS as votosValidos from votaciones_4 where AMBITO=5 and COD_AMBITO=1 and PORCENTAJE_TOTAL=%s and COD_ZONA=19001' % (percentage_id)
    cursor = db.cursor()
    cursor.execute(statement)
    return cursor.fetchall()
  
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
    
def getBlankVotes(db, percentage_id):
  try:
    statement = 'select VOTOS as votosValidos from votaciones_4 where AMBITO=6 and COD_AMBITO=1 and PORCENTAJE_TOTAL=%s and COD_ZONA=19001' % (percentage_id)
    cursor = db.cursor()
    cursor.execute(statement)
    return cursor.fetchall()
  
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

def insertParsedResult(db, parsedResult):
  try:
    statement = "INSERT INTO resultados(ACTUALIZADO, PARSEADO, COD_ELEC) VALUES (\'%s\', \'%s\', %d)" % (parsedResult['actualizado'], json.dumps(parsedResult), 4)
    print statement
    cursor = db.cursor()
    cursor.execute(statement)
    db.commit()
  
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
    db.rollback()


percentage_id = getLatestUpdate(db)[0][0]
candidates    = getCandidatesForPresidentList(db)
candidate_ids = map(lambda x: x[0], candidates)
candidate_results = {}

for ID in candidate_ids:
  result = getTotalVoteCountForCandidate(db, ID, percentage_id)
  candidate_results[str(ID)] = result[0][0]

validVotes = getValidVotes(db, percentage_id)
nullVotes  = getNullVotes(db, percentage_id)
blankVotes = getBlankVotes(db, percentage_id)

totalVotes = blankVotes[0][0] + nullVotes[0][0] +  validVotes[0][0]

voteResult = []

for candidate in candidates:
  name = candidate[4]
  candidate_id = str(candidate[0])
  cantVotos = str(candidate_results[candidate_id])
  porcentaje = (candidate_results[candidate_id]*100)/totalVotes
  entry = { 'id' : candidate_id, 'nombre' : name, 'votos' : cantVotos, 'porcentaje': str(round(porcentaje, 2)) }
  voteResult.append(entry)

result = {}
 
result['candidatos'] = voteResult
result['votos'] = { 'validos': str(validVotes[0][0]), 'nulos': str(nullVotes[0][0]), 'blancos' : str(blankVotes[0][0]), 'totales': str(totalVotes)} 
result['actualizado'] = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

print voteResult
insertParsedResult(db, result)






































