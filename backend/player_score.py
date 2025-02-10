import math
from scipy.stats import norm
import numpy as np

def calc_player_score(game):
    kda = (game['kills'] + game['assists']) / game['deaths']
    finalXpDiff = game['champXpDiff']
    xpDiff14 = game['xpDiff14']
    finalGoldDiff = game['goldDiff']
    goldDiff14 = game['golddiff14min']
    goldPerMinute = game['goldPerMinute']
    damagePerMinute = game['damagePerMinute']
    turretPlatesTaken = game['turretPlatesTaken']
    damagetoBuildings = game['damagetoBuildings']

    kda_score = 1 * normalise_value(kda)


# Creates a range between -1 and 1, should now try to use this to multiply by an appropriate factor
# (i.e. how much value I want to place on a stat)

def normalise_value(value, mean=2, std=1):
    """
    Map input values to a normal distribution between [-1, 1].
    
    Parameters:
    - value: The input value.
    - mean: The mean of the normal distribution.
    - std: The standard deviation of the normal distribution.

    Returns:
    - A value in the range [-1, 1].
    """
    # Compute the CDF of the normal distribution
    cdf_value = norm.cdf(value, loc=mean, scale=std)
    
    # Scale CDF output to [-1, 1]
    normalized_value = 2 * cdf_value - 1
    
    # Saturate the output within [-1, 1]
    return np.clip(normalized_value, -1, 1)

print (normalise_value(0.1))