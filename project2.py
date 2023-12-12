import pandas as pd
import zipfile 
import os
import matplotlib.pyplot as plt

##extracting zipfile 
with zipfile.ZipFile('names.zip','r') as name_df:
    name_df.extractall("names")

#List the files in the extracted folder.
name_files = os.listdir("names")
#print(name_files)

#creating empty data frame to store merged files
conacted_df = pd.DataFrame()

#reading individual files and finally merge into one
for files in name_files:
    fetch_data = "names\\" + files
    #print(fetch_data)
    data_in_csv = pd.read_csv(fetch_data,header=None)
    data_in_csv.columns = ["name","gender","count"]
    new_col_name = "yob"
    new_col_value = files[3:7]
    data_in_csv[new_col_name] = new_col_value
    conacted_df = pd.concat([conacted_df,data_in_csv],ignore_index= True)
#print(conacted_df)

# task-1: VISIUALIZE THE NUMBER OF MALE AND FEMALE BORN IN EACH YEAR
conacted_df = conacted_df.sort_values(by="yob")
x1 = conacted_df['yob'].value_counts().keys()
#print(x1)
x = x1.tolist()
x.sort()
#print(x)
gender_counts = conacted_df.groupby(['yob', 'gender']).size().reset_index(name='count')
#print(gender_counts)
y_val1 = gender_counts['count'][gender_counts["gender"]=="M"]
y_val2 = gender_counts['count'][gender_counts["gender"]=="F"]
# print(y_val1)
# print(y_val2)
color1 = 'orange'
color2 = "blue"
fig, ax = plt.subplots()
scat1 = ax.scatter(x ,y_val1 ,color = color1, label='male distribution')
scat2 = ax.scatter(x ,y_val2 ,color = color2, label='female distribution')
ax.set_xticklabels(x ,rotation=90,fontsize=5)
ax.set_xlabel('year of birth')
ax.set_ylabel('male and female born')
ax.set_title('gender distribution over the years')
ax.legend()
plt.show()

#most popular name among all names by birth counts
# print(conacted_df.sort_values(by="count",ascending=False))

#display the top 100 popular names
# name_counts =conacted_df.groupby('name')['count'].sum()

#print(name_counts)
# top_100_names = name_counts.sort_values(ascending=False).head(100)
# print(top_100_names)