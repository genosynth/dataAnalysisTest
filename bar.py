import matplotlib.pyplot as plt
import pandas as pd


data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [4, 7, 1, 8]
})

# Plot
plt.bar(data['Category'], data['Values'], color='skyblue')
plt.title('Category Values')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()