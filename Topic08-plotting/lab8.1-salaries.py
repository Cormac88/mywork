# Prints random salaries
# Author: Cormac Hennigan

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

print(salaries)

salariesPlus = salaries + 5000
print(salariesPlus)

salariesMult = salaries * 1.05
print(salariesMult)

newSalaries = salariesMult.astype(int)
print(newSalaries)
