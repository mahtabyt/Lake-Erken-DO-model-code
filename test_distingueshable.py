# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:52:31 2024

@author: mahta
"""

#pip install scipy scikit-posthocs

import numpy as np
from scipy.stats import friedmanchisquare
import scikit_posthocs as sp


data = np.array([
    [23, 45, 67, 89],   # Subject 1
    [34, 22, 34, 45],   # Subject 2
    [56, 78, 90, 12],   # Subject 3
    [24, 44, 65, 90],   # Subject 4
    [33, 23, 35, 46],   # Subject 5
    [55, 77, 91, 13],   # Subject 6
])


stat, p_value = friedmanchisquare(data[:, 0], data[:, 1], data[:, 2], data[:, 3])
print(f"Friedman test statistic: {stat}")
print(f"p-value: {p_value}")

#Friedman test statistic: 5.94915254237289
#p-value: 0.11411044128915748
#There is no significant difference among the groups.

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("There is a significant difference among the groups.")
else:
    print("There is no significant difference among the groups.")
    



    
#If the Friedman test indicates a significant difference, 
#use post-hoc tests to find out which groups are different.

#%%
import numpy as np
from scipy.stats import friedmanchisquare
import scikit_posthocs as sp

# Example data: each row represents a subject and each column represents a group
data = np.array([
    [100, 45, 67, 89],   # Subject 1
    [324, 22, 34, 45],   # Subject 2
    [556, 78, 2020, 12],   # Subject 3
    [200, 44, 65, 90],   # Subject 4
    [233, 200, 35, 46],   # Subject 5
    [255, 77, 91, 13],   # Subject 6
])

# Perform the Friedman test
stat, p_value = friedmanchisquare(data[:, 0], data[:, 1], data[:, 2], data[:, 3])
print(f"Friedman test statistic: {stat}")
print(f"p-value: {p_value}")

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("There is a significant difference among the groups.")
    
    # Perform post-hoc analysis using the Nemenyi test
    posthoc_results = sp.posthoc_nemenyi_friedman(data)
    print("Post-hoc test results:")
    print(posthoc_results)
else:
    print("There is no significant difference among the groups.")


#%%
import numpy as np
from scipy.stats import friedmanchisquare
import scikit_posthocs as sp

# Example data: each row represents a subject and each column represents a group
data = np.array([
    [100, 45, 67, 89],   # Subject 1
    [324, 22, 34, 45],   # Subject 2
    [556, 78, 2020, 12],   # Subject 3
    [200, 44, 65, 90],   # Subject 4
    [233, 200, 35, 46],   # Subject 5
    [255, 77, 91, 13],   # Subject 6
])

# Perform the Friedman test
stat, p_value = friedmanchisquare(data[:, 0], data[:, 1], data[:, 2], data[:, 3])
print(f"Friedman test statistic: {stat}")
print(f"p-value: {p_value}")

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("There is a significant difference among the groups.")
    
    # Perform post-hoc analysis using the Nemenyi test
    posthoc_results = sp.posthoc_nemenyi_friedman(data)
    print("Post-hoc test results:")
    print(posthoc_results)
    
    # Identify significant differences based on adjusted p-values
    for i in range(posthoc_results.shape[0]):
        for j in range(i + 1, posthoc_results.shape[1]):
            if posthoc_results.iloc[i, j] < alpha:
                print(f"Groups {i} and {j} are significantly different.")
else:
    print("There is no significant difference among the groups.")
