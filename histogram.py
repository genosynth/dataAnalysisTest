import matplotlib.pyplot as plt
import pandas as pd

data = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

# Plot
plt.hist(data, bins=5, color='orange', edgecolor='black')
plt.title('Histogram of Values')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()