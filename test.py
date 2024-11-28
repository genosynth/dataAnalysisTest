import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'Year': [2018, 2019, 2020, 2021, 2022,2023, 2024, 2025],
    'Sales': [200, 250, 300, 350, 400, 350, 250, 300 ]
})

# Plot
plt.plot(data['Year'], data['Sales'], marker='o')
plt.title('Yearly Sales')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.show()