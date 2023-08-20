#!/usr/bin/env python
# coding: utf-8

# ### Uber Pickups Analysis Quiz
# 
# The question set is based on the August dataset, `uber-raw-data-aug14.csv`.
# 
# #### Keeping the dataset ready before questions

# In[4]:


import pandas as pd

df = pd.read_csv('./data/uber-raw-data-aug14.csv')
df.head()


# #### Q1. On what date did we see the most number of Uber pickups?
# 
# **Skill Test:** Grouping & Counting

# In[6]:


# Convert the 'Date/Time' column to datetime format
df['Date/Time'] = pd.to_datetime(df['Date/Time'])
df1=df.copy()
df1.set_index('Date/Time', inplace=True)
df1

# Group by date and count the number of pickups
pickup_counts_by_date = df1.resample('D').size().reset_index(name='Pickups')


# Find the date with the highest number of pickups
date_with_the_highest_number_of_pickups = pickup_counts_by_date.loc[pickup_counts_by_date['Pickups'].idxmax(), 'Date/Time']
print(date_with_the_highest_number_of_pickups)



# #### Q.2 How many Uber pickups were made on the date with the highest number of pickups?
# 
# **Skill Test:** Indexing and filtering

# In[7]:


# Filter the DataFrame to include only the rows for the date with the highest number of pickups
dates_with_highest_number_of_pickups = df[df['Date/Time'].dt.date == date_with_the_highest_number_of_pickups.date()]
dates_with_highest_number_of_pickups

# Get the count of pickups on the highest date
count_of_pickups_on_highest_date = dates_with_highest_number_of_pickups.shape[0]
print("count of highest pickups on the date:", count_of_pickups_on_highest_date)




# #### Q.3 How many unique TLC base companies are affiliated with the Uber pickups in the dataset?
# 
# **Skill Test:** Counting unique values

# In[8]:


# Count the number of unique TLC base companies
unique_base_companies = df['Base'].nunique()
print("Number of unique TLC base companies:", unique_base_companies)


# #### Q.4 Which TLC base company had the highest number of pickups?
# 
# **Skill Test:** Grouping, counting, and finding the maximum

# In[9]:


# Group by TLC base company and count the number of pickups
base_company_pickup_counts = df.groupby('Base').size().reset_index(name='Pickups')
base_company_pickup_counts

# Find the TLC base company with the highest number of pickups
base_company_highest_pickups = base_company_pickup_counts.loc[base_company_pickup_counts['Pickups'].idxmax(), 'Base']
print("TLC Base company with the highest number of pickups:", base_company_highest_pickups)


# #### Q.5 How many Uber pickups were made at each unique TLC base company?
# 
# **Skill Test:** Grouping and counting

# In[10]:


# Group by TLC base company and count the number of pickups
base_company_highest_pickups = df.groupby('Base').size().reset_index(name='Pickups')
print(base_company_highest_pickups)




# #### Q.6 Can you determine the busiest time of day for Uber pickups based on the date/time column?
# 
# **Skill Test:** Extracting time components, grouping, counting, and finding the maximum

# In[11]:


# Extract the hour from the 'Date/Time' column
extract = df['Hour'] = df['Date/Time'].dt.hour
extract

# Group by hour and count the number of pickups
pickup_counts_by_hour = df.groupby('Hour').size().reset_index(name='Pickups')

# Find the hour with the highest number of pickups
hour_of_highest_pickups = pickup_counts_by_hour.loc[pickup_counts_by_hour['Pickups'].idxmax(), 'Hour']
print("Hour with the highest number of pickups:", hour_of_highest_pickups)



# #### Q.7 Can you create a visualization (e.g., a bar chart or line plot) to represent the number of Uber pickups over time?
# 
# **Skill Test:** Data Visualization using Plotting function 

# In[13]:


import matplotlib.pyplot as plt

# Group by date and count the number of pickups
counts_pickup_by_date = df.resample('D', on='Date/Time').size().reset_index(name='counts_pickup_by_date')    
counts_pickup_by_date

# Create a line plot to visualize the number of pickups over time
counts_pickup_by_date.plot(x='Date/Time', y='counts_pickup_by_date', kind='line', title='number of pickups over time')


# #### Q8. Can you create a scatter plot to visualize the distribution of Uber pickups based on latitude and longitude?
# 
# **Skill Test:** Scatter Plot

# In[14]:


# Create a scatter plot to visualize the distribution of Uber pickups based on latitude and longitude
plt.figure(figsize=(10, 6))
plt.scatter(df['Lon'], df['Lat'], alpha=0.5)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Distribution of Uber Pickups')
plt.grid(True)
plt.tight_layout()
plt.show()


# #### Q9. Can you create a bar chart to compare the number of Uber pickups for each TLC base company?
# 
# **Skill Test:** Bar Chart

# In[16]:


# Create a bar chart to compare the number of Uber pickups for each TLC base company
plt.figure(figsize=(10, 6))
plt.bar(base_company_pickup_counts['Base'], base_company_pickup_counts['Pickups'])
plt.xlabel('TLC Base Company')
plt.ylabel('Number of Pickups')
plt.title('Number of Uber Pickups by TLC Base Company')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# #### Q10. Can you create a pie chart to display the percentage distribution of Uber pickups for each day of the week?
# 
# **Skill Test:** Pie Chart

# In[19]:


# Group by day of the week and count the number of pickups
df['Day_of_Week'] = df['Date/Time'].dt.day_name()
pickup_counts_by_day_of_week = df.groupby('Day_of_Week').size()
pickup_counts_by_day_of_week

# Create a pie chart to display the percentage distribution of Uber pickups for each day of the week
plt.figure(figsize=(8, 8))
plt.pie(pickup_counts_by_day_of_week, labels=pickup_counts_by_day_of_week.index, autopct='%1.1f%%', startangle=90)
plt.title('Percentage Distribution of Uber Pickups by Day of the Week')
plt.axis('equal')
plt.tight_layout()
plt.show()


# In[ ]:




