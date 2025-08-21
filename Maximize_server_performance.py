#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMaxPerformanceSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY performanceScores
#  2. INTEGER_ARRAY activationStatus
#  3. INTEGER k
#

def getMaxPerformanceSum(performanceScores, activationStatus, k):
    n = len(performanceScores)
    already_active_sum = 0
    
    # 1. Calculate sum of already active servers
    for i in range(n):
        if activationStatus[i] == 1:
            already_active_sum += performanceScores[i]
    
    # 2. Calculate the maximum score we can gain by activating k consecutive servers
    max_gain = 0
    current_gain = 0
    
    # Initial window (first k servers)
    for i in range(k):
        if activationStatus[i] == 0:
            current_gain += performanceScores[i]
    max_gain = current_gain
    
    # Slide the window
    for i in range(k, n):
        # Remove outgoing element if it was inactive
        if activationStatus[i - k] == 0:
            current_gain -= performanceScores[i - k]
        # Add incoming element if it is inactive
        if activationStatus[i] == 0:
            current_gain += performanceScores[i]
        # Update max_gain
        max_gain = max(max_gain, current_gain)
    
    return already_active_sum + max_gain

if __name__ == '__main__':
    performanceScores = [1, 3, 5, 2, 1]
    activationStatus = [1, 1, 0, 1, 0]
    k = 2

    result = getMaxPerformanceSum(performanceScores, activationStatus, k)
    print(result)
