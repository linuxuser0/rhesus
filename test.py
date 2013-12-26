import os
from glimpse.experiment import *
from glimpse.models import *
from glimpse.pools import *

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
FEED_LOCATION= os.path.join(CURRENT_DIRECTORY, "test_feed")

exp = ExperimentData()
pool = MakePool('s')

def _initial_imprint():
    SetCorpus(exp, FEED_LOCATION)
    SetModel(exp, model=MakeModel())
    imprint() 

def imprint():
    """Imprints and returns a set of visual cells given a series of images."""
    MakePrototypes(exp, num_prototypes=10, algorithm="imprint", pool=pool)
    return [ GetPrototype(exp, n) for n in range(GetNumPrototypes(exp)) ] 
    
def feed_and_imprint():
    """Requests images from this Imprinter's imagefeed and imprints them, returning visual cells."""
    imagefeed.feed()
    return imprint()

_initial_imprint()


    

