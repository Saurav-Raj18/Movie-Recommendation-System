import streamlit as st
import pandas as pd
import pickle

def recommend(title):
    ind=movies[movies['title']==title].index.values[0]
    distanceVector=similarityVector[ind]
    indexed_distance_vector=list(enumerate(distanceVector))
    sorted_distance_vector=sorted(indexed_distance_vector,key=lambda x:x[1],reverse=True)[1:6]
    l=[]
    for i in sorted_distance_vector:
       l.append(movies.iloc[i[0]].title)
    return l


movies_list=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_list)
similarityVector=pickle.load(open('similarity.pkl','rb'))
st.title("Movie Recommendation System")
st.write("Select a movie to get recommendations:")
selected_movie = st.selectbox("Movie Title", movies['title'].tolist())
# Create a button to recommend movies
if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    if recommendations:
        st.write("Top 5 Recommendations:")
        for movie in recommendations:
            st.write(movie)
    else:
        st.write("No recommendations found.")