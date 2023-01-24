import pandas as pd
import streamlit as st
import joblib
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3136368ff79fd8b05a0b46aa15630807&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

with open('movies.joblib','rb') as f:
    movies=joblib.load(f)
with open('similarity.joblib','rb') as f:
    similarity=joblib.load(f)
st.title('Movie Recommendation system')
movie = st.selectbox('Select a movie name',movies['title'])


def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_lst = sorted(enumerate(distances),reverse=True,key=lambda x:x[1])[1:11]
    rec = []
    poster = []
    for i in movie_lst:
        rec.append(movies.iloc[i[0]].title)
        poster.append(fetch_poster(movies.iloc[i[0]].movie_id))
    rec = pd.DataFrame(rec)
    rec.columns=['Movies']
    return rec,poster


if st.button('Recommend'):
    recommendations,posters = recommend(movie)

    col1,col2,col3,col4,col5 = st.columns(5)
    

    with col1:
        st.text(recommendations.iloc[0,0])
        st.image(posters[0])
    with col2:
        st.text(recommendations.iloc[1,0])
        st.image(posters[1])
    with col3:
        st.text(recommendations.iloc[2,0])
        st.image(posters[2])
    with col4:
        st.text(recommendations.iloc[3,0])
        st.image(posters[3])
    with col5:
        st.text(recommendations.iloc[4,0])
        st.image(posters[4])
    with col1:
        st.text(recommendations.iloc[5,0])
        st.image(posters[5])
    with col2:
        st.text(recommendations.iloc[6,0])
        st.image(posters[6])
    with col3:
        st.text(recommendations.iloc[7,0])
        st.image(posters[7])
    with col4:
        st.text(recommendations.iloc[8,0])
        st.image(posters[8])
    with col5:
        st.text(recommendations.iloc[9,0])
        st.image(posters[9])
