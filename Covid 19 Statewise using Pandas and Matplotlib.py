#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import matplotlib.pyplot as plt

# Fetch the COVID data from the API using pandas
url = "https://data.covid19india.org/v4/min/data.min.json"
data = pd.read_json(url)

# Extract the required data for visualization
states = []
confirmed_cases = []
recovered_cases = []
deaths = []

for state, state_data in data.items():
    states.append(state)
    confirmed_cases.append(state_data['total']['confirmed'])
    recovered_cases.append(state_data['total']['recovered'])
    deaths.append(state_data['total']['deceased'])

# Create a bar chart for confirmed cases, recovered cases, and deaths
plt.figure(figsize=(10, 5))
plt.bar(states, confirmed_cases, color='b', label='Confirmed Cases')
plt.bar(states, recovered_cases, color='g', label='Recovered Cases')
plt.bar(states, deaths, color='r', label='Deaths')
plt.xticks(states, rotation=90)
plt.xlabel("States")
plt.ylabel("Number of Cases")
plt.title("COVID-19 Cases in India")
plt.legend()
plt.show()


delta=[]
delta7=[]
delta21_4=[]
meta=[]

for states,states_data in data.items
states.append(state)
delta.append(state_data['delta'])
delta7.append(state_data['delta7'])
delta21_4.append(state_data['delta21_4'])
meta.append(state_data['meta'])


# In[ ]:




