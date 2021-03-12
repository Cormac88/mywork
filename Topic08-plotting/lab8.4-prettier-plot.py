# Line and Scatter Plot
# Author: Cormac Hennigan

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

minAge = 21
maxAge = 65

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(minAge, maxAge, numberOfEntries)

plt.scatter(ages, salaries, label = "salaries")

xpoints = np.array(range(1,101))
ypoints = xpoints ** 2

plt.plot(xpoints, ypoints, color = "r", label = "x squared")
plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("age")
plt.legend()
#plt.show()

plt.savefig('prettier-plot.png')