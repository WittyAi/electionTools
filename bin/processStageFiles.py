import os 
import fnmatch
import datetime
import codecs

DESTINATION_PATH = os.environ.get("DESTINATION_PATH") if os.environ.get("DESTINATION_PATH") else './destination'
dir = os.listdir(DESTINATION_PATH)

# Escenario_Candidatos_018016.txt
# Escenario_Zonas_018016.txt
# Escenario_Elecciones_018016.txt
# Escenario_Pactos_018016.txt
# Escenario_SubPactos_018016.txt
# Escenario_Partidos_018016.txt
# Escenario_ZonasPadre_018016.txt

candidatosFile = fnmatch.filter(os.listdir(DESTINATION_PATH), 'Escenario_Candidatos_*.txt')
zonasFile      = fnmatch.filter(os.listdir(DESTINATION_PATH), 'Escenario_Zonas_*.txt')
eleccionesFile = fnmatch.filter(os.listdir(DESTINATION_PATH), 'Escenario_Elecciones_*.txt')
pactosFile     = fnmatch.filter(os.listdir(DESTINATION_PATH), 'Escenario_Pactos_*.txt')
subpactosFile  = fnmatch.filter(os.listdir(DESTINATION_PATH), 'Escenario_SubPactos_*.txt')
partidosFile   = fnmatch.filter(os.listdir(DESTINATION_PATH), 'Escenario_Partidos_*.txt')
zonaspadreFile = fnmatch.filter(os.listdir(DESTINATION_PATH), 'Escenario_ZonasPadre_*.txt')


#COD_CAND; COD_ELEC; COD_ZONA; CAN_ORDEN;GLOSA_CAND; COD_PART; COD_PACT; COD_SUBP; COD_IND; CAN_PAGINA; GLOSA_NOMBRE; GLOSA_APELLIDO;

with codecs.open(DESTINATION_PATH + '/' + candidatosFile[0], 'r', 'utf-8') as fp:
    for line in fp:
        print line.split(';')








