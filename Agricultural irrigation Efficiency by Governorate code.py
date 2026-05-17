import pandas as pd
import os
import matplotlib.pyplot as plt

df = pd.read_csv(r"F:\Career development program\Practice\Agricultural project\spss-e\crop1.csv")

# convert numerical data
df['G09'] = pd.to_numeric(df['G09'], errors='coerce')
df['G10'] = pd.to_numeric(df['G10'], errors='coerce')

# delet the empty rows
df = df.dropna(subset=['A02', 'G09', 'G10'])

# collection as sort of irrigation
irrigation_analysis = df.groupby('G08').agg({
    'G09':'sum',
    'G10':'sum'
    })
# rename the columns
irrigation_analysis.columns = [
    'Total Area',
    'Total Production' ]
# efficiency counting
irrigation_analysis['Efficiency'] = (
    irrigation_analysis['Total Production'] /
    irrigation_analysis['Total Area']
    )

# sort as efficiency
irrigation_analysis = irrigation_analysis.sort_values('Efficiency', ascending=False)

#show result
print(irrigation_analysis)

#create bar chart
plt.figure(figsize=(10,6))
irrigation_analysis['Efficiency'].plot(kind='bar')

#title and axise
plt.title('Irrigation Efficiency')
plt.xlabel('Irrigation Type')
plt.ylabel('Efficiency')

#governments rotation
plt.xticks(rotation=45)

#improvment present
plt.tight_layout()

#show bar chart
plt.show()
print(df['G08'].value_counts())

