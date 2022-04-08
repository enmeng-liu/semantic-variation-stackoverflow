import numpy as np
from scipy.spatial import distance

def apd(usages1, usages2, metric='cosine'):
    return np.nanmean(distance.cdist(usages1, usages2, metric='cosine'))
