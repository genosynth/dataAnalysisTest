import requests
import streamlit as st
import pandas as pd


response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=256da2d742d5a5979790e6833447e4b4').json()
Popularity = []
Vote_count = []
Orignal_lang = []
Title = []
Vote_avg = []
Overview = []
Release_Data = []

'''print(response["results"])'''

for i in response['results']:
    Popularity.append(i['popularity'])
    Vote_count.append(i['vote_count'])
    Orignal_lang.append(i['original_language'])
    Title.append(i['title'])
    Vote_avg.append(i['vote_average'])
    Overview.append(i['overview'])
    Release_Data.append(i['release_date'])

d = {'title':Title,'Overview':Overview,'Orignal_lang':Orignal_lang,'Release_Data':Release_Data,'Popularity':Popularity,'Vote_count':Vote_count,'Vote_avg':Vote_avg}
df = pd.DataFrame(d)
st.title("Movie Data Table")
st.dataframe(df)


# Sort by Popularity
sorted_df = df.sort_values(by='Vote_avg', ascending=False)

# Convert back to a dictionary if needed
sorted_d = pd.DataFrame(sorted_df.to_dict(orient='list'))


print(sorted_d)