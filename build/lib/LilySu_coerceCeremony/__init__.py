"""
helper functions
"""

import pandas as pd
import numpy as np

#samples
ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zero(50))

#sample functions
def increment(x):
    return(x+1)