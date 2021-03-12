# Bar Chart of counties with Dublin favoured
# Author: Cormac Hennigan

import numpy as np
import matplotlib.pyplot as plt

possibleCounties = ["Dublin", "Cork", "Galway", "Antrim", "Kerry"]
counties = np.random.choice(possibleCounties, p=[0.6, 0.1, 0.1, 0.1, 0.1 ], size = (100))

unique, counts = np.unique(counties, return_counts = True)

plt.bar(unique, counts)
plt.show()