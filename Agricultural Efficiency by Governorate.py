import pandas as pd
import matplotlib.pyplot as plt

#read the file
df = pd.read_csv(r"F:\Career development program\Practice\Agricultural project\spss-e\crop1.csv")

# create bar chat for agricultural efficiency of governments
plt.figure(figsize=(12,6))

gov_analysis['Efficiency'].plot(kind='bar')

plt.title('Agricultural Efficiency by Governorate')
plt.xlabel('Governorate')
plt.ylabel('Efficiency')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
