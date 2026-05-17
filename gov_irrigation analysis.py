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
gov_irrigation = df.groupby(['A02', 'G08']).agg({
    'G09':'sum',
    'G10':'sum'
    })
# rename the columns
gov_irrigation.columns = [
    'Total Area',
    'Total Production' ]
# efficiency counting
gov_irrigation['Efficiency'] = (
    gov_irrigation['Total Production'] /
    gov_irrigation['Total Area']
    )

# sort as efficiency
gov_irrigation = gov_irrigation.sort_values('Efficiency', ascending=False)

#show result
print(gov_irrigation)

#create bar chart
#top 10 results

top10 = gov_irrigation.head(10)
labels=[
    f"{idx[0]} - {idx[1]}"
    for idx in top10.index
    ]
top10 = top10.reset_index()
top10.columns = [
    'Governorate',
    'Irrigation Type',
    'Total Area',
    'Total Production',
    'Efficiency'
    ]
print(top10)
top10.to_csv(
    'Top10_Efficiency.csv', index=False])
print("\Top 10 table saved successfully.")
print("File: Top10_Efficiency.csv")
plt.figure(figsize=(12,6))
plt.bar(labels, top10['Efficiency'])
#title and axise
plt.title('Top 10 Irrigation Efficiency')
plt.xlabel('Governorate - Irrigation')
plt.ylabel('Efficiency')

#governments rotation
plt.xticks(rotation=45)

#improvment present
plt.tight_layout()

#show bar chart
plt.show()
#print(df['G08'].value_counts())
