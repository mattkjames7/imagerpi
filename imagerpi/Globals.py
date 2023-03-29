import numpy as np
import os

#get the data path
try:
    DataPath = os.getenv('IMAGERPI_PATH')
    if not DataPath.endswith('/'):
        DataPath += '/'
        
except:
    print('Set $IMAGERPI_PATH variable before importing this module')
    raise SystemExit


orbit = None

ModulePath = os.path.dirname(__file__)+'/' 
