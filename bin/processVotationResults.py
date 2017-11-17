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
    statement = 'select sum(votos) as votosTotales from votaciones_4 where COD_AMBITO=%s and AMBITO=4 and PORCENTAJE_TOTAL=%s' % (candidate_id, percentage_id)
    cursor = db.cursor()
    cursor.execute(statement)
    return cursor.fetchall()
  
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

def getValidVotes(db, percentage_id):
  try:
    statement = 'select sum(votos) as votosValidos from votaciones_4 where AMBITO=7 and COD_AMBITO=1 and PORCENTAJE_TOTAL=%s' % (percentage_id)
    cursor = db.cursor()
    cursor.execute(statement)
    return cursor.fetchall()
  
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

def getNullVotes(db, percentage_id):
  try:
    statement = 'select sum(votos) as votosValidos from votaciones_4 where AMBITO=5 and COD_AMBITO=1 and PORCENTAJE_TOTAL=%s' % (percentage_id)
    cursor = db.cursor()
    cursor.execute(statement)
    return cursor.fetchall()
  
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
    
def getBlankVotes(db, percentage_id):
  try:
    statement = 'select sum(votos) as votosValidos from votaciones_4 where AMBITO=6 and COD_AMBITO=1 and PORCENTAJE_TOTAL=%s' % (percentage_id)
    cursor = db.cursor()
    cursor.execute(statement)
    return cursor.fetchall()
  
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))


percentage_id = getLatestUpdate(db)[0][0]
print percentage_id

candidates = getCandidatesForPresidentList(db)
candidate_ids = map(lambda x: x[0], candidates)
print candidate_ids

candidate_results = {}
for ID in candidate_ids:
  result = getTotalVoteCountForCandidate(db, ID, percentage_id)
  candidate_results[str(ID)] = result[0][0]

print candidate_results

validVotes = getValidVotes(db, percentage_id)
nullVotes = getNullVotes(db, percentage_id)
blankVotes = getBlankVotes(db, percentage_id)

voteResult = []

for candidate in candidates:
  name = candidate[4].encode('utf-8')
  candidate_id = str(candidate[0])
  cantVotos = str(candidate_results[candidate_id])
  entry = { 'nombre' : name, 'votos' : cantVotos }
  voteResult.append(entry)

result = {}
 
result['candidatos'] = voteResult
result['votos'] = { 'validos': str(validVotes[0][0]), 'nulos': str(nullVotes[0][0]), 'blancos' : str(blankVotes[0][0]), 'totales': str(blankVotes[0][0] + nullVotes[0][0] +  validVotes[0][0])} 

print result



































