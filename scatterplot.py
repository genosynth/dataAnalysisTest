import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'Y': [2, 3, 5, 7, 11]
})

# Plot
plt.scatter(data['X'], data['Y'], color='green')
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()