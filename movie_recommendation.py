# -*- coding: utf-8 -*-
"""
Created on Thu May  8 20:38:17 2025

@author: AARTHI KRISHNAN
"""

import streamlit as st
from PIL import Image
import pickle


movie=pickle.load(open("movie_list.pkl",'rb'))
movie_list=movie.values

similarity=pickle.load(open("cosine_similarity.pkl",'rb'))

def recommendation(input_movie):

    
      index=movie[movie==input_movie].index[0]
      # finding the highest similarity score
      similarity_score=list(enumerate(similarity[index]))
      # sorted order of highest similarity
      sorted_similarity=sorted(similarity_score,key=lambda x:x[1],reverse=True)
      
      recommended_movie=[]
      for i in sorted_similarity[1:6]:
        recommended_movie.append(movie.iloc[i[0]])
        
      return recommended_movie
  


def web_page():
    img=Image.open("header_image.jpg")
    st.image(img,width=700)
    
    st.title("Movie Recomendation System")
    
    movie_title=st.selectbox("Enter the movie name",movie_list)
    
    if st.button("Recommend Movie"):
        st.info("List of movies that are similar to your interest....")
        
        result=recommendation(movie_title)
        # Top 5 similar movies
        for i in result:
          st.write(i)
    
if __name__=='__main__':
    web_page()