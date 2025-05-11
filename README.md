# 🎬 Content-Based Movie Recommendation System
Builds a content-based recommender by generating a TF-IDF matrix from movie overviews and computing cosine similarity. Processes textual data to find similarities between movies. Displays top 5 similar movies based on computed scores.

## Project Overview
Objective: Recommend movies similar to a selected title using content-based filtering.
Tech Stack: Python, Pandas, scikit-learn, Streamlit
Dataset: TMDB 5000 Movie Dataset from kaggle

## Methodology
#### Data Preprocessing:
Load the dataset using Pandas.
Handle missing values and duplicates.
Extract relevant features: genres, cast, director, and overview.

#### Feature Engineering:
Combine selected features into a single string for each movie.
Convert text to lowercase and remove spaces to standardize.

#### Text Vectorization:
Use CountVectorizer from scikit-learn to convert text data into numerical vectors.

#### Similarity Calculation:
Compute cosine similarity between movie vectors to determine similarity scores.

#### Recommendation Function:
Create a function that takes a movie title as input and returns the top 5 most similar movies based on the similarity scores.

## Deployment with Streamlit
The application is deployed using Streamlit, providing an interactive web interface.
Live Demo
Access the live application here: https://movie-content-based-recommendation.streamlit.app/
